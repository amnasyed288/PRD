import json
import time
from flow_tree_service_single import generate_single_app_flow
import os


def generate(app_names: list[str], output_file: str = "all_app_flows.txt"):
    """
    Generate and collect screen flow trees for multiple apps.
    Saves all flows into a single text file (append mode).
    """

    all_flows = []
    if not os.path.exists(output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Combined App Flow Trees\n\n")

    for i, app_name in enumerate(app_names, 1):
        print(f"\n{'='*70}")
        print(f"Processing app {i}/{len(app_names)}: {app_name}")
        print(f"{'='*70}\n")

        try:
            flow_result = generate_single_app_flow(app_name)

            # Save immediately to file to avoid loss on crash
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"\n\n{'='*60}\n")
                f.write(f"### APP {i}: {app_name}\n")
                f.write(f"{'='*60}\n")
                f.write(flow_result.strip())
                f.write("\n")

            # Try JSON parsing to validate
            try:
                parsed_flow = json.loads(flow_result)
                flow_data = parsed_flow.get("app_screen_flow", {})
                total_flows = len(flow_data.get("flows", []))
                total_screens = sum(len(f.get("screens", [])) for f in flow_data.get("flows", []))
                print(f"✅ {app_name}: {total_flows} flows, {total_screens} screens")

            except json.JSONDecodeError as e:
                print(f"⚠️ JSON parse error for {app_name}: {e}")

            all_flows.append(flow_result)

        except Exception as e:
            print(f"❌ Error processing {app_name}: {e}")
            all_flows.append({"app_name": app_name, "error": str(e)})

        # Short delay between apps
        if i < len(app_names):
            print("\n⏳ Waiting before next app...")
            time.sleep(2)

    print(f"\n✅ All flows saved to: {os.path.abspath(output_file)}")
    return all_flows


# ======================================================
# 3. EXAMPLE USAGE
# ======================================================
if __name__ == "__main__":
    apps_to_process = ["Spotify", "Airbnb", "Duolingo"]
    generate(apps_to_process)
