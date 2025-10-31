import os
from google import genai
from google.genai import types
import io
from contextlib import redirect_stdout


def summarize_prd(prd_text: str) -> str:
    """
    Summarizes a PRD document to extract key features, requirements, and design-critical information.
    
    Args:
        prd_text: The full text content extracted from the PRD PDF
        
    Returns:
        A structured summary of the PRD highlighting main features and key points
    """
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""You are provided with a Product Requirements Document (PRD) for a mobile application.

────────────────────────────
PRD DOCUMENT
────────────────────────────
{prd_text}

────────────────────────────
TASK
────────────────────────────
Analyze this PRD and create a **comprehensive, structured summary** that extracts all information critical for UI/UX design and app flow generation.

Your summary must include:

1. **Core Product Vision**
   - What problem does this app solve?
   - Who are the target users?
   - What is the unique value proposition?

2. **Key Features & Functionality**
   - List ALL major features mentioned
   - For each feature, note any specific requirements or constraints
   - Highlight priority/critical features

3. **User Flows & Journeys**
   - Primary user tasks and goals
   - Key user scenarios mentioned
   - Expected user interactions

4. **Technical Requirements**
   - Platform specifications (iOS/Android/Web)
   - Integration requirements (APIs, third-party services)
   - Performance or security requirements relevant to UX

5. **Design Requirements**
   - Branding guidelines or design constraints
   - Accessibility requirements
   - Any specific UI/UX patterns mentioned

6. **Business Rules & Logic**
   - Important business constraints
   - User permissions/roles
   - Data handling requirements affecting UX

Output your summary in a clear, structured markdown format that can be easily parsed and used as input for design generation.
"""),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=4096,
        ),
        max_output_tokens=8192,
        system_instruction=[
            types.Part.from_text(text="""You are a **Senior Product Analyst and UX Strategist** specializing in distilling Product Requirements Documents into actionable design briefs.

Your role is to:
1. Extract and organize all design-critical information from PRDs
2. Identify feature priorities and dependencies
3. Translate business requirements into UX considerations
4. Present information in a structured format optimized for design tools

**Output Guidelines:**
- Be comprehensive but concise
- Prioritize information relevant to UI/UX design
- Maintain original terminology and feature names
- Flag any ambiguities or missing information
- Use clear markdown formatting with headers and bullet points
- Focus on what needs to be built, not how to build it technically
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
    
    # Save the summary to a file for reference
    with open("prd_summary.md", "w", encoding="utf-8") as f:
        f.write(result)
    
    print("\n✅ PRD summary saved to prd_summary.md")
    
    return result