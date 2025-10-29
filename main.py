from competitive_analysis import generate as generate_similar_apps, extract_app_names
from flow_tree_service import generate as generate
from app_flow import generate_flow_tree as generate_flow_tree

def generate_complete_pipeline(app_description: str, app_name: str) -> dict:
    """
    Complete pipeline for Streamlit integration.
    Returns both competitor apps and their screen flows.
    
    Args:
        app_description: Description of target app
        
    Returns:
        dict with:
            - competitor_apps: list of competitor app data
            - screen_flows: JSON string of screen flows
    """
    # Step 1: Generate similar apps
    similar_apps_data = generate_similar_apps(app_description)
    
    # Step 2: Extract app names
    app_names = extract_app_names(similar_apps_data)
    
    # Step 3: Generate screen flows
    screen_flows_json = generate(app_names)

    # Step 4: Generate app flow tree
    app_flow_tree = generate_flow_tree(
        app_name=app_name,
        app_description=app_description,
        app_flow_trees=screen_flows_json
    )
    
    return {
        "competitor_apps": similar_apps_data,
        "app_names": app_names,
        "screen_flows": screen_flows_json,
        "app_flow_tree": app_flow_tree  
    }

#testing
if __name__ == "__main__":
    app_description = "WealthNest is a next-gen finance android app that helps users build financial stability by automatically analyzing income, expenses, and habits to create personalized savings and investment plans — all within a simple, intuitive interface."
    app_name = "WealthNest"
    result = generate_complete_pipeline(app_description, app_name)
    print(result)

