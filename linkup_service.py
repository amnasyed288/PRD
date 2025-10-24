from linkup import LinkupClient
from config import LINKUP_API_KEY


# -----------------------------------------------------------------------------------
# 1. CONSTANTS — PROMPT & STRUCTURED OUTPUT SCHEMA
# -----------------------------------------------------------------------------------

LINKUP_PROMPT = """You are a specialist in android app market research. Your task is to identify the top 10 most functionally similar and significant Android competitors to a specified target app. 

Goal: Find and list 10 **unique and distinct** Android apps that are directly comparable to the target app in terms of core functionality and market relevance.

Input :
- Target App Description: {app_description}

Method:
1. Determine the precise market category based on the description.
2. Search the entire web for apps in this category.
3. For each candidate app, assess its features, market presence, and user reviews.
4. MANDATORY FILTER 1: Discard and strictly exclude any app with fewer than 100,000 downloads. This is a non-negotiable rule.
5. MANDATORY FILTER 2: Ensure the final list contains **10 unique apps**. Do not include the same app more than once, even if it has a different URL or name variation. Check for duplicate package IDs.
6. From the remaining filtered, unique list, select the 10 apps that best meet all criteria.

Output Format: Return a structured list of exactly 10 unique apps. Provide all the fields specified in the schema. Do not include any commentary."""

LINKUP_OUTPUT_SCHEMA = (
    "{\"type\": \"object\",\"properties\": {\"apps\": {\"type\": \"array\",\"items\": {\"type\": \"object\","
    "\"properties\": {\"app_name\": { \"type\": \"string\" },"
    "\"estimated_download_count\": { \"type\": \"integer\" },"
)

# -----------------------------------------------------------------------------------
# 2. FUNCTION — CALL LINKUP API
# -----------------------------------------------------------------------------------

def find_competitor_apps(app_description: str):
    """
    Calls the Linkup API to identify top 10 competitor Android apps for a given app description.
     Args:
        app_description: The description of the target app.
    Returns:
        A dictionary with structured competitor data if successful, otherwise None.
    """

    FINAL_PROMPT = LINKUP_PROMPT.format(app_description=app_description)
    print(FINAL_PROMPT)

    try:
        client = LinkupClient(api_key=LINKUP_API_KEY)

        response = client.search(
            query=FINAL_PROMPT,
            depth="deep",
            output_type="structured",
            structured_output_schema=LINKUP_OUTPUT_SCHEMA,
            include_images=False,
            include_sources=False,
        )

        if response:
            return response
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

