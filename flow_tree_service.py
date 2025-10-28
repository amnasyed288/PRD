import os
from google import genai
from google.genai import types
from competitive_analysis import generate as generate_similar_apps, extract_app_names
import io
from contextlib import redirect_stdout
from dotenv import load_dotenv

load_dotenv()


def generate(app_names:list[str]):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    app_list_formatted = "\n\n".join(app_names)
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""Generate the complete, accurate, and fully hierarchical screen flow tree for the following Android app:

    {app_list_formatted}

────────────────────────────
INSTRUCTIONS
────────────────────────────

Access the Mobbin platform and locate the app.

Navigate to its Flows section and extract:

The entire unified Flow Tree, or

All individual flows if not unified.

Capture every screen, user action, and transition exactly as documented.

Do not perform general web searches or infer flows from unrelated sources.

Only supplement with verified UX sources specific to the app(e.g., official app case studies, app teardowns, app product demos, app walkthroughs). No approximations.


Do not skip, summarize, hallucinate, or omit any screens, actions, or transitions.

Return one valid JSON object following the given schema — nothing else.

────────────────────────────
VALIDATION CHECKS
────────────────────────────
✅ All transitions are valid and resolvable.
✅ All screens have at least one user action.
✅ JSON passes full schema compliance.

────────────────────────────
OUTPUT FORMAT
────────────────────────────
Return only one JSON object with root key "apps_screen_flows". No commentary, explanation, or prose."""),
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
            types.Part.from_text(text="""You are a senior Mobile UX Research Analyst and Product Flow Architect.
Your mission is to extract the complete, accurate, and verifiable end-to-end screen flow trees for multiple Android apps.

Each flow tree must reflect the app’s true real-world user experience, never summaries, guesses, or approximations. These flow trees will directly feed an AI system that designs new products — completeness and correctness are critical.

────────────────────────────
INTERNAL OPERATING PROTOCOL (Never Output)
────────────────────────────

PHASE 1 — Source Discovery

Search each app on the Mobbin platform.

Navigate to its Flows section.

Extract:

The entire Flow Tree if unified.

All individual flows if separate.

Capture every screen, user action, and transition exactly as documented.

Do not infer flows or generate approximations. Only extract what is verified.

PHASE 2 — Source Fusion

Combine all extracted flows into a single unified hierarchical flow tree.

Maintain strict hierarchy:
main_flow → sub_flow → screens → actions → next_screen.

PHASE 3 — Verified External Completion (Strict Rules)

Only supplement if Mobbin lacks a flow, using official or verified UX sources specific to the app (e.g., official product demos, app teardowns, walkthroughs).

Never infer or hallucinate missing screens, actions, or transitions.

PHASE 4 — Structural & Semantic Validation

Ensure no broken links — every \"next_screen\" exists in \"screens\".

Every flow must have ≥ 1 screen; every screen must have ≥ 1 action or \"end_state\": true.

Validate strict JSON syntax and full schema compliance.

Remove duplicate screens; normalize names (consistent casing/spacing).

PHASE 5 — Self-Verification Loop

Only output the flow tree once fully verified end-to-end.

Cover the app depthwise and breadthwise completely.

────────────────────────────
OUTPUT REQUIREMENTS
────────────────────────────

Return a single valid JSON object only conforming exactly to the schema below. No extra text, no markdown, no commentary.

Root key: \"apps_screen_flows\".

JSON must be hierarchical, exhaustive, and syntactically valid.

Do not include any commentary, explanations, or prose.

────────────────────────────
OUTPUT STRUCTURE (Enforced Schema)
────────────────────────────

{
  \"apps_screen_flows\": [
    {
      \"app_name\": \"string\",
      \"app_screen_flows\": [
        {
          \"flow_name\": \"string\",
          \"screens\": [
            {
              \"screen_name\": \"string\",
              \"actions\": [
                {
                  \"user_action\": \"string\",
                  \"next_screen\": \"string\",
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
────────────────────────────
QUALITY CONSTRAINTS (MANDATORY)
────────────────────────────
✅ No empty lists, missing keys, or incomplete branches.
✅ Maintain full screen hierarchy: flow → screen → action → next.
✅ Never skip, summarize, or hallucinate.
✅ Only output one JSON object per app.

────────────────────────────
FEW-SHOT EXAMPLES (Partial, illustrative)
────────────────────────────
{ \"app_name\": \"Instagram\", \"app_screen_flows\": [ { \"flow_name\": \"Authentication Flow\",\"screens\": [ { \"screen_name\": \"Splash Screen\", \"actions\": [ { \"user_action\": \"Wait 3s\", \"next_screen\": \"Login / Signup Screen\"} ] }, { \"screen_name\": \"Login / Signup Screen\", \"actions\": [ { \"user_action\": \"Login with Facebook\", \"next_screen\": \"Home Feed Screen\"}, { \"user_action\": \"Sign Up\", \"next_screen\": \"Username Creation Screen\"} ] } ] }, { \"flow_name\": \"Main Interaction Flow\", \"screens\": [ { \"screen_name\": \"Home Feed Screen\", \"actions\": [ { \"user_action\": \"Scroll Feed\", \"next_screen\": \"Post Detail Screen\"}, { \"user_action\": \"Tap Reel Icon\", \"next_screen\": \"Reels Viewer Screen\"} ] }, { \"screen_name\": \"Post Detail Screen\", \"actions\": [ { \"user_action\": \"Tap Profile Picture\", \"next_screen\": \"Profile Screen\"} ] } ] }, { \"flow_name\": \"Profile & Settings Flow\",\"screens\": [ { \"screen_name\": \"Profile Screen\", \"actions\": [ { \"user_action\": \"Tap Menu\", \"next_screen\": \"Settings Screen\"}, { \"user_action\": \"Edit Profile\", \"next_screen\": \"Edit Profile Screen\"} ] } ] } ] }"""),
        ],
    )

    # Capture the output
    output = io.StringIO()
    with redirect_stdout(output):
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
    
    return output.getvalue()



# if __name__ == "__main__":
#     # Example usage
#     target_app_description = ""
#     result = generate_complete_pipeline(target_app_description)
    
#     print("=" * 60)
#     print("COMPETITOR APPS:")
#     print("=" * 60)
#     print(json.dumps(result["competitor_apps"], indent=2))
    
#     print("\n" + "=" * 60)
#     print("SCREEN FLOWS:")
#     print("=" * 60)
#     print(result["screen_flows"])