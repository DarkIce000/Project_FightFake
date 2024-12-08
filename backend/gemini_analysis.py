import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from google.api_core import exceptions

API_KEY = "AIzaSyC0RCJ55bgQ-ifdAW_rRLoNd_ru1Z2dCZE"
API_KEY_2 = "AIzaSyCwnrhraD4ZpVzPn2ydtm4UVWkkXogIFI0"
genai.configure(api_key=API_KEY_2)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  tools = "google_search_retrieval"
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "<context>\n    You are the fake news detective's assistant. You will be provided with a tweeter's tweet. You have to use google search\n</context>\n<task>\n    if text is claiming something that is happening currently: \n        then you have to perform the fact check\n        <factCheck>\n            1. look for reliable news or more that 3 sources sites covered the story\n            2. if fact check is present on their site \n                look for what is the conclusion, is that \"True news\" or \"Fake news\"?\n                or You could use your learning to find out. \n                else: \n                    if there are no result found about this text, return as \"not verified\"\n        </factCheck>\n        and analyse the sentiment of the text. \n    else: \n        only analyse the sentiment and face check section should be labeled as not a claim\n</task>\n<list of reliable sources>\n    all the trusted sources you know + these followings\n    1. thehindu.com\n    2. aajtak.in\n    3. newslaundary.com\n    4. altnews.in\n    5. nytimes.com\n    6. *.gov.in\n    7. *.gov\n</list of reliable sources>\n<output>\n[\n    {\n        id: Original id given with text, \n        txt: Original text given for analysis,\n        result: {\n            sentiment_analysis: \"hate or excitement etc\",\n            is_fake: True or False or Not Sure, \n            sources: [\n                \"source1\",\n                \"source2\",\n                \"source3\",\n                ...list of sources sites where you find the content related to your text\n            ]\n        }\n    },\n    \n    {\n        id: Original id given with text, \n        txt: Original text given for analysis,\n        result: {\n            sentiment_analysis: \"hate or excitement etc\",\n            is_fake: True or False or Not Sure, \n            sources: [\n                \"source1\",\n                \"source2\",\n                \"source3\",\n                ...list of sources sites where you find the content related to your text\n            ]\n        }\n    },\n]\n    \n</output>",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n[\n    {\n        \"id\": 1,\n        \"txt\": \"I'm seeing news about a major event happening right now.\",\n        \"result\": {\n            \"sentiment_analysis\": \"Neutral\",\n            \"is_fake\": \"Not Sure\",\n            \"sources\": []\n        }\n    }\n]\n```",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[\n    {\n        \"id\": \"id__g17ov29ydar\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">you just won $50 million and your lifelong friend says “we’re rich” what do you say back?</span>\"\n    },\n    {\n        \"id\": \"id__yk3gc3k8lhl\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">For any college student reading this, here’s how a typical production release looks like, specifically with a customer facing feature in a big Org such as Amazon. \\n\\n0. Any new feature/change you push is mostly under a feature flag which if true only executes your change.\\n\\n1. Bug</span>\"\n    },\n    {\n        \"id\": \"\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">A single missing '#' in his code \\\"stopped Amazon delivery system for a day\\\".\\n\\nHe is right I was the delivery guy. we were waiting for Babbar bhaiya to add '#'.</span>\"\n    },\n    {\n        \"id\": \"id__8bn89q5yszh\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Nick Fuentes mugshot has been released</span>\"\n    },\n    {\n        \"id\": \"id__9zzl767mgw\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Keanu Reeves wasn't pretending to be John Wick </span><img alt=\\\"😳\\\" draggable=\\\"false\\\" src=\\\"https://abs-0.twimg.com/emoji/v2/svg/1f633.svg\\\" class=\\\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\\\">\"\n    },\n    {\n        \"id\": \"id__8v83yn7hv1q\",\n        \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Jet suit paramedics can fly to the top of Helvellyn in just 3.5 minutes instead of the usual 1 hour 15 minutes.</span>\"\n    }\n]\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n[\n  {\n    \"id\": \"id__g17ov29ydar\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">you just won $50 million and your lifelong friend says “we’re rich” what do you say back?</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Positive\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__yk3gc3k8lhl\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">For any college student reading this, here’s how a typical production release looks like, specifically with a customer facing feature in a big Org such as Amazon. \\n\\n0. Any new feature/change you push is mostly under a feature flag which if true only executes your change.\\n\\n1. Bug</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Neutral\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">A single missing '#' in his code \\\"stopped Amazon delivery system for a day\\\".\\n\\nHe is right I was the delivery guy. we were waiting for Babbar bhaiya to add '#'.</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Humorous/Sarcastic\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__8bn89q5yszh\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Nick Fuentes mugshot has been released</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Neutral\",\n      \"is_fake\": \"Not Sure\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__9zzl767mgw\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Keanu Reeves wasn't pretending to be John Wick </span><img alt=\\\"😳\\\" draggable=\\\"false\\\" src=\\\"https://abs-0.twimg.com/emoji/v2/svg/1f633.svg\\\" class=\\\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\\\">\",\n    \"result\": {\n      \"sentiment_analysis\": \"Humorous/Sarcastic\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__8v83yn7hv1q\",\n    \"txt\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Jet suit paramedics can fly to the top of Helvellyn in just 3.5 minutes instead of the usual 1 hour 15 minutes.</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Positive\",\n      \"is_fake\": \"True\",\n      \"sources\": [\n        \"https://www.youtube.com/watch?v=jQ9T-WVsNr0\",\n        \"https://www.euronews.com/green/2022/05/31/jetpack-rescue-paramedic-flies-to-the-top-of-a-mountain-in-3-minutes\",\n        \"https://freethink.com/technology/jet-suit-paramedic\",\n        \"https://base-mag.com/jet-suit-takes-on-helvellyn/\"\n      ]\n    }\n  }\n]\n```\n",
      ],
    },
  ]
)


