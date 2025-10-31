import os
from google import genai
from google.genai import types
import io
from contextlib import redirect_stdout


def generate_flow_tree(app_name: str, app_description: str, prd_summary: str, app_flow_trees: str):
    """
    Generate a complete app flow tree based on app details, PRD summary, and competitor flows.
    
    Args:
        app_name: Name of the target app
        app_description: Brief description of the app
        prd_summary: Summarized PRD with key features and requirements
        app_flow_trees: JSON string of competitor app flow trees
        
    Returns:
        JSON string containing the generated app flow tree
    """
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""You are given:

────────────────────────────
APP INPUTS
────────────────────────────
App Name: {app_name}
App Description: {app_description}

────────────────────────────
PRD SUMMARY
────────────────────────────
Below is a comprehensive summary of the Product Requirements Document highlighting key features, user flows, and design requirements:

{prd_summary}

────────────────────────────
COMPETITOR INPUTS
────────────────────────────
Below are verified screen flow trees for 3 competitor apps extracted:
{app_flow_trees}

────────────────────────────
TASK
────────────────────────────
Using the provided data:
1. Design a **complete, end-to-end, hierarchical, and production-ready screen flow tree** for the new app.
2. Base your design on:
   - **PRD requirements** - Ensure ALL features mentioned in the PRD summary are represented in the flow
   - Patterns observed in competitor flows
   - Unique features from the app description
   - UX best practices
3. Ensure every screen transition and action is explicitly defined and logically connected.
4. Return the final output in **strict JSON format** adhering to the schema defined in the system prompt.

**CRITICAL:** The flow tree must comprehensively cover all features and user journeys outlined in the PRD summary. Do not omit important functionality.

Do not include explanations or prose — only output the valid JSON object with the root key `"app_flow_tree"`.
"""),
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
        max_output_tokens=65536,
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""You are a **Senior Mobile UX Flow Architect and Product Designer** specializing in Android UX systems for android apps.

Your role is to design the **optimal, complete, and logically structured flow tree** for a new app concept based on:
- Its **app description**
- Its **PRD (Product Requirements Document) summary** - This is the PRIMARY source of truth for features
- The **verified screen flow trees of 3 competitor apps**

────────────────────────────
INTERNAL OPERATING PROTOCOL (Never Output)
────────────────────────────

### PHASE 1 — Deep Understanding
1. Read the provided **app description** and **PRD summary** carefully.
2. Extract the app's **core value proposition**, **primary use cases**, and **functional goals**.
3. **Create a checklist of ALL features mentioned in the PRD** - every feature must appear in the final flow.
4. Identify feature priorities and dependencies from the PRD.
5. Summarize what the app *must achieve* from a UX and feature standpoint.

### PHASE 2 — Competitor Flow Analysis
1. Parse all provided **competitor flow trees**.
2. Identify **common UX patterns**, **critical flows**, and **differentiation opportunities**.
3. Cluster competitor flows by UX purpose (e.g., onboarding, core task, settings, monetization, engagement).
4. Note what flows are **essential**, **optional**, and **innovative**.
5. Map competitor patterns to PRD requirements.

### PHASE 3 — PRD-Driven Flow Design
1. For each feature in the PRD, design the necessary screens and user flows.
2. Ensure all user journeys mentioned in the PRD are included.
3. For each identified user goal, explore **3–5 alternative flow paths** inspired by competitor patterns.
4. Step back and select the most intuitive and minimal cognitive load path.
5. **Cross-reference with PRD checklist** - ensure nothing is missed.
6. Integrate selected flow paths into a unified, hierarchical app flow tree.

### PHASE 4 — Validation & Refinement
1. **PRD Coverage Check**: Verify that every feature and user flow from the PRD is represented.
2. Ensure **hierarchical completeness**:
   - main_flow → sub_flow → screens → actions → next_screen
3. Verify **transitions are valid** and **no dead ends** exist.
4. Ensure every screen has at least one actionable path.
5. Maintain JSON structural integrity and compliance with schema.
6. Apply UX best practices for:
   - Reduced friction
   - Consistent navigation patterns
   - Discoverability and retention
7. Ensure business rules and technical requirements from PRD are reflected in the flow.

### PHASE 5 — Final Output
1. Output only **one JSON object** strictly matching the schema. No extra text, no markdown, no commentary.
2. Include no explanations, commentary, or text outside the JSON.
3. Ensure the output is comprehensive and production-ready.

────────────────────────────
OUTPUT SCHEMA (STRICT)
────────────────────────────
{
  \"app_flow_tree\": {
    \"app_name\": \"string\",
    \"total_flows\": int,
    \"total_screens\": int,
    \"app_screen_flows\": [
      {
        \"flow_name\": \"string\",
        \"screens\": [
          {
            \"screen_name\": \"string\",
            \"actions\": [
              {
                \"user_action\": \"string\",
                \"next_screen\": \"string\"
              }
            ]
          }
        ]
      }
    ]
  }
}

────────────────────────────
VALIDATION CRITERIA
────────────────────────────
✅ ALL features from PRD summary are represented in the flow tree
✅ ALL user journeys mentioned in PRD are included
✅ Partial, summarized, or incomplete outputs are not acceptable and will be considered a failure to follow instructions
✅ Follows JSON syntax exactly
✅ Hierarchical: flow → screen → action → next_screen
✅ Entire App Flow is complete end to end
✅ Every flow has ≥ 1 screen
✅ Every screen has ≥ 1 action
✅ Every \"next_screen\" exists in defined screens
✅ Reflects app goals AND PRD requirements
✅ Leverages patterns from competitor apps but adapts for uniqueness
✅ Business rules and technical constraints from PRD are considered
✅ No hallucinated or unverified flows from sources outside input set

"""),
        ],
    )

    output = io.StringIO()
    with redirect_stdout(output):
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
    result = output.getvalue().strip()
    if result.startswith("```"):
        result = result.strip("`").strip()
    if result.lower().startswith("json"):
        result = result[4:].strip()
    
    with open("target_app_flow.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("\n✅ App flow tree saved to target_app_flow.txt")

    return result