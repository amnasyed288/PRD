# Combined Android Design Specifications



============================================================
## APP 1: App_1
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

# Boomy: Android Design Specification

## I. Global Specifications

### Platform
- **Platform:** Android Mobile App
- **Target SDK:** 34 (Android 14)
- **Minimum SDK:** 26 (Android 8.0)

### Design System
- **System:** Material Design 3
- **Theming:** Supports Light and Dark modes. Implements dynamic color (Material You) where available, using the seed color as a fallback.
- **Density:** Default screen density. All components should adhere to Material 3 guidelines.

### Colors
- **Seed Color:** `#8E44AD` (Vibrant Purple)
- **Source:** This seed color is used to generate the full Material 3 tonal palette.

#### Light Theme Color Roles
- **Primary:** `md.sys.color.primary` (#6750A4)
- **On Primary:** `md.sys.color.on-primary` (#FFFFFF)
- **Primary Container:** `md.sys.color.primary-container` (#EADDFF)
- **On Primary Container:** `md.sys.color.on-primary-container` (#21005D)
- **Secondary:** `md.sys.color.secondary` (#625B71)
- **On Secondary:** `md.sys.color.on-secondary` (#FFFFFF)
- **Secondary Container:** `md.sys.color.secondary-container` (#E8DEF8)
- **On Secondary Container:** `md.sys.color.on-secondary-container` (#1D192B)
- **Tertiary:** `md.sys.color.tertiary` (#7D5260)
- **On Tertiary:** `md.sys.color.on-tertiary` (#FFFFFF)
- **Tertiary Container:** `md.sys.color.tertiary-container` (#FFD8E4)
- **On Tertiary Container:** `md.sys.color.on-tertiary-container` (#31111D)
- **Error:** `md.sys.color.error` (#B3261E)
- **On Error:** `md.sys.color.on-error` (#FFFFFF)
- **Error Container:** `md.sys.color.error-container` (#F9DEDC)
- **On Error Container:** `md.sys.color.on-error-container` (#410E0B)
- **Background:** `md.sys.color.background` (#FFFBFE)
- **On Background:** `md.sys.color.on-background` (#1C1B1F)
- **Surface:** `md.sys.color.surface` (#FFFBFE)
- **On Surface:** `md.sys.color.on-surface` (#1C1B1F)
- **Surface Variant:** `md.sys.color.surface-variant` (#E7E0EC)
- **On Surface Variant:** `md.sys.color.on-surface-variant` (#49454F)
- **Outline:** `md.sys.color.outline` (#79747E)
- **Outline Variant:** `md.sys.color.outline-variant` (#CAC4D0)
- **Scrim:** `md.sys.color.scrim` (#000000)
- **Inverse Surface:** `md.sys.color.inverse-surface` (#313033)
- **Inverse On Surface:** `md.sys.color.inverse-on-surface` (#F4EFF4)
- **Inverse Primary:** `md.sys.color.inverse-primary` (#D0BCFF)

#### Dark Theme Color Roles
- **Primary:** `md.sys.color.primary` (#D0BCFF)
- **On Primary:** `md.sys.color.on-primary` (#381E72)
- **Primary Container:** `md.sys.color.primary-container` (#4F378B)
- **On Primary Container:** `md.sys.color.on-primary-container` (#EADDFF)
- **Secondary:** `md.sys.color.secondary` (#CCC2DC)
- **On Secondary:** `md.sys.color.on-secondary` (#332D41)
- **Secondary Container:** `md.sys.color.secondary-container` (#4A4458)
- **On Secondary Container:** `md.sys.color.on-secondary-container` (#E8DEF8)
- **Tertiary:** `md.sys.color.tertiary` (#EFB8C8)
- **On Tertiary:** `md.sys.color.on-tertiary` (#492532)
- **Tertiary Container:** `md.sys.color.tertiary-container` (#633B48)
- **On Tertiary Container:** `md.sys.color.on-tertiary-container` (#FFD8E4)
- **Error:** `md.sys.color.error` (#F2B8B5)
- **On Error:** `md.sys.color.on-error` (#601410)
- **Error Container:** `md.sys.color.error-container` (#8C1D18)
- **On Error Container:** `md.sys.color.on-error-container` (#F9DEDC)
- **Background:** `md.sys.color.background` (#1C1B1F)
- **On Background:** `md.sys.color.on-background` (#E6E1E5)
- **Surface:** `md.sys.color.surface` (#1C1B1F)
- **On Surface:** `md.sys.color.on-surface` (#E6E1E5)
- **Surface Variant:** `md.sys.color.surface-variant` (#49454F)
- **On Surface Variant:** `md.sys.color.on-surface-variant` (#CAC4D0)
- **Outline:** `md.sys.color.outline` (#938F99)
- **Outline Variant:** `md.sys.color.outline-variant` (#49454F)
- **Scrim:** `md.sys.color.scrim` (#000000)
- **Inverse Surface:** `md.sys.color.inverse-surface` (#E6E1E5)
- **Inverse On Surface:** `md.sys.color.inverse-on-surface` (#313033)
- **Inverse Primary:** `md.sys.color.inverse-primary` (#6750A4)

### Typography
- **Font Family:** Roboto
- **Type Scale (Material 3):**
  - **Display Large:** Roboto, 57sp
  - **Display Medium:** Roboto, 45sp
  - **Display Small:** Roboto, 36sp
  - **Headline Large:** Roboto, 32sp
  - **Headline Medium:** Roboto, 28sp
  - **Headline Small:** Roboto, 24sp
  - **Title Large:** Roboto, 22sp
  - **Title Medium:** Roboto, 16sp, Weight 500
  - **Title Small:** Roboto, 14sp, Weight 500
  - **Body Large:** Roboto, 16sp
  - **Body Medium:** Roboto, 14sp
  - **Body Small:** Roboto, 12sp
  - **Label Large:** Roboto, 14sp, Weight 500
  - **Label Medium:** Roboto, 12sp, Weight 500
  - **Label Small:** Roboto, 11sp, Weight 500

### Spacing & Sizing
- **Base Grid Unit:** 8dp
- **Standard Margins:** 16dp
- **Standard Padding:** 16dp
- **Minimum Touch Target:** 48dp x 48dp

### Accessibility
- **Target Standard:** WCAG 2.1 Level AA
- **Requirements:**
  - All interactive elements must have a minimum touch target of 48x48dp.
  - Color contrast ratios must meet or exceed WCAG AA standards.
  - All images and icons that convey information must have content descriptions.
  - Dynamic text sizing should be supported.

---

## II. Screen Specifications

### 01_Welcome_Screen
- **Screen Name/ID:** `01_Welcome_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, filling max size. Elements are horizontally centered. Vertical arrangement is spaced with a large central graphic.

#### Components
1.  **Component: App Logo**
    - **Name:** `Image`
    - **Position & Size:** Centered horizontally. `200dp x 200dp`. Margin top `120dp`.
    - **Style:** A stylized 'B' logo with sound wave elements.
    - **Content:** `res/drawable/boomy_logo.xml`

2.  **Component: Headline Text**
    - **Name:** `Text`
    - **Position & Size:** Centered horizontally. Margin top `32dp`.
    - **Style:** Typography `md.sys.typography.headlineMedium`. Color `md.sys.color.onSurface`. Text alignment `Center`.
    - **Content:** "Make music with AI"

3.  **Component: Body Text**
    - **Name:** `Text`
    - **Position & Size:** Centered horizontally. Margin top `16dp`. Padding horizontal `32dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Color `md.sys.color.onSurfaceVariant`. Text alignment `Center`.
    - **Content:** "Create original songs in seconds, even if you've never made music before."

4.  **Component: Primary CTA Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Centered horizontally. `fillMaxWidth` with horizontal margin `24dp`. Height `52dp`. Margin top `64dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Create your song"

5.  **Component: Secondary CTA Button**
    - **Name:** `TextButton`
    - **Position & Size:** Centered horizontally. `fillMaxWidth` with horizontal margin `24dp`. Height `52dp`. Margin top `16dp`. Margin bottom `32dp`.
    - **Style:** Color `md.sys.color.primary`. Typography `md.sys.typography.labelLarge`.
    - **Content:** "Sign In"

#### Interaction & Behavior
- **Primary CTA Button:**
  - **States:** Standard Material 3 state layers for pressed (12% onPrimary overlay), hover, focused.
  - **Interaction:** On tap -> Navigate to `02_SignUp_Screen` using a `MaterialSharedAxis` (Z-axis) transition.
- **Secondary CTA Button:**
  - **States:** Standard Material 3 state layers for pressed (12% primary overlay), hover, focused.
  - **Interaction:** On tap -> Navigate to `03_SignIn_Screen` using a `MaterialSharedAxis` (Z-axis) transition.

---

### 02_SignUp_Screen
- **Screen Name/ID:** `02_SignUp_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `verticalScroll` enabled. Padding `16dp`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`. No elevation.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Create Account", style `md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:**
        - **Label:** "Email"
        - **Leading Icon:** `Icon` with `Icons.Filled.Email`.
        - **Keyboard Type:** `Email`.

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:**
        - **Label:** "Password"
        - **Leading Icon:** `Icon` with `Icons.Filled.Lock`.
        - **Trailing Icon:** `IconButton` for password visibility toggle (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`).
        - **Keyboard Type:** `Password`.

4.  **Component: Create Account Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Create Account"

5.  **Component: Social Sign-Up Divider**
    - **Name:** `Row` with `Divider` and `Text`
    - **Position & Size:** `fillMaxWidth`. Margin vertical `32dp`.
    - **Style:** `Divider` color `md.sys.color.outline`. `Text` style `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.
    - **Content:** Two `Divider`s with a `Text` element "or" in the middle.

6.  **Component: Social Sign-Up Buttons**
    - **Name:** `Column` of `OutlinedButton`s
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Each button is `OutlinedButton` with `fillMaxWidth`, height `52dp`, shape `Shape.Corner.Full`.
    - **Content:**
        - **Button 1:** Icon `res/drawable/google_logo.xml`, Text "Continue with Google". Margin top `0dp`.
        - **Button 2:** Icon `res/drawable/apple_logo.xml`, Text "Sign in with Apple". Margin top `16dp`.
        - **Button 3:** Icon `res/drawable/facebook_logo.xml`, Text "Login with Facebook". Margin top `16dp`.

7.  **Component: Sign In Link**
    - **Name:** `Row` with `Text` and `TextButton`
    - **Position & Size:** Centered horizontally at the bottom of the view. Margin top `32dp`.
    - **Style:** `Text` style `md.sys.typography.bodyMedium`. `TextButton` style `md.sys.typography.labelLarge`.
    - **Content:** `Text`: "Already have an account?", `TextButton`: "Sign in"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_Welcome_Screen`.
- **Create Account Button:** On tap -> Validate fields. On success, show `CircularProgressIndicator` inside the button, disable it, and navigate to `05_Home_Create_Screen`. On validation failure, show error text on the respective `OutlinedTextField`.
- **Social Sign-Up Buttons:** On tap -> Initiate the respective social sign-in flow. On success, navigate to `05_Home_Create_Screen`.
- **Sign In Link:** On tap -> Navigate to `03_SignIn_Screen`.

---

### 03_SignIn_Screen
- **Screen Name/ID:** `03_SignIn_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `verticalScroll` enabled. Padding `16dp`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Sign In", style `md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:**
        - **Label:** "Email"
        - **Leading Icon:** `Icon` with `Icons.Filled.Email`.
        - **Keyboard Type:** `Email`.

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:**
        - **Label:** "Password"
        - **Leading Icon:** `Icon` with `Icons.Filled.Lock`.
        - **Trailing Icon:** `IconButton` for password visibility toggle.
        - **Keyboard Type:** `Password`.

4.  **Component: Forgot Password Link**
    - **Name:** `TextButton`
    - **Position & Size:** Aligned to the end of the `Column`. Margin top `8dp`.
    - **Style:** Typography `md.sys.typography.labelLarge`.
    - **Content:** "Forgot your password?"

5.  **Component: Sign In Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Sign in"

6.  **Component: Social Sign-In Divider & Buttons:**
    - **(Identical to `02_SignUp_Screen`)**

7.  **Component: Sign Up Link**
    - **Name:** `Row` with `Text` and `TextButton`
    - **Position & Size:** Centered horizontally at the bottom of the view. Margin top `32dp`.
    - **Style:** `Text` style `md.sys.typography.bodyMedium`. `TextButton` style `md.sys.typography.labelLarge`.
    - **Content:** `Text`: "Don't have an account?", `TextButton`: "Sign up"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_Welcome_Screen`.
- **Forgot Password Link:** On tap -> Navigate to `04_Password_Reset_Screen`.
- **Sign In Button:** On tap -> Validate fields. On success, navigate to `05_Home_Create_Screen`. On failure, show a `Snackbar` with the message "Invalid email or password."
- **Social Sign-In Buttons:** On tap -> Initiate social sign-in. On success, navigate to `05_Home_Create_Screen`.
- **Sign Up Link:** On tap -> Navigate to `02_SignUp_Screen`.

---

### 04_Password_Reset_Screen
- **Screen Name/ID:** `04_Password_Reset_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout. Padding `16dp`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Reset Password", style `md.sys.typography.titleLarge`.

2.  **Component: Info Text**
    - **Name:** `Text`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.bodyMedium`. Color `md.sys.color.onSurfaceVariant`.
    - **Content:** "Enter the email address associated with your account and we'll send you a link to reset your password."

3.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:**
        - **Label:** "Email"
        - **Leading Icon:** `Icon` with `Icons.Filled.Email`.
        - **Keyboard Type:** `Email`.

4.  **Component: Reset Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Send Reset Link"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `03_SignIn_Screen`.
- **Reset Button:** On tap -> Validate email field. On success, show a `Snackbar` with the message "Password reset link sent to your email.", and navigate back to `03_SignIn_Screen`. On failure (e.g., email not found), show an error on the `OutlinedTextField`.

---

### 05_Home_Create_Screen
- **Screen Name/ID:** `05_Home_Create_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` layout with a `TopAppBar`, main content area, and `BottomNavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** `TopAppBarDefaults.enterAlwaysScrollBehavior`. Container color `md.sys.color.surface`.
    - **Content:**
        - **Title:** `Text` with content "Create Song", style `md.sys.typography.titleLarge`.
        - **Actions:** `IconButton` with `Icons.Filled.AccountCircle` for user profile.

2.  **Component: Main Content (Select Style)**
    - **Name:** `LazyVerticalGrid`
    - **Position & Size:** Fills the main content area of the `Scaffold`. Padding `16dp`.
    - **Layout:** 2 columns. `Arrangement.spacedBy(16.dp)`.
    - **Content:** A grid of `Card` components for each music style.
        - **Card Item:**
            - **Name:** `Card`
            - **Size:** `168dp x 168dp`.
            - **Style:** `CardDefaults.cardColors(containerColor = md.sys.color.surfaceVariant)`. Shape `Shape.Corner.Large`.
            - **Content:** `Column` with an `Image` (representing the style, e.g., a synth for Electronic) and a `Text` label below it.
                - **Image:** `120dp x 120dp`.
                - **Text:** "Electronic Dance", "Rap Beats", "Lo-fi", "Custom", etc. Style `md.sys.typography.titleMedium`, color `md.sys.color.onSurfaceVariant`.

3.  **Component: Bottom Navigation Bar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`. `fillMaxWidth`.
    - **Style:** Container color `md.sys.color.surfaceContainer`.
    - **Content:** Two `NavigationBarItem`s.
        - **Item 1 (Selected):**
            - **Icon:** `Icons.Filled.AddCircle`
            - **Label:** "Create"
            - **Selected:** `true`
        - **Item 2 (Unselected):**
            - **Icon:** `Icons.Outlined.LibraryMusic`
            - **Label:** "Library"
            - **Selected:** `false`

#### Interaction & Behavior
- **Style Card:** On tap -> Navigate to `06_Create_Song_Select_Sub-style_Screen` (or `07_Create_Song_Custom_Style_Screen` for "Custom"). Pass the selected style as an argument. Use `MaterialSharedAxis` (X-axis) transition.
- **Library Navigation Item:** On tap -> Navigate to `14_Library_Screen`. Use a `MaterialFadeThrough` transition.
- **Profile Icon:** On tap -> Open a user profile screen/menu (out of scope for this flow).

---

### 06_Create_Song_Select_Sub-style_Screen
- **Screen Name/ID:** `06_Create_Song_Select_Sub-style_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with a `LazyColumn` for the list of sub-styles.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with dynamic content, e.g., "Electronic Dance", style `md.sys.typography.titleLarge`.

2.  **Component: Sub-style List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the remaining space. Padding horizontal `16dp`.
    - **Content:** A list of `ListItem` components.
        - **ListItem:**
            - **Name:** `ListItem`
            - **Size:** `fillMaxWidth`, height `72dp`.
            - **Style:** `ListItemDefaults.colors(containerColor = md.sys.color.surfaceVariant)`. Rounded corners `Shape.Corner.Medium`. Margin vertical `8dp`.
            - **Content:**
                - **Headline Content:** `Text` with sub-style name (e.g., "Warehouse Groove", "Hyperdrive"). Style `md.sys.typography.titleMedium`.
                - **Supporting Content:** `Text` with a brief description. Style `md.sys.typography.bodyMedium`.
                - **Trailing Content:** `IconButton` with `Icons.Filled.PlayArrow` to preview the style.

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `05_Home_Create_Screen`.
- **ListItem:** On tap -> Navigate to `08_Song_Generating_Screen`. Pass the selected sub-style as an argument.
- **Play Icon:** On tap -> Play a short audio preview of the sub-style. The icon should change to `Icons.Filled.Stop` while playing.

---

### 07_Create_Song_Custom_Style_Screen
- **Screen Name/ID:** `07_Create_Song_Custom_Style_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with `verticalScroll`. Padding `16dp`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Custom Style", style `md.sys.typography.titleLarge`.

2.  **Component: Parameter Sliders**
    - **Name:** `Column` of `Slider` components.
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Content:** Multiple labeled sliders.
        - **Slider 1: Tempo**
            - **Label:** `Text` "Tempo", style `md.sys.typography.titleMedium`.
            - **Slider:** `Slider` component. Value range 60-180 BPM.
            - **Value Label:** `Text` showing the current BPM.
        - **Slider 2: Density**
            - **Label:** `Text` "Density", style `md.sys.typography.titleMedium`.
            - **Slider:** `Slider` component. Value range 0.0f to 1.0f.
            - **Value Label:** `Text` showing "Low", "Medium", "High".
        - **(Add more sliders for other parameters like 'Energy', 'Instrumentation Mix', etc.)**

3.  **Component: Create Song Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `32dp`, margin bottom `16dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Create Song"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `05_Home_Create_Screen`.
- **Slider:** On value change -> Update the corresponding value label text.
- **Create Song Button:** On tap -> Navigate to `08_Song_Generating_Screen`. Pass all custom parameters as arguments.

---

### 08_Song_Generating_Screen
- **Screen Name/ID:** `08_Song_Generating_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.scrim` with 80% opacity, overlaying the previous screen.
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center` and `horizontalAlignment = Alignment.CenterHorizontally`.

#### Components
1.  **Component: Progress Indicator**
    - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered on screen. Size `64dp x 64dp`.
    - **Style:** Color `md.sys.color.primary`. Stroke width `5dp`.

2.  **Component: Status Text**
    - **Name:** `Text`
    - **Position & Size:** Centered, below the progress indicator. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.titleMedium`. Color `md.sys.color.inverseOnSurface`.
    - **Content:** "Composing your masterpiece..." (Can be animated to cycle through messages like "Tuning the synths...", "Laying down the beat...").

#### Interaction & Behavior
- **Lifecycle:** This screen is displayed modally.
- **Behavior:** After a simulated or real processing time (e.g., 5-10 seconds), the app automatically navigates to `09_Song_Editor_Screen`. The transition should be a `Crossfade`.
- **Back Press:** The back press action should be disabled on this screen to prevent interruption of the generation process.

---

### 09_Song_Editor_Screen
- **Screen Name/ID:** `09_Song_Editor_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`, main content, a player control bar, and `BottomNavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** Colors `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`.
        - **Title:** `OutlinedTextField` (borderless style) for the song title. Initial content "Untitled Song".
        - **Actions:** `FilledButton` with text "Save".

2.  **Component: Song Waveform/Visualization**
    - **Name:** `Canvas` or `Image`
    - **Position & Size:** `fillMaxWidth`, height `200dp`. Margin top `16dp`.
    - **Style:** A visual representation of the song's audio waveform.
    - **Content:** Dynamically generated waveform graphic.

3.  **Component: Player Controls**
    - **Name:** `Row`
    - **Position & Size:** Centered horizontally, below the waveform. `fillMaxWidth`. Padding `16dp`.
    - **Content:**
        - `IconButton` with `Icons.Filled.Replay10`.
        - `LargeFloatingActionButton` with `Icons.Filled.PlayArrow` / `Icons.Filled.Pause`.
        - `IconButton` with `Icons.Filled.Forward10`.

4.  **Component: Editing Options**
    - **Name:** `LazyVerticalGrid`
    - **Position & Size:** Fills remaining space above the bottom nav bar. Padding `16dp`.
    - **Layout:** 2 columns. `Arrangement.spacedBy(16.dp)`.
    - **Content:** Grid of `Card`s for editing actions.
        - **Card 1:** Icon `Icons.Filled.Autorenew`, Text "Rewrite".
        - **Card 2:** Icon `Icons.Filled.ViewQuilt`, Text "Rearrange".
        - **Card 3:** Icon `Icons.Filled.Piano`, Text "Instruments & Sounds".
        - **Card 4:** Icon `Icons.Filled.Mic`, Text "Add Vocals".

5.  **Component: Bottom Navigation Bar**
    - **(Identical to `05_Home_Create_Screen`, but no item is selected as this is a modal-like editor view).**

#### Interaction & Behavior
- **Close Icon:** On tap -> Show a confirmation `AlertDialog` ("Discard unsaved changes?"). On confirm, navigate to `14_Library_Screen`.
- **Save Button:** On tap -> Save the song to the user's library. Show a `Snackbar` "Song saved to Library". Navigate to `14_Library_Screen`.
- **Play/Pause FAB:** On tap -> Toggles song playback. Icon changes between Play and Pause.
- **Rewrite Card:** On tap -> Open `10_Rewrite_Options_Screen` as a `ModalBottomSheet`.
- **Rearrange Card:** On tap -> Navigate to `11_Rearrange_Options_Screen`.
- **Instruments Card:** On tap -> Open `12_Instruments_Sounds_Options_Screen` as a `ModalBottomSheet`.
- **Add Vocals Card:** On tap -> Open `13_Add_Vocals_Screen` as a `ModalBottomSheet`.
- **Library/Create Tabs:** Navigate to the respective screens, prompting for unsaved changes first.

---

### 10_Rewrite_Options_Screen
- **Screen Name/ID:** `10_Rewrite_Options_Screen`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.
- **Layout:** `Column` with padding `16dp`.

#### Components
1.  **Component: Bottom Sheet Handle**
    - **Name:** `DragHandle`
    - **Position & Size:** Top center of the sheet.
    - **Style:** Standard Material 3 drag handle.

2.  **Component: Title**
    - **Name:** `Text`
    - **Position & Size:** `fillMaxWidth`. Margin bottom `16dp`.
    - **Style:** Typography `md.sys.typography.titleLarge`. Text alignment `Center`.
    - **Content:** "Rewrite Song"

3.  **Component: Parameter Sliders**
    - **(Identical in structure to `07_Create_Song_Custom_Style_Screen`, but with different parameters like "Tempo", "Lead Density", "Drum Intensity").**

4.  **Component: Rewrite Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`, margin bottom `16dp`.
    - **Style:** Color `md.sys.color.primary`. Shape `Shape.Corner.Full`.
    - **Content:** "Rewrite Song"

#### Interaction & Behavior
- **Rewrite Button:** On tap -> Dismiss the bottom sheet. Navigate to `08_Song_Generating_Screen` with the new parameters.
- **Swipe Down/Back Press:** Dismisses the bottom sheet.

---

### 11_Rearrange_Options_Screen
- **Screen Name/ID:** `11_Rearrange_Options_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with a `LazyColumn` for draggable items.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` "Rearrange Song".
        - **Actions:** `TextButton` with text "Save".

2.  **Component: Draggable Section List**
    - **Name:** `LazyColumn` with `dragAndDrop` modifier.
    - **Position & Size:** Fills the remaining space. Padding `16dp`.
    - **Content:** List of `ListItem`s representing song sections.
        - **ListItem:**
            - **Name:** `ListItem`
            - **Size:** `fillMaxWidth`.
            - **Style:** Container `md.sys.color.surfaceVariant`.
            - **Content:**
                - **Leading Content:** `Icon` `Icons.Filled.DragHandle`.
                - **Headline Content:** `Text` "Intro", "Verse 1", "Chorus", etc.

#### Interaction & Behavior
- **Navigation Icon:** On tap -> Navigate back to `09_Song_Editor_Screen`.
- **Save Button:** On tap -> Save the new arrangement. Navigate back to `09_Song_Editor_Screen`.
- **Drag Handle:** On long press and drag -> Allows reordering of the `ListItem`s in the `LazyColumn`.

---

### 12_Instruments_Sounds_Options_Screen
- **Screen Name/ID:** `12_Instruments_Sounds_Options_Screen`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.
- **Layout:** `Column` with a `LazyColumn`.

#### Components
1.  **Component: Bottom Sheet Handle & Title**
    - **(Identical to `10_Rewrite_Options_Screen`, Title is "Instruments & Sounds").**

2.  **Component: Instrument List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills available space. Padding horizontal `16dp`.
    - **Content:** List of `ListItem`s for each instrument track.
        - **ListItem:**
            - **Headline Content:** `Text` "Lead Synth", "Drums", "Bassline".
            - **Supporting Content:** `Slider` to adjust the volume of the track.
            - **Trailing Content:** `IconButton` with `Icons.Filled.Delete` to remove the track.

3.  **Component: Save Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Padding `16dp`.
    - **Content:** "Save"

#### Interaction & Behavior
- **Delete Icon:** On tap -> Show confirmation `AlertDialog`. On confirm, remove the item from the list.
- **Save Button:** On tap -> Apply changes. Dismiss the bottom sheet and return to `09_Song_Editor_Screen`.

---

### 13_Add_Vocals_Screen
- **Screen Name/ID:** `13_Add_Vocals_Screen`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.
- **Layout:** `Column` with padding `16dp`.

#### Components
1.  **Component: Bottom Sheet Handle & Title**
    - **(Identical to `10_Rewrite_Options_Screen`, Title is "Add Vocals").**

2.  **Component: Auto Vocals Button**
    - **Name:** `FilledTonalButton`
    - **Position & Size:** `fillMaxWidth`. Height `64dp`. Margin top `16dp`.
    - **Content:** `Row` with `Icon` `Icons.Filled.AutoAwesome` and `Text` "Auto Vocals".

3.  **Component: Record Voice Button**
    - **Name:** `FilledTonalButton`
    - **Position & Size:** `fillMaxWidth`. Height `64dp`. Margin top `16dp`. Margin bottom `16dp`.
    - **Content:** `Row` with `Icon` `Icons.Filled.Mic` and `Text` "Record Voice".

#### Interaction & Behavior
- **Auto Vocals Button:** On tap -> Initiate AI vocal generation. Dismiss sheet and return to `09_Song_Editor_Screen`, showing a progress indicator on the waveform.
- **Record Voice Button:** On tap -> Request microphone permissions. Open a dedicated voice recording interface (out of scope). On completion, return to `09_Song_Editor_Screen`.

---

### 14_Library_Screen
- **Screen Name/ID:** `14_Library_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `BottomNavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** `TopAppBarDefaults.enterAlwaysScrollBehavior`.
    - **Content:**
        - **Title:** `Text` "Library".
        - **Actions:** `IconButton` with `Icons.Filled.Search`.

2.  **Component: Song List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the main content area. Padding `16dp`.
    - **Content:** List of song items.
        - **Song Item Card:**
            - **Name:** `Card`
            - **Size:** `fillMaxWidth`.
            - **Style:** `CardDefaults.outlinedCardColors()`.
            - **Content:** `Row` containing:
                - `Image` (Album Art): `64dp x 64dp`. Shape `Shape.Corner.Medium`.
                - `Column` (Song Info): `weight(1f)`. Padding horizontal `16dp`.
                    - `Text` (Title): "Cosmic Drift", style `md.sys.typography.titleMedium`.
                    - `Text` (Artist/Date): "Boomy AI - Oct 26", style `md.sys.typography.bodyMedium`.
                - `IconButton` (More Options): `Icons.Filled.MoreVert`.

3.  **Component: Bottom Navigation Bar**
    - **(Identical to `05_Home_Create_Screen`, but with 'Library' selected).**

#### Interaction & Behavior
- **Song Item Card:** On tap -> Navigate to `09_Song_Editor_Screen` to play/edit the song.
- **More Options Icon:** On tap -> Open `15_Song_Options_Menu_Screen` as a `ModalBottomSheet`.
- **Create Navigation Item:** On tap -> Navigate to `05_Home_Create_Screen`. Use `MaterialFadeThrough` transition.
- **Empty State:** If the library is empty, show a centered `Column` with an `Icon` (`Icons.Outlined.MusicNote`), a `Text` "Your library is empty", and a `FilledButton` "Create your first song" which navigates to `05_Home_Create_Screen`.

---

### 15_Song_Options_Menu_Screen
- **Screen Name/ID:** `15_Song_Options_Menu_Screen`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.
- **Layout:** `Column`.

#### Components
1.  **Component: Bottom Sheet Handle**
    - **(Identical to `10_Rewrite_Options_Screen`)**

2.  **Component: Menu Item List**
    - **Name:** `Column`
    - **Position & Size:** `fillMaxWidth`.
    - **Content:** A list of `ListItem` components for menu actions.
        - **ListItem 1:** `Icon` `Icons.Filled.Download`, `Text` "Download".
        - **ListItem 2:** `Icon` `Icons.Filled.Publish`, `Text` "Release Song".
        - **ListItem 3:** `Icon` `Icons.Filled.ContentCopy`, `Text` "Duplicate Song".
        - **ListItem 4:** `Icon` `Icons.Filled.Edit`, `Text` "Edit Song".
        - **ListItem 5:** `Icon` `Icons.Filled.Archive`, `Text` "Archive Song" (color `md.sys.color.error`).

#### Interaction & Behavior
- **Download:** On tap -> Initiate file download. Show progress in system notifications. Dismiss sheet.
- **Release Song:** On tap -> Dismiss sheet. Navigate to `16_Release_Song_Details_Screen`.
- **Duplicate Song:** On tap -> Create a copy of the song in the library. Show `Snackbar` "Song duplicated". Dismiss sheet.
- **Edit Song:** On tap -> Dismiss sheet. Navigate to `09_Song_Editor_Screen`.
- **Archive Song:** On tap -> Show confirmation `AlertDialog`. On confirm, archive the song. Dismiss sheet.

---

### 16_Release_Song_Details_Screen
- **Screen Name/ID:** `16_Release_Song_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with `verticalScroll`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` "Release Song".

2.  **Component: Cover Art Uploader**
    - **Name:** `Card`
    - **Position & Size:** `150dp x 150dp`. Centered horizontally. Margin top `24dp`.
    - **Style:** Dotted border.
    - **Content:** `Column` with `Icon` `Icons.Filled.AddPhotoAlternate` and `Text` "Upload Cover Art".

3.  **Component: Song Title Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Padding horizontal `16dp`. Margin top `24dp`.
    - **Content:** Label "Song Title".

4.  **Component: Artist Name Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Padding horizontal `16dp`. Margin top `16dp`.
    - **Content:** Label "Artist Name".

5.  **Component: Tags/Genre Field**
    - **Name:** `OutlinedTextField` (or a specialized chip input field).
    - **Position & Size:** `fillMaxWidth`. Padding horizontal `16dp`. Margin top `16dp`.
    - **Content:** Label "Tags (e.g., lofi, chill, electronic)".

6.  **Component: Submit Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Padding `16dp`. Margin top `32dp`.
    - **Content:** "Submit and Review"

#### Interaction & Behavior
- **Navigation Icon:** On tap -> Navigate back to `14_Library_Screen`.
- **Cover Art Uploader:** On tap -> Open system file picker to select an image.
- **Submit Button:** On tap -> Validate all fields. On success, show a `Snackbar` "Song submitted for review". Navigate to `14_Library_Screen`. On failure, show errors on the relevant fields.

---

## V. Critical Scenarios & States

### Error States
- **No Internet Connection:**
  - **UI:** A `Snackbar` is displayed at the bottom of the screen.
  - **Style:** Container color `md.sys.color.errorContainer`, text color `md.sys.color.onErrorContainer`.
  - **Content:** Message "No internet connection." with an optional "Retry" `TextButton`.
- **API/Server Error:**
  - **UI:** A `Snackbar` is displayed.
  - **Content:** Message "Something went wrong. Please try again."
- **Form Validation Error:**
  - **UI:** The `OutlinedTextField` component displays an error state.
  - **Style:** The outline and label color change to `md.sys.color.error`.
  - **Content:** Helper text below the field describes the error (e.g., "Please enter a valid email address.").

### Empty States
- **Library Screen (`14_Library_Screen`):**
  - **UI:** When no songs are present, the `LazyColumn` is replaced with a centered `Column`.
  - **Layout:** `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.
  - **Content:**
    1.  `Icon`: `Icons.Outlined.MusicNote`, size `64dp`, tint `md.sys.color.onSurfaceVariant`.
    2.  `Text`: "Your library is empty", style `md.sys.typography.titleLarge`, margin top `16dp`.
    3.  `Text`: "Songs you create and save will appear here.", style `md.sys.typography.bodyMedium`, margin top `8dp`.
    4.  `FilledButton`: "Create your first song", margin top `24dp`. Navigates to `05_Home_Create_Screen`.

### Loading States
- **Initial Data Fetch (e.g., Library):**
  - **UI:** A full-screen `CircularProgressIndicator` is displayed centered within the screen's content area.
  - **Behavior:** The indicator is shown while the initial list of songs is being fetched. It is replaced by the content or the empty state once the fetch is complete.
- **Button Loading State:**
  - **UI:** For actions like "Sign In" or "Create Account", the button's text is replaced by a `CircularProgressIndicator` (size `24dp`). The button is disabled.
  - **Behavior:** This indicates an in-progress network request initiated by the button.
- **Song Generation (`08_Song_Generating_Screen`):**
  - **UI:** A dedicated full-screen modal view with a large `CircularProgressIndicator` and descriptive text. This is a blocking UI to focus the user on the creation process.

---


============================================================
## APP 2: App_2
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Splash - Android App Design Specification

## I. Global Specifications

### Platform
- **Target:** Android Mobile App
- **API Level:** Target SDK 34 (Android 14)
- **Orientation:** Portrait

### Design System
- **System:** Material Design 3
- **Theming:** Light and Dark modes supported. Dynamic color (Material You) enabled, using the brand color as a fallback seed.

### Colors
- **Seed Color:** `#7E57C2` (Deep Purple 300)
- **Light Theme Color Roles:**
  - `md.sys.color.primary`: `#6750A4`
  - `md.sys.color.onPrimary`: `#FFFFFF`
  - `md.sys.color.primaryContainer`: `#EADDFF`
  - `md.sys.color.onPrimaryContainer`: `#21005D`
  - `md.sys.color.secondary`: `#625B71`
  - `md.sys.color.onSecondary`: `#FFFFFF`
  - `md.sys.color.secondaryContainer`: `#E8DEF8`
  - `md.sys.color.onSecondaryContainer`: `#1D192B`
  - `md.sys.color.tertiary`: `#7D5260`
  - `md.sys.color.onTertiary`: `#FFFFFF`
  - `md.sys.color.tertiaryContainer`: `#FFD8E4`
  - `md.sys.color.onTertiaryContainer`: `#31111D`
  - `md.sys.color.error`: `#B3261E`
  - `md.sys.color.onError`: `#FFFFFF`
  - `md.sys.color.errorContainer`: `#F9DEDC`
  - `md.sys.color.onErrorContainer`: `#410E0B`
  - `md.sys.color.background`: `#FFFBFE`
  - `md.sys.color.onBackground`: `#1C1B1F`
  - `md.sys.color.surface`: `#FFFBFE`
  - `md.sys.color.onSurface`: `#1C1B1F`
  - `md.sys.color.surfaceVariant`: `#E7E0EC`
  - `md.sys.color.onSurfaceVariant`: `#49454F`
  - `md.sys.color.outline`: `#79747E`
  - `md.sys.color.outlineVariant`: `#CAC4D0`
  - `md.sys.color.inverseSurface`: `#313033`
  - `md.sys.color.inverseOnSurface`: `#F4EFF4`
  - `md.sys.color.inversePrimary`: `#D0BCFF`
- **Dark Theme Color Roles:**
  - `md.sys.color.primary`: `#D0BCFF`
  - `md.sys.color.onPrimary`: `#381E72`
  - `md.sys.color.primaryContainer`: `#4F378B`
  - `md.sys.color.onPrimaryContainer`: `#EADDFF`
  - `md.sys.color.secondary`: `#CCC2DC`
  - `md.sys.color.onSecondary`: `#332D41`
  - `md.sys.color.secondaryContainer`: `#4A4458`
  - `md.sys.color.onSecondaryContainer`: `#E8DEF8`
  - `md.sys.color.tertiary`: `#EFB8C8`
  - `md.sys.color.onTertiary`: `#492532`
  - `md.sys.color.tertiaryContainer`: `#633B48`
  - `md.sys.color.onTertiaryContainer`: `#FFD8E4`
  - `md.sys.color.error`: `#F2B8B5`
  - `md.sys.color.onError`: `#601410`
  - `md.sys.color.errorContainer`: `#8C1D18`
  - `md.sys.color.onErrorContainer`: `#F9DEDC`
  - `md.sys.color.background`: `#1C1B1F`
  - `md.sys.color.onBackground`: `#E6E1E5`
  - `md.sys.color.surface`: `#1C1B1F`
  - `md.sys.color.onSurface`: `#E6E1E5`
  - `md.sys.color.surfaceVariant`: `#49454F`
  - `md.sys.color.onSurfaceVariant`: `#CAC4D0`
  - `md.sys.color.outline`: `#938F99`
  - `md.sys.color.outlineVariant`: `#49454F`
  - `md.sys.color.inverseSurface`: `#E6E1E5`
  - `md.sys.color.inverseOnSurface`: `#313033`
  - `md.sys.color.inversePrimary`: `#6750A4`

### Typography
- **Font Family:** Roboto
- **Type Scale:** Material 3 Default
  - `displayLarge`: Roboto, 57sp
  - `displayMedium`: Roboto, 45sp
  - `displaySmall`: Roboto, 36sp
  - `headlineLarge`: Roboto, 32sp
  - `headlineMedium`: Roboto, 28sp
  - `headlineSmall`: Roboto, 24sp
  - `titleLarge`: Roboto, 22sp
  - `titleMedium`: Roboto, 16sp, Weight 500
  - `titleSmall`: Roboto, 14sp, Weight 500
  - `labelLarge`: Roboto, 14sp, Weight 500
  - `labelMedium`: Roboto, 12sp, Weight 500
  - `labelSmall`: Roboto, 11sp, Weight 500
  - `bodyLarge`: Roboto, 16sp
  - `bodyMedium`: Roboto, 14sp
  - `bodySmall`: Roboto, 12sp

### Spacing & Grid
- **Base Unit:** 8dp
- **Standard Margins:** 16dp
- **Standard Padding:** 16dp
- **Minimum Touch Target:** 48dp x 48dp

### Accessibility
- **Target Standard:** WCAG 2.1 Level AA
- **Requirements:**
  - All interactive elements must have a minimum touch target of 48x48dp.
  - Text must meet a minimum contrast ratio of 4.5:1 (AA) against its background.
  - All images and icons that convey information must have content descriptions.

---

## II. Screen Specifications

### Flow: Onboarding and Authentication

---

### **Screen 1: Welcome**
- **Screen Name/ID:** `01_01_Welcome`
- **Dimensions:** 393x852dp (typical phone)
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, elements are horizontally centered. Vertical arrangement is `SpaceBetween`.

#### Components:
1.  **Name:** `Spacer`
    - **Position & Size:** Height: 64dp.
2.  **Name:** `Image` (App Logo)
    - **Position & Size:** Width: 120dp, Height: 120dp. Alignment: `centerHorizontal`.
    - **Style:** Placeholder for the "Splash" app logo.
    - **Content:** `ic_splash_logo.svg`
3.  **Name:** `Column` (Text Content)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 24dp. Alignment: `centerHorizontal`.
    - **Layout:** Contains Headline and Body text.
    - **Components:**
        1.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Alignment: `centerHorizontal`.
            - **Style:** Typography: `md.sys.typography.headlineLarge`. Color: `md.sys.color.onSurface`. Text Alignment: `Center`.
            - **Content:** "Create Music in Seconds"
        2.  **Name:** `Text` (Body)
            - **Position & Size:** `wrapContent`. Margin: top 16dp. Alignment: `centerHorizontal`.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text Alignment: `Center`.
            - **Content:** "Use AI to generate lyrics, vocals, and beats. No experience needed."
4.  **Name:** `FilledButton` (Primary CTA)
    - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: horizontal 16dp, bottom 32dp.
    - **Style:** Color: `md.sys.color.primary`. Text Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
    - **Content:** "Get Started"
    - **Typography:** `md.sys.typography.labelLarge`.

#### Interaction & Behavior:
- **States:**
  - `FilledButton`: Standard Material 3 states for pressed (shows ripple, `md.sys.state.pressed-state-layer-opacity`), hover, focused, and disabled.
- **Interactions:**
  - On tap of `FilledButton` -> Navigate to `01_02_Onboarding_Create_Music`.
- **Animations:**
  - Screen Transition (Exit): `MaterialSharedAxis` (Z-axis).

---

### **Screen 2: Onboarding - Create Music**
- **Screen Name/ID:** `01_02_Onboarding_Create_Music`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `fillMaxHeight`.

#### Components:
1.  **Name:** `Image` (Onboarding Illustration)
    - **Position & Size:** `fillMaxWidth`. Height: 300dp.
    - **Style:** A vibrant illustration depicting music creation (e.g., sound waves, musical notes).
    - **Content:** `img_onboarding_create.svg`
2.  **Name:** `Column` (Text & Controls)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 24dp, vertical 32dp.
    - **Layout:** Contains progress indicator, text, and button.
    - **Components:**
        1.  **Name:** `LinearProgressIndicator` (Step Indicator)
            - **Position & Size:** `fillMaxWidth`.
            - **Style:** Color: `md.sys.color.primary`. Background Color: `md.sys.color.surfaceVariant`.
            - **Content:** Progress value: 0.33 (1 of 3).
        2.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 32dp.
            - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text Alignment: `Start`.
            - **Content:** "1. Create Music"
        3.  **Name:** `Text` (Body)
            - **Position & Size:** `wrapContent`. Margin: top 16dp.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text Alignment: `Start`.
            - **Content:** "Pick a genre, choose an AI singer, and generate lyrics from a simple prompt."
        4.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`. Pushes the button to the bottom.
        5.  **Name:** `FilledButton` (Next)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 32dp.
            - **Style:** Color: `md.sys.color.primary`. Text Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
            - **Content:** "Next"
            - **Typography:** `md.sys.typography.labelLarge`.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `FilledButton` -> Navigate to `01_03_Onboarding_Share_Music`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 3: Onboarding - Share Music**
- **Screen Name/ID:** `01_03_Onboarding_Share_Music`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `fillMaxHeight`.

#### Components:
1.  **Name:** `Image` (Onboarding Illustration)
    - **Position & Size:** `fillMaxWidth`. Height: 300dp.
    - **Style:** An illustration showing music being shared to social platforms.
    - **Content:** `img_onboarding_share.svg`
2.  **Name:** `Column` (Text & Controls)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 24dp, vertical 32dp.
    - **Layout:** Contains progress indicator, text, and button.
    - **Components:**
        1.  **Name:** `LinearProgressIndicator` (Step Indicator)
            - **Position & Size:** `fillMaxWidth`.
            - **Style:** Color: `md.sys.color.primary`. Background Color: `md.sys.color.surfaceVariant`.
            - **Content:** Progress value: 0.66 (2 of 3).
        2.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 32dp.
            - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text Alignment: `Start`.
            - **Content:** "2. Share Your Music"
        3.  **Name:** `Text` (Body)
            - **Position & Size:** `wrapContent`. Margin: top 16dp.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text Alignment: `Start`.
            - **Content:** "Export your creations and share them with the world on TikTok, Instagram, and more."
        4.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`.
        5.  **Name:** `FilledButton` (Next)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 32dp.
            - **Style:** Color: `md.sys.color.primary`. Text Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
            - **Content:** "Next"
            - **Typography:** `md.sys.typography.labelLarge`.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `FilledButton` -> Navigate to `01_04_Onboarding_Discover_Music`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 4: Onboarding - Discover Music**
- **Screen Name/ID:** `01_04_Onboarding_Discover_Music`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `fillMaxHeight`.

#### Components:
1.  **Name:** `Image` (Onboarding Illustration)
    - **Position & Size:** `fillMaxWidth`. Height: 300dp.
    - **Style:** An illustration showing a feed of music created by other users.
    - **Content:** `img_onboarding_discover.svg`
2.  **Name:** `Column` (Text & Controls)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 24dp, vertical 32dp.
    - **Layout:** Contains progress indicator, text, and button.
    - **Components:**
        1.  **Name:** `LinearProgressIndicator` (Step Indicator)
            - **Position & Size:** `fillMaxWidth`.
            - **Style:** Color: `md.sys.color.primary`. Background Color: `md.sys.color.surfaceVariant`.
            - **Content:** Progress value: 1.0 (3 of 3).
        2.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 32dp.
            - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text Alignment: `Start`.
            - **Content:** "3. Discover & Remix"
        3.  **Name:** `Text` (Body)
            - **Position & Size:** `wrapContent`. Margin: top 16dp.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text Alignment: `Start`.
            - **Content:** "Explore a feed of music from the community and remix tracks you love."
        4.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`.
        5.  **Name:** `FilledButton` (Let's go)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 32dp.
            - **Style:** Color: `md.sys.color.primary`. Text Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
            - **Content:** "Let's go"
            - **Typography:** `md.sys.typography.labelLarge`.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `FilledButton` -> Navigate to `01_05_Sign_Up_Options`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 5: Sign Up Options**
- **Screen Name/ID:** `01_05_Sign_Up_Options`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `fillMaxHeight`, padding horizontal 16dp, padding bottom 32dp.

#### Components:
1.  **Name:** `Spacer`
    - **Position & Size:** `weight(1f)`.
2.  **Name:** `Image` (App Logo)
    - **Position & Size:** Width: 80dp, Height: 80dp. Alignment: `centerHorizontal`.
    - **Content:** `ic_splash_logo.svg`
3.  **Name:** `Text` (Headline)
    - **Position & Size:** `wrapContent`. Margin: top 24dp. Alignment: `centerHorizontal`.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`.
    - **Content:** "Sign up or log in"
4.  **Name:** `Spacer`
    - **Position & Size:** `weight(1f)`.
5.  **Name:** `OutlinedButton` (Continue with Google)
    - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 24dp.
    - **Style:** Outline Color: `md.sys.color.outline`. Shape: `Shape.Corner.Full`.
    - **Content:** `Row` containing an icon and text.
        - **Icon:** Google logo, 24x24dp.
        - **Text:** "Continue with Google". Typography: `md.sys.typography.labelLarge`. Color: `md.sys.color.onSurface`. Margin: start 16dp.
6.  **Name:** `OutlinedButton` (Continue with Apple)
    - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 16dp.
    - **Style:** Outline Color: `md.sys.color.outline`. Shape: `Shape.Corner.Full`.
    - **Content:** `Row` containing an icon and text.
        - **Icon:** Apple logo, 24x24dp.
        - **Text:** "Continue with Apple". Typography: `md.sys.typography.labelLarge`. Color: `md.sys.color.onSurface`. Margin: start 16dp.
7.  **Name:** `FilledButton` (Sign up with email)
    - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 16dp.
    - **Style:** Color: `md.sys.color.primary`. Text Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
    - **Content:** "Sign up with email"
    - **Typography:** `md.sys.typography.labelLarge`.
8.  **Name:** `Row` (Log in link)
    - **Position & Size:** `wrapContent`. Alignment: `centerHorizontal`. Margin: top 24dp.
    - **Components:**
        1.  **Name:** `Text`
            - **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`.
            - **Content:** "Already have an account? "
        2.  **Name:** `TextButton`
            - **Position & Size:** `wrapContent`. Min height 48dp.
            - **Style:** Text Color: `md.sys.color.primary`.
            - **Content:** "Log in"
            - **Typography:** `md.sys.typography.labelLarge`.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Continue with Google' -> (Initiate Google Sign-In flow) -> On success, navigate to `03_01_Home_Feed`.
  - On tap of 'Continue with Apple' -> (Initiate Apple Sign-In flow) -> On success, navigate to `03_01_Home_Feed`.
  - On tap of 'Sign up with email' -> Navigate to `01_06_Email_Sign_Up`.
  - On tap of 'Log in' `TextButton` -> Navigate to `01_07_Email_Log_In`.
- **Animations:**
  - Screen Transition (Enter): `MaterialSharedAxis` (Z-axis).
  - Screen Transition (Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 6: Email Sign Up**
- **Screen Name/ID:** `01_06_Email_Sign_Up`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`. Body is a `Column` with padding.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
2.  **Name:** `Column` (Form)
    - **Position & Size:** `fillMaxSize`. Padding: horizontal 16dp.
    - **Components:**
        1.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 16dp.
            - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`.
            - **Content:** "Create your account"
        2.  **Name:** `OutlinedTextField` (Email)
            - **Position & Size:** `fillMaxWidth`. Margin: top 32dp.
            - **Style:** Standard M3 `OutlinedTextField`.
            - **Content:** Label: "Email". Keyboard type: `Email`.
        3.  **Name:** `OutlinedTextField` (Password)
            - **Position & Size:** `fillMaxWidth`. Margin: top 16dp.
            - **Style:** Standard M3 `OutlinedTextField`.
            - **Content:** Label: "Password". Keyboard type: `Password`. Visual transformation: `PasswordVisualTransformation`. Trailing icon: `IconButton` with `Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff` to toggle visibility.
        4.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`.
        5.  **Name:** `FilledButton` (Sign up)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 16dp.
            - **Style:** Color: `md.sys.color.primary`. Shape: `Shape.Corner.Full`.
            - **Content:** "Sign up"
            - **State:** Disabled until both fields are valid.
        6.  **Name:** `Row` (Log in link)
            - **Position & Size:** `wrapContent`. Alignment: `centerHorizontal`. Margin: bottom 32dp.
            - **Components:**
                - **Text:** "Already have an account? "
                - **TextButton:** "Log in"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `ArrowBack` icon -> Navigate back to `01_05_Sign_Up_Options`.
  - On tap of `FilledButton` 'Sign up' -> (Perform validation) -> On success, navigate to `03_01_Home_Feed`.
  - On tap of `TextButton` 'Log in' -> Navigate to `01_07_Email_Log_In`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 7: Email Log In**
- **Screen Name/ID:** `01_07_Email_Log_In`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`. Body is a `Column` with padding.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
2.  **Name:** `Column` (Form)
    - **Position & Size:** `fillMaxSize`. Padding: horizontal 16dp.
    - **Components:**
        1.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 16dp.
            - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`.
            - **Content:** "Welcome back"
        2.  **Name:** `OutlinedTextField` (Email)
            - **Position & Size:** `fillMaxWidth`. Margin: top 32dp.
            - **Style:** Standard M3 `OutlinedTextField`.
            - **Content:** Label: "Email".
        3.  **Name:** `OutlinedTextField` (Password)
            - **Position & Size:** `fillMaxWidth`. Margin: top 16dp.
            - **Style:** Standard M3 `OutlinedTextField`.
            - **Content:** Label: "Password". Visual transformation: `PasswordVisualTransformation`.
        4.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`.
        5.  **Name:** `FilledButton` (Log in)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 16dp.
            - **Style:** Color: `md.sys.color.primary`. Shape: `Shape.Corner.Full`.
            - **Content:** "Log in"
            - **State:** Disabled until both fields are filled.
        6.  **Name:** `Row` (Sign up link)
            - **Position & Size:** `wrapContent`. Alignment: `centerHorizontal`. Margin: bottom 32dp.
            - **Components:**
                - **Text:** "Don't have an account? "
                - **TextButton:** "Sign up"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `ArrowBack` icon -> Navigate back to `01_05_Sign_Up_Options`.
  - On tap of `FilledButton` 'Log in' -> (Perform validation) -> On success, navigate to `03_01_Home_Feed`.
  - On tap of `TextButton` 'Sign up' -> Navigate to `01_06_Email_Sign_Up`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### Flow: Create Music

---

### **Screen 8: Select Genre**
- **Screen Name/ID:** `02_01_Select_Genre`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Select a Genre". Typography: `md.sys.typography.titleLarge`.
2.  **Name:** `LazyVerticalGrid`
    - **Position & Size:** `fillMaxSize`. Padding: 16dp.
    - **Grid Cells:** `GridCells.Fixed(2)`. Spacing: `16dp` between items.
    - **Content:** A list of `Card` components.
3.  **Name:** `Card` (Genre Item - Example)
    - **Position & Size:** `aspectRatio(1f)`.
    - **Style:** `ElevatedCard`. Elevation: `Elevation.Level1`. Shape: `Shape.Corner.Large` (16dp).
    - **Layout:** `Box` with content aligned to the bottom start.
    - **Components:**
        1.  **Name:** `Image` (Genre Artwork)
            - **Position & Size:** `fillMaxSize`.
            - **Style:** `ContentScale.Crop`.
            - **Content:** Placeholder image for the genre (e.g., `img_genre_hiphop.jpg`).
        2.  **Name:** `Box` (Gradient Scrim)
            - **Position & Size:** `fillMaxSize`.
            - **Style:** Black gradient from transparent (top) to 60% opacity (bottom).
        3.  **Name:** `Text` (Genre Name)
            - **Position & Size:** Alignment: `BottomStart`. Padding: 16dp.
            - **Style:** Typography: `md.sys.typography.titleLarge`. Color: `#FFFFFF`.
            - **Content:** "Hip Hop"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of a genre `Card` -> Navigate to `02_02_Select_Vocal_Style`.
  - On tap of `ArrowBack` icon -> Navigate to `03_01_Home_Feed`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (Z-axis).
  - On tap of card: Material `ElevationScale` transition for the card.

---

### **Screen 9: Select Vocal Style**
- **Screen Name/ID:** `02_02_Select_Vocal_Style`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Select Vocal Style". Typography: `md.sys.typography.titleLarge`.
2.  **Name:** `Column`
    - **Position & Size:** `fillMaxSize`. Padding: horizontal 16dp.
    - **Components:**
        1.  **Name:** `FilledTonalButton` (Instrumental)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 16dp.
            - **Style:** Shape: `Shape.Corner.Full`.
            - **Content:** "Instrumental"
        2.  **Name:** `Text` (Section Header)
            - **Position & Size:** `wrapContent`. Margin: top 24dp.
            - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
            - **Content:** "AI Singers"
        3.  **Name:** `LazyVerticalGrid`
            - **Position & Size:** `fillMaxWidth`. Margin: top 16dp.
            - **Grid Cells:** `GridCells.Fixed(3)`. Spacing: `12dp`.
            - **Content:** List of AI Singer cards.
4.  **Name:** `Column` (AI Singer Card - Example)
    - **Position & Size:** `wrapContent`.
    - **Layout:** Vertical column, horizontally centered.
    - **Components:**
        1.  **Name:** `Image` (Singer Avatar)
            - **Position & Size:** 80dp x 80dp.
            - **Style:** `ContentScale.Crop`. Shape: `CircleShape`.
            - **Content:** Placeholder avatar for the singer (e.g., `avatar_nova.jpg`).
        2.  **Name:** `Text` (Singer Name)
            - **Position & Size:** `wrapContent`. Margin: top 8dp.
            - **Style:** Typography: `md.sys.typography.labelLarge`. Color: `md.sys.color.onSurface`.
            - **Content:** "Nova"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of an AI Singer card -> Navigate to `02_03_AI_Lyric_Generation_Prompt`.
  - On tap of 'Instrumental' button -> Navigate to `02_06_Studio`.
  - On tap of `ArrowBack` icon -> Navigate to `02_01_Select_Genre`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 10: AI Lyric Generation Prompt**
- **Screen Name/ID:** `02_03_AI_Lyric_Generation_Prompt`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Generate Lyrics". Typography: `md.sys.typography.titleLarge`.
2.  **Name:** `Column`
    - **Position & Size:** `fillMaxSize`. Padding: 16dp.
    - **Components:**
        1.  **Name:** `Text` (Instruction)
            - **Position & Size:** `wrapContent`.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`.
            - **Content:** "Describe what you want your song to be about."
        2.  **Name:** `OutlinedTextField` (Prompt Input)
            - **Position & Size:** `fillMaxWidth`, `minHeight(160dp)`. Margin: top 16dp.
            - **Style:** `singleLine = false`.
            - **Content:** Label: "e.g., a song about driving at night".
        3.  **Name:** `Spacer`
            - **Position & Size:** `weight(1f)`.
        4.  **Name:** `FilledButton` (Generate)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: bottom 16dp.
            - **Style:** Shape: `Shape.Corner.Full`.
            - **Content:** `Row` with text and icon.
                - **Text:** "Generate".
                - **Icon:** `Icons.Filled.AutoAwesome`. Margin: start 8dp.
            - **State:** Disabled if text field is empty.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `FilledButton` 'Generate' -> Navigate to `02_04_AI_Lyric_Generation_Loading`.
  - On tap of `ArrowBack` icon -> Navigate to `02_02_Select_Vocal_Style`.
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 11: AI Lyric Generation - Loading**
- **Screen Name/ID:** `02_04_AI_Lyric_Generation_Loading`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Box` with content centered.

#### Components:
1.  **Name:** `Column`
    - **Position & Size:** `wrapContent`. Alignment: `Center`.
    - **Layout:** Vertically arranged, horizontally centered.
    - **Components:**
        1.  **Name:** `CircularProgressIndicator`
            - **Position & Size:** 64dp x 64dp.
            - **Style:** `strokeWidth = 5dp`. Color: `md.sys.color.primary`.
        2.  **Name:** `Text` (Loading Message)
            - **Position & Size:** `wrapContent`. Margin: top 24dp.
            - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurfaceVariant`.
            - **Content:** "Writing your hit song..."

#### Interaction & Behavior:
- **Interactions:**
  - System event: When lyric generation is complete -> Navigate to `02_05_AI_Lyric_Generation_Results`.
- **Animations:**
  - The `CircularProgressIndicator` animates indefinitely.
  - Screen Transition (Enter): `MaterialFadeThrough`.

---

### **Screen 12: AI Lyric Generation - Results**
- **Screen Name/ID:** `02_05_AI_Lyric_Generation_Results`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Title:** `Text` with content "Your Lyrics". Typography: `md.sys.typography.titleLarge`.
2.  **Name:** `Column`
    - **Position & Size:** `fillMaxSize`.
    - **Components:**
        1.  **Name:** `LazyColumn` (Lyrics Display)
            - **Position & Size:** `fillMaxWidth`, `weight(1f)`. Padding: 16dp.
            - **Content:** A `Text` component containing the full, generated lyrics.
            - **Style:** Typography: `md.sys.typography.bodyLarge`. `lineHeight = 24.sp`.
        2.  **Name:** `Row` (Action Buttons)
            - **Position & Size:** `fillMaxWidth`. Padding: 16dp.
            - **Layout:** `Arrangement.spacedBy(16dp)`.
            - **Components:**
                1.  **Name:** `OutlinedButton` (Try again)
                    - **Position & Size:** `weight(1f)`. Height: 56dp.
                    - **Style:** Shape: `Shape.Corner.Full`.
                    - **Content:** "Try again"
                2.  **Name:** `FilledButton` (Make music)
                    - **Position & Size:** `weight(1f)`. Height: 56dp.
                    - **Style:** Shape: `Shape.Corner.Full`.
                    - **Content:** "Make music"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Make music' button -> Navigate to `02_06_Studio`.
  - On tap of 'Try again' button -> Navigate to `02_03_AI_Lyric_Generation_Prompt`.
- **Animations:**
  - Screen Transition (Enter): `MaterialFadeThrough`.
  - Screen Transition (Exit): `MaterialSharedAxis` (X-axis).

---

### **Screen 13: Studio**
- **Screen Name/ID:** `02_06_Studio`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surfaceVariant`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** Colors: `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`.
        - **Title:** `Text` with content "New Project". Typography: `md.sys.typography.titleLarge`.
        - **Actions:** `TextButton` with content "Save".
2.  **Name:** `LazyColumn` (Track Layers)
    - **Position & Size:** `fillMaxSize`. Padding: top from `TopAppBar`, bottom from `BottomAppBar`. Padding horizontal 16dp.
    - **Content:** A list of track layer components.
3.  **Name:** `Card` (Track Layer - Example)
    - **Position & Size:** `fillMaxWidth`. Height: 80dp. Margin: vertical 8dp.
    - **Style:** `OutlinedCard`.
    - **Layout:** `Row` with vertical alignment `CenterVertically`.
    - **Components:**
        1.  **Name:** `Icon` (Track Type)
            - **Position & Size:** 40x40dp. Margin: 16dp.
            - **Content:** e.g., `Icons.Filled.MusicNote` for Vocals, custom icon for Drums.
        2.  **Name:** `Text` (Track Name)
            - **Position & Size:** `weight(1f)`.
            - **Style:** Typography: `md.sys.typography.titleMedium`.
            - **Content:** "Drums"
        3.  **Name:** `IconButton` (Mute)
            - **Content:** `Icons.Filled.VolumeUp` / `Icons.Filled.VolumeOff`.
        4.  **Name:** `IconButton` (Solo)
            - **Content:** Custom 'S' icon.
4.  **Name:** `BottomAppBar` (Transport Controls)
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** `containerColor` is `md.sys.color.surface`.
    - **Content:** `Row` with `Arrangement.SpaceEvenly`.
        - **IconButton:** `Icons.Filled.SkipPrevious`.
        - **IconButton:** `Icons.Filled.PlayArrow` / `Icons.Filled.Pause`. Size: 48x48dp.
        - **IconButton:** `Icons.Filled.SkipNext`.
        - **TextButton:** "Vocals".

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Save' `TextButton` -> Show `02_10_Save_Project` as an `AlertDialog`.
  - On tap of a track layer `Card` -> Open `02_07_Track_Editor` as a `ModalBottomSheet`.
  - On tap of 'Vocals' `TextButton` -> Open `02_08_Vocal_Editor` as a `ModalBottomSheet`.
  - On tap of 'Close' `IconButton` -> Navigate to `03_01_Home_Feed`.
- **Animations:**
  - Screen Transition (Enter): `MaterialSharedAxis` (Z-axis).

---

### **Screen 14: Track Editor**
- **Screen Name/ID:** `02_07_Track_Editor`
- **Dimensions:** Modal Bottom Sheet overlaying `02_06_Studio`.
- **Background:** `md.sys.color.surfaceContainerLow`.
- **Layout:** `ModalBottomSheet` with a `Column` layout.

#### Components:
1.  **Name:** `DragHandle`
    - **Position & Size:** Centered at the top of the sheet.
2.  **Name:** `Row` (Header)
    - **Position & Size:** `fillMaxWidth`. Padding: 16dp.
    - **Components:**
        - **Text:** "Edit Drums". Typography: `md.sys.typography.titleLarge`. `weight(1f)`.
        - **IconButton:** `Icons.Filled.Close`.
3.  **Name:** `Column` (Controls)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 16dp, bottom 32dp.
    - **Components:**
        1.  **Name:** `Text` (Volume Label)
            - **Content:** "Volume". Typography: `md.sys.typography.labelMedium`.
        2.  **Name:** `Slider`
            - **Position & Size:** `fillMaxWidth`.
            - **Content:** Value from 0.0 to 1.0.
        3.  **Name:** `Text` (Effect Label)
            - **Content:** "Effects". Margin: top 24dp.
        4.  **Name:** `FilterChip` (Example)
            - **Content:** "Reverb". `selected` state.
        5.  **Name:** `FilterChip` (Example)
            - **Content:** "Compressor".

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Close' `IconButton` -> Dismiss the `ModalBottomSheet`, returning to `02_06_Studio`.
  - On swipe down -> Dismiss the `ModalBottomSheet`.
- **Animations:**
  - Standard `ModalBottomSheet` slide-in/slide-out animation.

---

### **Screen 15: Vocal Editor**
- **Screen Name/ID:** `02_08_Vocal_Editor`
- **Dimensions:** Modal Bottom Sheet overlaying `02_06_Studio`.
- **Background:** `md.sys.color.surfaceContainerLow`.
- **Layout:** `ModalBottomSheet` with a `Column` layout.

#### Components:
1.  **Name:** `DragHandle`
2.  **Name:** `Row` (Header)
    - **Position & Size:** `fillMaxWidth`. Padding: 16dp.
    - **Components:**
        - **Text:** "Edit Vocals". Typography: `md.sys.typography.titleLarge`. `weight(1f)`.
        - **IconButton:** `Icons.Filled.Close`.
3.  **Name:** `Column` (Controls)
    - **Position & Size:** `fillMaxWidth`. Padding: horizontal 16dp, bottom 32dp.
    - **Components:**
        1.  **Name:** `Text` (Lyrics Label)
            - **Content:** "Lyrics".
        2.  **Name:** `OutlinedTextField` (Lyrics Editor)
            - **Position & Size:** `fillMaxWidth`, `height(200dp)`.
            - **Content:** Contains the generated lyrics, editable.
        3.  **Name:** `TextButton`
            - **Content:** "Re-generate Lyrics". Margin: top 8dp.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Close' `IconButton` -> Dismiss the `ModalBottomSheet`, returning to `02_06_Studio`.
- **Animations:**
  - Standard `ModalBottomSheet` slide-in/slide-out animation.

---

### **Screen 16: Save Project**
- **Screen Name/ID:** `02_10_Save_Project`
- **Dimensions:** `AlertDialog` overlaying `02_06_Studio`.
- **Background:** `md.sys.color.surfaceContainerHigh`.
- **Layout:** `AlertDialog` component.

#### Components:
1.  **Name:** `Icon` (Dialog Icon)
    - **Position & Size:** Displayed above the title.
    - **Content:** `Icons.Outlined.Save`.
2.  **Name:** `Text` (Dialog Title)
    - **Content:** "Save Project".
3.  **Name:** `Text` (Dialog Body)
    - **Content:** `Column` containing a text field.
        - **OutlinedTextField:** `fillMaxWidth`. Label: "Project Name".
4.  **Name:** `Row` (Dialog Actions)
    - **Position & Size:** `fillMaxWidth`. `Arrangement.End`.
    - **Components:**
        1.  **Name:** `TextButton`
            - **Content:** "Cancel".
        2.  **Name:** `TextButton`
            - **Content:** "Save".
            - **State:** Disabled if text field is empty.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Save' `TextButton` -> (Save project) -> Dismiss dialog -> Navigate to `02_11_Project_Saved_Confirmation`.
  - On tap of 'Cancel' `TextButton` -> Dismiss dialog, returning to `02_06_Studio`.
- **Animations:**
  - Standard `AlertDialog` fade-in/scale-in animation.

---

### **Screen 17: Project Saved Confirmation**
- **Screen Name/ID:** `02_11_Project_Saved_Confirmation`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Box` with content centered.

#### Components:
1.  **Name:** `Column`
    - **Position & Size:** `wrapContent`. Alignment: `Center`. Padding: 32dp.
    - **Layout:** Vertically arranged, horizontally centered.
    - **Components:**
        1.  **Name:** `Icon`
            - **Position & Size:** 80dp x 80dp.
            - **Style:** Tint: `md.sys.color.primary`.
            - **Content:** `Icons.Filled.CheckCircle`.
        2.  **Name:** `Text` (Headline)
            - **Position & Size:** `wrapContent`. Margin: top 24dp.
            - **Style:** Typography: `md.sys.typography.headlineSmall`.
            - **Content:** "Project Saved!"
        3.  **Name:** `FilledButton` (Share)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 32dp.
            - **Style:** Shape: `Shape.Corner.Full`.
            - **Content:** "Share"
        4.  **Name:** `TextButton` (Done)
            - **Position & Size:** `fillMaxWidth`. Height: 56dp. Margin: top 8dp.
            - **Content:** "Done"

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Done' button -> Navigate to `03_01_Home_Feed`.
  - On tap of 'Share' button -> (Open Android Share Sheet) -> After share, navigate to `03_01_Home_Feed`.
- **Animations:**
  - Screen Transition (Enter): `MaterialFadeThrough`.

---

### Flow: Main Navigation

---

### **Screen 18: Home Feed**
- **Screen Name/ID:** `03_01_Home_Feed`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `NavigationBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Title:** `Image` of the Splash wordmark logo.
        - **Actions:** `IconButton` with `Icons.Outlined.Notifications`.
2.  **Name:** `LazyColumn` (Feed)
    - **Position & Size:** `fillMaxSize`. Padding: top from `TopAppBar`, bottom from `NavigationBar`.
    - **Content:** A list of `Card` components, each representing a song.
3.  **Name:** `Card` (Song Item - Example)
    - **Position & Size:** `fillMaxWidth`. Margin: vertical 8dp, horizontal 16dp.
    - **Style:** `ElevatedCard`.
    - **Layout:** `Column`.
    - **Components:**
        - **Image:** `fillMaxWidth`, `height(180dp)`. Album art.
        - **Row:** `fillMaxWidth`, padding 16dp. Contains song title, artist name, and a play button.
4.  **Name:** `NavigationBar` (Bottom Nav)
    - **Position & Size:** `fillMaxWidth`.
    - **Content:** Three `NavigationBarItem`s.
        1.  **Item 1 (Home):** `selected = true`. Icon: `Icons.Filled.Home`. Label: "Home".
        2.  **Item 2 (Create):** `selected = false`. Icon: `Icons.Filled.AddCircle`. Label: "Create".
        3.  **Item 3 (Profile):** `selected = false`. Icon: `Icons.Outlined.Person`. Label: "Profile".

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Create' `NavigationBarItem` -> Navigate to `02_01_Select_Genre`.
  - On tap of 'Profile' `NavigationBarItem` -> Navigate to `03_02_Profile`.
- **Animations:**
  - Screen transitions between bottom nav items: `MaterialFadeThrough`.

---

### **Screen 19: Profile**
- **Screen Name/ID:** `03_02_Profile`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `NavigationBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Title:** `Text` with content "Profile".
        - **Actions:** `IconButton` with `Icons.Outlined.Settings`.
2.  **Name:** `LazyColumn`
    - **Position & Size:** `fillMaxSize`.
    - **Content:**
        1.  **Item (Profile Header):** `Column` with padding 16dp, `centerHorizontal`.
            - `Image` (Avatar): 96x96dp, `CircleShape`.
            - `Text` (Username): Margin top 16dp. Typography: `md.sys.typography.titleLarge`.
        2.  **Item (Section Header):** `Text` with content "My Projects". Padding: horizontal 16dp, top 24dp. Typography: `md.sys.typography.titleMedium`.
        3.  **Items (Project List):** A list of `ListItem` components.
            - **ListItem:** Headline: "Project Name". Supporting text: "Last edited: 2 days ago". Trailing content: `IconButton` with `Icons.Filled.MoreVert`.
4.  **Name:** `NavigationBar` (Bottom Nav)
    - **Position & Size:** `fillMaxWidth`.
    - **Content:**
        1.  **Item 1 (Home):** `selected = false`. Icon: `Icons.Outlined.Home`. Label: "Home".
        2.  **Item 2 (Create):** `selected = false`. Icon: `Icons.Filled.AddCircle`. Label: "Create".
        3.  **Item 3 (Profile):** `selected = true`. Icon: `Icons.Filled.Person`. Label: "Profile".

#### Interaction & Behavior:
- **Interactions:**
  - On tap of 'Home' `NavigationBarItem` -> Navigate to `03_01_Home_Feed`.
  - On tap of 'Create' `NavigationBarItem` -> Navigate to `02_01_Select_Genre`.
  - On tap of a project `ListItem` -> Navigate to `02_06_Studio`.
  - On tap of Settings `IconButton` -> Navigate to `04_01_Settings`.
- **Animations:**
  - Screen transitions between bottom nav items: `MaterialFadeThrough`.

---

### Flow: Settings

---

### **Screen 20: Settings**
- **Screen Name/ID:** `04_01_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components:
1.  **Name:** `TopAppBar`
    - **Position & Size:** `fillMaxWidth`, height 56dp.
    - **Style:** `containerColor` is `md.sys.color.surface`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Settings".
2.  **Name:** `LazyColumn`
    - **Position & Size:** `fillMaxSize`.
    - **Content:**
        1.  **Name:** `ListItem` (Account)
            - **Headline:** `Text` "Account".
            - **Leading Content:** `Icon` `Icons.Outlined.AccountCircle`.
        2.  **Name:** `ListItem` (Notifications)
            - **Headline:** `Text` "Notifications".
            - **Leading Content:** `Icon` `Icons.Outlined.Notifications`.
        3.  **Name:** `ListItem` (Privacy Policy)
            - **Headline:** `Text` "Privacy Policy".
            - **Leading Content:** `Icon` `Icons.Outlined.Shield`.
        4.  **Name:** `Divider`
            - **Position & Size:** Margin: vertical 16dp, horizontal 16dp.
        5.  **Name:** `ListItem` (Log Out)
            - **Headline:** `Text` "Log Out". Color: `md.sys.color.error`.
            - **Leading Content:** `Icon` `Icons.Outlined.Logout`. Tint: `md.sys.color.error`.

#### Interaction & Behavior:
- **Interactions:**
  - On tap of `ArrowBack` icon -> Navigate to `03_02_Profile`.
  - On tap of 'Log Out' `ListItem` -> (Show confirmation dialog) -> On confirm, navigate to `01_05_Sign_Up_Options`.
  - On tap of 'Account', 'Notifications', 'Privacy Policy' -> No navigation defined in flow, remains on `04_01_Settings`. (In a real app, these would navigate to sub-screens).
- **Animations:**
  - Screen Transition (Enter/Exit): `MaterialSharedAxis` (X-axis).

---

## V. Critical Scenarios & States

### Error States
- **No Internet Connection:**
  - **UI:** A `Snackbar` appears at the bottom of the screen.
  - **Style:** Container color: `md.sys.color.inverseSurface`. Text color: `md.sys.color.inverseOnSurface`.
  - **Message:** "No internet connection. Please check your network and try again."
  - **Action:** Optional "Retry" `TextButton` on the Snackbar.
- **Form Validation Error:**
  - **UI:** The `OutlinedTextField` that fails validation will show an error state.
  - **Style:** The outline and label color change to `md.sys.color.error`.
  - **Message:** Helper text appears below the field in `md.sys.color.error` color. Example: "Please enter a valid email address."

### Empty States
- **Profile - No Projects:**
  - **Location:** In the `LazyColumn` of the `03_02_Profile` screen, in place of the project list.
  - **Layout:** `Column` with `padding(32dp)`, `centerHorizontal` alignment.
  - **Components:**
    1.  **Icon:** `Icons.Outlined.MusicNote`, size 64dp, tint `md.sys.color.surfaceVariant`.
    2.  **Text (Headline):** "No Projects Yet". Typography: `md.sys.typography.titleLarge`. Margin top 24dp.
    3.  **Text (Body):** "Tap the create button to make your first song.". Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`. Margin top 8dp.
    4.  **FilledButton:** "Create Song". Margin top 24dp. On tap -> Navigates to `02_01_Select_Genre`.

### Loading States
- **General Data Fetching (e.g., Home Feed):**
  - **UI:** A `CircularProgressIndicator` is displayed, centered within the content area (e.g., the `LazyColumn` area on the Home Feed).
  - **Style:** Color: `md.sys.color.primary`.
- **Specific Loading Screen:**
  - See `02_04_AI_Lyric_Generation_Loading` for a full-screen loading state implementation.
```

---


============================================================
## APP 3: App_3
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# BandLab – Android App Design Specification

## I. Global Specifications

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Dynamic Color**: Enabled (Material You). The specified colors serve as the baseline when dynamic color is unavailable.
    *   **Modes**: Light and Dark themes are supported. All color roles are defined for both.
*   **Colors**:
    *   **Seed Color**: `#E54424` (BandLab Red/Orange)
    *   **Key Color Roles (Light Theme)**:
        *   `md.sys.color.primary`: `#A13F1B`
        *   `md.sys.color.onPrimary`: `#FFFFFF`
        *   `md.sys.color.primaryContainer`: `#FFDBCF`
        *   `md.sys.color.onPrimaryContainer`: `#3A0B00`
        *   `md.sys.color.secondary`: `#77574D`
        *   `md.sys.color.onSecondary`: `#FFFFFF`
        *   `md.sys.color.secondaryContainer`: `#FFDBCF`
        *   `md.sys.color.onSecondaryContainer`: `#2C160F`
        *   `md.sys.color.tertiary`: `#695F2E`
        *   `md.sys.color.onTertiary`: `#FFFFFF`
        *   `md.sys.color.tertiaryContainer`: `#F2E3A6`
        *   `md.sys.color.onTertiaryContainer`: `#211C00`
        *   `md.sys.color.error`: `#BA1A1A`
        *   `md.sys.color.onError`: `#FFFFFF`
        *   `md.sys.color.background`: `#FFFBFF`
        *   `md.sys.color.onBackground`: `#201A18`
        *   `md.sys.color.surface`: `#FFFBFF`
        *   `md.sys.color.onSurface`: `#201A18`
        *   `md.sys.color.surfaceVariant`: `#F5DED8`
        *   `md.sys.color.onSurfaceVariant`: `#53433F`
        *   `md.sys.color.outline`: `#85736E`
    *   **Key Color Roles (Dark Theme)**:
        *   `md.sys.color.primary`: `#FFB59B`
        *   `md.sys.color.onPrimary`: `#5F1500`
        *   `md.sys.color.primaryContainer`: `#802804`
        *   `md.sys.color.onPrimaryContainer`: `#FFDBCF`
        *   `md.sys.color.secondary`: `#E7BDB2`
        *   `md.sys.color.onSecondary`: `#442A22`
        *   `md.sys.color.secondaryContainer`: `#5D4037`
        *   `md.sys.color.onSecondaryContainer`: `#FFDBCF`
        *   `md.sys.color.tertiary`: `#D5C78D`
        *   `md.sys.color.onTertiary`: `#393004`
        *   `md.sys.color.tertiaryContainer`: `#504719`
        *   `md.sys.color.onTertiaryContainer`: `#F2E3A6`
        *   `md.sys.color.error`: `#FFB4AB`
        *   `md.sys.color.onError`: `#690005`
        *   `md.sys.color.background`: `#201A18`
        *   `md.sys.color.onBackground`: `#EDE0DC`
        *   `md.sys.color.surface`: `#201A18`
        *   `md.sys.color.onSurface`: `#EDE0DC`
        *   `md.sys.color.surfaceVariant`: `#53433F`
        *   `md.sys.color.onSurfaceVariant`: `#D8C2BC`
        *   `md.sys.color.outline`: `#A08D87`
*   **Typography**:
    *   **Font Family**: Roboto
    *   **Type Scale**: Standard Material 3 type scale roles will be used (e.g., `displayLarge`, `headlineMedium`, `titleLarge`, `bodyMedium`, `labelLarge`).
*   **Spacing**:
    *   **Base Grid Unit**: 8dp. All spacing and component sizes should be multiples of 8dp where possible.
    *   **Standard Padding**: 16dp for screen edges.
*   **Accessibility**:
    *   **Target Standard**: WCAG 2.1 Level AA.
    *   **Minimum Touch Target**: 48x48dp for all interactive elements.
    *   **Content Descriptions**: All icons and images must have descriptive content descriptions for screen readers.

---

## Flow: Onboarding and Sign Up

### Screen 01: Welcome
*   **Screen Name/ID**: `01_Welcome_Screen`
*   **Dimensions**: 393x852dp (Typical mobile viewport)
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered, horizontally aligned to center.
    *   `verticalArrangement`: `Arrangement.Center`
    *   `horizontalAlignment`: `Alignment.CenterHorizontally`
    *   `padding`: `16dp` on all sides.

#### Components:
1.  **Component**: `Image` (App Logo)
    *   **Name**: App Logo
    *   **Position & Size**:
        *   Size: `120dp` x `120dp`
        *   Alignment: Centered horizontally.
        *   Margin Bottom: `32dp`
    *   **Content**: BandLab vector logo.
2.  **Component**: `Text` (Headline)
    *   **Name**: Headline Text
    *   **Position & Size**:
        *   Width: `fillMaxWidth`
        *   Margin Bottom: `16dp`
    *   **Style**:
        *   Typography: `md.sys.typography.headlineLarge`
        *   Color: `md.sys.color.onSurface`
        *   Text Alignment: `Center`
    *   **Content**: "Make Music Everywhere"
3.  **Component**: `Text` (Body)
    *   **Name**: Body Text
    *   **Position & Size**:
        *   Width: `fillMaxWidth`
        *   Margin Bottom: `48dp`
    *   **Style**:
        *   Typography: `md.sys.typography.bodyLarge`
        *   Color: `md.sys.color.onSurfaceVariant`
        *   Text Alignment: `Center`
    *   **Content**: "Join millions of creators on the ultimate social music creation platform."
4.  **Component**: `FilledButton`
    *   **Name**: Sign Up Button
    *   **Position & Size**:
        *   Width: `fillMaxWidth`
        *   Height: `56dp`
        *   Margin Bottom: `16dp`
    *   **Style**:
        *   Color: `md.sys.color.primary`
        *   Text Color: `md.sys.color.onPrimary`
        *   Typography: `md.sys.typography.labelLarge`
        *   Shape: `ShapeDefaults.Full` (Pill shape)
    *   **Content**: "Sign Up"
5.  **Component**: `TextButton`
    *   **Name**: Log In Link
    *   **Position & Size**:
        *   Width: `wrapContent`
        *   Height: `48dp` (min touch target)
    *   **Style**:
        *   Text Color: `md.sys.color.primary`
        *   Typography: `md.sys.typography.labelLarge`
    *   **Content**: "Log In"

#### Interaction & Behavior:
*   **Sign Up Button**:
    *   **State**: `Pressed` state shows a `md.sys.color.onPrimary` overlay with `0.12` opacity.
    *   **Interaction**: On tap -> Navigate to `02_Sign_Up_Options`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) transition.
*   **Log In Link**:
    *   **State**: `Pressed` state shows a `md.sys.color.primary` overlay with `0.12` opacity.
    *   **Interaction**: On tap -> Navigate to `09_Log_In_Options`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) transition.

---

### Screen 02: Sign Up Options
*   **Screen Name/ID**: `02_Sign_Up_Options`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout.
    *   `padding`: `16dp` horizontal.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Position & Size**: Top of the screen, `fillMaxWidth`, height `64dp`.
    *   **Style**:
        *   Container Color: `md.sys.color.surface`
        *   Elevation: `0dp`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
        *   **Title**: `Text` element with content "Sign Up". Typography: `md.sys.typography.titleLarge`.
2.  **Component**: `OutlinedButton` (Social Sign Up)
    *   **Name**: Continue with Google Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`, margin top `32dp`.
    *   **Style**:
        *   Stroke Color: `md.sys.color.outline`
        *   Typography: `md.sys.typography.labelLarge`
        *   Text Color: `md.sys.color.onSurface`
    *   **Content**:
        *   **Icon**: Google 'G' logo, size `24dp`, placed at the start.
        *   **Text**: "Continue with Google"
3.  **Component**: `OutlinedButton` (Social Sign Up)
    *   **Name**: Continue with Facebook Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`, margin top `16dp`.
    *   **Style**:
        *   Stroke Color: `md.sys.color.outline`
        *   Typography: `md.sys.typography.labelLarge`
        *   Text Color: `md.sys.color.onSurface`
    *   **Content**:
        *   **Icon**: Facebook 'f' logo, size `24dp`, placed at the start.
        *   **Text**: "Continue with Facebook"
4.  **Component**: `Row` with `Divider`
    *   **Name**: Or Separator
    *   **Position & Size**: `fillMaxWidth`, margin `32dp` vertical.
    *   **Layout**: `Row` with `verticalAlignment = Alignment.CenterVertically`. Contains two `Divider`s and one `Text`.
    *   **Content**:
        *   `Divider` (weight 1f)
        *   `Text` "OR", padding `16dp` horizontal. Style: `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.
        *   `Divider` (weight 1f)
5.  **Component**: `FilledButton`
    *   **Name**: Sign up with Email Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`.
    *   **Style**:
        *   Color: `md.sys.color.primary`
        *   Text Color: `md.sys.color.onPrimary`
        *   Typography: `md.sys.typography.labelLarge`
    *   **Content**: "Sign up with Email"
6.  **Component**: `Row` (Log In Prompt)
    *   **Name**: Log In Prompt
    *   **Position & Size**: Bottom of the screen, `fillMaxWidth`, padding bottom `32dp`.
    *   **Layout**: `Row` with `horizontalArrangement = Arrangement.Center`.
    *   **Content**:
        *   `Text`: "Already have an account? ". Style: `md.sys.typography.bodyMedium`, color `md.sys.color.onSurface`.
        *   `TextButton`: "Log In". Style: `md.sys.typography.bodyMedium` (bold), color `md.sys.color.primary`.

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `01_Welcome_Screen`. Animation: `MaterialSharedAxis` (Z-axis).
*   **Continue with Google**: On tap -> Navigate to `04_Google_Authentication`.
*   **Continue with Facebook**: On tap -> Navigate to `05_Facebook_Authentication`.
*   **Sign up with Email**: On tap -> Navigate to `03_Sign_Up_With_Email`. Animation: `MaterialSharedAxis` (X-axis).
*   **Log In TextButton**: On tap -> Navigate to `09_Log_In_Options`. Animation: `MaterialSharedAxis` (Z-axis).

---

### Screen 03: Sign Up With Email
*   **Screen Name/ID**: `03_Sign_Up_With_Email`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `verticalScroll`. Padding `16dp` horizontal.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Position & Size**: Top, `fillMaxWidth`, height `64dp`.
    *   **Style**: Container Color: `md.sys.color.surface`, Elevation: `0dp`.
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
        *   **Title**: `Text` "Sign Up". Typography: `md.sys.typography.titleLarge`.
2.  **Component**: `OutlinedTextField`
    *   **Name**: Name Field
    *   **Position & Size**: `fillMaxWidth`, margin top `32dp`.
    *   **Style**: Standard `OutlinedTextField` style.
    *   **Content**:
        *   `label`: "Name"
        *   `placeholder`: "Enter your full name"
        *   `leadingIcon`: `Icons.Outlined.Person`
        *   `keyboardOptions`: `KeyboardType.Text`, `ImeAction.Next`.
3.  **Component**: `OutlinedTextField`
    *   **Name**: Email Field
    *   **Position & Size**: `fillMaxWidth`, margin top `16dp`.
    *   **Style**: Standard `OutlinedTextField` style.
    *   **Content**:
        *   `label`: "Email"
        *   `placeholder`: "Enter your email address"
        *   `leadingIcon`: `Icons.Outlined.Email`
        *   `keyboardOptions`: `KeyboardType.Email`, `ImeAction.Next`.
4.  **Component**: `OutlinedTextField`
    *   **Name**: Password Field
    *   **Position & Size**: `fillMaxWidth`, margin top `16dp`.
    *   **Style**: Standard `OutlinedTextField` style.
    *   **Content**:
        *   `label`: "Password"
        *   `placeholder`: "Create a password"
        *   `leadingIcon`: `Icons.Outlined.Lock`
        *   `visualTransformation`: `PasswordVisualTransformation`
        *   `trailingIcon`: `IconButton` to toggle password visibility (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`).
        *   `keyboardOptions`: `KeyboardType.Password`, `ImeAction.Done`.
        *   `supportingText`: "Must be at least 8 characters."
5.  **Component**: `FilledButton`
    *   **Name**: Sign Up Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`, margin top `32dp`.
    *   **Style**: Default state is `disabled`. Enabled when all fields are valid.
        *   `Enabled`: Color `md.sys.color.primary`.
        *   `Disabled`: Color `md.sys.color.onSurface` with `0.12` opacity. Text color `md.sys.color.onSurface` with `0.38` opacity.
    *   **Content**: "Sign Up"

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `02_Sign_Up_Options`.
*   **Sign Up Button**:
    *   **Interaction**: On tap (when enabled) -> Validate fields. If successful, show `CircularProgressIndicator` and navigate to `06_Create_Your_Profile`.
    *   **Animation**: `MaterialSharedAxis` (X-axis).

#### Critical Scenarios & States:
*   **Error State**: If email is invalid or password is too short, the `OutlinedTextField` border and label turn to `md.sys.color.error`. A supporting text message appears below the field, e.g., "Enter a valid email" or "Password is too short".
*   **Loading State**: On tapping "Sign Up", the button text is replaced by a `CircularProgressIndicator` (size `24dp`) until the network call completes.

---

### Screen 04: Google Authentication
*   **Screen Name/ID**: `04_Google_Authentication`
*   **Dimensions**: N/A (System UI)
*   **Background**: This screen is a system-level dialog or Chrome Custom Tab provided by the Google Sign-In SDK.
*   **Layout**: Conforms to Google's standard authentication flow.

#### Interaction & Behavior:
*   **Successful Authentication**: User completes the Google sign-in flow -> System navigates to `06_Create_Your_Profile`.
*   **Failed/Cancelled Authentication**: User cancels the flow -> System returns to `02_Sign_Up_Options` or `09_Log_In_Options`.

---

### Screen 05: Facebook Authentication
*   **Screen Name/ID**: `05_Facebook_Authentication`
*   **Dimensions**: N/A (System UI)
*   **Background**: This screen is a system-level dialog or WebView provided by the Facebook Login SDK.
*   **Layout**: Conforms to Facebook's standard authentication flow.

#### Interaction & Behavior:
*   **Successful Authentication**: User completes the Facebook sign-in flow -> System navigates to `06_Create_Your_Profile`.
*   **Failed/Cancelled Authentication**: User cancels the flow -> System returns to `02_Sign_Up_Options` or `09_Log_In_Options`.

---

### Screen 06: Create Your Profile
*   **Screen Name/ID**: `06_Create_Your_Profile`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `verticalScroll`. Padding `16dp` horizontal.

#### Components:
1.  **Component**: `Text` (Title)
    *   **Name**: Screen Title
    *   **Position & Size**: Top of the screen, `fillMaxWidth`, margin top `32dp`.
    *   **Style**: Typography `md.sys.typography.headlineMedium`, Text Alignment `Center`.
    *   **Content**: "Create Your Profile"
2.  **Component**: `Box` (Avatar)
    *   **Name**: Avatar Upload
    *   **Position & Size**: `120dp` x `120dp`, centered horizontally, margin top `32dp`.
    *   **Layout**: A `Box` containing a `CircleShape` `Image` and an `IconButton` overlay.
    *   **Content**:
        *   `Image`: Placeholder avatar icon (`Icons.Filled.Person`), size `120dp`, background `md.sys.color.surfaceVariant`.
        *   `IconButton`: `FilledIconButton` with `Icons.Filled.AddAPhoto` icon, placed on the bottom-right edge of the avatar.
3.  **Component**: `OutlinedTextField`
    *   **Name**: Username Field
    *   **Position & Size**: `fillMaxWidth`, margin top `32dp`.
    *   **Style**: Standard `OutlinedTextField` style.
    *   **Content**:
        *   `label`: "Username"
        *   `placeholder`: "Choose a unique username"
        *   `leadingIcon`: `Icons.Outlined.AlternateEmail`
        *   `supportingText`: "This is how others will find you."
4.  **Component**: `FilledButton`
    *   **Name**: Continue Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`, margin top `32dp`.
    *   **Style**: Disabled until username is valid and unique.
    *   **Content**: "Continue"

#### Interaction & Behavior:
*   **Avatar Upload**: On tap -> Opens the system image picker to select a profile picture.
*   **Username Field**: As user types, perform an async check for username availability.
*   **Continue Button**: On tap (when enabled) -> Navigate to `07_Pick_Your_Genres`. Animation: `MaterialSharedAxis` (X-axis).

#### Critical Scenarios & States:
*   **Error State**: If username is taken, the `OutlinedTextField` shows an error state with supporting text: "Username already taken. Try another one."

---

### Screen 07: Pick Your Genres
*   **Screen Name/ID**: `07_Pick_Your_Genres`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `TopAppBar` and a `Column` for content.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Position & Size**: Top, `fillMaxWidth`, height `64dp`.
    *   **Style**: Centered title. Container Color: `md.sys.color.surface`.
    *   **Content**:
        *   **Title**: `Text` "What do you listen to?". Typography: `md.sys.typography.titleLarge`.
        *   **Subtitle**: `Text` "Select at least 3 genres.". Typography: `md.sys.typography.bodyMedium`, Color: `md.sys.color.onSurfaceVariant`.
2.  **Component**: `LazyVerticalGrid`
    *   **Name**: Genre Grid
    *   **Position & Size**: Fills the available space below the header. Padding `16dp`.
    *   **Layout**: `GridCells.Adaptive(minSize = 120.dp)`. Spacing `8dp`.
    *   **Content**: A grid of `FilterChip` components.
3.  **Component**: `FilterChip` (Repeated for each genre)
    *   **Name**: Genre Chip
    *   **Position & Size**: As determined by the grid.
    *   **Style**:
        *   `selected`: `true`/`false`
        *   `colors`: `FilterChipDefaults.filterChipColors()`
        *   `leadingIcon`: Displayed when `selected` is `true`, using `Icons.Filled.Check`.
    *   **Content**: Genre name (e.g., "Rock", "Hip Hop", "Pop", "Electronic").
4.  **Component**: `FilledButton`
    *   **Name**: Continue Button
    *   **Position & Size**: Anchored to the bottom of the screen. `fillMaxWidth`, height `56dp`. Padding `16dp`.
    *   **Style**: Disabled until at least 3 genres are selected.
    *   **Content**: "Continue"

#### Interaction & Behavior:
*   **Genre Chip**: On tap -> Toggles the `selected` state of the chip.
*   **Continue Button**:
    *   **State**: Becomes enabled when `selectedChips.count() >= 3`.
    *   **Interaction**: On tap (when enabled) -> Navigate to `08_Follow_Creators`. Animation: `MaterialSharedAxis` (X-axis).

---

### Screen 08: Follow Creators
*   **Screen Name/ID**: `08_Follow_Creators`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Position & Size**: Top, `fillMaxWidth`, height `64dp`.
    *   **Style**: Container Color: `md.sys.color.surface`.
    *   **Content**:
        *   **Title**: `Text` "Follow Creators". Typography: `md.sys.typography.titleLarge`.
        *   **Actions**: `TextButton` with content "Skip".
2.  **Component**: `LazyColumn`
    *   **Name**: Creators List
    *   **Position & Size**: Fills the available space.
    *   **Content**: A list of `ListItem` components, one for each suggested creator.
3.  **Component**: `ListItem` (Repeated)
    *   **Name**: Creator Item
    *   **Position & Size**: `fillMaxWidth`.
    *   **Style**: `ListItemDefaults.colors(containerColor = md.sys.color.surface)`.
    *   **Content**:
        *   `leadingContent`: `Image` (Avatar), `40dp` x `40dp`, `CircleShape`.
        *   `headlineContent`: `Text` (Creator's Username). Typography: `md.sys.typography.titleMedium`.
        *   `supportingContent`: `Text` (Creator's Name or follower count). Typography: `md.sys.typography.bodyMedium`.
        *   `trailingContent`: `OutlinedButton` with text "Follow". When tapped, changes to a `FilledButton` with text "Following".
4.  **Component**: `FilledButton`
    *   **Name**: Done Button
    *   **Position & Size**: Anchored to the bottom. `fillMaxWidth`, height `56dp`. Padding `16dp`.
    *   **Content**: "Done"

#### Interaction & Behavior:
*   **Follow/Following Button**: On tap -> Toggles follow state for the user.
*   **Skip Button**: On tap -> Navigate to `11_Home_Feed`.
*   **Done Button**: On tap -> Navigate to `11_Home_Feed`.
*   **Animation**: `MaterialFadeThrough` transition for all navigation actions.

---

## Flow: Log In

### Screen 09: Log In Options
*   **Screen Name/ID**: `09_Log_In_Options`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout. Padding `16dp` horizontal.
*   **Note**: This screen is structurally identical to `02_Sign_Up_Options`, with minor text changes.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Content**: Title `Text` is "Log In".
2.  **Component**: `OutlinedButton` (Social Log In)
    *   **Name**: Continue with Google Button
    *   **Content**: Text "Continue with Google".
3.  **Component**: `OutlinedButton` (Social Log In)
    *   **Name**: Continue with Facebook Button
    *   **Content**: Text "Continue with Facebook".
4.  **Component**: `Row` with `Divider`
    *   **Name**: Or Separator
5.  **Component**: `FilledButton`
    *   **Name**: Log in with Email Button
    *   **Content**: "Log in with Email"
6.  **Component**: `Row` (Sign Up Prompt)
    *   **Name**: Sign Up Prompt
    *   **Content**: `Text`: "Don't have an account? ", `TextButton`: "Sign Up".

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `01_Welcome_Screen`.
*   **Continue with Google**: On tap -> Navigate to `04_Google_Authentication`.
*   **Continue with Facebook**: On tap -> Navigate to `05_Facebook_Authentication`.
*   **Log in with Email**: On tap -> Navigate to `10_Log_In_With_Email`. Animation: `MaterialSharedAxis` (X-axis).
*   **Sign Up TextButton**: On tap -> Navigate to `02_Sign_Up_Options`. Animation: `MaterialSharedAxis` (Z-axis).

---

### Screen 10: Log In With Email
*   **Screen Name/ID**: `10_Log_In_With_Email`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `verticalScroll`. Padding `16dp` horizontal.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Screen Header
    *   **Content**: Title `Text` is "Log In". Navigation Icon is `Icons.Filled.ArrowBack`.
2.  **Component**: `OutlinedTextField`
    *   **Name**: Email/Username Field
    *   **Position & Size**: `fillMaxWidth`, margin top `32dp`.
    *   **Content**: `label`: "Email or Username".
3.  **Component**: `OutlinedTextField`
    *   **Name**: Password Field
    *   **Position & Size**: `fillMaxWidth`, margin top `16dp`.
    *   **Content**: `label`: "Password".
4.  **Component**: `FilledButton`
    *   **Name**: Log In Button
    *   **Position & Size**: `fillMaxWidth`, height `56dp`, margin top `32dp`.
    *   **Content**: "Log In"

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `09_Log_In_Options`.
*   **Log In Button**: On tap -> Authenticate user. On success, navigate to `11_Home_Feed`. Animation: `MaterialFadeThrough`.

#### Critical Scenarios & States:
*   **Error State**: On failed login, a `Snackbar` appears at the bottom of the screen with the message "Invalid username or password."
*   **Loading State**: On tapping "Log In", the button shows a `CircularProgressIndicator`.

---

## Flow: Core Navigation

### Screen 11: Home Feed
*   **Screen Name/ID**: `11_Home_Feed`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold`

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Home Top Bar
    *   **Position & Size**: Top, `fillMaxWidth`, height `64dp`.
    *   **Style**: `scrollBehavior`: `TopAppBarDefaults.enterAlwaysScrollBehavior()`.
    *   **Content**:
        *   `navigationIcon`: `IconButton` with user's profile avatar (`Image`).
        *   `title`: `Image` of the BandLab wordmark logo.
        *   `actions`:
            *   `IconButton` with `Icons.Outlined.Notifications`. A badge appears if there are unread notifications.
2.  **Component**: `LazyColumn`
    *   **Name**: Feed Content
    *   **Position & Size**: Fills the main content area of the `Scaffold`.
    *   **Content**: A list of `Card` components, each representing a post.
3.  **Component**: `Card` (Post - Repeated)
    *   **Name**: Post Card
    *   **Position & Size**: `fillMaxWidth`, margin vertical `8dp`.
    *   **Style**: `CardDefaults.elevatedCardColors()`.
    *   **Layout**: `Column`
        *   **Header**: `Row` with user avatar, username, and timestamp.
        *   **Content**: `Text` for post description, followed by an `AsyncImage` or player for the music track.
        *   **Actions**: `Row` with `IconToggleButton` for Like (`Icons.Outlined.FavoriteBorder` / `Icons.Filled.Favorite`), `IconButton` for Comment (`Icons.Outlined.ChatBubbleOutline`), and `IconButton` for Share (`Icons.Outlined.Share`).
4.  **Component**: `NavigationBar`
    *   **Name**: Bottom Navigation
    *   **Position & Size**: Bottom of the `Scaffold`, `fillMaxWidth`.
    *   **Style**: `md.sys.color.surfaceContainer`.
    *   **Content**: Five `NavigationBarItem`s:
        *   **Home**: `selected = true`. Icon: `Icons.Filled.Home`. Label: "Home".
        *   **Explore**: `selected = false`. Icon: `Icons.Outlined.Explore`. Label: "Explore".
        *   **Create**: `selected = false`. Icon: `Icons.Filled.AddCircle`. Icon size `40dp`. Label: "Create".
        *   **Library**: `selected = false`. Icon: `Icons.Outlined.VideoLibrary`. Label: "Library".
        *   **Profile**: `selected = false`. Icon: `Icons.Outlined.AccountCircle`. Label: "Profile".

#### Interaction & Behavior:
*   **Profile Avatar (Top Bar)**: On tap -> Navigate to `30_Profile`.
*   **Notifications Icon**: On tap -> Navigate to `33_Notifications`.
*   **Explore Tab**: On tap -> Navigate to `22_Explore`.
*   **Create Tab**: On tap -> Navigate to `12_Create`.
*   **Library Tab**: On tap -> Navigate to `29_Library`.
*   **Scroll Behavior**: The `TopAppBar` scrolls out of view when the user scrolls down the feed and reappears when they scroll up.

#### Critical Scenarios & States:
*   **Loading State**: A full-screen `CircularProgressIndicator` is shown on initial load. For pull-to-refresh, a `PullRefreshIndicator` is shown at the top.
*   **Empty State**: If the feed is empty (e.g., new user not following anyone), display a message: "Your feed is empty. Explore to find creators to follow!" with a `FilledButton` "Explore Now" that navigates to `22_Explore`.
*   **Error State**: If the feed fails to load, a `Snackbar` appears with "Couldn't refresh feed. Please check your connection."

---

## Flow: Music Creation

### Screen 12: Create
*   **Screen Name/ID**: `12_Create`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `Arrangement.Center` and `Alignment.CenterHorizontally`. Padding `16dp`.

#### Components:
1.  **Component**: `Text` (Title)
    *   **Name**: Create Title
    *   **Style**: `md.sys.typography.headlineMedium`.
    *   **Content**: "Start a New Track"
2.  **Component**: `LazyVerticalGrid`
    *   **Name**: Creation Options Grid
    *   **Position & Size**: `fillMaxWidth`, margin top `32dp`.
    *   **Layout**: `GridCells.Fixed(2)`, spacing `16dp`.
    *   **Content**: A grid of `Card` components for creation options.
3.  **Component**: `Card` (Creation Option - Repeated)
    *   **Name**: Option Card (e.g., Voice/Mic)
    *   **Style**: `CardDefaults.outlinedCardColors()`. `onClick` is defined.
    *   **Layout**: `Column` with `Alignment.CenterHorizontally`, padding `16dp`.
    *   **Content**:
        *   `Icon`: e.g., `Icons.Filled.Mic`, size `48dp`, color `md.sys.color.primary`.
        *   `Text`: e.g., "Voice/Mic", typography `md.sys.typography.titleMedium`.
4.  **Options to include**:
    *   "Import Track" (`Icons.Filled.UploadFile`)
    *   "Voice/Mic" (`Icons.Filled.Mic`)
    *   "Sampler" (`Icons.Filled.GridOn`)
    *   "Looper" (`Icons.Filled.Loop`)
    *   "Virtual Instruments" (`Icons.Filled.Piano`)

#### Interaction & Behavior:
*   **Import Track Card**: On tap -> Navigate to `13_File_Picker`.
*   **Voice/Mic Card**: On tap -> Navigate to `17_Studio`.
*   **Sampler Card**: On tap -> Navigate to `14_Sampler`.
*   **Looper Card**: On tap -> Navigate to `15_Looper`.
*   **Virtual Instruments Card**: On tap -> Navigate to `17_Studio`.
*   **Animation**: `MaterialElevationScale` (outgoing) for card taps.

---

### Screen 13: File Picker
*   **Screen Name/ID**: `13_File_Picker`
*   **Dimensions**: N/A (System UI)
*   **Background**: This screen is the native Android file picker interface.
*   **Layout**: Conforms to the system file picker.

#### Interaction & Behavior:
*   **File Selected**: User selects a compatible audio file -> System navigates to `17_Studio` with the selected file loaded.
*   **Cancelled**: User cancels the picker -> System returns to `12_Create`.

---

### Screen 14: Sampler
*   **Screen Name/ID**: `14_Sampler`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `TopAppBar`. The main content is a custom UI.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Sampler Header
    *   **Content**: Title "Sampler", Navigation Icon `Icons.Filled.Close`.
2.  **Component**: Custom Sampler UI
    *   **Description**: A grid of 16 pads. A waveform display at the top. Record/Import buttons at the bottom.
3.  **Component**: `FilledButton`
    *   **Name**: Done Button
    *   **Position & Size**: Anchored to the bottom. `fillMaxWidth`, height `56dp`. Padding `16dp`.
    *   **Content**: "Done"

#### Interaction & Behavior:
*   **Close Icon**: On tap -> Discard changes and navigate back to `12_Create`.
*   **Done Button**: On tap -> Add the created sample as a track and navigate to `17_Studio`.

---

### Screen 15: Looper
*   **Screen Name/ID**: `15_Looper`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Looper Header
    *   **Content**: Title "Looper Packs", Navigation Icon `Icons.Filled.Close`.
2.  **Component**: `LazyColumn`
    *   **Name**: Looper Pack List
    *   **Content**: A list of available looper packs, each represented by a `ListItem` with artwork, name, and genre.

#### Interaction & Behavior:
*   **Close Icon**: On tap -> Navigate back to `12_Create`.
*   **Looper Pack Item**: On tap -> Navigate to `16_Looper_Interface`.

---

### Screen 16: Looper Interface
*   **Screen Name/ID**: `16_Looper_Interface`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.onSurface` (typically a dark UI for creation tools).
*   **Layout**: Custom UI representing a DJ-style launchpad.

#### Components:
1.  **Component**: Custom Looper UI
    *   **Description**: A grid of pads, each corresponding to a loop from the selected pack. Pads light up when active. Transport controls (Play, Record) are at the bottom.
2.  **Component**: `IconButton`
    *   **Name**: Open in Studio Button
    *   **Position**: Top right corner.
    *   **Content**: Icon `Icons.Filled.Launch`.

#### Interaction & Behavior:
*   **Pads**: On tap -> Trigger/untrigger the associated loop.
*   **Record Button**: On tap -> Start recording the arrangement.
*   **Open in Studio Button**: On tap -> Take the recorded arrangement and navigate to `17_Studio`.

---

### Screen 17: Studio
*   **Screen Name/ID**: `17_Studio`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surfaceVariant`
*   **Layout**: `Scaffold` with a custom layout. This is a highly complex, custom screen.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Studio Header
    *   **Style**: `containerColor`: `md.sys.color.surface`.
    *   **Content**:
        *   `navigationIcon`: `Icons.Filled.ArrowBack`.
        *   `title`: Project Name (editable on tap).
        *   `actions`: `IconButton` with `Icons.Filled.CloudUpload` (Save).
2.  **Component**: Custom Timeline UI
    *   **Name**: Track Timeline
    *   **Description**: A horizontally scrollable view showing audio tracks stacked vertically. Each track has a header with controls (Mute, Solo, Volume) and a timeline displaying the audio waveform/MIDI data. A playhead indicates the current position.
3.  **Component**: Transport Controls
    *   **Name**: Playback Controls
    *   **Position**: A fixed bar at the bottom of the screen.
    *   **Content**: `IconButton`s for Go to Beginning, Rewind, Play/Pause, Record, and Metronome toggle.
4.  **Component**: `FloatingActionButton`
    *   **Name**: Add Track Button
    *   **Position**: Bottom right, above the transport controls.
    *   **Content**: `Icon` `Icons.Filled.Add`.

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Show "Save changes?" dialog. If yes, navigate to `18_Save_Project`. If no, navigate to `11_Home_Feed`.
*   **Save Icon**: On tap -> Navigate to `18_Save_Project`.
*   **Add Track FAB**: On tap -> Navigate to `19_Add_Track`.

---

### Screen 18: Add Track
*   **Screen Name/ID**: `19_Add_Track`
*   **Dimensions**: N/A (Bottom Sheet Dialog)
*   **Background**: `md.sys.color.surfaceContainer`
*   **Layout**: `ModalBottomSheet` that slides up from the bottom.

#### Components:
1.  **Component**: `Text` (Title)
    *   **Name**: Sheet Title
    *   **Position & Size**: Top of the sheet, padding `16dp`.
    *   **Style**: `md.sys.typography.titleLarge`.
    *   **Content**: "Add Track"
2.  **Component**: `LazyVerticalGrid`
    *   **Name**: Track Type Grid
    *   **Layout**: `GridCells.Fixed(3)`, content padding `16dp`.
    *   **Content**: A grid of items, each with an `Icon` and `Text` label (e.g., "Voice/Mic", "Guitar", "Bass", "MIDI Instruments").

#### Interaction & Behavior:
*   **Track Type Item**: On tap -> Dismisses the bottom sheet and adds a new track of the selected type to the `17_Studio` screen.
*   **Dismiss**: Swiping down or tapping outside the sheet dismisses it and returns to `17_Studio`.

---

### Screen 19: Save Project
*   **Screen Name/ID**: `18_Save_Project`
*   **Dimensions**: N/A (Dialog)
*   **Background**: `md.sys.color.surfaceContainer`
*   **Layout**: `AlertDialog`

#### Components:
1.  **Component**: `AlertDialog`
    *   **Name**: Save Project Dialog
    *   **Content**:
        *   `icon`: `Icons.Filled.Save`.
        *   `title`: `Text` "Save Project".
        *   `text`: A `Column` containing an `OutlinedTextField` for the project name.
        *   `confirmButton`: `TextButton` with text "Save".
        *   `dismissButton`: `TextButton` with text "Cancel".
        *   **Extra Action**: A `FilledButton` below the text field with text "Publish".

#### Interaction & Behavior:
*   **Cancel Button**: On tap -> Dismiss dialog, return to `17_Studio`.
*   **Save Button**: On tap -> Save the project, show a confirmation `Snackbar` ("Project Saved!"), and navigate to `29_Library`.
*   **Publish Button**: On tap -> Navigate to `20_Publish_Project`.

---

### Screen 20: Publish Project
*   **Screen Name/ID**: `20_Publish_Project`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Publish Header
    *   **Content**: Title "Publish", Navigation Icon `Icons.Filled.ArrowBack`. Action `TextButton` "Publish".
2.  **Component**: `Column` (Scrollable)
    *   **Layout**: Padding `16dp`.
    *   **Content**:
        *   `Image` (Album Art), `120dp` x `120dp`.
        *   `OutlinedTextField` for "Title".
        *   `OutlinedTextField` for "Description" (multiline).
        *   `OutlinedTextField` with dropdown for "Genre".
        *   `TextField` for "Hashtags" (using chips for input).
3.  **Component**: `TextButton` (Action in TopAppBar)
    *   **Name**: Publish Button
    *   **Style**: Disabled until required fields are filled.

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `18_Save_Project`.
*   **Publish Button**: On tap -> Publish the project, show a confirmation `Snackbar`, and navigate to `30_Profile`.

---

## Flow: Explore and Search

### Screen 21: Explore
*   **Screen Name/ID**: `22_Explore`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `NavigationBar`.

#### Components:
1.  **Component**: `SearchBar`
    *   **Name**: Search Bar
    *   **Position & Size**: Top of the screen, `fillMaxWidth`, padding `16dp`.
    *   **Style**: `DockedSearchBar`.
    *   **Content**: `placeholder`: "Search tracks, people, #hashtags". `leadingIcon`: `Icons.Filled.Search`.
2.  **Component**: `LazyColumn`
    *   **Name**: Explore Content
    *   **Content**: A mix of content sections, such as:
        *   "Featured Tracks" (horizontal scrolling `LazyRow` of `Card`s).
        *   "Trending Hashtags" (`LazyRow` of `Chip`s).
        *   "Top Creators" (`LazyRow` of circular `Image` avatars).
3.  **Component**: `NavigationBar`
    *   **Name**: Bottom Navigation
    *   **Content**: Same as `11_Home_Feed`, but with "Explore" selected.

#### Interaction & Behavior:
*   **Search Bar**: On tap -> Navigate to `23_Search`.
*   **Track Card**: On tap -> Navigate to `25_Track_Details`.
*   **User Profile Avatar**: On tap -> Navigate to `30_Profile`.

---

### Screen 22: Search
*   **Screen Name/ID**: `23_Search`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold`.

#### Components:
1.  **Component**: `SearchBar`
    *   **Name**: Active Search Bar
    *   **Position & Size**: Top of the screen, `fillMaxWidth`.
    *   **Style**: `Expanded` state.
    *   **Content**: `leadingIcon`: `Icons.Filled.ArrowBack`. `trailingIcon`: `Icons.Filled.Close` to clear text. The search field is focused.
2.  **Component**: `LazyColumn`
    *   **Name**: Search Suggestions
    *   **Content**: A list of recent searches or trending topics.

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `22_Explore`.
*   **Keyboard Search Action**: User types query and presses search on keyboard -> Navigate to `24_Search_Results`.

---

### Screen 23: Search Results
*   **Screen Name/ID**: `24_Search_Results`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Search Results Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: The search query in a `TextField`.
2.  **Component**: `TabRow`
    *   **Name**: Results Tabs
    *   **Position & Size**: Below `TopAppBar`, `fillMaxWidth`.
    *   **Content**: `Tab`s for "Tracks", "People", "Hashtags".
3.  **Component**: `HorizontalPager` or `Column`
    *   **Name**: Tab Content
    *   **Content**: Displays the content for the currently selected tab. Each tab contains a `LazyColumn` of results.

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `23_Search`.
*   **Track Result**: On tap -> Navigate to `25_Track_Details`.
*   **People Result**: On tap -> Navigate to `30_Profile`.

---

### Screen 24: Track Details
*   **Screen Name/ID**: `25_Track_Details`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Track Details Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: "Playing".
2.  **Component**: `Column` (Scrollable)
    *   **Layout**: Padding `16dp`.
    *   **Content**:
        *   `Image` (Album Art), large, `fillMaxWidth`.
        *   `Text` (Track Title), `md.sys.typography.headlineSmall`.
        *   `Text` (Artist Name), `md.sys.typography.titleMedium`.
        *   `Slider` for playback progress.
        *   `Row` of transport controls (Play/Pause, etc.).
        *   `Row` of action buttons (Like, Comment, Share).

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to the previous screen (`22_Explore` or `24_Search_Results`).

---

## Flow: Library

### Screen 25: Library
*   **Screen Name/ID**: `29_Library`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `NavigationBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Library Header
    *   **Content**: `title`: "Library".
2.  **Component**: `LazyColumn`
    *   **Name**: Projects List
    *   **Content**: A list of `ListItem`s, each representing a saved project.
3.  **Component**: `ListItem` (Project)
    *   **Content**: `headlineContent`: Project Name. `supportingContent`: Last modified date. `trailingContent`: `IconButton` with `Icons.Filled.MoreVert`.
4.  **Component**: `NavigationBar`
    *   **Name**: Bottom Navigation
    *   **Content**: Same as `11_Home_Feed`, but with "Library" selected.

#### Interaction & Behavior:
*   **Project ListItem**: On tap -> Open the project in `17_Studio`.
*   **Home Tab**: On tap -> Navigate to `11_Home_Feed`.

#### Critical Scenarios & States:
*   **Empty State**: If no projects exist, show an icon (`Icons.Outlined.MusicNote`), a title "Your Projects Live Here", supporting text "Start creating to see your projects.", and a `FilledButton` "Start Creating" that navigates to `12_Create`.

---

## Flow: Profile and Settings

### Screen 26: Profile
*   **Screen Name/ID**: `30_Profile`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `NavigationBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Profile Header
    *   **Content**: `title`: Username. `actions`: `IconButton` with `Icons.Filled.Settings`.
2.  **Component**: `LazyColumn`
    *   **Name**: Profile Content
    *   **Content**:
        *   **Header Section**: `Column` with Profile Picture, Name, Follower/Following counts, and an "Edit Profile" `OutlinedButton`.
        *   **TabRow**: Tabs for "Published", "Projects", "Playlists".
        *   **Content Area**: A list of tracks/projects based on the selected tab.
3.  **Component**: `NavigationBar`
    *   **Name**: Bottom Navigation
    *   **Content**: Same as `11_Home_Feed`, but with "Profile" selected.

#### Interaction & Behavior:
*   **Settings Icon**: On tap -> Navigate to `28_Settings`.
*   **Edit Profile Button**: On tap -> Navigate to `27_Edit_Profile`.
*   **Home Tab**: On tap -> Navigate to `11_Home_Feed`.

---

### Screen 27: Edit Profile
*   **Screen Name/ID**: `27_Edit_Profile`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Edit Profile Header
    *   **Content**: `navigationIcon`: `Icons.Filled.Close`. `title`: "Edit Profile". `actions`: `TextButton` "Save".
2.  **Component**: `Column` (Scrollable)
    *   **Layout**: Padding `16dp`.
    *   **Content**:
        *   Profile Picture with "Change Photo" `TextButton`.
        *   `OutlinedTextField` for "Name".
        *   `OutlinedTextField` for "Username".
        *   `OutlinedTextField` for "Bio".

#### Interaction & Behavior:
*   **Close Icon**: On tap -> Navigate back to `30_Profile`.
*   **Save Button**: On tap -> Save changes and navigate back to `30_Profile`.

---

### Screen 28: Settings
*   **Screen Name/ID**: `28_Settings`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Settings Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: "Settings".
2.  **Component**: `LazyColumn`
    *   **Name**: Settings List
    *   **Content**: A list of `ListItem`s for different settings categories.
        *   `ListItem`: "Account Settings"
        *   `ListItem`: "Notifications"
        *   `ListItem`: "Privacy"
        *   `ListItem`: "About"
        *   `ListItem`: "Log Out" (styled with `md.sys.color.error`).

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `30_Profile`.
*   **Account Settings**: On tap -> Navigate to `31_Account_Settings`.
*   **Notifications**: On tap -> Navigate to `32_Notification_Settings`.
*   **Log Out**: On tap -> Show confirmation dialog. If confirmed, log out and navigate to `01_Welcome_Screen`.

---

### Screen 29: Account Settings
*   **Screen Name/ID**: `31_Account_Settings`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Account Settings Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: "Account Settings".
2.  **Component**: `LazyColumn`
    *   **Name**: Settings List
    *   **Content**: `ListItem`s for "Change Email", "Change Password", "Delete Account".

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `28_Settings`.

---

### Screen 30: Notification Settings
*   **Screen Name/ID**: `32_Notification_Settings`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Notification Settings Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: "Notifications".
2.  **Component**: `LazyColumn`
    *   **Name**: Settings List
    *   **Content**: `ListItem`s with `Switch` components for toggling different notification types (e.g., "New Followers", "Comments", "Likes").

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `28_Settings`.
*   **Switch**: On toggle -> Update user's notification preferences.

---

### Screen 31: Notifications
*   **Screen Name/ID**: `33_Notifications`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`.

#### Components:
1.  **Component**: `TopAppBar`
    *   **Name**: Notifications Header
    *   **Content**: `navigationIcon`: `Icons.Filled.ArrowBack`. `title`: "Notifications".
2.  **Component**: `LazyColumn`
    *   **Name**: Notifications List
    *   **Content**: A list of `ListItem`s, each representing a notification (e.g., "@user liked your track.").

#### Interaction & Behavior:
*   **Back Arrow**: On tap -> Navigate back to `11_Home_Feed`.

#### Critical Scenarios & States:
*   **Empty State**: If no notifications, show an icon (`Icons.Outlined.NotificationsOff`), a title "All Caught Up!", and supporting text "You have no new notifications.".

---
*This specification documents all 33 screens as requested in the input flow tree.*
```

---
