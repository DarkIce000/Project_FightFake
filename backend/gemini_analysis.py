import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from google.api_core import exceptions

API_KEY = "AIzaSyC0RCJ55bgQ-ifdAW_rRLoNd_ru1Z2dCZE"
API_KEY_2 = "AIzaSyCwnrhraD4ZpVzPn2ydtm4UVWkkXogIFI0"

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
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  tools = "google_search_retrieval"
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "<context>\n    You are the fake news detective's assistant. You will be provided with a tweeter's tweet. You have to use google search\n</context>\n<task>\n    if text is claiming something that is happening currently: \n        then you have to perform the fact check\n        <factCheck>\n            1. look for reliable news or more that 3 sources sites covered the story\n            2. if fact check is present on their site \n                look for what is the conclusion, is that \"True news\" or \"Fake news\"?\n                or You could use your learning to find out. \n                else: \n                    if there are no result found about this text, return as \"not verified\"\n        </factCheck>\n        and analyse the sentiment of the text. \n    else: \n        only analyse the sentiment and face check section should be labeled as not a claim\n</task>\n<list of reliable sources>\n    all the trusted sources you know + these followings\n    1. thehindu.com\n    2. aajtak.in\n    3. newslaundary.com\n    4. altnews.in\n    5. nytimes.com\n    6. *.gov.in\n    7. *.gov\n</list of reliable sources>\n<output>\n[\n    {\n        id: Original id given with text, \n        text: Original text given for analysis,\n        result: {\n            sentiment_analysis: \"hate or excitement etc\",\n            is_fake: True or False or Not Sure, \n            sources: [\n                \"source1\",\n                \"source2\",\n                \"source3\",\n                ...list of sources sites where you find the content related to your text\n            ]\n        }\n    },\n    \n    {\n        id: Original id given with text, \n        text: Original text given for analysis,\n        result: {\n            sentiment_analysis: \"hate or excitement etc\",\n            is_fake: True or False or Not Sure, \n            sources: [\n                \"source1\",\n                \"source2\",\n                \"source3\",\n                ...list of sources sites where you find the content related to your text\n            ]\n        }\n    },\n]\n    \n</output>",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n[\n    {\n        \"id\": 1,\n        \"text\": \"I'm seeing news about a major event happening right now.\",\n        \"result\": {\n            \"sentiment_analysis\": \"Neutral\",\n            \"is_fake\": \"Not Sure\",\n            \"sources\": []\n        }\n    }\n]\n```",
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
        "```json\n[\n  {\n    \"id\": \"id__g17ov29ydar\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">you just won $50 million and your lifelong friend says “we’re rich” what do you say back?</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Positive\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__yk3gc3k8lhl\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">For any college student reading this, here’s how a typical production release looks like, specifically with a customer facing feature in a big Org such as Amazon. \\n\\n0. Any new feature/change you push is mostly under a feature flag which if true only executes your change.\\n\\n1. Bug</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Neutral\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">A single missing '#' in his code \\\"stopped Amazon delivery system for a day\\\".\\n\\nHe is right I was the delivery guy. we were waiting for Babbar bhaiya to add '#'.</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Humorous/Sarcastic\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__8bn89q5yszh\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Nick Fuentes mugshot has been released</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Neutral\",\n      \"is_fake\": \"Not Sure\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__9zzl767mgw\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Keanu Reeves wasn't pretending to be John Wick </span><img alt=\\\"😳\\\" draggable=\\\"false\\\" src=\\\"https://abs-0.twimg.com/emoji/v2/svg/1f633.svg\\\" class=\\\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\\\">\",\n    \"result\": {\n      \"sentiment_analysis\": \"Humorous/Sarcastic\",\n      \"is_fake\": \"Not a claim\",\n      \"sources\": []\n    }\n  },\n  {\n    \"id\": \"id__8v83yn7hv1q\",\n    \"text\": \"<span class=\\\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\\\" style=\\\"text-overflow: unset;\\\">Jet suit paramedics can fly to the top of Helvellyn in just 3.5 minutes instead of the usual 1 hour 15 minutes.</span>\",\n    \"result\": {\n      \"sentiment_analysis\": \"Positive\",\n      \"is_fake\": \"True\",\n      \"sources\": [\n        \"https://www.youtube.com/watch?v=jQ9T-WVsNr0\",\n        \"https://www.euronews.com/green/2022/05/31/jetpack-rescue-paramedic-flies-to-the-top-of-a-mountain-in-3-minutes\",\n        \"https://freethink.com/technology/jet-suit-paramedic\",\n        \"https://base-mag.com/jet-suit-takes-on-helvellyn/\"\n      ]\n    }\n  }\n]\n```\n",
      ],
    },
  ]
)

