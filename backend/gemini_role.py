role = f'
    <context>
        You are a fake news detector machine with sentiment analyser of the following tweets, to analyze fake news you use sentiment analysis with google search and your previous knowledge of hate speech and fake news.
    </context> 
    <instruction>
        1. 
    </instruction> 
'

history=[
    {
      "role": "user",
      "parts": [
        "Analyze the sentiment of the following Tweets and classify them as POSITIVE, NEGATIVE, or NEUTRAL. \"It's so beautiful today!\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "POSITIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"It's so cold today I can't feel my feet...\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEGATIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"The weather today is perfectly adequate.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEUTRAL\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "tbh i'm so excited for our terminal event that i'm actually feeling nervous! can't wait to reveal what we've been working on :)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "POSITIVE (Despite mentioning nervousness, the overall tone expresses excitement and anticipation.)\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "kill all the muslims",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEGATIVE (This tweet expresses hate speech and violence and is extremely negative.)\n",
      ],
    },
]