import os
import io
from google import genai
from google.genai import types
from contextlib import redirect_stdout
from dotenv import load_dotenv

load_dotenv()


def generate_single_app_flow(app_name: str):
    """
    Generate a verified, complete app screen flow tree using Mobbin and official sources.
    """

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    model = "gemini-2.5-pro"

    user_prompt = f"""
    Generate a complete, verified, and hierarchical screen flow JSON for the Android app "{app_name}".

    Primary source: mobbin.com → search "{app_name}" → Flows tab.
    If not found or incomplete, use only verified, app-specific sources:
    • Official product or UX documentation
    • Official demo or feature videos
    • App store screenshots/descriptions
    • Case studies about this exact app

    Never use generic UX patterns or other apps’ data.

    Extract all flows: Authentication, Onboarding, Navigation, Features, Search, Settings, Profile, Notifications, etc.

    For each flow, include every screen, all user actions, transitions, and conditions.

    Output strictly in JSON:
    {{
      "app_screen_flow": {{
        "app_name": "{app_name}",
        "total_flows": int,
        "total_screens": int,
        "flows": [
          {{
            "flow_name": "string",
            "screens": [
              {{
                "screen_name": "string",
                "actions": [
                  {{
                    "user_action": "string (specific)",
                    "next_screen": "string",
                  }}
                ]
              }}
            ]
          }}
        ]
      }}
    }}

    Rules:
    1. Only JSON (no markdown or prose)
    2. All next_screen refs must exist
    3. Each screen has ≥1 action or marked end_state
    4. No truncation, ellipses, or summaries
    5. Output must be complete in a single JSON object
    """

    system_instruction = """
    You are a Mobile UX Flow Analyst.
    Task: produce a complete, factual app flow JSON for real Android apps.

    Always prioritize Mobbin data; if missing, use only official or app-specific verified sources.
    Never infer or guess screens.

    Output: valid JSON only (no markdown, no text outside JSON).
    Ensure all references and transitions are consistent and complete.
    """

    contents = [types.Content(role="user", parts=[types.Part.from_text(text=user_prompt)])]
    tools = [types.Tool(googleSearch=types.GoogleSearch())]

    config = types.GenerateContentConfig(
        temperature=0,
        top_p=1,
        max_output_tokens=65536,
        tools=tools,
        system_instruction=[types.Part.from_text(text=system_instruction)],
    )

    output = io.StringIO()
    full_response = []

    try:
        with redirect_stdout(output):
            for chunk in client.models.generate_content_stream(
                model=model, contents=contents, config=config
            ):
                if chunk.text:
                    print(chunk.text, end="")
                    full_response.append(chunk.text)

        complete_output = output.getvalue().strip()

        if complete_output.startswith("```"):
            complete_output = complete_output.strip("`").strip()

        return complete_output

    except Exception as e:
        print(f"\n⚠️ Error during streaming: {e}")
        return output.getvalue() or "".join(full_response)

#testing
if __name__ == "__main__":
    result = generate_single_app_flow("Duolingo")
    print(result)