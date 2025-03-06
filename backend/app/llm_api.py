from parse import parse_file
from dotenv import load_dotenv
import openai
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

system_prompt = """ You are an assistant that analyze tax related documents and generate a short summary.
    You should follow these instructions:
    - Keep the summary concise, focusing only on the most important details.
    - Highlight the points you think most important. 
    - If document contains unclear information highlight it, but avoid making assumptions.
    - Respond in markdown."""
    
user_prompt = """You are looking at a document. The content of this document is as follows.
    Please provide a short summary.\n"""

# we communicate with openai endpoint and send the parsed text 
# and with prompt engineering we leverage the summarize ability of model
def generate_summary(file_path):
    augmented_prompt = user_prompt + parse_file(file_path) 
    response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": augmented_prompt}
          ],
        temperature=0.3
    )
    summary = response.choices[0].message.content
    return summary