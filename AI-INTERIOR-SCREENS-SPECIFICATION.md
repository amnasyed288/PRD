# AI Interior Design App - Complete Screen Specifications

## Overview
This document defines all screens for the AI Interior Design mobile app, following the module.md PRD and applying the design system rules from DESIGN-SYSTEM-SUMMARY.md.

**Platform**: Android Mobile (360×800dp)
**Design System**: Sage Olive theme with dual light/dark mode support
**Accessibility**: WCAG 2.1 AA compliant
**Grid System**: 8px base grid

---

## PAGE 02: APP LAUNCH & ONBOARDING

### Screen 02_Splash_Default
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Ivory - Light) / #121212 (Dark)

**Components**:
1. **Logo Container** (centered)
   - App logo/icon: 120×120dp
   - Position: Vertical center, -80dp offset
   - Color: #6B8E4E (Sage Olive)

2. **Tagline** (below logo)
   - Text: "Reimagine Your Space with AI"
   - Typography: H3 (Inter 700, 20px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Position: 24dp below logo

3. **Loading Indicator** (bottom)
   - Circular progress: 40dp diameter
   - Color: #6B8E4E (Sage Olive)
   - Position: 48dp from bottom

**States**: Default, Loading
**Animation**: Logo fade-in (300ms), tagline slide-up (400ms delay)

---

### Screen 02_Onboarding_01_Generate
**Dimensions**: 360×800dp
**Background**: #FFFFFF (Light) / #121212 (Dark)

**Components**:
1. **Skip Button** (top-right)
   - Text button: "Skip"
   - Typography: Button (Inter 600, 14px)
   - Color: #8E837A (Secondary)
   - Position: 16dp from top-right
   - Touch target: 44×44dp

2. **Illustration Container** (top section)
   - Size: 360×320dp
   - Position: 0dp from top
   - Content: AI generation illustration
   - Background: #F3EEE7 (Light) / #1F1F1F (Dark)

3. **Content Container** (bottom section)
   - Padding: 32dp horizontal, 24dp vertical
   
   **Headline**:
   - Text: "Generate Stunning Designs"
   - Typography: H2 (Source Serif 4, 600, 24px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Line height: 1.20
   
   **Description**:
   - Text: "Upload a photo of your space and let AI transform it with professional interior design styles"
   - Typography: Body Large (Inter 400, 16px)
   - Color: #3B2F2A (Light) / #E5E5E5 (Dark)
   - Margin-top: 16dp
   
   **Navigation Dots**:
   - Container: 3 dots, 8dp spacing
   - Active dot: 8dp diameter, #6B8E4E (Sage Olive)
   - Inactive dots: 8dp diameter, #D9D9D9 (Light) / #3A3A3A (Dark)
   - Position: 32dp from bottom
   
   **Next Button**:
   - Primary button: "Next"
   - Size: Full width - 64dp (32dp margins)
   - Height: 48dp
   - Corner radius: 16px
   - Background: #6B8E4E (Sage Olive)
   - Text: #FFFFFF
   - Position: 16dp from bottom

**States**: Default, Skip hover, Next pressed
**Interaction**: Swipe left to next screen, tap Next, tap Skip → Home

---

### Screen 02_Onboarding_02_Explore
**Dimensions**: 360×800dp
**Structure**: Same as Onboarding_01 with different content

**Content Changes**:
- **Headline**: "Explore Design Styles"
- **Description**: "Browse curated interior styles from modern to bohemian, and discover inspiration for your perfect space"
- **Illustration**: Style library showcase
- **Navigation Dots**: Second dot active

---

### Screen 02_Onboarding_03_Customize
**Dimensions**: 360×800dp
**Structure**: Same as Onboarding_01 with different content

**Content Changes**:
- **Headline**: "Customize Every Detail"
- **Description**: "Fine-tune colors, furniture, lighting, and decor to match your unique vision and preferences"
- **Illustration**: Customization controls
- **Navigation Dots**: Third dot active
- **Button**: "Get Started" (instead of "Next")

---

### Screen 02_Welcome_Auth
**Dimensions**: 360×800dp
**Background**: #FFFFFF (Light) / #121212 (Dark)

### 🔧 Auto Layout & Structure Rules
- **Root Frame:** Vertical Auto Layout  
  - Direction: Vertical  
  - Spacing: 32dp between sections  
  - Padding: 0 top/bottom (handled by sections)  
  - Alignment: Center horizontally  
  - Constraints: Top and bottom responsive  
- **All Containers** (Header, Auth Buttons, Divider, Guest Mode, Terms Text)  
  - Use Auto Layout (vertical for stacks, horizontal where icons + text are combined)  
  - Maintain consistent spacing and alignment  
  - Apply component constraints for both light and dark modes  
  - Ensure full-width responsive behavior for buttons  
- **Agent Action:**  
  - Automatically apply Figma Auto Layout tool to all sections  
  - Maintain uniform vertical rhythm (consistent spacing and hierarchy)  
  - Enforce consistent corner radius, padding, and text alignment 
  - 

**Components**:
1. **Header Section** (top)
   - Padding: 48dp top, 32dp horizontal
   
   **Logo**:
   - Size: 80×80dp
   - Position: Centered horizontally
   
   **Welcome Text**:
   - Text: "Welcome to AI Interior"
   - Typography: H2 (Source Serif 4, 600, 24px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 24dp
   - Alignment: Center
   
   **Subtitle**:
   - Text: "Transform your space with AI-powered design"
   - Typography: Body Medium (Inter 400, 14px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 8dp
   - Alignment: Center

2. **Auth Buttons Container** (middle)
   - Padding: 32dp horizontal
   - Margin-top: 64dp
   
   **Google Sign In Button**:
   - Size: Full width, 48dp height
   - Corner radius: 16px
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border: 2px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Icon: Google logo (20×20dp), 12dp from left
   - Text: "Continue with Google"
   - Typography: Button (Inter 600, 14px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   
   **Apple Sign In Button**:
   - Same structure as Google
   - Margin-top: 12dp
   - Icon: Apple logo
   - Text: "Continue with Apple"
   
   **Email Sign In Button**:
   - Same structure
   - Margin-top: 12dp
   - Icon: Email icon
   - Text: "Continue with Email"

3. **Divider** (below auth buttons)
   - Margin-top: 24dp
   - Text: "or"
   - Typography: Caption (Inter 400, 11px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Alignment: Center
   - Lines: 1px height, #E5E0DA (Light) / #3A3A3A (Dark)

4. **Guest Mode Button** (below divider)
   - Margin-top: 24dp
   - Text button: "Continue as Guest"
   - Typography: Button (Inter 600, 14px)
   - Color: #6B8E4E (Sage Olive)
   - Alignment: Center

5. **Terms Text** (bottom)
   - Position: 24dp from bottom
   - Text: "By continuing, you agree to our Terms of Service and Privacy Policy"
   - Typography: Caption (Inter 400, 11px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Alignment: Center
   - Links: Underlined, #6B8E4E

**States**: Default, Button hover, Button pressed, Loading (spinner in button)

---

## PAGE 03: HOME & NAVIGATION

### Screen 03_Home_Default
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Light) / #121212 (Dark)

### 🔧 Auto Layout & Structure Rules
- **Root Frame:** Vertical Auto Layout  
  - Direction: Vertical  
  - Spacing: 32dp between sections  
  - Padding: 0 top/bottom (handled by sections)  
  - Alignment: Center horizontally  
  - Constraints: Top and bottom responsive  
- **All Containers** (Header, Auth Buttons, Divider, Guest Mode, Terms Text)  
  - Use Auto Layout (vertical for stacks, horizontal where icons + text are combined)  
  - Maintain consistent spacing and alignment  
  - Apply component constraints for both light and dark modes  
  - Ensure full-width responsive behavior for buttons  
- **Agent Action:**  
  - Automatically apply Figma Auto Layout tool to all sections  
  - Maintain uniform vertical rhythm (consistent spacing and hierarchy)  
  - Enforce consistent corner radius, padding, and text alignment 

**Components**:
1. **Status Bar** (top)
   - Height: 24dp
   - Background: Transparent
   - Icons: System status icons

2. **Top App Bar** (below status bar)
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Elevation: Level 0 (no shadow initially)
   - Padding: 16dp horizontal
   
   **Left Section**:
   - App logo: 32×32dp
   
   **Right Section**:
   - Notification bell icon: 24×24dp, #3B2F2A (Light) / #E5E5E5 (Dark)
   - Badge: 8dp diameter, #FF3B30 (Error red), positioned top-right of icon
   - User avatar: 32×32dp circle, 16dp margin-left
   - Touch targets: 44×44dp each

3. **Greeting Section** (below app bar)
   - Padding: 32dp horizontal, 24dp top
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   
   **Greeting Text**:
   - Text: "Good morning, Sarah"
   - Typography: H3 (Inter 700, 20px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   
   **Subtitle**:
   - Text: "What would you like to design today?"
   - Typography: Body Medium (Inter 400, 14px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 4dp

4. **Feature Cards Grid** (main content)
   - Padding: 16dp horizontal, 24dp top
   - Grid: 2 columns, 12dp gap
   - Scroll: Vertical
   
   **Feature Card Structure** (5 cards):
   - Size: (360-44dp)/2 = 158dp width, 158dp height (1:1 ratio)
   - Corner radius: 16px
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Elevation: Level 1 (2dp shadow)
   - Padding: 16dp
   
   **Card Content**:
   - Icon: 48×48dp, centered top, 16dp from top
   - Icon color: #6B8E4E (Sage Olive)
   - Label: H4 (Inter 600, 16px), centered, 12dp below icon
   - Label color: #2C2926 (Light) / #FFFFFF (Dark)
   - Description: Body Small (Inter 400, 12px), centered, 8dp below label
   - Description color: #8E837A (Light) / #B3B3B3 (Dark)
   
   **5 Feature Cards**:
   1. Interior Design (icon: sofa)
   2. Exterior Design (icon: house)
   3. Garden Design (icon: plant)
   4. Virtual Staging (icon: furniture)
   5. Floor Redesign (icon: floor tiles)
   
   **Card States**:
   - Default: As specified
   - Hover: Border #6B8E4E, Elevation Level 2, Scale 1.02
   - Pressed: Background rgba(107,142,78,0.08), Scale 0.98

5. **Recent Designs Section** (below feature cards)
   - Margin-top: 32dp
   - Padding: 0dp horizontal (full width scroll)
   
   **Section Header**:
   - Padding: 0dp 16dp
   - Text: "Recent Designs"
   - Typography: H4 (Inter 600, 16px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - "See All" link: Body Small, #6B8E4E, right-aligned
   
   **Horizontal Scroll Container**:
   - Margin-top: 16dp
   - Padding: 0dp 16dp
   - Scroll: Horizontal, snap to items
   - Gap: 12dp between cards
   
   **Room Card** (repeated 5-10 times):
   - Size: 200×150dp (16:9 aspect ratio)
   - Corner radius: 16px
   - Elevation: Level 1
   - Image: Full container, object-fit cover
   - Gradient overlay: Linear, bottom, rgba(0,0,0,0) to rgba(0,0,0,0.6)
   
   **Card Overlay Content**:
   - Style chip (top-left, 8dp from edges):
     * Background: rgba(255,255,255,0.9) Light / rgba(0,0,0,0.7) Dark
     * Text: "Modern" (example)
     * Typography: Caption (Inter 400, 11px)
     * Padding: 6px 12px
     * Corner radius: 8px
   
   - Metadata (bottom-left, 8dp from edges):
     * Text: "2 days ago"
     * Typography: Caption (Inter 400, 11px)
     * Color: #FFFFFF
     * Icon: Clock icon 12×12dp

6. **Inspiration Hub Section** (below recent designs)
   - Margin-top: 32dp
   - Padding: 0dp 16dp
   
   **Section Header**:
   - Text: "Trending Styles"
   - Typography: H4 (Inter 600, 16px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   
   **Carousel Container**:
   - Margin-top: 16dp
   - Auto-scroll: 5 seconds per item
   - Manual control: Swipe or dots
   
   **Style Card**:
   - Size: 328dp width (360-32dp margins), 200dp height
   - Corner radius: 16px
   - Image: Full container
   - Overlay: Gradient bottom
   - Title: H4, #FFFFFF, bottom-left, 16dp padding
   - Subtitle: Body Small, #FFFFFF, below title

7. **Bottom Navigation Bar** (fixed bottom)
   - Height: 56dp + safe area inset
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Elevation: Level 2 (4dp shadow)
   - Items: 3 tabs, evenly distributed
   
   **Tab Items**:
   1. Home (active)
      - Icon: Home filled, 24×24dp, #6B8E4E
      - Label: "Home", Caption, #6B8E4E, Semi-Bold
      - Indicator: 3dp bar, #6B8E4E, top of bar
   
   2. Recents (inactive)
      - Icon: Clock outline, 24×24dp, #8E837A (Light) / #B3B3B3 (Dark)
      - Label: "Recents", Caption, #8E837A (Light) / #B3B3B3 (Dark)
   
   3. Settings (inactive)
      - Icon: Settings outline, 24×24dp, #8E837A (Light) / #B3B3B3 (Dark)
      - Label: "Settings", Caption, #8E837A (Light) / #B3B3B3 (Dark)

**Scroll Behavior**:
- Top app bar gains elevation (Level 2) when scrolled
- Pull-to-refresh on inspiration content
- Smooth scroll performance

**States**: Default, Scrolled, Pull-to-refresh, Card hover, Tab active

---

## PAGE 04: DESIGN GENERATION FLOW

### Screen 04_Upload_Gallery
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Light) / #121212 (Dark)

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Elevation: Level 2

   **Left**: Back button (44×44dp touch target)
   **Center**: "Upload Photo" (H4)
   **Right**: Empty

2. **Progress Indicator** (below app bar)
   - Height: 4dp
   - Background: #E5E0DA (Light) / #3A3A3A (Dark)
   - Progress: 20% (Step 1 of 5)
   - Color: #6B8E4E (Sage Olive)

3. **Step Title** (below progress)
   - Padding: 32dp horizontal, 24dp top
   - Text: "Choose Your Space"
   - Typography: H2 (Source Serif 4, 600, 24px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)

   **Subtitle**:
   - Text: "Upload a photo or select a template"
   - Typography: Body Medium (Inter 400, 14px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 8dp

4. **Action Buttons** (below title)
   - Padding: 32dp horizontal
   - Margin-top: 32dp
   - Gap: 12dp vertical

   **Camera Button**:
   - Primary button
   - Size: Full width, 56dp height
   - Background: #6B8E4E
   - Icon: Camera (24×24dp), left, 16dp from edge
   - Text: "Take Photo"
   - Typography: Button (Inter 600, 14px)
   - Color: #FFFFFF

   **Gallery Button**:
   - Secondary button
   - Size: Full width, 56dp height
   - Background: Transparent
   - Border: 2px solid #6B8E4E
   - Icon: Gallery (24×24dp), left
   - Text: "Choose from Gallery"
   - Color: #6B8E4E

5. **Divider**
   - Margin-top: 32dp
   - Text: "or start with a template"
   - Typography: Caption
   - Color: #8E837A (Light) / #B3B3B3 (Dark)

6. **Template Grid** (below divider)
   - Padding: 16dp horizontal
   - Margin-top: 24dp
   - Grid: 2 columns, 12dp gap
   - Scroll: Vertical

   **Template Card**:
   - Size: 158×118dp (4:3 ratio)
   - Corner radius: 12px
   - Border: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Image: Room template preview
   - Label: Body Small, centered, 8dp padding bottom
   - Overlay on hover: rgba(107,142,78,0.1)

   **Templates**: Living Room, Bedroom, Kitchen, Bathroom, Office, Dining Room

**States**: Default, Camera pressed, Gallery pressed, Template selected

---

### Screen 04_RoomType_Selection
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar** (same structure)
   - Center: "Room Type"

2. **Progress Indicator**
   - Progress: 40% (Step 2 of 5)

3. **Step Title**
   - Text: "Select Room Type"
   - Subtitle: "What space are you designing?"

4. **Room Type Grid**
   - Padding: 16dp horizontal, 24dp top
   - Grid: 2 columns, 12dp gap
   - Scroll: Vertical

   **Room Card** (7 cards):
   - Size: 158×140dp
   - Corner radius: 16px
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border: 2px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Elevation: Level 1
   - Padding: 16dp

   **Card Content**:
   - Icon: 64×64dp, centered, room illustration
   - Icon color: #6B8E4E
   - Label: H4, centered, 12dp below icon
   - Label color: #2C2926 (Light) / #FFFFFF (Dark)

   **Room Types**:
   1. Living Room
   2. Bedroom
   3. Kitchen
   4. Bathroom
   5. Office
   6. Dining Room
   7. Other (with text input option)

   **Selected State**:
   - Border: 3px solid #6B8E4E
   - Background: rgba(107,142,78,0.08)
   - Checkmark: 20dp circle, #6B8E4E, top-right corner, white check icon

5. **Continue Button** (fixed bottom)
   - Margin: 16dp horizontal, 16dp bottom
   - Primary button: "Continue"
   - Size: Full width, 48dp height
   - Disabled until selection made

**States**: Default, Card selected, Continue enabled/disabled

---

### Screen 04_Style_Selection
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Center: "Design Style"

2. **Progress Indicator**
   - Progress: 60% (Step 3 of 5)

3. **Step Title**
   - Text: "Choose Your Style"
   - Subtitle: "Select a design aesthetic"

4. **Style Grid**
   - Padding: 16dp horizontal, 24dp top
   - Grid: 2 columns, 12dp gap

   **Style Card** (8 cards):
   - Size: 158×180dp
   - Corner radius: 12px
   - Border: 2px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Elevation: Level 1

   **Card Structure**:
   - Image: 158×120dp, top, style preview
   - Label: H4, 12dp padding horizontal/vertical
   - Label color: #2C2926 (Light) / #FFFFFF (Dark)

   **Styles**:
   1. Modern
   2. Farmhouse
   3. Minimalist
   4. Industrial
   5. Scandinavian
   6. Luxury
   7. Bohemian
   8. Custom (upload reference)

   **Selected State**:
   - Border: 3px solid #6B8E4E
   - Checkmark: 20dp circle, top-right
   - Overlay: rgba(107,142,78,0.1) tint on image

5. **Continue Button** (fixed bottom)

**States**: Default, Style selected, Continue enabled

---

### Screen 04_Customize_Options
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Center: "Customize"

2. **Progress Indicator**
   - Progress: 80% (Step 4 of 5)

3. **Step Title**
   - Text: "Fine-Tune Your Design"
   - Subtitle: "Adjust colors and intensity"

4. **Customization Panel** (scrollable)
   - Padding: 32dp horizontal, 24dp top

   **Color Theme Section**:
   - Label: "Color Theme"
   - Typography: H4
   - Margin-bottom: 16dp

   **Color Chips** (horizontal scroll):
   - Chip size: 80×80dp
   - Corner radius: 12px
   - Gap: 12dp
   - Border: 2px solid #E5E0DA (Light) / #3A3A3A (Dark)

   **Chips**:
   1. Earthy Hues (gradient: browns/greens)
   2. Surprise Me (rainbow gradient)
   3. Terracotta Mirage (orange/red tones)
   4. Monochrome (black/white/gray)
   5. Vibrant (bright colors)

   **Selected Chip**:
   - Border: 3px solid #6B8E4E
   - Checkmark: 16dp circle, bottom-right

   **Intensity Slider Section**:
   - Margin-top: 32dp
   - Label: "Transformation Intensity"
   - Typography: H4

   **Slider**:
   - Margin-top: 16dp
   - Track: Full width, 4dp height, #E5E0DA (Light) / #3A3A3A (Dark)
   - Progress: #6B8E4E
   - Thumb: 20dp diameter, #FFFFFF, shadow Level 2
   - Labels: "Subtle" (left), "Dramatic" (right)
   - Typography: Caption, #8E837A (Light) / #B3B3B3 (Dark)

   **Element Focus Section**:
   - Margin-top: 32dp
   - Label: "Focus On"
   - Typography: H4

   **Toggle Chips** (multi-select):
   - Margin-top: 16dp
   - Chips: "Furniture", "Lighting", "Decor", "Colors"
   - Size: Auto width, 36dp height
   - Padding: 12px 16px
   - Corner radius: 18px (pill)
   - Gap: 8dp, wrap

   **Unselected**:
   - Background: Transparent
   - Border: 2px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Text: #8E837A (Light) / #B3B3B3 (Dark)

   **Selected**:
   - Background: #6B8E4E
   - Border: None
   - Text: #FFFFFF

5. **Generate Button** (fixed bottom)
   - Primary button: "Generate Design"
   - Size: Full width - 32dp margins, 48dp height
   - Background: #6B8E4E
   - Icon: Sparkle/AI icon (20×20dp), left
   - Text: #FFFFFF

**States**: Default, Chip selected, Slider dragging, Generate pressed

---

### Screen 04_Generate_Processing
**Dimensions**: 360×800dp
**Background**: rgba(255,255,255,0.95) Light / rgba(18,18,18,0.95) Dark (semi-transparent overlay)

**Components**:
1. **Content Container** (centered vertically)
   - Padding: 32dp horizontal

   **Animation**:
   - Lottie animation or custom illustration
   - Size: 120×120dp
   - Position: Centered horizontally
   - Animation: AI generation visual (sparkles, room transformation)

   **Title**:
   - Text: "Crafting Your Dream Space..."
   - Typography: H3 (Inter 700, 20px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 24dp
   - Alignment: Center

   **Message**:
   - Text: "Our AI is analyzing your space and applying your chosen style"
   - Typography: Body Medium (Inter 400, 14px)
   - Color: #3B2F2A (Light) / #E5E5E5 (Dark)
   - Margin-top: 12dp
   - Alignment: Center

   **Progress Bar**:
   - Margin-top: 32dp
   - Width: Full width - 64dp
   - Height: 4dp
   - Track: #E5E0DA (Light) / #3A3A3A (Dark)
   - Progress: #6B8E4E (animated 0-100%)
   - Corner radius: 2px

   **Time Estimate**:
   - Text: "Estimated time: 45 seconds"
   - Typography: Caption (Inter 400, 11px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 8dp
   - Alignment: Center

   **Cancel Button**:
   - Margin-top: 48dp
   - Text button: "Cancel"
   - Typography: Button (Inter 600, 14px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Alignment: Center

**States**: Processing (0-100%), Complete (transition to results)
**Animation**: Progress bar smooth animation, rotating AI icon

---

### Screen 04_Results_Success
**Dimensions**: 360×800dp
**Background**: #121212 (Dark background for image focus)

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: rgba(18,18,18,0.9) with blur
   - Elevation: None

   **Left**: Back button (white icon)
   **Right**: Share icon (24×24dp, white)

2. **Result Image Container** (main content)
   - Size: 360×480dp (3:4 ratio)
   - Position: Top, below app bar
   - Image: Generated design result
   - Pinch-to-zoom enabled
   - Pan enabled when zoomed

   **Before/After Toggle** (overlay on image):
   - Position: Top-right, 16dp from edges
   - Size: 80×32dp
   - Background: rgba(0,0,0,0.7)
   - Corner radius: 16px
   - Text: "Before" / "After"
   - Typography: Caption, #FFFFFF
   - Toggle animation: Slide

3. **Action Bar** (below image)
   - Height: Auto
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Padding: 24dp horizontal, 16dp vertical
   - Corner radius: 24px 24px 0 0 (top corners rounded)

   **Primary Actions** (horizontal row):
   - Gap: 12dp

   **Save Button**:
   - Primary button
   - Size: Flex 1, 48dp height
   - Background: #6B8E4E
   - Icon: Save (20×20dp), left
   - Text: "Save"
   - Color: #FFFFFF

   **Regenerate Button**:
   - Secondary button
   - Size: Flex 1, 48dp height
   - Border: 2px solid #6B8E4E
   - Icon: Refresh (20×20dp), left
   - Text: "Regenerate"
   - Color: #6B8E4E

   **Secondary Actions** (below primary, margin-top 12dp):
   - Horizontal row, gap 12dp

   **Enhance Button**:
   - Text button with icon
   - Icon: Sparkle (20×20dp)
   - Text: "Enhance"
   - Color: #6B8E4E

   **Share Button**:
   - Text button with icon
   - Icon: Share (20×20dp)
   - Text: "Share"
   - Color: #6B8E4E

   **Try Another Style**:
   - Text button with icon
   - Icon: Palette (20×20dp)
   - Text: "Try Another Style"
   - Color: #6B8E4E

4. **Style Variants** (bottom section)
   - Margin-top: 16dp
   - Label: "Quick Variations"
   - Typography: H4
   - Color: #2C2926 (Light) / #FFFFFF (Dark)

   **Variant Chips** (horizontal scroll):
   - Margin-top: 12dp
   - Chip size: 80×80dp
   - Corner radius: 12px
   - Gap: 8dp
   - Image: Style preview thumbnail
   - Label: Caption, centered, 4dp padding
   - Border: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)

   **Variants**: Modern, Minimalist, Bohemian, Industrial

**States**: Default, Zoomed, Before/After toggle, Button pressed
**Interactions**: Pinch-to-zoom, swipe for before/after, tap variants

---

## PAGE 05: SAVED DESIGNS & RECENTS

### Screen 05_Recents_Grid
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Light) / #121212 (Dark)

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Elevation: Level 2

   **Center**: "Recents" (H4)
   **Right**: Search icon (24×24dp), Filter icon (24×24dp)

2. **Tab Navigation** (below app bar)
   - Height: 48dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border-bottom: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)

   **Tabs**:
   - "Recent" (active): #6B8E4E, Semi-Bold, 3dp indicator bottom
   - "Saved": #8E837A (Light) / #B3B3B3 (Dark), Regular

3. **Filter Bar** (below tabs)
   - Height: 56dp
   - Padding: 16dp horizontal
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)

   **Filter Chips** (horizontal scroll):
   - Chips: "All", "Interior", "Exterior", "Garden", "Staging", "Floor"
   - Size: Auto width, 32dp height
   - Padding: 12px 16px
   - Corner radius: 16px
   - Gap: 8dp

   **Unselected**:
   - Background: #F3EEE7 (Light) / #2C2C2C (Dark)
   - Text: #8E837A (Light) / #B3B3B3 (Dark)

   **Selected** ("All"):
   - Background: #6B8E4E
   - Text: #FFFFFF

4. **Design Grid** (main content)
   - Padding: 16dp horizontal, 16dp top
   - Grid: 2 columns, 12dp gap
   - Scroll: Vertical, lazy loading

   **Design Card** (repeated):
   - Size: 158×118dp (4:3 ratio)
   - Corner radius: 12px
   - Elevation: Level 1
   - Image: Design thumbnail, object-fit cover
   - Gradient overlay: rgba(0,0,0,0) to rgba(0,0,0,0.5)

   **Card Overlay**:
   - Style chip (top-left, 8dp):
     * Background: rgba(255,255,255,0.9) Light / rgba(0,0,0,0.7) Dark
     * Text: "Modern" (example)
     * Typography: Caption
     * Padding: 4px 8px
     * Corner radius: 6px

   - Timestamp (bottom-left, 8dp):
     * Text: "2 days ago"
     * Typography: Caption
     * Color: #FFFFFF
     * Icon: Clock 10×10dp

   - Action button (bottom-right, 8dp):
     * Icon: More vertical (16×16dp)
     * Background: rgba(255,255,255,0.9) Light / rgba(0,0,0,0.7) Dark
     * Size: 28×28dp circle
     * Touch target: 44×44dp

   **Card States**:
   - Default: As specified
   - Hover: Elevation Level 2, Scale 1.02
   - Long press: Selection mode (checkmark top-right)

5. **Floating Action Button** (bottom-right)
   - Size: 56×56dp circle
   - Background: #6B8E4E
   - Icon: Plus (24×24dp), #FFFFFF
   - Elevation: Level 3 (8dp shadow)
   - Position: 16dp from bottom-right (above nav bar)
   - Touch target: 56×56dp

6. **Bottom Navigation Bar** (fixed bottom)
   - Same structure as Home screen
   - "Recents" tab active

**States**: Default, Scrolled, Filter selected, Card long-press, Selection mode
**Interactions**: Pull-to-refresh, infinite scroll, swipe to delete

---

### Screen 05_Design_Detail
**Dimensions**: 360×800dp
**Background**: #121212 (Dark for image focus)

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: rgba(18,18,18,0.9) with blur
   - Elevation: None

   **Left**: Back button (white)
   **Right**: More menu (3 dots, white)

2. **Image Viewer** (main content)
   - Size: 360×540dp (2:3 ratio)
   - Position: Top, below app bar
   - Image: Full design, high resolution
   - Pinch-to-zoom enabled
   - Swipe left/right: Navigate between designs

   **Zoom Controls** (overlay, bottom-right of image):
   - Position: 16dp from bottom-right
   - Background: rgba(0,0,0,0.7)
   - Corner radius: 8px
   - Padding: 8dp
   - Icons: Zoom in, Zoom out (20×20dp each)
   - Color: #FFFFFF

3. **Details Panel** (below image)
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Corner radius: 24px 24px 0 0
   - Padding: 24dp horizontal, 20dp vertical
   - Scroll: Vertical (if content exceeds)

   **Header Row**:
   - Style name: H3, #2C2926 (Light) / #FFFFFF (Dark)
   - Favorite icon: Heart outline (24×24dp), right-aligned

   **Metadata Row** (below header, margin-top 8dp):
   - Created date: Body Small, #8E837A (Light) / #B3B3B3 (Dark)
   - Room type chip: Caption, #6B8E4E, background rgba(107,142,78,0.1)

   **Description** (if available):
   - Margin-top: 16dp
   - Text: Design description or AI prompt used
   - Typography: Body Medium
   - Color: #3B2F2A (Light) / #E5E5E5 (Dark)

   **Parameters Section**:
   - Margin-top: 24dp
   - Label: "Design Parameters"
   - Typography: H4

   **Parameter List**:
   - Margin-top: 12dp
   - Items: Style, Color Theme, Intensity, Room Type
   - Each item:
     * Label: Body Small, #8E837A (Light) / #B3B3B3 (Dark)
     * Value: Body Medium, #2C2926 (Light) / #FFFFFF (Dark)
     * Spacing: 12dp between items

   **Action Buttons** (bottom of panel):
   - Margin-top: 24dp
   - Horizontal row, gap 12dp

   **Regenerate Button**:
   - Primary button
   - Size: Flex 1, 48dp height
   - Background: #6B8E4E
   - Icon: Refresh (20×20dp)
   - Text: "Regenerate"

   **Share Button**:
   - Secondary button
   - Size: Flex 1, 48dp height
   - Border: 2px solid #6B8E4E
   - Icon: Share (20×20dp)
   - Text: "Share"

**States**: Default, Zoomed, Favorite toggled, Swiping between designs
**Interactions**: Pinch-to-zoom, swipe navigation, favorite toggle

---

### Screen 05_Saved_Categories
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Center: "Saved Designs"
   - Right: Search, Filter icons

2. **Tab Navigation**
   - "Recent" (inactive)
   - "Saved" (active): #6B8E4E, indicator

3. **Category Grid** (main content)
   - Padding: 16dp horizontal, 24dp top
   - Grid: 2 columns, 16dp gap

   **Category Card** (6 cards):
   - Size: 158×140dp
   - Corner radius: 16px
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)
   - Elevation: Level 1
   - Padding: 16dp

   **Card Content**:
   - Icon: 48×48dp, centered top
   - Icon color: #6B8E4E
   - Label: H4, centered, 12dp below icon
   - Count: Body Small, #8E837A (Light) / #B3B3B3 (Dark), centered, 4dp below label

   **Categories**:
   1. Interior (icon: sofa, count: "24 designs")
   2. Exterior (icon: house, count: "8 designs")
   3. Garden (icon: plant, count: "12 designs")
   4. Staging (icon: furniture, count: "6 designs")
   5. Floor (icon: tiles, count: "10 designs")
   6. All Designs (icon: grid, count: "60 designs")

   **Card States**:
   - Default: As specified
   - Hover: Border #6B8E4E, Elevation Level 2
   - Pressed: Background rgba(107,142,78,0.08)

4. **Bottom Navigation Bar**
   - "Recents" tab active

**States**: Default, Category hover, Category pressed

---

## PAGE 06: SETTINGS & PROFILE

### Screen 06_Settings_Main
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Light) / #121212 (Dark)

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Elevation: Level 2

   **Left**: Back button (if navigated from elsewhere)
   **Center**: "Settings" (H4)

2. **Profile Section** (below app bar)
   - Height: 120dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Padding: 24dp horizontal, 20dp vertical
   - Border-bottom: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)

   **Avatar**:
   - Size: 64×64dp circle
   - Position: Left
   - Image: User profile photo or initials
   - Border: 2px solid #6B8E4E

   **User Info** (right of avatar, 16dp margin-left):
   - Name: H4, #2C2926 (Light) / #FFFFFF (Dark)
   - Email: Body Small, #8E837A (Light) / #B3B3B3 (Dark), margin-top 4dp
   - Edit button: Text button, "Edit Profile", #6B8E4E, margin-top 8dp

3. **Settings List** (main content)
   - Scroll: Vertical
   - Background: #FBFAF8 (Light) / #121212 (Dark)

   **Section: Account**
   - Padding: 24dp horizontal, 16dp top
   - Label: "Account"
   - Typography: Label (Inter 500, 13px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)

   **List Items**:
   1. Subscription
      - Icon: Crown (24×24dp), #C96F4A (Terracotta)
      - Label: "Subscription"
      - Subtitle: "Free Plan"
      - Arrow: Chevron right (20×20dp)
      - Height: 64dp
      - Background: #FFFFFF (Light) / #1F1F1F (Dark)
      - Border-bottom: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)

   2. Account Settings
      - Icon: User (24×24dp), #6B8E4E
      - Label: "Account Settings"
      - Subtitle: "Password, email, security"
      - Arrow: Chevron right

   **Section: Preferences** (margin-top 24dp)
   - Label: "Preferences"

   **List Items**:
   1. Theme
      - Icon: Moon (24×24dp), #6B8E4E
      - Label: "Theme"
      - Toggle: Switch component (36×20dp), right-aligned
      - Current: "Dark Mode"
      - Height: 64dp

   2. Language
      - Icon: Globe (24×24dp), #6B8E4E
      - Label: "Language"
      - Value: "English", Body Small, #8E837A (Light) / #B3B3B3 (Dark)
      - Arrow: Chevron right

   3. Notifications
      - Icon: Bell (24×24dp), #6B8E4E
      - Label: "Notifications"
      - Toggle: Switch, right-aligned
      - Current: On

   **Section: AI Settings** (margin-top 24dp)
   - Label: "AI Settings"

   **List Items**:
   1. Default Style
      - Icon: Palette (24×24dp), #6B8E4E
      - Label: "Default Style"
      - Value: "Modern"
      - Arrow: Chevron right

   2. Render Quality
      - Icon: Image (24×24dp), #6B8E4E
      - Label: "Render Quality"
      - Value: "High"
      - Arrow: Chevron right

   3. Auto-save
      - Icon: Save (24×24dp), #6B8E4E
      - Label: "Auto-save Designs"
      - Toggle: Switch, right-aligned
      - Current: On

   **Section: Support** (margin-top 24dp)
   - Label: "Support"

   **List Items**:
   1. Help Center
      - Icon: Question circle (24×24dp), #6B8E4E
      - Label: "Help Center"
      - Arrow: Chevron right

   2. Contact Support
      - Icon: Message (24×24dp), #6B8E4E
      - Label: "Contact Support"
      - Arrow: Chevron right

   3. Privacy Policy
      - Icon: Shield (24×24dp), #6B8E4E
      - Label: "Privacy Policy"
      - Arrow: Chevron right

   4. Terms of Service
      - Icon: Document (24×24dp), #6B8E4E
      - Label: "Terms of Service"
      - Arrow: Chevron right

   **Section: Account Actions** (margin-top 24dp)
   - Label: "Account"

   **List Items**:
   1. Log Out
      - Icon: Log out (24×24dp), #FF3B30 (Error)
      - Label: "Log Out"
      - Color: #FF3B30
      - Arrow: None

   2. Delete Account
      - Icon: Trash (24×24dp), #FF3B30
      - Label: "Delete Account"
      - Color: #FF3B30
      - Arrow: None

4. **Bottom Navigation Bar**
   - "Settings" tab active

**States**: Default, List item hover, Toggle on/off, Scrolled
**Interactions**: Tap list items, toggle switches, scroll

---

### Screen 06_Profile_Edit
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Left: Back button
   - Center: "Edit Profile"
   - Right: "Save" text button (#6B8E4E)

2. **Avatar Section** (below app bar)
   - Padding: 32dp horizontal, 24dp vertical
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)

   **Avatar**:
   - Size: 96×96dp circle
   - Position: Centered horizontally
   - Image: Current profile photo
   - Border: 2px solid #6B8E4E

   **Change Photo Button** (overlay on avatar):
   - Position: Bottom-right of avatar
   - Size: 32×32dp circle
   - Background: #6B8E4E
   - Icon: Camera (16×16dp), #FFFFFF
   - Elevation: Level 2

3. **Form Fields** (below avatar)
   - Padding: 32dp horizontal, 24dp top
   - Scroll: Vertical

   **Name Field**:
   - Label: "Full Name"
   - Typography: Label (Inter 500, 13px)
   - Color: #3B2F2A (Light) / #E5E5E5 (Dark)
   - Input: Text field
   - Height: 48dp
   - Margin-top: 8dp
   - Value: "Sarah Johnson"

   **Email Field**:
   - Margin-top: 24dp
   - Label: "Email"
   - Input: Text field
   - Value: "sarah.j@email.com"
   - Helper text: "Email cannot be changed"
   - Helper color: #8E837A (Light) / #B3B3B3 (Dark)

   **Phone Field**:
   - Margin-top: 24dp
   - Label: "Phone Number"
   - Input: Text field
   - Value: "+1 (555) 123-4567"

   **Bio Field**:
   - Margin-top: 24dp
   - Label: "Bio"
   - Input: Text area (multi-line)
   - Height: 96dp
   - Max characters: 150
   - Character counter: "45/150", Caption, right-aligned

   **Location Field**:
   - Margin-top: 24dp
   - Label: "Location"
   - Input: Text field
   - Value: "San Francisco, CA"

4. **Save Button** (fixed bottom)
   - Margin: 16dp horizontal, 16dp bottom
   - Primary button: "Save Changes"
   - Size: Full width, 48dp height
   - Background: #6B8E4E
   - Disabled until changes made

**States**: Default, Input focused, Input error, Save enabled/disabled
**Interactions**: Edit fields, upload photo, save changes

---

## ERROR & EMPTY STATES

### Screen Error_Network
**Dimensions**: 360×800dp
**Background**: #FBFAF8 (Light) / #121212 (Dark)

**Components**:
1. **Top App Bar** (if applicable)
   - Left: Back button
   - Center: Screen title

2. **Error Container** (centered vertically)
   - Padding: 48dp horizontal

   **Illustration**:
   - Size: 160×160dp
   - Position: Centered horizontally
   - Image: Network error illustration (disconnected wifi, broken connection)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)

   **Title**:
   - Text: "No Internet Connection"
   - Typography: H3 (Inter 700, 20px)
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 32dp
   - Alignment: Center

   **Message**:
   - Text: "Please check your internet connection and try again"
   - Typography: Body Medium (Inter 400, 14px)
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 12dp
   - Alignment: Center

   **Retry Button**:
   - Margin-top: 32dp
   - Primary button: "Try Again"
   - Size: 200dp width, 48dp height
   - Background: #6B8E4E
   - Text: #FFFFFF
   - Alignment: Center

**States**: Default, Retry pressed
**Interactions**: Tap retry, auto-retry on connection restore

---

### Screen Error_Generation_Failed
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Left: Back button
   - Center: "Generation Failed"

2. **Error Container** (centered)
   - Padding: 48dp horizontal

   **Illustration**:
   - Size: 160×160dp
   - Image: AI error illustration (broken robot, error symbol)
   - Color: #FF3B30 (Error red)

   **Title**:
   - Text: "Generation Failed"
   - Typography: H3
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 32dp
   - Alignment: Center

   **Message**:
   - Text: "We couldn't generate your design. This might be due to image quality or server issues."
   - Typography: Body Medium
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 12dp
   - Alignment: Center

   **Error Details** (collapsible):
   - Margin-top: 16dp
   - Text button: "View Details"
   - Color: #6B8E4E
   - Expands to show: Error code, timestamp, technical details

   **Action Buttons**:
   - Margin-top: 32dp
   - Horizontal row, gap 12dp

   **Try Again Button**:
   - Primary button
   - Size: Flex 1, 48dp height
   - Background: #6B8E4E
   - Text: "Try Again"

   **Change Photo Button**:
   - Secondary button
   - Size: Flex 1, 48dp height
   - Border: 2px solid #6B8E4E
   - Text: "Change Photo"

   **Contact Support Link**:
   - Margin-top: 24dp
   - Text button: "Contact Support"
   - Color: #6B8E4E
   - Alignment: Center

**States**: Default, Details expanded, Button pressed

---

### Screen Empty_Recents
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Center: "Recents"
   - Right: Search, Filter icons (disabled/grayed)

2. **Tab Navigation**
   - "Recent" (active)
   - "Saved" (inactive)

3. **Empty State Container** (centered vertically)
   - Padding: 48dp horizontal

   **Illustration**:
   - Size: 200×200dp
   - Image: Empty folder, clock with no history
   - Color: #D9D9D9 (Light) / #3A3A3A (Dark)

   **Title**:
   - Text: "No Recent Designs"
   - Typography: H3
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 32dp
   - Alignment: Center

   **Message**:
   - Text: "Your recently generated designs will appear here"
   - Typography: Body Medium
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 12dp
   - Alignment: Center

   **Create Button**:
   - Margin-top: 32dp
   - Primary button: "Create Your First Design"
   - Size: Auto width, 48dp height
   - Padding: 24px horizontal
   - Background: #6B8E4E
   - Icon: Plus (20×20dp), left
   - Text: #FFFFFF
   - Alignment: Center

4. **Bottom Navigation Bar**
   - "Recents" tab active

**States**: Default, Create button pressed

---

### Screen Empty_Saved
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Center: "Saved Designs"

2. **Tab Navigation**
   - "Recent" (inactive)
   - "Saved" (active)

3. **Empty State Container** (centered)
   - Padding: 48dp horizontal

   **Illustration**:
   - Size: 200×200dp
   - Image: Empty bookmark, heart outline
   - Color: #D9D9D9 (Light) / #3A3A3A (Dark)

   **Title**:
   - Text: "No Saved Designs Yet"
   - Typography: H3
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Margin-top: 32dp
   - Alignment: Center

   **Message**:
   - Text: "Save your favorite designs to access them anytime"
   - Typography: Body Medium
   - Color: #8E837A (Light) / #B3B3B3 (Dark)
   - Margin-top: 12dp
   - Alignment: Center

   **Browse Button**:
   - Margin-top: 32dp
   - Primary button: "Browse Recents"
   - Size: Auto width, 48dp height
   - Background: #6B8E4E
   - Text: #FFFFFF
   - Alignment: Center

**States**: Default, Browse pressed

---

## ADDITIONAL SCREENS

### Screen Search_Results
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar**
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)

   **Search Field** (full width):
   - Height: 44dp
   - Padding: 12px horizontal
   - Corner radius: 24px (pill)
   - Background: #F3EEE7 (Light) / #2C2C2C (Dark)
   - Icon: Search (20×20dp), left, 12dp from edge
   - Placeholder: "Search designs..."
   - Typography: Body Medium
   - Clear button: X icon (20×20dp), right, when text present

   **Back Button** (left of search):
   - Icon: Arrow left (24×24dp)
   - Touch target: 44×44dp

2. **Filter Bar** (below app bar)
   - Height: 56dp
   - Padding: 16dp horizontal
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Border-bottom: 1px solid #E5E0DA (Light) / #3A3A3A (Dark)

   **Filter Chips**:
   - Chips: "All", "Interior", "Exterior", "Garden", "Modern", "Minimalist"
   - Horizontal scroll
   - Same styling as Recents filter chips

3. **Results Count** (below filter bar)
   - Padding: 16dp horizontal, 12dp vertical
   - Text: "24 results for 'modern living room'"
   - Typography: Body Small
   - Color: #8E837A (Light) / #B3B3B3 (Dark)

4. **Results Grid** (main content)
   - Same structure as Recents grid
   - 2 columns, design cards
   - Lazy loading

5. **No Results State** (if no matches)
   - Centered container
   - Illustration: Magnifying glass with X
   - Title: "No Results Found"
   - Message: "Try different keywords or filters"
   - Button: "Clear Filters"

**States**: Default, Searching, Results loaded, No results
**Interactions**: Type search, apply filters, tap results

---

### Screen Comparison_View
**Dimensions**: 360×800dp
**Background**: #121212 (Dark)

**Components**:
1. **Top App Bar**
   - Background: rgba(18,18,18,0.9) with blur
   - Left: Back button (white)
   - Center: "Compare Designs"
   - Right: Share icon (white)

2. **Comparison Container** (main content)
   - Size: 360×720dp (full height minus app bar)

   **Split View Mode**:
   - Two images side-by-side
   - Divider: 2px white line, vertical center
   - Draggable divider: Adjust split ratio

   **Before Image** (left):
   - Label: "Before", top-left, 16dp padding
   - Background: rgba(0,0,0,0.7)
   - Typography: Caption, #FFFFFF
   - Padding: 6px 12px
   - Corner radius: 8px

   **After Image** (right):
   - Label: "After", top-right, 16dp padding
   - Same styling as Before label

3. **View Mode Toggle** (overlay, bottom center)
   - Position: 16dp from bottom
   - Size: 160×40dp
   - Background: rgba(0,0,0,0.8)
   - Corner radius: 20px
   - Padding: 4dp

   **Toggle Options**:
   - "Split" (active): Background #6B8E4E, Text #FFFFFF
   - "Slider": Background transparent, Text #FFFFFF
   - "Overlay": Background transparent, Text #FFFFFF
   - Each option: 50dp width, 32dp height, corner radius 16px

4. **Action Buttons** (overlay, bottom)
   - Position: 16dp from bottom-left and bottom-right
   - Size: 48×48dp circles each
   - Background: rgba(0,0,0,0.8)
   - Elevation: Level 2

   **Left Button**:
   - Icon: Download (24×24dp), #FFFFFF

   **Right Button**:
   - Icon: Share (24×24dp), #FFFFFF

**States**: Split view, Slider view, Overlay view, Divider dragging
**Interactions**: Drag divider, toggle view modes, pinch-to-zoom

---

### Screen Share_Options
**Dimensions**: 360×800dp
**Type**: Bottom Sheet Modal

**Components**:
1. **Handle** (top)
   - Size: 32×4dp
   - Corner radius: 2px
   - Background: #E5E0DA (Light) / #3A3A3A (Dark)
   - Position: Centered, 8dp from top

2. **Header** (below handle)
   - Padding: 24dp horizontal, 16dp vertical
   - Text: "Share Design"
   - Typography: H4
   - Color: #2C2926 (Light) / #FFFFFF (Dark)

3. **Preview Card** (below header)
   - Padding: 16dp horizontal
   - Size: 328×246dp (4:3 ratio)
   - Corner radius: 12px
   - Image: Design preview
   - Elevation: Level 1

4. **Share Options** (below preview)
   - Padding: 24dp horizontal, 16dp top

   **Option Grid**:
   - Grid: 4 columns, 16dp gap
   - Each option: 70×90dp

   **Option Structure**:
   - Icon container: 56×56dp circle, centered
   - Background: #F3EEE7 (Light) / #2C2C2C (Dark)
   - Icon: 28×28dp, centered
   - Label: Caption, centered, 8dp below icon

   **Options**:
   1. Instagram (icon: Instagram logo, color: #E4405F)
   2. Pinterest (icon: Pinterest logo, color: #E60023)
   3. Facebook (icon: Facebook logo, color: #1877F2)
   4. Twitter (icon: Twitter logo, color: #1DA1F2)
   5. WhatsApp (icon: WhatsApp logo, color: #25D366)
   6. Messages (icon: Message, color: #6B8E4E)
   7. Email (icon: Email, color: #6B8E4E)
   8. More (icon: More, color: #6B8E4E)

5. **Export Options** (below share options)
   - Margin-top: 24dp
   - Padding: 24dp horizontal
   - Label: "Export As"
   - Typography: H4
   - Margin-bottom: 16dp

   **Export Buttons**:
   - Horizontal row, gap 12dp

   **JPG Button**:
   - Size: Flex 1, 48dp height
   - Background: #F3EEE7 (Light) / #2C2C2C (Dark)
   - Text: "JPG"
   - Typography: Button
   - Color: #2C2926 (Light) / #FFFFFF (Dark)
   - Corner radius: 12px

   **PNG Button**:
   - Same structure as JPG
   - Text: "PNG"

   **PDF Button**:
   - Same structure
   - Text: "PDF"

6. **Copy Link Button** (bottom)
   - Margin: 24dp horizontal, 24dp bottom
   - Secondary button: "Copy Link"
   - Size: Full width, 48dp height
   - Border: 2px solid #6B8E4E
   - Icon: Link (20×20dp), left
   - Text: #6B8E4E

**States**: Default, Option pressed, Export format selected, Link copied
**Interactions**: Tap share option, select export format, copy link, swipe down to dismiss

---

## LOADING STATES

### Screen Loading_Skeleton_Home
**Dimensions**: 360×800dp

**Components**:
1. **Top App Bar Skeleton**
   - Height: 56dp
   - Background: #FFFFFF (Light) / #1F1F1F (Dark)
   - Left: Circle skeleton (32×32dp)
   - Right: Two circle skeletons (32×32dp each, 16dp gap)

2. **Greeting Skeleton**
   - Padding: 32dp horizontal, 24dp top
   - Line 1: 200×20dp rectangle, shimmer
   - Line 2: 280×14dp rectangle, shimmer, margin-top 8dp

3. **Feature Cards Skeleton**
   - Padding: 16dp horizontal, 24dp top
   - Grid: 2 columns, 12dp gap
   - 6 card skeletons: 158×158dp each
   - Corner radius: 16px
   - Shimmer animation

4. **Recent Section Skeleton**
   - Margin-top: 32dp
   - Header: 150×16dp rectangle, 16dp horizontal padding
   - Cards: Horizontal scroll, 5 cards (200×150dp each)
   - Shimmer animation

**Shimmer Animation**:
- Base color: #F3EEE7 (Light) / #2C2C2C (Dark)
- Shimmer color: #E5E0DA (Light) / #3A3A3A (Dark)
- Animation: Linear gradient moving left to right, 1.5s infinite

**States**: Loading (animated shimmer)

---

## SCREEN SUMMARY

**Total Screens Defined**: 25+ screens

**Page 02 - Onboarding**: 5 screens
- Splash
- Onboarding 1, 2, 3
- Welcome/Auth

**Page 03 - Home**: 1 screen
- Home Default

**Page 04 - Generation Flow**: 6 screens
- Upload Gallery
- Room Type Selection
- Style Selection
- Customize Options
- Generate Processing
- Results Success

**Page 05 - Recents & Saved**: 3 screens
- Recents Grid
- Design Detail
- Saved Categories

**Page 06 - Settings**: 2 screens
- Settings Main
- Profile Edit

**Error & Empty States**: 4 screens
- Network Error
- Generation Failed
- Empty Recents
- Empty Saved

**Additional Screens**: 4 screens
- Search Results
- Comparison View
- Share Options (Bottom Sheet)
- Loading Skeleton

**All screens follow**:
- ✓ 360×800dp Android mobile viewport
- ✓ 8px spacing grid system
- ✓ Sage Olive (#6B8E4E) primary color
- ✓ Dual theme support (light/dark)
- ✓ WCAG 2.1 AA accessibility (4.5:1 text contrast, 44dp touch targets)
- ✓ Material Design elevation (0dp, 2dp, 4dp, 8dp)
- ✓ Inter font for UI, Source Serif 4 for headings
- ✓ Complete state definitions (default, hover, pressed, focused, disabled, loading, error)
- ✓ Component reuse (buttons, cards, navigation, inputs)

---

**END OF SCREEN SPECIFICATIONS**


