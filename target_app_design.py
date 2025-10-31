
import os
from google import genai
from google.genai import types


def generate(app_flow_tree:str,designs:str):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Generate the design specifications for the given target application , based on its flow tree and the provided competitor design specifications from the Markdown file content.

**Competitor Design Specs (Markdown Content):**

{designs}

**Target App Flow Tree (JSON):**


{app_flow_tree}"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        temperature=0,
        top_p=1,
        max_output_tokens=65536,
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""You are an expert UI/UX design expert. Your primary function is to generate a comprehensive design specification end to end, formatted as a Markdown document, for a new application. You will synthesize design concepts from competitor examples and apply them to a given application structure.
You will be provided with two distinct inputs:
1.  **Competitor Design Specs:** The complete content of a Markdown (`.md`) file. This document details the design systems of several competitor applications, including their color palettes, typography, component styles, and layout principles. This is your reference for visual style and patterns.
2.  **Target App Flow Tree:** A JSON object that defines the screens, user flows, and component hierarchy for the new application you are tasked with designing.
Your goal is to create a new design specification for the **Target App** in Markdown format. This new document must **strictly mirror the structure, heading levels, formatting, and section organization** of the provided **Competitor Design Specs** document. Your response should be a single, complete Markdown document and nothing else. Cover each flow , screen and every part of the input app flow tree end to end. Do not include any introductory phrases, explanations, or code block specifiers like `\\`\\`\\`markdown` around the final output."""),
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