test = [
    {
        "id": "id__u0e5wgo8w4d",
        "text": "<span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">BREAKING: Rapper Jay-Z accused of r*ping a 13-year-old girl in 2000 with Diddy, according to NBC News.\n\nThe incident was previously reported on but the ‘celebrity’ (Jay Z) was not named at the time.\n\nThe incident happened at an MTV Music Awards afterparty after the girl was</span>"
    },
    {
        "id": "id__4zag94cz8ao",
        "text": "<span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">bro can literally give everyone on earth 1 million dollars and still have money left over </span><img alt=\"😭\" draggable=\"false\" src=\"https://abs-0.twimg.com/emoji/v2/svg/1f62d.svg\" title=\"Loudly crying face\" class=\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\">"
    },
    {
        "id": "id__p48gd0k4uja",
        "text": "<span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">The Raspberry Pi 500 launches today, for $90. Raspberry Pi sent one to test, and of course the first thing I did was rip the shell apart to see if it had an M.2 slot inside... </span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/Pi500?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#Pi500</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> </span><img alt=\"🧵\" draggable=\"false\" src=\"https://abs-0.twimg.com/emoji/v2/svg/1f9f5.svg\" title=\"Thread\" class=\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\">"
    },
    {
        "id": "id__fpcjkun74n",
        "text": "<span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">NBC News reports that Jay-Z has been accused of raping a 13-year-old girl with Diddy in 2000, according to a civil lawsuit.</span>"
    },
    {
        "id": "id__o8ilmm09mjr",
        "text": "<img alt=\"✔️\" draggable=\"false\" src=\"https://abs-0.twimg.com/emoji/v2/svg/2714.svg\" title=\"Heavy check mark\" class=\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\"><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> Solved day 87 of n-day </span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/potd?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#potd</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> solution \nAt </span><div class=\"css-175oi2r r-xoduu5\"><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/geeksforgeeks\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">@geeksforgeeks</a></span></div><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> \n\n</span><img alt=\"✔️\" draggable=\"false\" src=\"https://abs-0.twimg.com/emoji/v2/svg/2714.svg\" title=\"Heavy check mark\" class=\"r-4qtqp9 r-dflpy8 r-k4bwe5 r-1kpi4qh r-pp5qcn r-h9hxbl\"><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">Day 23 of 160 days challenge!!\n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/DSA?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#DSA</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> \n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/geekstreak2024?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#geekstreak2024</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> \n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/geeksforgeeks?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#geeksforgeeks</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> \n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/gfg?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#gfg</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">\n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/160days_challenge?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#160days_challenge</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\">\n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/CodingChallenge?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#CodingChallenge</a></span><span class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3\" style=\"text-overflow: unset;\"> \n</span><span class=\"r-18u37iz\"><a dir=\"ltr\" href=\"/hashtag/dsachallenge?src=hashtag_click\" role=\"link\" class=\"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21\" style=\"text-overflow: unset; color: rgb(29, 155, 240);\">#dsachallenge</a></span>"
    }
]

sample_analysis_result =[
    {
        "id": "id__lae4wulxjp",
        "text": "Krunal Pandya was too good in Pushpa 2.",
        "result": {
            "sentiment_analysis": "Positive",
            "confidence_score": 60,
            "extra_comment": "what gemini has extra to say about this text",
            "is_fake": False,
            "sources": [
                "https://www.cinestaan.com/articles/27754/krunal-pandya-the-cricketer-was-not-in-pushpa-the-rule",
                "https://www.republicworld.com/sports-news/cricket-news/ipl-2023-krunal-pandya-reveals-all-about-his-pushpa-celebration-after-dismissing-virat-kohli-articles-119234",
                "https://www.news18.com/cricketnext/news/krunal-pandyas-pushpa-celebration-after-virat-kohlis-wicket-goes-viral-7529279.html"


            ]
        }
    },
    {
        "id": "id__h051bt5l8kr",
        "text": "That's why...🤔",
        "result": {
            "sentiment_analysis": "Neutral",
            "confidence_score": 60,
            "extra_comment": "what gemini think about this text",
            "is_fake": "Not verifiable",
            "sources": []
        }
    },
    {
        "id": "id__bv9ujpab2m",
        "text": "Explorable Todo List",
        "result": {
            "sentiment_analysis": "Neutral",
            "confidence_score": 60,
            "extra_comment": "ai comments about given text",
            "is_fake": "Not verifiable",
            "sources": []
        }
    },
    {
        "id": "id__5qffdw89x5q",
        "text": "source: tech twitter",
        "result": {
            "sentiment_analysis": "Neutral",
            "confidence_score": 60,
            "extra_comment": "ai comments about given text",
            "is_fake": "Not verifiable",
            "sources": []
        }
    },
    {
        "id": "id__oo6pxa080v",
        "text": "We found it in archives. 16 years ago, in 2008, at a summit of Arab leaders in Damascus, Gaddafi, showing the execution of Saddam Hussein, said:",
        "result": {
            "sentiment_analysis": "Neutral",
            "confidence_score": 60,
            "extra_comment": "ai comments about given text", 
            "is_fake": "Not verifiable", 
            "sources": []
        }
    }
]

def askGemini():
#   try:
#     response = chat_session.send_message(str(tweetsarray))
#     print(response)
#   except(exceptions.ResourceExhausted):
#     return "Resource exhausted error"
#   except:
#     return "something went wrong"
# #   return sample_analysis
  return sample_analysis_result

print(askGemini())
# r = askGemini(str(test))
# print(r)