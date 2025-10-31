from competitive_analysis import generate as generate_similar_apps, extract_app_names
from flow_tree_service import generate as generate
from app_flow import generate_flow_tree as generate_flow_tree
from flow_tree_design import generate as generate_design_specs
from target_app_design import generate as generate_target_design
import os
from io import StringIO
import sys

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
    print(f"App names:\n\n {app_names}")

    
    # Step 3: Generate screen flows
    screen_flows_json = generate(app_names)

    
    # Step 4: Generate app flow tree
    app_flow_tree = generate_flow_tree(
        app_name=app_name,
        app_description=app_description,
        app_flow_trees=screen_flows_json
    )

    # Step 5: generate design specs of all apps
    output_md = "all_design_specs.md"
    designs = generate_design_specs(app_flow_trees=screen_flows_json,output_file = output_md)

    if not os.path.exists(output_md):
        raise FileNotFoundError(f"Expected file '{output_md}' not found after design spec generation.")

    with open(output_md, "r", encoding="utf-8") as f:
        designs_text = f.read().strip()

    print(f"\n🎨 Generating final target design spec for: {app_name}\n")

    # Step 6: Generate design specs for the target app
    buffer = StringIO()
    stdout_backup = sys.stdout
    sys.stdout = buffer

    try:
        generate_target_design(app_flow_tree=app_flow_tree, designs=designs_text)
    finally:
        sys.stdout = stdout_backup

    target_design_spec = buffer.getvalue().strip()
    buffer.close()

    # Save final design spec to Markdown
    target_output_md = f"{app_name}_final_design_spec.md"
    with open(target_output_md, "w", encoding="utf-8") as f:
        f.write(target_design_spec)

    print(f"✅ Target design spec saved to: {os.path.abspath(target_output_md)}")

    # Final combined result
    return {
        "competitor_apps": similar_apps_data,
        "app_names": app_names,
        "screen_flows": screen_flows_json,
        "app_flow_tree": app_flow_tree,
        "design_specs": designs,
        "target_design_spec": target_design_spec,
    }

#testing
if __name__ == "__main__":
    app_description = "WealthNest is a next-gen finance android app that helps users build financial stability by automatically analyzing income, expenses, and habits to create personalized savings and investment plans — all within a simple, intuitive interface."
    app_name = "WealthNest"
    generate_complete_pipeline(app_description, app_name)
   

