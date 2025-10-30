# To run this code you need to install the following dependency:
# pip install google-genai python-dotenv

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


def generate(output_path: str = "design_spec.md"):
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
                    text="""Your task is to act as a Senior Product Designer and generate a complete, end-to-end, hyper-detailed set of screen-by-screen design specifications for the provided Android application flow tree. The output must be a single, well-structured Markdown (.md) file.
Crucial Requirement: The output MUST be exhaustive. You are required to document every single flow and screen listed in the input app_screen_flow JSON. The number of screens specified in your final Markdown output must exactly match the total_screens value provided. Partial, summarized, or incomplete outputs are not acceptable and will be considered a failure to follow instructions.
The design specifications must be meticulous and detailed enough for a downstream AI design generation model to create a high-fidelity, interactive prototype that is a faithful representation of the specified application.
The generated design specs must be based on the real, current Android version of the input mobile app, utilizing Google's Material Design 3 principles as the foundational design system.
Input App Flow Tree:
{
  "app_screen_flow": {
    "app_name": "Spotify",
    "total_flows": 8,
    "total_screens": 47,
    "flows": [
      {
        "flow_name": "Authentication",
        "screens": [
          {
            "screen_name": "Launch Screen",
            "actions": [
              {
                "user_action": "Taps 'Sign up free' button",
                "next_screen": "Sign Up - Email"
              },
              {
                "user_action": "Taps 'Continue with Google' button",
                "next_screen": "External Google Authentication"
              },
              {
                "user_action": "Taps 'Continue with Facebook' button",
                "next_screen": "External Facebook Authentication"
              },
              {
                "user_action": "Taps 'Log in' button",
                "next_screen": "Log In"
              }
            ]
          },
          {
            "screen_name": "Log In",
            "actions": [
              {
                "user_action": "Enters email and password, taps 'Log in' button",
                "next_screen": "Home"
              },
              {
                "user_action": "Taps 'Log in without password' button",
                "next_screen": "Passwordless Login"
              },
              {
                "user_action": "Taps back arrow",
                "next_screen": "Launch Screen"
              }
            ]
          },
          {
            "screen_name": "Passwordless Login",
            "actions": [
              {
                "user_action": "Enters email or username, taps 'GET LINK' button",
                "next_screen": "Check Your Email"
              },
              {
                "user_action": "Taps back arrow",
                "next_screen": "Log In"
              }
            ]
          },
          {
            "screen_name": "Check Your Email",
            "actions": [
              {
                "user_action": "User must switch to email client to complete login",
                "end_state": true
              }
            ]
          },
          {
            "screen_name": "External Google Authentication",
            "actions": [
              {
                "user_action": "Completes Google sign-in flow",
                "next_screen": "Home"
              }
            ]
          },
          {
            "screen_name": "External Facebook Authentication",
            "actions": [
              {
                "user_action": "Completes Facebook sign-in flow",
                "next_screen": "Home"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Sign Up and Onboarding",
        "screens": [
          {
            "screen_name": "Sign Up - Email",
            "actions": [
              {
                "user_action": "Enters email address, taps 'Next' button",
                "next_screen": "Sign Up - Create Password"
              }
            ]
          },
          {
            "screen_name": "Sign Up - Create Password",
            "actions": [
              {
                "user_action": "Enters password, taps 'Next' button",
                "next_screen": "Sign Up - Date of Birth"
              }
            ]
          },
          {
            "screen_name": "Sign Up - Date of Birth",
            "actions": [
              {
                "user_action": "Enters date of birth, taps 'Next' button",
                "next_screen": "Sign Up - Gender"
              }
            ]
          },
          {
            "screen_name": "Sign Up - Gender",
            "actions": [
              {
                "user_action": "Selects a gender, taps 'Next' button",
                "next_screen": "Sign Up - Profile Name"
              }
            ]
          },
          {
            "screen_name": "Sign Up - Profile Name",
            "actions": [
              {
                "user_action": "Enters profile name, accepts terms, taps 'Create account' button",
                "next_screen": "Onboarding - Choose Artists"
              }
            ]
          },
          {
            "screen_name": "Onboarding - Choose Artists",
            "actions": [
              {
                "user_action": "Selects 3 or more artists, taps 'Done' button",
                "next_screen": "Home"
              },
              {
                "user_action": "Taps 'Search' to find an artist",
                "next_screen": "Onboarding - Artist Search"
              }
            ]
          },
          {
            "screen_name": "Onboarding - Artist Search",
            "actions": [
              {
                "user_action": "Enters artist name in search bar and selects artist",
                "next_screen": "Onboarding - Choose Artists"
              },
              {
                "user_action": "Taps 'Cancel'",
                "next_screen": "Onboarding - Choose Artists"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Core Navigation",
        "screens": [
          {
            "screen_name": "Home",
            "actions": [
              {
                "user_action": "Taps 'Search' tab in bottom navigation",
                "next_screen": "Search"
              },
              {
                "user_action": "Taps 'Your Library' tab in bottom navigation",
                "next_screen": "Your Library"
              },
              {
                "user_action": "Taps 'Premium' tab in bottom navigation",
                "next_screen": "Premium Plan Overview"
              },
              {
                "user_action": "Taps Settings gear icon in top right",
                "next_screen": "Settings"
              },
              {
                "user_action": "Taps a song, album, or playlist",
                "next_screen": "Now Playing"
              }
            ]
          },
          {
            "screen_name": "Search",
            "actions": [
              {
                "user_action": "Taps the search bar 'What do you want to listen to?'",
                "next_screen": "Search Input"
              },
              {
                "user_action": "Taps a 'Browse all' category card (e.g., Podcasts)",
                "next_screen": "Browse Category"
              },
              {
                "user_action": "Taps 'Home' tab in bottom navigation",
                "next_screen": "Home"
              },
              {
                "user_action": "Taps 'Your Library' tab in bottom navigation",
                "next_screen": "Your Library"
              }
            ]
          },
          {
            "screen_name": "Your Library",
            "actions": [
              {
                "user_action": "Taps '+' icon to add new content",
                "next_screen": "Create New Menu"
              },
              {
                "user_action": "Taps a playlist",
                "next_screen": "Playlist View"
              },
              {
                "user_action": "Taps an album",
                "next_screen": "Album View"
              },
              {
                "user_action": "Taps 'Home' tab in bottom navigation",
                "next_screen": "Home"
              },
              {
                "user_action": "Taps 'Search' tab in bottom navigation",
                "next_screen": "Search"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Search and Discovery",
        "screens": [
          {
            "screen_name": "Search Input",
            "actions": [
              {
                "user_action": "Enters text into search bar",
                "next_screen": "Search Results"
              },
              {
                "user_action": "Taps 'Cancel'",
                "next_screen": "Search"
              }
            ]
          },
          {
            "screen_name": "Search Results",
            "actions": [
              {
                "user_action": "Taps a song from the results list",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps an artist from the results list",
                "next_screen": "Artist Profile"
              },
              {
                "user_action": "Taps a playlist from the results list",
                "next_screen": "Playlist View"
              },
              {
                "user_action": "Taps an album from the results list",
                "next_screen": "Album View"
              }
            ]
          },
          {
            "screen_name": "Browse Category",
            "actions": [
              {
                "user_action": "Taps a sub-category or specific podcast/playlist",
                "next_screen": "Playlist View"
              }
            ]
          },
          {
            "screen_name": "Artist Profile",
            "actions": [
              {
                "user_action": "Taps 'Follow' button",
                "next_screen": "Artist Profile"
              },
              {
                "user_action": "Taps a song from 'Popular' list",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps 'See Discography'",
                "next_screen": "Artist Discography"
              }
            ]
          },
          {
            "screen_name": "Artist Discography",
            "actions": [
              {
                "user_action": "Taps an album",
                "next_screen": "Album View"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Music and Playlist Management",
        "screens": [
          {
            "screen_name": "Playlist View",
            "actions": [
              {
                "user_action": "Taps a song to play it",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps 'Add songs' button",
                "next_screen": "Add to Playlist - Suggestions"
              },
              {
                "user_action": "Taps three-dots menu for playlist options",
                "next_screen": "Playlist Options Menu"
              }
            ]
          },
          {
            "screen_name": "Album View",
            "actions": [
              {
                "user_action": "Taps a song to play it",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps the play button to play the album",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps the heart icon to like the album",
                "next_screen": "Album View"
              }
            ]
          },
          {
            "screen_name": "Create New Menu",
            "actions": [
              {
                "user_action": "Taps 'Playlist'",
                "next_screen": "Create Playlist"
              },
              {
                "user_action": "Taps 'Blend'",
                "next_screen": "Create Blend"
              }
            ]
          },
          {
            "screen_name": "Create Playlist",
            "actions": [
              {
                "user_action": "Enters a playlist name, taps 'Create'",
                "next_screen": "Playlist View"
              }
            ]
          },
          {
            "screen_name": "Create Blend",
            "actions": [
              {
                "user_action": "Taps 'Invite' to select friends",
                "next_screen": "Invite Friends to Blend"
              }
            ]
          },
          {
            "screen_name": "Invite Friends to Blend",
            "actions": [
              {
                "user_action": "Selects a friend and sends invite",
                "next_screen": "Your Library"
              }
            ]
          },
          {
            "screen_name": "Add to Playlist - Suggestions",
            "actions": [
              {
                "user_action": "Taps '+' icon next to a suggested song",
                "next_screen": "Playlist View"
              },
              {
                "user_action": "Uses the search bar to find a specific song",
                "next_screen": "Add to Playlist - Search"
              }
            ]
          },
          {
            "screen_name": "Add to Playlist - Search",
            "actions": [
              {
                "user_action": "Enters song name, taps '+' icon next to the desired song",
                "next_screen": "Playlist View"
              }
            ]
          },
          {
            "screen_name": "Playlist Options Menu",
            "actions": [
              {
                "user_action": "Taps 'Edit playlist'",
                "next_screen": "Edit Playlist"
              },
              {
                "user_action": "Taps 'Add to profile'",
                "next_screen": "Playlist View"
              },
              {
                "user_action": "Taps 'Delete playlist'",
                "next_screen": "Delete Playlist Confirmation"
              }
            ]
          },
          {
            "screen_name": "Edit Playlist",
            "actions": [
              {
                "user_action": "Changes playlist name or description, taps 'Done'",
                "next_screen": "Playlist View"
              }
            ]
          },
          {
            "screen_name": "Delete Playlist Confirmation",
            "actions": [
              {
                "user_action": "Taps 'DELETE'",
                "next_screen": "Your Library"
              },
              {
                "user_action": "Taps 'CANCEL'",
                "next_screen": "Playlist View"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Player Controls",
        "screens": [
          {
            "screen_name": "Now Playing",
            "actions": [
              {
                "user_action": "Taps pause/play button",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps queue icon",
                "next_screen": "Queue"
              },
              {
                "user_action": "Taps 'Connect to a device' icon",
                "next_screen": "Connect to a Device"
              },
              {
                "user_action": "Taps three-dots menu for song options",
                "next_screen": "Song Options Menu"
              },
              {
                "user_action": "Swipes down to minimize player",
                "next_screen": "Home"
              }
            ]
          },
          {
            "screen_name": "Queue",
            "actions": [
              {
                "user_action": "Drags a song to reorder the queue",
                "next_screen": "Queue"
              },
              {
                "user_action": "Taps 'Clear queue'",
                "next_screen": "Queue"
              },
              {
                "user_action": "Taps back arrow",
                "next_screen": "Now Playing"
              }
            ]
          },
          {
            "screen_name": "Connect to a Device",
            "actions": [
              {
                "user_action": "Selects a device from the list (e.g., Chromecast, Bluetooth speaker)",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Closes the device list",
                "next_screen": "Now Playing"
              }
            ]
          },
          {
            "screen_name": "Song Options Menu",
            "actions": [
              {
                "user_action": "Taps 'Add to Playlist'",
                "next_screen": "Add to Playlist"
              },
              {
                "user_action": "Taps 'View Artist'",
                "next_screen": "Artist Profile"
              },
              {
                "user_action": "Taps 'View Album'",
                "next_screen": "Album View"
              }
            ]
          },
          {
            "screen_name": "Add to Playlist",
            "actions": [
              {
                "user_action": "Taps an existing playlist",
                "next_screen": "Now Playing"
              },
              {
                "user_action": "Taps 'New playlist'",
                "next_screen": "Create Playlist"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Settings and Profile",
        "screens": [
          {
            "screen_name": "Settings",
            "actions": [
              {
                "user_action": "Taps 'View Profile'",
                "next_screen": "Profile"
              },
              {
                "user_action": "Taps 'Account'",
                "next_screen": "Account Settings"
              },
              {
                "user_action": "Taps 'Data Saver'",
                "next_screen": "Data Saver Settings"
              },
              {
                "user_action": "Taps 'Playback'",
                "next_screen": "Playback Settings"
              },
              {
                "user_action": "Scrolls down and taps 'Log out'",
                "next_screen": "Log Out Confirmation"
              }
            ]
          },
          {
            "screen_name": "Profile",
            "actions": [
              {
                "user_action": "Taps 'Edit profile'",
                "next_screen": "Edit Profile"
              },
              {
                "user_action": "Taps a public playlist",
                "next_screen": "Playlist View"
              }
            ]
          },
          {
            "screen_name": "Edit Profile",
            "actions": [
              {
                "user_action": "Changes profile picture or name, taps 'Save'",
                "next_screen": "Profile"
              }
            ]
          },
          {
            "screen_name": "Account Settings",
            "actions": [
              {
                "user_action": "Taps 'Email address'",
                "next_screen": "Update Email"
              },
              {
                "user_action": "Taps 'Password'",
                "next_screen": "Change Password"
              }
            ]
          },
          {
            "screen_name": "Data Saver Settings",
            "actions": [
              {
                "user_action": "Toggles 'Data Saver' on/off",
                "next_screen": "Settings"
              }
            ]
          },
          {
            "screen_name": "Playback Settings",
            "actions": [
              {
                "user_action": "Toggles 'Gapless' playback",
                "next_screen": "Settings"
              },
              {
                "user_action": "Adjusts 'Streaming Quality'",
                "next_screen": "Settings"
              }
            ]
          },
          {
            "screen_name": "Log Out Confirmation",
            "actions": [
              {
                "user_action": "Taps 'LOG OUT'",
                "next_screen": "Launch Screen"
              },
              {
                "user_action": "Taps 'CANCEL'",
                "next_screen": "Settings"
              }
            ]
          },
          {
            "screen_name": "Update Email",
            "actions": [
              {
                "user_action": "Enters new email and current password, taps 'SAVE'",
                "next_screen": "Account Settings"
              }
            ]
          },
          {
            "screen_name": "Change Password",
            "actions": [
              {
                "user_action": "Enters current and new password, taps 'SET NEW PASSWORD'",
                "next_screen": "Account Settings"
              }
            ]
          }
        ]
      },
      {
        "flow_name": "Premium Upsell",
        "screens": [
          {
            "screen_name": "Premium Plan Overview",
            "actions": [
              {
                "user_action": "Taps 'GET PREMIUM'",
                "next_screen": "Subscription Purchase"
              },
              {
                "user_action": "Taps 'VIEW ALL PLANS'",
                "next_screen": "All Premium Plans"
              }
            ]
          },
          {
            "screen_name": "All Premium Plans",
            "actions": [
              {
                "user_action": "Selects a plan (e.g., Duo, Family) and taps 'GET PREMIUM'",
                "next_screen": "Subscription Purchase"
              }
            ]
          },
          {
            "screen_name": "Subscription Purchase",
            "actions": [
              {
                "user_action": "Completes purchase via Google Play payment sheet",
                "next_screen": "Home"
              }
            ]
          }
        ]
      }
    ]
  }
}
Output Requirements:
The output must be a single Markdown file that strictly follows the structure and includes all the detailed specifications as outlined in the \"System Prompt\" instructions you will receive. It is mandatory that every aspect of the provided flow tree is covered with absolute precision and accuracy, reflecting the actual Android design of the input app. The final document must be a single, complete file with no omissions. All specifications should reflect Android-native components and patterns."""
                ),
            ],
        ),
    ]

    tools = [types.Tool(googleSearch=types.GoogleSearch())]

    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=tools,
        system_instruction=[
            types.Part.from_text(
                text="""You are a Senior Product Designer. Your task is to generate a complete and hyper-detailed Android design specification from the user's app flow tree. The output must be a single, actionable Markdown file.
Non-Negotiable Rule: You MUST document every single screen listed in the input. The final output must be exhaustive, with no omissions or summaries.
Core Principles:
Platform: Android Mobile, using Material Design 3.
Fidelity: The specification must be detailed enough for an AI to generate a high-fidelity prototype without further input.
Accuracy: All details must reflect the real-world design patterns of a modern Android application.
Output Structure
I. Global Specifications
Platform: Android Mobile
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

    # Prepare to stream and write simultaneously
    with open(output_path, "w", encoding="utf-8") as md_file:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if chunk.text:
                print(chunk.text, end="") 
                md_file.write(chunk.text)  

    print(f"\n\n✅ Generation complete! Markdown file saved at: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    generate()
