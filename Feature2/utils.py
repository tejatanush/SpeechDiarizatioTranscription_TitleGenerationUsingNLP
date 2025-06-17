import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    api_key=groq_api_key
)
prompt = PromptTemplate.from_template("""
You are a helpful assistant. Given the content of a blog post, generate 3 creative and catchy blog post titles.

Blog Content:
{blog_content}

Return only the 3 titles, each on a new line.
""")

chain = prompt | llm | StrOutputParser()
def suggest_titles(blog_content: str):
    result = chain.invoke({"blog_content": blog_content})
    return result.strip().split("\n")