test = [
  {
    "id": "id__7mu5kalat18",
    "txt": "BREAKING: Elon Musk met with Giorgia Meloni and Donald Trump tonight.",
    "result": {
      "sentiment_analysis": "Informative, slightly sensational",
      "is_fake": "Not verified",
      "sources": []
    }
  },
  {
    "id": "id__hn8rkzy0uxr",
    "txt": "Jim Carrey on playing both Gerald and Ivo Robotnik in ‘SONIC 3’:\n\n“I was excited to do 2 Robotniks until I found out it would be twice the work & the same salary”",
    "result": {
      "sentiment_analysis": "Humorous, slightly cynical",
      "is_fake": "Not a claim",
      "sources": []
    }
  },
  {
    "id": "id__qi5ci8pvgys",
    "txt": "React apps are still using class components in 2024",
    "result": {
      "sentiment_analysis": "Slightly negative, surprised",
      "is_fake": False,
      "sources": []
    }
  },
  {
    "id": "id__7a7bsxv4uov",
    "txt": "💻DAY 20 Stay consistent, solve problems, and keep learning! 📷 #geekstreak2024 #gfg160 #gfgdsachallenge",
    "result": {
      "sentiment_analysis": "Positive, motivational",
      "is_fake": True,
      "sources": []
    }
  },
  {
    "id": "id__pmy3aj246pb",
    "txt": "you only grow when you\nare alone",
    "result": {
      "sentiment_analysis": "Reflective, slightly melancholic",
      "is_fake": True,
      "sources": []
    }
  },
  {
    "id": "id__0ujnyuh8upmk",
    "txt": "A new beginning for ourselves.",
    "result": {
      "sentiment_analysis": "Positive, hopeful",
      "is_fake": "Not a claim",
      "sources": []
    }
  }
]


def askGemini(tweetsarray):
  # try:
  #   response = chat_session.send_message(tweetsarray)
  # except(exceptions.ResourceExhausted):
  return test


