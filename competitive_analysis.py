import os
from google import genai
from google.genai import types
import io
import json
from contextlib import redirect_stdout
import sys 
from dotenv import load_dotenv

load_dotenv()

def generate(app_description: str):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""You are a top-tier Android app market research analyst. Your task is to identify the top 3 Android apps that are most functionally and semantically similar and highly relevant to the target app described below.

INPUT:
Target App Description: {app_description}

MANDATORY FILTERS:

Exclude any app with fewer than 100,000 downloads.

Ensure each app is unique by package ID and official name.

Output exactly 3 apps. Deduplicate any repeated apps.

METHOD (Advanced & Structured):

Determine the precise market category and core functionality of the target app.

Research globally across authoritative sources (Google Play Store, data.ai, Sensor Tower, SimilarWeb, app review sites, tech press).

For each candidate app, internally perform:

Chain-of-Thought (CoT) reasoning to evaluate functional and semantic similarity and relevance.

Step-back reasoning to double-check any borderline cases.

Internal comparison to known benchmark apps for accurate ranking.

Verify for each candidate app:

Official app name exactly as listed in verified stores.

Estimated download count (must be ≥100,000; use lower bound of Play Store install range, e.g., "1M+" → 1000000).

Functional similarity and market relevance.

Output ONLY the JSON object conforming exactly to the schema below. No extra text, no markdown, no commentary.
⚠️ **Do NOT include:**
- Markdown formatting (e.g., ```json, ```)

OUTPUT SCHEMA:
{{
"type": "object",
"properties": {{
"apps": {{
"type": "array",
"description": "List of the top 3 Android apps that are functionally similar, popular, and market-relevant to the target app. Each entry must represent a real, existing app with verified data.",
"items": {{
"type": "object",
"properties": {{
"app_name": {{
"type": "string",
"description": "The official, publicly listed name of the Android app exactly as it appears on the Google Play Store or verified app marketplace (no placeholders, no partial names)."
}},
"estimated_download_count": {{
"type": "integer",
"description": "The most accurate publicly available estimated total number of downloads for the app, sourced from the Play Store or other verified analytics platforms. Must represent realistic download figures, not rough guesses."
}}
}},
"required": ["app_name", "estimated_download_count"],
"additionalProperties": false
}},
"minItems": 3,
"maxItems": 3
}}
}},
"required": ["apps"],
"additionalProperties": false
}}

FINAL INSTRUCTION:
Perform the task for the target app description and return ONLY the JSON object above, fully populated with verified data."""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=8192,
        ),
        max_output_tokens=65536,
        system_instruction=[
            types.Part.from_text(text="""You are a world-class Android app market research specialist and competitive intelligence expert with mastery in advanced AI reasoning techniques.

Responsibilities:
1. Identify, verify, and rank the top Android apps that are most functionally and semantically similar, popular, and market-relevant to a given target app.
2. Use multiple authoritative sources (Google Play Store, data.ai, Sensor Tower, SimilarWeb, app review sites, tech press) to validate app existence, download counts, and core features.
3. Apply advanced reasoning techniques internally to ensure precision:
   - Chain-of-Thought (CoT): Break down functional similarity, popularity, and relevance for each candidate app.
   - Step-back reasoning: Double-check any app that might not fully match the target’s core functionality.
4. Strictly adhere to the user’s output instructions.
5. Confirm uniqueness of each app by package ID and official app name.
6. Output must strictly conform to the provided JSON schema and format. No extra text, commentary, or markdown is allowed.
"""),
        ],
    )

    # for chunk in client.models.generate_content_stream(
    #     model=model,
    #     contents=contents,
    #     config=generate_content_config,
    # ):
    #     print(chunk.text, end="")
    output = io.StringIO()
    with redirect_stdout(output):
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
    
    json_output = output.getvalue()
    
    # Parse JSON and return
    try:
        return json.loads(json_output)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        print(f"Raw output: {json_output}", file=sys.stderr)
        raise

def extract_app_names(similar_apps_data: dict) -> list[str]:
    """
    Pre-processing function: Extract app names from File 1 output.
    
    Args:
        similar_apps_data: JSON object from generate_similar_apps()
        
    Returns:
        List of app names as strings
    """
    if "apps" not in similar_apps_data:
        raise ValueError("Invalid input: 'apps' key not found in data")
    
    app_names = [app["app_name"] for app in similar_apps_data["apps"]]
    
    return app_names


