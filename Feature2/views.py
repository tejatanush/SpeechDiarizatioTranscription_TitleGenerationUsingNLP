from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from utils import suggest_titles
@csrf_exempt
def suggest_titles_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        content = data.get("blog_content", "")
        if not content:
            return JsonResponse({"error": "No blog content provided"}, status=400)

        titles = suggest_titles(content)
        return JsonResponse({"titles": titles})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
