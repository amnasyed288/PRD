import os
from google import genai
from google.genai import types
import io
from contextlib import redirect_stdout



def generate_flow_tree(app_name: str, app_description: str, app_flow_trees: str):
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
COMPETITOR INPUTS
────────────────────────────
Below are verified screen flow trees for 10 competitor apps extracted :
{app_flow_trees}
────────────────────────────
TASK
────────────────────────────
Using the provided data:
1. Design a **complete,end-to-end, hierarchical, and production-ready screen flow tree** for the new app.
2. Base your design on:
   - Patterns observed in competitor flows
   - Unique features from app
   - UX best practices
3. Ensure every screen transition and action is explicitly defined and logically connected.
4. Return the final output in **strict JSON format** adhering to the schema defined in the system prompt.

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
- The **verified screen flow trees of 10 competitor apps**

────────────────────────────
INTERNAL OPERATING PROTOCOL (Never Output)
────────────────────────────

### PHASE 1 — Deep Understanding
1. Read the provided **app description** carefully.
2. Extract the app’s **core value proposition**, **primary use cases**, and **functional goals**.
3. Summarize what the app *must achieve* from a UX and feature standpoint.

### PHASE 2 — Competitor Flow Analysis
1. Parse all provided **competitor flow trees**.
2. Identify **common UX patterns**, **critical flows**, and **differentiation opportunities**.
3. Cluster competitor flows by UX purpose (e.g., onboarding, core task, settings, monetization, engagement).
4. Note what flows are **essential**, **optional**, and **innovative**.

### PHASE 3 — Ideation Flow Synthesis (Tree-of-Thought Expansion)
1. For each identified user goal, explore **3–5 alternative flow paths** inspired by competitor patterns.
2. Step back and select the most intuitive and minimal cognitive load path.
3. Integrate selected flow paths into a unified, hierarchical app flow tree.

### PHASE 4 — Validation & Refinement
1. Ensure **hierarchical completeness**:
   - main_flow → sub_flow → screens → actions → next_screen
2. Verify **transitions are valid** and **no dead ends** exist.
3. Ensure every screen has at least one actionable path.
4. Maintain JSON structural integrity and compliance with schema.
5. Apply UX best practices for:
   - Reduced friction
   - Consistent navigation patterns
   - Discoverability and retention

### PHASE 5 — Final Output
1. Output only **one JSON object** strictly matching the schema No extra text, no markdown, no commentary..
2. Include no explanations, commentary, or text outside the JSON.

────────────────────────────
OUTPUT SCHEMA (STRICT)
────────────────────────────
{
  \"app_flow_tree\": {
    \"app_name\": \"string\",
    \"based_on_competitors\": [\"list_of_app_names\"],
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
✅ Follows JSON syntax exactly  
✅ Hierarchical: flow → screen → action → next_screen  
✅ Entire App Flow is complete end to end.
✅ Every flow has ≥ 1 screen  
✅ Every screen has ≥ 1 action  
✅ Every \"next_screen\" exists in defined screens  
✅ Reflects app goals  
✅ Leverages patterns from competitor apps but adapts for uniqueness  
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
    
    return output.getvalue()
