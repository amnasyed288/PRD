# AI Music Maker: Android Design Specification

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
- **Seed Color:** `#007AFF` (Vibrant Blue)
- **Source:** This seed color is used to generate the full Material 3 tonal palette.

#### Light Theme Color Roles
- **Primary:** `md.sys.color.primary` (#0B57D0)
- **On Primary:** `md.sys.color.on-primary` (#FFFFFF)
- **Primary Container:** `md.sys.color.primary-container` (#D8E2FF)
- **On Primary Container:** `md.sys.color.on-primary-container` (#001849)
- **Secondary:** `md.sys.color.secondary` (#565E71)
- **On Secondary:** `md.sys.color.on-secondary` (#FFFFFF)
- **Secondary Container:** `md.sys.color.secondary-container` (#DAE2F9)
- **On Secondary Container:** `md.sys.color.on-secondary-container` (#131C2B)
- **Tertiary:** `md.sys.color.tertiary` (#705574)
- **On Tertiary:** `md.sys.color.on-tertiary` (#FFFFFF)
- **Tertiary Container:** `md.sys.color.tertiary-container` (#FAD7FE)
- **On Tertiary Container:** `md.sys.color.on-tertiary-container` (#29132D)
- **Error:** `md.sys.color.error` (#B3261E)
- **On Error:** `md.sys.color.on-error` (#FFFFFF)
- **Error Container:** `md.sys.color.error-container` (#F9DEDC)
- **On Error Container:** `md.sys.color.on-error-container` (#410E0B)
- **Background:** `md.sys.color.background` (#FEFBFF)
- **On Background:** `md.sys.color.on-background` (#1B1B1F)
- **Surface:** `md.sys.color.surface` (#FEFBFF)
- **On Surface:** `md.sys.color.on-surface` (#1B1B1F)
- **Surface Variant:** `md.sys.color.surface-variant` (#E1E2EC)
- **On Surface Variant:** `md.sys.color.on-surface-variant` (#44474F)
- **Outline:** `md.sys.color.outline` (#74777F)
- **Outline Variant:** `md.sys.color.outline-variant` (#C4C6D0)
- **Scrim:** `md.sys.color.scrim` (#000000)
- **Inverse Surface:** `md.sys.color.inverse-surface` (#2F3033)
- **Inverse On Surface:** `md.sys.color.inverse-on-surface` (#F2F0F4)
- **Inverse Primary:** `md.sys.color.inverse-primary` (#ADC6FF)

#### Dark Theme Color Roles
- **Primary:** `md.sys.color.primary` (#ADC6FF)
- **On Primary:** `md.sys.color.on-primary` (#002B75)
- **Primary Container:** `md.sys.color.primary-container` (#0040A3)
- **On Primary Container:** `md.sys.color.on-primary-container` (#D8E2FF)
- **Secondary:** `md.sys.color.secondary` (#BEC6DC)
- **On Secondary:** `md.sys.color.on-secondary` (#283041)
- **Secondary Container:** `md.sys.color.secondary-container` (#3E4759)
- **On Secondary Container:** `md.sys.color.on-secondary-container` (#DAE2F9)
- **Tertiary:** `md.sys.color.tertiary` (#DEBCF1)
- **On Tertiary:** `md.sys.color.on-tertiary` (#3F2843)
- **Tertiary Container:** `md.sys.color.tertiary-container` (#573E5B)
- **On Tertiary Container:** `md.sys.color.on-tertiary-container` (#FAD7FE)
- **Error:** `md.sys.color.error` (#F2B8B5)
- **On Error:** `md.sys.color.on-error` (#601410)
- **Error Container:** `md.sys.color.error-container` (#8C1D18)
- **On Error Container:** `md.sys.color.on-error-container` (#F9DEDC)
- **Background:** `md.sys.color.background` (#1B1B1F)
- **On Background:** `md.sys.color.on-background` (#E3E2E6)
- **Surface:** `md.sys.color.surface` (#1B1B1F)
- **On Surface:** `md.sys.color.on-surface` (#E3E2E6)
- **Surface Variant:** `md.sys.color.surface-variant` (#44474F)
- **On Surface Variant:** `md.sys.color.on-surface-variant` (#C4C6D0)
- **Outline:** `md.sys.color.outline` (#8E9099)
- **Outline Variant:** `md.sys.color.outline-variant` (#44474F)
- **Scrim:** `md.sys.color.scrim` (#000000)
- **Inverse Surface:** `md.sys.color.inverse-surface` (#E3E2E6)
- **Inverse On Surface:** `md.sys.color.inverse-on-surface` (#2F3033)
- **Inverse Primary:** `md.sys.color.inverse-primary` (#0B57D0)

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

### Flow: Onboarding and Authentication

---

### 01_01_Welcome
- **Screen Name/ID:** `01_01_Welcome`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, filling max size. Elements are horizontally centered. Vertical arrangement is spaced with a large central graphic.

#### Components
1.  **Component: App Logo**
    - **Name:** `Image`
    - **Position & Size:** Centered horizontally. `180dp x 180dp`. Margin top `100dp`.
    - **Style:** A stylized sound wave forming a brain silhouette.
    - **Content:** `res/drawable/app_logo.xml`

2.  **Component: Headline Text**
    - **Name:** `Text`
    - **Position & Size:** Centered horizontally. Margin top `32dp`.
    - **Style:** Typography `md.sys.typography.headlineLarge`. Color `md.sys.color.onSurface`. Text alignment `Center`.
    - **Content:** "Your Ideas, Your Music"

3.  **Component: Body Text**
    - **Name:** `Text`
    - **Position & Size:** Centered horizontally. Margin top `16dp`. Padding horizontal `32dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Color `md.sys.color.onSurfaceVariant`. Text alignment `Center`.
    - **Content:** "Create unique tracks from text, photos, or your own audio with the power of AI."

4.  **Component: Primary CTA Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Centered horizontally. `fillMaxWidth` with horizontal margin `24dp`. Height `52dp`. Margin top `64dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Get Started"

5.  **Component: Secondary CTA Button**
    - **Name:** `TextButton`
    - **Position & Size:** Centered horizontally. `fillMaxWidth` with horizontal margin `24dp`. Height `52dp`. Margin top `16dp`. Margin bottom `32dp`.
    - **Style:** Color `md.sys.color.primary`. Typography `md.sys.typography.labelLarge`.
    - **Content:** "Log In"

#### Interaction & Behavior
- **Primary CTA Button:**
  - **States:** Standard Material 3 state layers for pressed (12% onPrimary overlay), hover, focused.
  - **Interaction:** On tap -> Navigate to `01_02_Sign_Up_Options` using a `MaterialSharedAxis` (Z-axis) transition.
- **Secondary CTA Button:**
  - **States:** Standard Material 3 state layers for pressed (12% primary overlay), hover, focused.
  - **Interaction:** On tap -> Navigate to `01_04_Log_In` using a `MaterialSharedAxis` (Z-axis) transition.

---

### 01_02_Sign_Up_Options
- **Screen Name/ID:** `01_02_Sign_Up_Options`
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

2.  **Component: Social Sign-Up Buttons**
    - **Name:** `Column` of `OutlinedButton`s
    - **Position & Size:** `fillMaxWidth`. Margin top `32dp`.
    - **Style:** Each button is `OutlinedButton` with `fillMaxWidth`, height `52dp`, shape `Shape.Corner.Full`.
    - **Content:**
        - **Button 1:** Icon `res/drawable/google_logo.xml`, Text "Continue with Google".
        - **Button 2:** Icon `res/drawable/apple_logo.xml`, Text "Continue with Apple". Margin top `16dp`.

3.  **Component: Divider**
    - **Name:** `Row` with `Divider` and `Text`
    - **Position & Size:** `fillMaxWidth`. Margin vertical `32dp`.
    - **Style:** `Divider` color `md.sys.color.outline`. `Text` style `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.
    - **Content:** Two `Divider`s with a `Text` element "or" in the middle.

4.  **Component: Email Sign-Up Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`.
    - **Style:** Color `md.sys.color.primary`. Text color `md.sys.color.onPrimary`. Typography `md.sys.typography.labelLarge`. Shape `Shape.Corner.Full`.
    - **Content:** "Sign up with email"

5.  **Component: Log In Link**
    - **Name:** `Row` with `Text` and `TextButton`
    - **Position & Size:** Centered horizontally at the bottom of the view. Margin top `32dp`.
    - **Style:** `Text` style `md.sys.typography.bodyMedium`. `TextButton` style `md.sys.typography.labelLarge`.
    - **Content:** `Text`: "Already have an account?", `TextButton`: "Log in"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_01_Welcome`.
- **Continue with Google/Apple:** On tap -> Initiate social sign-in flow. On success, navigate to `02_01_Create_Home`.
- **Sign up with email Button:** On tap -> Navigate to `01_03_Email_Sign_Up`.
- **Log in link:** On tap -> Navigate to `01_04_Log_In`.

---

### 01_03_Email_Sign_Up
- **Screen Name/ID:** `01_03_Email_Sign_Up`
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
        - **Title:** `Text` with content "Sign up with Email", style `md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:** Label "Email", Leading Icon `Icons.Filled.Email`, Keyboard Type `Email`.

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Style:** Typography `md.sys.typography.bodyLarge`. Shape `Shape.Corner.Medium`.
    - **Content:** Label "Password", Leading Icon `Icons.Filled.Lock`, Trailing Icon for visibility toggle, Keyboard Type `Password`.

4.  **Component: Sign Up Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Shape `Shape.Corner.Full`.
    - **Content:** "Sign up"

5.  **Component: Log In Link**
    - **Name:** `Row` with `Text` and `TextButton`
    - **Position & Size:** Centered horizontally. Margin top `32dp`.
    - **Style:** `Text` style `md.sys.typography.bodyMedium`. `TextButton` style `md.sys.typography.labelLarge`.
    - **Content:** `Text`: "Already have an account?", `TextButton`: "Log in"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_02_Sign_Up_Options`.
- **Sign Up Button:** On tap -> Validate fields. On success, show loading indicator in button and navigate to `02_01_Create_Home`. On failure, show error on text fields.
- **Log in link:** On tap -> Navigate to `01_04_Log_In`.

---

### 01_04_Log_In
- **Screen Name/ID:** `01_04_Log_In`
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
        - **Title:** `Text` with content "Log In", style `md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Content:** Label "Email".

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Content:** Label "Password".

4.  **Component: Forgot Password Link**
    - **Name:** `TextButton`
    - **Position & Size:** Aligned to the end of the `Column`. Margin top `8dp`.
    - **Style:** Typography `md.sys.typography.labelLarge`.
    - **Content:** "Forgot Password?"

5.  **Component: Log In Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Shape `Shape.Corner.Full`.
    - **Content:** "Log in"

6.  **Component: Sign Up Link**
    - **Name:** `Row` with `Text` and `TextButton`
    - **Position & Size:** Centered horizontally. Margin top `32dp`.
    - **Content:** `Text`: "Don't have an account?", `TextButton`: "Sign up"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_01_Welcome`.
- **Forgot Password Link:** On tap -> Navigate to `01_05_Password_Reset`.
- **Log In Button:** On tap -> Validate fields. On success, navigate to `02_01_Create_Home`. On failure, show a `Snackbar` with "Invalid email or password."
- **Sign up link:** On tap -> Navigate to `01_03_Email_Sign_Up`.

---

### 01_05_Password_Reset
- **Screen Name/ID:** `01_05_Password_Reset`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout. Padding `16dp`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Reset Password", style `md.sys.typography.titleLarge`.

2.  **Component: Info Text**
    - **Name:** `Text`
    - **Position & Size:** `fillMaxWidth`. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.bodyMedium`. Color `md.sys.color.onSurfaceVariant`.
    - **Content:** "Enter your account's email address and we will send you a link to reset your password."

3.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`. Margin top `16dp`.
    - **Content:** Label "Email".

4.  **Component: Reset Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Margin top `24dp`.
    - **Style:** Color `md.sys.color.primary`. Shape `Shape.Corner.Full`.
    - **Content:** "Send Reset Link"

#### Interaction & Behavior
- **Top App Bar Navigation Icon:** On tap -> Navigate back to `01_04_Log_In`.
- **Reset Button:** On tap -> Validate email. On success, show a `Snackbar` "Reset link sent." and navigate to `01_04_Log_In`.

---

### Flow: Main App Navigation

---

### 02_01_Create_Home
- **Screen Name/ID:** `02_01_Create_Home`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`, main content area, and `NavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth`, height `56dp`.
    - **Style:** `TopAppBarDefaults.enterAlwaysScrollBehavior`. Container color `md.sys.color.surface`.
    - **Content:**
        - **Title:** `Text` with content "Create Music", style `md.sys.typography.titleLarge`.

2.  **Component: Main Content**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the main content area of the `Scaffold`. Padding `16dp`.
    - **Layout:** `Arrangement.spacedBy(16.dp)`.
    - **Content:** A list of `Card` components for each creation method.
        - **Card 1: Text-to-Music:** `ElevatedCard` with Icon `Icons.Filled.TextFields`, Title "Text-to-Music", Subtitle "Describe the song you want to create".
        - **Card 2: Photo-to-Music:** `ElevatedCard` with Icon `Icons.Filled.Photo`, Title "Photo-to-Music", Subtitle "Turn any photo into a unique track".
        - **Card 3: Studio Mode:** `ElevatedCard` with Icon `Icons.Filled.Tune`, Title "Studio Mode", Subtitle "Fine-tune your creation with detailed inputs".
        - **Card 4: Import Audio:** `ElevatedCard` with Icon `Icons.Filled.UploadFile`, Title "Import Device Audio", Subtitle "Remix your own audio files".

3.  **Component: Bottom Navigation Bar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`. `fillMaxWidth`.
    - **Style:** Container color `md.sys.color.surfaceContainer`.
    - **Content:** Four `NavigationBarItem`s.
        - **Item 1 (Selected):** Icon `Icons.Filled.AddCircle`, Label "Create", `selected = true`.
        - **Item 2:** Icon `Icons.Outlined.Explore`, Label "Explore", `selected = false`.
        - **Item 3:** Icon `Icons.Outlined.LibraryMusic`, Label "My Music", `selected = false`.
        - **Item 4:** Icon `Icons.Outlined.AccountCircle`, Label "Profile", `selected = false`.

#### Interaction & Behavior
- **Text-to-Music Card:** On tap -> Navigate to `03_02_Text_Generation`.
- **Photo-to-Music Card:** On tap -> Navigate to `03_04_Photo_Selection`.
- **Studio Mode Card:** On tap -> Navigate to `03_08_Studio_Mode_Input`.
- **Import Audio Card:** On tap -> Navigate to `03_09_Device_File_Picker`.
- **Explore Tab:** On tap -> Navigate to `02_02_Explore`.
- **My Music Tab:** On tap -> Navigate to `02_03_My_Music_Queue`.
- **Profile Tab:** On tap -> Navigate to `02_04_Profile`.

---

### 02_02_Explore
- **Screen Name/ID:** `02_02_Explore`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Explore".
2.  **Component: Category Filters**
    - **Name:** `LazyRow` of `FilterChip`s
    - **Position & Size:** Below Top App Bar. Padding horizontal `16dp`.
    - **Content:** Chips for "Pop", "Lo-Fi", "Electronic", "Hip Hop", "Ambient", etc.
3.  **Component: Song List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space. Padding `16dp`.
    - **Content:** List of pre-generated songs in `Card`s, each with album art, title, and a play button.
4.  **Component: Bottom Navigation Bar**
    - **(Identical to `02_01_Create_Home`, but with 'Explore' selected).**

#### Interaction & Behavior
- **Filter Chip:** On tap -> Reloads the song list with filtered content.
- **Song Card:** On tap -> Navigate to `04_03_Song_Playback`.
- **Other Nav Tabs:** Navigate to the respective screens (`Create Home`, `My Music - Queue`, `Profile`).

---

### 02_03_My_Music_Queue
- **Screen Name/ID:** `02_03_My_Music_Queue`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `TabRow`, and `NavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Title `Text` "My Music".
2.  **Component: Tab Row**
    - **Name:** `TabRow`
    - **Position & Size:** Below Top App Bar.
    - **Content:** Two `Tab`s: "Queue" and "Library".
3.  **Component: Queue List**
    - **Name:** `LazyColumn` (for the "Queue" tab)
    - **Position & Size:** Fills the content area.
    - **Content:** List of songs currently being generated or in an error state.
        - **Generating Item:** Shows song title, a `LinearProgressIndicator`, and a "Cancel" `IconButton`.
        - **Error Item:** Shows song title, an error message, and a "Regenerate" `TextButton`.
        - **Completed Item:** Shows song title, "Completed", and is tappable.
4.  **Component: Bottom Navigation Bar**
    - **(Identical to `02_01_Create_Home`, but with 'My Music' selected).**

#### Interaction & Behavior
- **'Library' Tab:** On tap -> Switch content view to `04_02_My_Music_Library`.
- **'Cancel' Button:** On tap -> Cancels the song generation. Item is removed from the list.
- **'Regenerate' Button:** On tap -> Re-initiates the generation process for that song.
- **Completed Song Item:** On tap -> Navigate to `04_03_Song_Playback`.
- **Push Notification:** On tap -> Navigates directly to `04_03_Song_Playback` for the completed song.

---

### 02_04_Profile
- **Screen Name/ID:** `02_04_Profile`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `NavigationBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Profile". Actions: `IconButton` with `Icons.Filled.Settings`.
2.  **Component: Profile Header**
    - **Name:** `Column`
    - **Position & Size:** Top of content area. Padding `16dp`.
    - **Content:** `Image` (Avatar), `Text` (Username), `Text` (Email).
3.  **Component: Credits Info**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`. Margin horizontal `16dp`.
    - **Content:** `Row` with `Text` "Available Credits: 5" and a `FilledButton` "Get More Credits".
4.  **Component: Bottom Navigation Bar**
    - **(Identical to `02_01_Create_Home`, but with 'Profile' selected).**

#### Interaction & Behavior
- **Settings Icon:** On tap -> Navigate to `06_02_Settings`.
- **'Get More Credits' Button:** On tap -> Navigate to `07_01_Purchase_Credits`.
- **Other Nav Tabs:** Navigate to the respective screens.

---

### Flow: Core Music Creation

---

### 03_02_Text_Generation
- **Screen Name/ID:** `03_02_Text_Generation`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Body is a `Column` with `verticalScroll`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Text-to-Music".
2.  **Component: Prompt Input**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `minHeight(120dp)`. Padding `16dp`.
    - **Content:** Label "Describe your song...".
3.  **Component: Inspire Me Button**
    - **Name:** `TextButton`
    - **Position & Size:** Aligned to the end of the prompt field.
    - **Content:** Icon `Icons.Filled.AutoAwesome`, Text "Inspire Me".
4.  **Component: Parameter Selection**
    - **Name:** `Column`
    - **Position & Size:** Padding `16dp`.
    - **Content:** Labeled `ExposedDropdownMenuBox` components for "Genre", "Mood", and "Vocals".
5.  **Component: Generate Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`. Height `52dp`. Padding `16dp`.
    - **Content:** "Generate"

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `02_01_Create_Home`.
- **'Inspire Me' Button:** On tap -> Show `03_03_Inspire_Me_Overlay` as a `ModalBottomSheet`.
- **'Generate' Button:** On tap -> Add song to generation queue. Navigate to `02_03_My_Music_Queue`.

---

### 03_03_Inspire_Me_Overlay
- **Screen Name/ID:** `03_03_Inspire_Me_Overlay`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.
- **Layout:** `Column` with a `LazyColumn`.

#### Components
1.  **Component: Bottom Sheet Handle & Title**
    - **Name:** `DragHandle` and `Text`
    - **Content:** Title "Inspire Me".
2.  **Component: Prompt List**
    - **Name:** `LazyColumn`
    - **Content:** A list of `ListItem`s with suggested prompts (e.g., "A chill lofi beat for studying", "An epic cinematic score for a space battle").

#### Interaction & Behavior
- **Prompt ListItem:** On tap -> Dismiss the sheet and populate the selected prompt into the text field on `03_02_Text_Generation`.
- **Close/Dismiss:** On tap of close button or swipe down -> Return to `03_02_Text_Generation`.

---

### 03_04_Photo_Selection
- **Screen Name/ID:** `03_04_Photo_Selection`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Body is a `Column`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Photo-to-Music".
2.  **Component: Upload Button**
    - **Name:** `FilledTonalButton`
    - **Position & Size:** `fillMaxWidth`. Height `64dp`. Margin `16dp`.
    - **Content:** Icon `Icons.Filled.PhotoLibrary`, Text "Upload from Gallery".
3.  **Component: Camera Button**
    - **Name:** `FilledTonalButton`
    - **Position & Size:** `fillMaxWidth`. Height `64dp`. Margin horizontal `16dp`.
    - **Content:** Icon `Icons.Filled.CameraAlt`, Text "Take Photo".

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `02_01_Create_Home`.
- **Upload Button:** On tap -> Request photo permissions. On grant, navigate to `03_05_System_File_Picker`. On deny, navigate to `08_03_Permission_Denied_Dialog`.
- **Camera Button:** On tap -> Request camera permissions. On grant, navigate to `03_06_Camera_Interface`. On deny, navigate to `08_03_Permission_Denied_Dialog`.

---

### 03_05_System_File_Picker
- **Screen Name/ID:** `03_05_System_File_Picker`
- **Dimensions:** N/A (System UI)
- **Behavior:** Native Android file/photo picker interface.

#### Interaction & Behavior
- **Selects a photo:** Navigate to `03_07_Photo_Edit_and_Generation`.
- **Cancels selection:** Navigate back to `03_04_Photo_Selection`.

---

### 03_06_Camera_Interface
- **Screen Name/ID:** `03_06_Camera_Interface`
- **Dimensions:** N/A (System UI)
- **Behavior:** Native Android camera interface.

#### Interaction & Behavior
- **Captures a photo:** Navigate to `03_07_Photo_Edit_and_Generation`.
- **Cancels capture:** Navigate back to `03_04_Photo_Selection`.

---

### 03_07_Photo_Edit_and_Generation
- **Screen Name/ID:** `03_07_Photo_Edit_and_Generation`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Generate from Photo".
2.  **Component: Image Preview & Cropper**
    - **Name:** `Image` with crop controls.
    - **Position & Size:** `fillMaxWidth`, `aspectRatio(1f)`.
    - **Content:** The selected/captured photo.
3.  **Component: Parameter Selection**
    - **Name:** `Column`
    - **Content:** Dropdowns for "Mood" and "Genre".
4.  **Component: Generate Button**
    - **Name:** `FilledButton`
    - **Content:** "Generate"

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `03_04_Photo_Selection`.
- **'Generate' Button:** On tap -> Add song to queue. Navigate to `02_03_My_Music_Queue`.

---

### 03_08_Studio_Mode_Input
- **Screen Name/ID:** `03_08_Studio_Mode_Input`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Body is `Column` with `verticalScroll`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Studio Mode".
2.  **Component: Input Fields**
    - **Name:** `Column` of `OutlinedTextField`s
    - **Position & Size:** Padding `16dp`.
    - **Content:** Fields for "Name", "Relation", "Occasion", "Prompt", and a dropdown for "Style".
3.  **Component: Generate Button**
    - **Name:** `FilledButton`
    - **Content:** "Generate"

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `02_01_Create_Home`.
- **'Generate' Button:** On tap -> Add song to queue. Navigate to `02_03_My_Music_Queue`.

---

### 03_09_Device_File_Picker
- **Screen Name/ID:** `03_09_Device_File_Picker`
- **Dimensions:** N/A (System UI)
- **Behavior:** Native Android file picker, filtered for audio files.

#### Interaction & Behavior
- **Selects an audio file:** Navigate to `03_10_Audio_Processing`.
- **Cancels selection:** Navigate back to `02_01_Create_Home`.

---

### 03_10_Audio_Processing
- **Screen Name/ID:** `03_10_Audio_Processing`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center` and `horizontalAlignment = Alignment.CenterHorizontally`.

#### Components
1.  **Component: Progress Indicator**
    - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered on screen. Size `64dp x 64dp`.
2.  **Component: Status Text**
    - **Name:** `Text`
    - **Position & Size:** Centered, below the progress indicator. Margin top `24dp`.
    - **Style:** Typography `md.sys.typography.titleMedium`.
    - **Content:** "Analyzing your audio..."

#### Interaction & Behavior
- **Lifecycle:** This screen is displayed modally.
- **Behavior:** On successful processing, automatically navigate to `03_11_Remix_Preview`. On failure, show a `Snackbar` and navigate to `02_01_Create_Home`.

---

### 03_11_Remix_Preview
- **Screen Name/ID:** `03_11_Remix_Preview`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Remix Preview".
2.  **Component: Player UI**
    - **Name:** `Column`
    - **Content:** Album art, song title, `Slider` for progress, and `IconButton`s for play/pause.
3.  **Component: Action Buttons**
    - **Name:** `Row`
    - **Position & Size:** Bottom of the screen. Padding `16dp`.
    - **Content:**
        - `OutlinedButton` "Try another suggestion".
        - `FilledButton` "Export".

#### Interaction & Behavior
- **Back/Cancel:** On tap -> Navigate to `02_01_Create_Home`.
- **'Try another suggestion' Button:** On tap -> Navigate back to `03_10_Audio_Processing`.
- **'Export' Button:** On tap -> Save song. Navigate to `04_02_My_Music_Library`.

---

### Flow: Music Management (My Music)

---

### 04_02_My_Music_Library
- **Screen Name/ID:** `04_02_My_Music_Library`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `TabRow`, and `NavigationBar`.

#### Components
1.  **Component: Top App Bar & Tab Row**
    - **(Identical to `02_03_My_Music_Queue`, but with the 'Library' tab selected).**
2.  **Component: Library List**
    - **Name:** `LazyColumn`
    - **Content:** List of saved songs. Each item is a `ListItem` with album art, title, artist, and a three-dot `IconButton`.
3.  **Component: Bottom Navigation Bar**
    - **(Identical to `02_03_My_Music_Queue`).**

#### Interaction & Behavior
- **'Queue' Tab:** On tap -> Switch content view to `02_03_My_Music_Queue`.
- **Song ListItem:** On tap -> Navigate to `04_03_Song_Playback`.
- **Three-dot Menu:** On tap -> Open `04_05_Song_Options_Menu` as a `ModalBottomSheet`.
- **Empty State:** If library is empty, show a centered message "Your saved songs will appear here."

---

### 04_03_Song_Playback
- **Screen Name/ID:** `04_03_Song_Playback`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Now Playing".
2.  **Component: Player UI**
    - **Name:** `Column`
    - **Position & Size:** `fillMaxSize`, padding `24dp`.
    - **Content:** Large album art, `Text` for title, `Text` for artist, `Slider` for progress, `Row` of player controls (prev, play/pause, next).
3.  **Component: Action Buttons**
    - **Name:** `Row`
    - **Position & Size:** Below player controls. `Arrangement.SpaceEvenly`.
    - **Content:**
        - `IconButton` with `Icons.Filled.Download`, Label "Download".
        - `IconButton` with `Icons.Filled.Share`, Label "Share".
        - `IconButton` with `Icons.Filled.Edit`, Label "Edit Lyrics".

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate back to `04_02_My_Music_Library`.
- **'Download' Button:** On tap -> Initiate download. Show `Snackbar` "Downloading...". Return to `04_02_My_Music_Library`.
- **'Share' Button:** On tap -> Open `04_06_System_Share_Sheet`.
- **'Edit Lyrics' Button:** On tap -> Navigate to `04_04_Lyrics_Editor`.

---

### 04_04_Lyrics_Editor
- **Screen Name/ID:** `04_04_Lyrics_Editor`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Edit Lyrics", Action `TextButton` "Save".
2.  **Component: Lyrics Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxSize`, padding `16dp`.
    - **Content:** The song's lyrics.
3.  **Component: Action Buttons**
    - **Name:** `Row`
    - **Position & Size:** Anchored to bottom, above keyboard.
    - **Content:** `FilledTonalButton` "Regenerate Lyrics", `FilledTonalButton` "Inspire Me".

#### Interaction & Behavior
- **Back/Cancel:** On tap -> Discard changes and navigate to `04_03_Song_Playback`.
- **'Save' Button:** On tap -> Save changes and navigate to `04_03_Song_Playback`.
- **'Regenerate Lyrics' Button:** On tap -> Show progress indicator, then replace text with new lyrics.
- **'Inspire Me' Button:** On tap -> Open `03_03_Inspire_Me_Overlay`.

---

### 04_05_Song_Options_Menu
- **Screen Name/ID:** `04_05_Song_Options_Menu`
- **Dimensions:** `fillMaxWidth`, height `wrap_content`.
- **Behavior:** `ModalBottomSheet`.

#### Components
1.  **Component: Menu Item List**
    - **Name:** `Column` of `ListItem`s
    - **Content:**
        - `ListItem` with Icon `Icons.Filled.Download`, Text "Download".
        - `ListItem` with Icon `Icons.Filled.Share`, Text "Share".
        - `ListItem` with Icon `Icons.Filled.Edit`, Text "Edit Lyrics".
        - `ListItem` with Icon `Icons.Filled.Delete`, Text "Delete" (color `md.sys.color.error`).

#### Interaction & Behavior
- **Download:** On tap -> Initiate download, dismiss sheet.
- **Share:** On tap -> Open `04_06_System_Share_Sheet`, dismiss sheet.
- **Edit Lyrics:** On tap -> Navigate to `04_04_Lyrics_Editor`, dismiss sheet.
- **Delete:** On tap -> Show confirmation dialog. On confirm, delete song and dismiss sheet.
- **Dismiss:** Tap outside or swipe down to dismiss.

---

### 04_06_System_Share_Sheet
- **Screen Name/ID:** `04_06_System_Share_Sheet`
- **Dimensions:** N/A (System UI)
- **Behavior:** Native Android share sheet.

#### Interaction & Behavior
- **Selects an app or cancels:** Returns to `04_03_Song_Playback`.

---

### Flow: Profile and Settings

---

### 06_02_Settings
- **Screen Name/ID:** `06_02_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Settings".
2.  **Component: Settings List**
    - **Name:** `LazyColumn`
    - **Content:**
        - `ListItem` "Account", navigates to `06_03_Account_Settings`.
        - `ListItem` "Notifications", navigates to `06_04_Notification_Settings`.
        - `ListItem` "Privacy Policy", navigates to `06_05_Web_View_Privacy_Policy`.
        - `ListItem` "Log Out", styled with `md.sys.color.error`.

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `02_04_Profile`.
- **Log Out:** On tap -> Show confirmation dialog. On confirm, navigate to `01_01_Welcome`.

---

### 06_03_Account_Settings
- **Screen Name/ID:** `06_03_Account_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Account Settings".
2.  **Component: Settings List**
    - **Name:** `LazyColumn`
    - **Content:** `ListItem`s for "Change Email", "Change Password", "Delete Account".

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `06_02_Settings`.

---

### 06_04_Notification_Settings
- **Screen Name/ID:** `06_04_Notification_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.ArrowBack`, Title `Text` "Notification Settings".
2.  **Component: Toggles List**
    - **Name:** `LazyColumn`
    - **Content:** `ListItem`s with a `Switch` as trailing content for "Song Ready", "Promotions", etc.

#### Interaction & Behavior
- **Back Arrow:** On tap -> Navigate to `06_02_Settings`.
- **Switch:** On toggle -> Update user preferences.

---

### 06_05_Web_View_Privacy_Policy
- **Screen Name/ID:** `06_05_Web_View_Privacy_Policy`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and a `WebView`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.Close`, Title `Text` "Privacy Policy".
2.  **Component: Web View**
    - **Name:** `WebView`
    - **Content:** Loads the privacy policy URL.

#### Interaction & Behavior
- **Close Icon:** On tap -> Navigate back to `06_02_Settings`.

---

### Flow: Monetization

---

### 07_01_Purchase_Credits
- **Screen Name/ID:** `07_01_Purchase_Credits`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.

#### Components
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** Navigation Icon `Icons.Filled.Close`, Title `Text` "Get More Credits".
2.  **Component: Credit Packs**
    - **Name:** `LazyColumn`
    - **Position & Size:** Padding `16dp`.
    - **Content:** A list of `Card`s, each representing a credit pack (e.g., "50 Credits - $4.99", "120 Credits - $9.99").

#### Interaction & Behavior
- **Close Icon:** On tap -> Navigate to `02_04_Profile`.
- **Credit Pack Card:** On tap -> Initiate purchase flow, navigate to `07_02_In_App_Purchase_Confirmation`.

---

### 07_02_In_App_Purchase_Confirmation
- **Screen Name/ID:** `07_02_In_App_Purchase_Confirmation`
- **Dimensions:** N/A (System UI)
- **Behavior:** Google Play Store purchase sheet.

#### Interaction & Behavior
- **Completes purchase:** Navigate to `07_03_Purchase_Successful`.
- **Cancels purchase:** Navigate back to `07_01_Purchase_Credits`.

---

### 07_03_Purchase_Successful
- **Screen Name/ID:** `07_03_Purchase_Successful`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` centered on screen.

#### Components
1.  **Component: Success Icon**
    - **Name:** `Icon`
    - **Content:** `Icons.Filled.CheckCircle`, size `80dp`, tint `md.sys.color.primary`.
2.  **Component: Success Text**
    - **Name:** `Text`
    - **Content:** "Purchase Successful!", style `md.sys.typography.headlineSmall`.
3.  **Component: Done Button**
    - **Name:** `FilledButton`
    - **Content:** "Done".

#### Interaction & Behavior
- **'Done' Button:** On tap -> Navigate to `02_04_Profile`.

---

### Flow: Permissions

---

### 08_03_Permission_Denied_Dialog
- **Screen Name/ID:** `08_03_Permission_Denied_Dialog`
- **Dimensions:** N/A (Dialog)
- **Behavior:** `AlertDialog`.

#### Components
1.  **Component: Alert Dialog**
    - **Icon:** `Icons.Outlined.Warning`
    - **Title:** "Permission Required"
    - **Text:** "To use this feature, please grant the required permissions in your device settings."
    - **Confirm Button:** `TextButton` "Go to Settings".
    - **Dismiss Button:** `TextButton` "Cancel".

#### Interaction & Behavior
- **'Go to Settings' Button:** On tap -> Navigate to `08_04_System_App_Settings`.
- **'Cancel' Button:** On tap -> Dismiss dialog and navigate to `02_01_Create_Home`.

---

### 08_04_System_App_Settings
- **Screen Name/ID:** `08_04_System_App_Settings`
- **Dimensions:** N/A (System UI)
- **Behavior:** The app's settings page within the Android OS settings.

#### Interaction & Behavior
- **User returns to app:** The app returns to the foreground, landing on `02_01_Create_Home`.

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
- **My Music - Library (`04_02_My_Music_Library`):**
  - **UI:** When no songs are saved, the `LazyColumn` is replaced with a centered `Column`.
  - **Layout:** `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.
  - **Content:**
    1.  `Icon`: `Icons.Outlined.MusicNote`, size `64dp`, tint `md.sys.color.onSurfaceVariant`.
    2.  `Text`: "Your library is empty", style `md.sys.typography.titleLarge`, margin top `16dp`.
    3.  `Text`: "Songs you create and save will appear here.", style `md.sys.typography.bodyMedium`, margin top `8dp`.
    4.  `FilledButton`: "Create your first song", margin top `24dp`. Navigates to `02_01_Create_Home`.

### Loading States
- **Initial Data Fetch (e.g., Library, Explore):**
  - **UI:** A full-screen `CircularProgressIndicator` is displayed centered within the screen's content area.
- **Button Loading State:**
  - **UI:** For actions like "Log In" or "Sign Up", the button's text is replaced by a `CircularProgressIndicator` (size `24dp`). The button is disabled.
- **Song Generation (`02_03_My_Music_Queue`):**
  - **UI:** A `ListItem` in the queue shows a `LinearProgressIndicator` to indicate ongoing generation.
- **Audio Processing (`03_10_Audio_Processing`):**
  - **UI:** A dedicated full-screen modal view with a large `CircularProgressIndicator` and descriptive text.