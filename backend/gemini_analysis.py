import os
import google.generativeai as genai
import asyncio

API_KEY = "AIzaSyC0RCJ55bgQ-ifdAW_rRLoNd_ru1Z2dCZE"

genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "<context>\n    You are the fake news detective's assistant. You will be provided with a tweeter's tweet. You have to use google search\n</context>\n\n<task>\n    if text is claiming something that is happening currently: \n        then you have to perform the fact check\n\n        <factCheck>\n            1. look for reliable news or more that 3 sources sites covered the story\n            2. if fact check is present on their site \n                look for what is the conclusion, is that \"True news\" or \"Fake news\"?\n                or You could use your learning to find out. \n                else: \n                    if there are no result found about this text, return as \"not verified\"\n        </factCheck>\n\n\n        and analyse the sentiment of the text. \n    else: \n        only analyse the sentiment and face check section should be labeled as not a claim\n</task>\n\n<list of reliable sources>\n    all the trusted sources you know + these followings\n    1. thehindu.com\n    2. aajtak.in\n    3. newslaundary.com\n    4. altnews.in\n    5. nytimes.com\n    6. *.gov.in\n    7. *.gov\n</list of reliable sources>\n\n<output>\n    {\n        \"original_text\": \"user original prompt\", \n        \"analysis_result\": \"if any, or post is not claming anything\",\n        \"sentiment\": \"hate or excitement etc\", \n        \"sources\": [\n            list of sources sites where you find the content related to your text,\n        ]\n    }\n</output>\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n    \"original_text\": \"Heavy clashes erupted between Indian and Chinese troops in Arunachal Pradesh's Tawang Sector on December 9, 2022, with both sides suffering injuries.\",\n    \"analysis_result\": \"True news\",\n    \"sentiment\": \"negative\",\n    \"sources\": [\n        \"https://www.ndtv.com/india-news/india-china-clash-in-tawang-several-injured-sources-3575346\",\n        \"https://www.thehindu.com/news/national/india-china-soldiers-clash-along-lac-in-tawang-sector-of-arunachal-pradesh/article66223678.ece\",\n        \"https://www.bbc.com/news/world-asia-india-63937143\",\n        \"https://indianexpress.com/article/india/india-china-face-off-arunachal-tawang-lac-8315360/\"\n\n    ]\n}\n```\n",
      ],
    },
  ]
)

def askGemini(input):
    # response = chat_session.send_message(input)
    response = [ "hii", True, False] 
    return response


