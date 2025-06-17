import os
import tempfile
import whisperx
import torch
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from pyannote.audio import Pipeline

@csrf_exempt
@require_http_methods(["POST"])
def transcribe_audio(request):
    if 'audio_file' not in request.FILES:
        return JsonResponse({'error': 'No audio file provided'}, status=400)
    
    audio_file = request.FILES['audio_file']
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
        for chunk in audio_file.chunks():
            temp_file.write(chunk)
        temp_file_path = temp_file.name
    
    try:
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = whisperx.load_model("medium", device, compute_type="float32")
        
        
        transcription_result = model.transcribe(temp_file_path)
        
        
        align_model, metadata = whisperx.load_align_model(
            language_code=transcription_result["language"], 
            device=device
        )
        transcription_result = whisperx.align(
            transcription_result["segments"], 
            align_model, 
            metadata, 
            temp_file_path, 
            device
        )
        
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token="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"
        )
        diarization = pipeline(temp_file_path, num_speakers=3)
        
        
        result = []
        for segment in transcription_result["segments"]:
            segment_start = segment['start']
            segment_end = segment['end']
            segment_text = segment['text']
            
            speaker = None
            max_overlap = 0
            
            for turn, _, speaker_label in diarization.itertracks(yield_label=True):
                overlap_start = max(segment_start, turn.start)
                overlap_end = min(segment_end, turn.end)
                overlap_duration = max(0, overlap_end - overlap_start)
                
                if overlap_duration > max_overlap:
                    max_overlap = overlap_duration
                    speaker = speaker_label
            
            result.append({
                "speaker": speaker,
                "text": segment_text.strip(),
                "start": segment_start,
                "end": segment_end
            })
        
        return JsonResponse(result, safe=False)
        
    finally:
        os.unlink(temp_file_path)