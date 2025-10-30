import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


def generate_single_design(app_flow_trees:str):
    """
    Generate a complete screen-by-screen Android design specification in Markdown format
    using Gemini 2.5 Pro and save the output to a .md file.
    """

    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    model = "gemini-2.5-pro"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"""Generate a complete, end-to-end, hyper-detailed set of screen-by-screen design specifications for the provided android app flow tree. The output must be a single, well-structured Markdown (.md) file.
Crucial Requirement: The output MUST be exhaustive. You are required to document every single flow and screen listed in the input app_screen_flow JSON. The number of screens specified in your final Markdown output must exactly match the total_screens value provided. Partial, summarized, or incomplete outputs are not acceptable and will be considered a failure to follow instructions.
The design specifications must be meticulous and detailed enough for a downstream AI design generation model to create a high-fidelity, interactive prototype that is a faithful representation of the specified application.
The generated design specs must be based on the real, current android version of the provided input app, utilizing Google's Material Design 3 principles as the foundational design system.
Input App Flow Tree:
{app_flow_trees}
Output Requirements:
The output must be a single Markdown file that strictly follows the structure and includes all the detailed specifications as outlined in the \"System Prompt\" instructions you will receive. It is mandatory that every aspect of the provided flow tree is covered with absolute precision and accuracy, reflecting the actual Android design of the input app. The final document must be a single, complete file with no omissions. All specifications should reflect Android-native components and patterns.Dont add any extra information other than the design specification requested."""
                ),
            ],
        ),
    ]

    tools = [types.Tool(googleSearch=types.GoogleSearch())]

    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        top_p=1,
        max_output_tokens=65536,
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=tools,
        system_instruction=[
            types.Part.from_text(
                text="""You are a Senior Product Designer. Your task is to generate a complete and hyper-detailed Android design specification from the user's app flow tree. The output must be a single, actionable Markdown file.
Non-Negotiable Rule: 
You MUST document every single screen listed in the input. The final output must be exhaustive, with no omissions or summaries.
Core Principles:
Platform: Android Mobile, using Material Design 3.
Fidelity: The specification must be detailed enough for an AI to generate a high-fidelity prototype without further input.
Accuracy: All details must reflect the real-world design patterns of a modern Android application.
Output Structure
I. Global Specifications
Platform: Android Mobile App
Design System: Material Design 3 (Light/Dark modes, Material You)
Colors: Key brand/seed color and resulting Material 3 color roles (Primary, Surface, etc.).
Typography: Font family (e.g., Roboto) and Material 3 type scale roles (e.g., Headline Medium).
Spacing: Base grid unit (e.g., 8dp).
Accessibility: Target standard (e.g., WCAG 2.1 AA).
II. Screen Specifications (For each screen)
Screen Name/ID: Unique identifier (e.g., 01_Welcome_Screen).
Dimensions: Viewport size (e.g., 393x852dp).
Background: Material 3 color role (e.g., md.sys.color.background).
Layout: Core structure (e.g., Column, LazyColumn) and key spacing.
III. Component Specifications (For each element on a screen)
Name: Material Design component name (e.g., Filled Button, TopAppBar).
Position & Size: Dimensions (fillMaxWidth, 56dp), alignment, margins, padding, and minimum touch target (48x48dp).
Style: Material 3 color roles, typography roles, icon names (e.g., Icons.Filled.Add), shape, and elevation.
Content: Exact string for text or labels.
IV. Interaction & Behavior
States: Visuals for default, pressed, disabled, etc., using Material Design state layers.
Interactions: User action and resulting navigation/event (e.g., On tap -> Navigate to 03_Home_Screen).
Animations: Screen transitions and motion effects (e.g., MaterialSharedAxis).
Scroll Behavior: How elements react to scrolling (e.g., TopAppBar collapses).
V. Critical Scenarios & States
Error States: Designs for errors (e.g., 'No Internet'). Specify UI (e.g., Snackbar) and messages.
Empty States: Designs for screens with no content. Include text and a primary CTA.
Loading States: Designs for data fetching."""
            ),
        ],
    )

    print(f"\n🚀 Generating detailed design specs... (output will stream below)\n{'='*80}\n")

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if chunk.text:
            print(chunk.text, end="") 
         



