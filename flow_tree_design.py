import time
import os
from flow_trees_design_single import generate_single_design


def generate(app_flow_trees: list[str], output_file: str = "all_design_specs.md"):
    """
    Generate and collect detailed Android design specifications for multiple apps.
    Saves all specs into a single Markdown file (append mode).

    Parameters:
        app_flow_trees (list[str]): List of app flow tree JSON strings.
        output_file (str): Path to the combined Markdown file.
    """

    # Initialize output file
    if not os.path.exists(output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Combined Android Design Specifications\n\n")

    all_designs = []

    for i, app_flow_tree in enumerate(app_flow_trees, 1):
        app_name = f"App_{i}" 

        print(f"\n{'='*70}")
        print(f"Processing app {i}/{len(app_flow_trees)}")
        print(f"{'='*70}\n")

        try:
        
            from io import StringIO
            import sys

            buffer = StringIO()
            stdout_backup = sys.stdout
            sys.stdout = buffer

            try:
                generate_single_design(app_flow_tree)
            finally:
                sys.stdout = stdout_backup

            design_result = buffer.getvalue().strip()
            buffer.close()

            # Save each design to file immediately
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"\n\n{'='*60}\n")
                f.write(f"## APP {i}: {app_name}\n")
                f.write(f"{'='*60}\n\n")
                f.write(design_result)
                f.write("\n\n---\n")

            print(f"✅ {app_name}: Design specification generated successfully.")

            all_designs.append({
                "app_index": i,
                "design_spec": design_result
            })

        except Exception as e:
            print(f"❌ Error generating design for {app_name}: {e}")
            all_designs.append({
                "app_index": i,
                "error": str(e)
            })

        # Optional delay between API calls
        if i < len(app_flow_trees):
            print("\n⏳ Waiting before next app...")
            time.sleep(2)

    print(f"\n✅ All design specifications saved to: {os.path.abspath(output_file)}")
    return all_designs
