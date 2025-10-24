user_prompt="""Generate the screen flow tree for the Airbnb android app.

First, search for "Airbnb" on Mobbin.

Go to the Flows section and extract the entire flow tree exactly as presented under the Flow Tree heading.

Capture all screens, branches, and user actions exactly as shown.

Only if the flow tree is unavailable on Mobbin, use high-quality web sources top extract the app flow tree.

Do not invent, assume, or omit any flows.

Output the result as a single, valid JSON object with the root key "app_screen_flows", containing a list with Airbnb's flow tree.
No commentary, explanations, or extra text outside the JSON."""


# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=8192,
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""You are an UI/UX Researcher who's tasked to research and find the end to end accurate and complete flow tree for the given app.
Give the response in json format."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
