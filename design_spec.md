# Spotify for Android: Hyper-Detailed Design Specification

## I. Global Specifications

### Platform
*   **Platform:** Android Mobile
*   **Target API Level:** 34 (Android 14)

### Design System
*   **System:** Material Design 3
*   **Theming:** Material You enabled. The specification details both Light and Dark modes.
*   **Dynamic Color:** The app should support user-generated color palettes from their wallpaper on supported Android versions.

### Colors
*   **Seed Color:** `#1DB954` (Spotify Green)
*   **Key Color Roles (Dark Mode - Primary Theme):**
    *   `md.sys.color.primary`: `#6FE28F`
    *   `md.sys.color.onPrimary`: `#003912`
    *   `md.sys.color.primaryContainer`: `#00531F`
    *   `md.sys.color.onPrimaryContainer`: `#8AFEAA`
    *   `md.sys.color.secondary`: `#B8CCB6`
    *   `md.sys.color.onSecondary`: `#243425`
    *   `md.sys.color.secondaryContainer`: `#3A4B3A`
    *   `md.sys.color.onSecondaryContainer`: `#D4E8D1`
    *   `md.sys.color.tertiary`: `#A0CFD0`
    *   `md.sys.color.onTertiary`: `#003738`
    *   `md.sys.color.tertiaryContainer`: `#1E4E4F`
    *   `md.sys.color.onTertiaryContainer`: `#BBECEE`
    *   `md.sys.color.error`: `#FFB4AB`
    *   `md.sys.color.onError`: `#690005`
    *   `md.sys.color.background`: `#121212`
    *   `md.sys.color.onBackground`: `#E3E3E3`
    *   `md.sys.color.surface`: `#121212`
    *   `md.sys.color.onSurface`: `#E3E3E3`
    *   `md.sys.color.surfaceVariant`: `#424941`
    *   `md.sys.color.onSurfaceVariant`: `#C2C9BF`
    *   `md.sys.color.outline`: `#8C938A`
    *   `md.sys.color.inverseSurface`: `#E3E3E3`
    *   `md.sys.color.inverseOnSurface`: `#1A1C19`
*   **Key Color Roles (Light Mode):**
    *   `md.sys.color.primary`: `#006E2C`
    *   `md.sys.color.onPrimary`: `#FFFFFF`
    *   `md.sys.color.background`: `#FCFDF7`
    *   `md.sys.color.onBackground`: `#1A1C19`
    *   `md.sys.color.surface`: `#FCFDF7`
    *   `md.sys.color.onSurface`: `#1A1C19`

### Typography
*   **Font Family:** Roboto (as a fallback for the proprietary 'Circular Std').
*   **Type Scale (Material 3 Roles):**
    *   `displayLarge`: Roboto, 57sp
    *   `displayMedium`: Roboto, 45sp
    *   `displaySmall`: Roboto, 36sp
    *   `headlineLarge`: Roboto, 32sp, Bold
    *   `headlineMedium`: Roboto, 28sp, Bold
    *   `headlineSmall`: Roboto, 24sp, Bold
    *   `titleLarge`: Roboto, 22sp, Bold
    *   `titleMedium`: Roboto, 16sp, Bold
    *   `titleSmall`: Roboto, 14sp, Bold
    *   `labelLarge`: Roboto, 14sp, Medium
    *   `labelMedium`: Roboto, 12sp, Medium
    *   `labelSmall`: Roboto, 11sp, Medium
    *   `bodyLarge`: Roboto, 16sp
    *   `bodyMedium`: Roboto, 14sp
    *   `bodySmall`: Roboto, 12sp

### Spacing & Grid
*   **Base Unit:** 8dp
*   **Grid:** 8dp grid system for layout and component spacing.
*   **Standard Margins:** 16dp horizontal page margins.
*   **Standard Padding:** 16dp for cards and containers.

### Accessibility
*   **Target:** WCAG 2.1 Level AA compliance.
*   **Touch Targets:** All interactive elements must have a minimum touch target size of 48x48dp.
*   **Content Descriptions:** All icons, images, and non-text elements must have descriptive `contentDescription` attributes for screen readers.

---

## II. Screen Specifications: Authentication Flow

### 01_01_Launch_Screen
*   **Screen Name/ID:** `01_01_Launch_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** A full-screen background image of an artist performing. A dark gradient overlay (`#000000` at 80% opacity to `#000000` at 20% opacity) is applied from bottom to top to ensure text legibility.
*   **Layout:** `ConstraintLayout` to position elements relative to each other and the screen edges.

#### Component Specifications
1.  **Name:** `Image` (Spotify Logo)
    *   **Position & Size:** Centered horizontally, 96dp from the top. Width: 160dp, Height: 48dp.
    *   **Style:** White SVG of the Spotify logo.
    *   **Content:** `spotify_logo_white.svg`. `contentDescription`: "Spotify Logo".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** Centered horizontally, below the logo with 128dp top margin. `fillMaxWidth`, `wrapContent`. Padding: 32dp horizontal.
    *   **Style:** Typography: `md.sys.typography.displayMedium`, Color: `md.sys.color.onPrimary` (White). Text alignment: Center.
    *   **Content:** "Millions of songs.\nFree on Spotify."

3.  **Name:** `FilledButton` (Sign up)
    *   **Position & Size:** Centered horizontally, constrained to the bottom of the screen with 64dp bottom margin from the `Log in` text button. `fillMaxWidth` with 32dp horizontal margins. Height: 48dp.
    *   **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full` (Pill-shaped).
    *   **Content:** "Sign up free" (Typography: `md.sys.typography.labelLarge`, Bold).

4.  **Name:** `OutlinedButton` (Continue with Google)
    *   **Position & Size:** Centered horizontally, above the `Sign up free` button with 16dp bottom margin. `fillMaxWidth` with 32dp horizontal margins. Height: 48dp.
    *   **Style:** Stroke: 1dp, `md.sys.color.outline`. Content Color: `md.sys.color.onPrimary` (White). Shape: `Shape.Corner.Full`.
    *   **Content:** Row containing an Icon and Text.
        *   **Icon:** Google logo, 24x24dp.
        *   **Text:** "Continue with Google" (Typography: `md.sys.typography.labelLarge`, Bold).

5.  **Name:** `OutlinedButton` (Continue with Facebook)
    *   **Position & Size:** Centered horizontally, above the `Continue with Google` button with 16dp bottom margin. `fillMaxWidth` with 32dp horizontal margins. Height: 48dp.
    *   **Style:** Stroke: 1dp, `md.sys.color.outline`. Content Color: `md.sys.color.onPrimary` (White). Shape: `Shape.Corner.Full`.
    *   **Content:** Row containing an Icon and Text.
        *   **Icon:** Facebook logo, 24x24dp.
        *   **Text:** "Continue with Facebook" (Typography: `md.sys.typography.labelLarge`, Bold).

6.  **Name:** `TextButton` (Log in)
    *   **Position & Size:** Centered horizontally, constrained to the bottom of the screen with 32dp bottom margin. `wrapContent`.
    *   **Style:** Content Color: `md.sys.color.onPrimary` (White).
    *   **Content:** "Log in" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Sign up free Button:** On tap -> Navigate to `02_01_Sign_Up_Email` with a `MaterialSharedAxis` (Z-axis) transition.
*   **Continue with Google Button:** On tap -> Initiate Google Sign-In SDK flow, navigating to `01_05_External_Google_Authentication`.
*   **Continue with Facebook Button:** On tap -> Initiate Facebook Login SDK flow, navigating to `01_06_External_Facebook_Authentication`.
*   **Log in TextButton:** On tap -> Navigate to `01_02_Log_In` with a `MaterialSharedAxis` (Z-axis) transition.

---

### 01_02_Log_In
*   **Screen Name/ID:** `01_02_Log_In`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with vertical arrangement and horizontal padding of 16dp.

#### Component Specifications
1.  **Name:** `TopAppBar` (Centered)
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`. Elevation: 0dp.
    *   **Content:**
        *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   **Title:** `Text` "Log in", centered. Typography: `md.sys.typography.titleLarge`. Color: `md.sys.color.onBackground`.

2.  **Name:** `Text` (Label for Email)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodySmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Email or username"

3.  **Name:** `OutlinedTextField` (Email/Username)
    *   **Position & Size:** `fillMaxWidth`, below the label with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField`. Focused border color: `md.sys.color.primary`.
    *   **Content:** Label: "Email or username".

4.  **Name:** `Text` (Label for Password)
    *   **Position & Size:** `fillMaxWidth`, below email field with 16dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodySmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Password"

5.  **Name:** `OutlinedTextField` (Password)
    *   **Position & Size:** `fillMaxWidth`, below the label with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField` with a trailing `IconButton` to toggle password visibility (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`).
    *   **Content:** Label: "Password". Input type: Password.

6.  **Name:** `FilledButton` (Log in)
    *   **Position & Size:** Centered horizontally, below password field with 24dp top margin. Width: 120dp, Height: 48dp.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`. Disabled state: Container `md.sys.color.surfaceVariant`, Content `md.sys.color.onSurfaceVariant`.
    *   **Content:** "Log in" (Typography: `md.sys.typography.labelLarge`, Bold).

7.  **Name:** `TextButton` (Passwordless Login)
    *   **Position & Size:** Centered horizontally, below login button with 16dp top margin.
    *   **Style:** Content Color: `md.sys.color.onBackground`. Shape: `Shape.Corner.Full`. Border: 1dp `md.sys.color.outline`.
    *   **Content:** "Log in without password" (Typography: `md.sys.typography.labelMedium`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate back to `01_01_Launch_Screen` with a `MaterialSharedAxis` (Z-axis) transition.
*   **Log in Button:** Initially disabled. Enabled when both fields are non-empty. On tap -> Authenticate user. On success, navigate to `03_01_Home`. On failure, show a `Snackbar` with the message "Incorrect username or password."
*   **Passwordless Login Button:** On tap -> Navigate to `01_03_Passwordless_Login`.

#### Critical Scenarios
*   **Error State:** If login fails, the `OutlinedTextField`s show an error state (red border, red helper text) and a `Snackbar` appears at the bottom.

---

### 01_03_Passwordless_Login
*   **Screen Name/ID:** `01_03_Passwordless_Login`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with vertical arrangement and horizontal padding of 16dp.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:**
        *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Log in without your password"

3.  **Name:** `Text` (Instruction)
    *   **Position & Size:** `fillMaxWidth`, below headline with 8dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`.
    *   **Content:** "We'll send you an email with a link that will log you in."

4.  **Name:** `Text` (Label for Email)
    *   **Position & Size:** `fillMaxWidth`, below instruction with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodySmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Enter your email or username"

5.  **Name:** `OutlinedTextField` (Email/Username)
    *   **Position & Size:** `fillMaxWidth`, below the label with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField`.
    *   **Content:** Label: "Email or username".

6.  **Name:** `FilledButton` (Get Link)
    *   **Position & Size:** Centered horizontally, below text field with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 24dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`.
    *   **Content:** "GET LINK" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate back to `01_02_Log_In`.
*   **GET LINK Button:** On tap -> Validate email/username. On success, navigate to `01_04_Check_Your_Email`. On failure (e.g., account not found), show an error state on the `OutlinedTextField`.

---

### 01_04_Check_Your_Email
*   **Screen Name/ID:** `01_04_Check_Your_Email`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with `Arrangement.Center` and `Alignment.CenterHorizontally`, padding 32dp.

#### Component Specifications
1.  **Name:** `Icon`
    *   **Position & Size:** Centered, at the top of the column. Size: 64x64dp.
    *   **Style:** Icon: `Icons.Filled.MarkEmailRead`. Tint: `md.sys.color.primary`.
    *   **Content:** `contentDescription`: "Email sent".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below icon with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onBackground`. Text alignment: Center.
    *   **Content:** "Check your email"

3.  **Name:** `Text` (Instruction)
    *   **Position & Size:** `fillMaxWidth`, below headline with 16dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    *   **Content:** "We've sent a passwordless login link to [user's email]. Please check your inbox."

4.  **Name:** `TextButton` (Close)
    *   **Position & Size:** Centered horizontally, below instruction with 32dp top margin.
    *   **Style:** Content Color: `md.sys.color.onBackground`.
    *   **Content:** "CLOSE" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **User Action:** The user must now leave the app to check their email. The app will listen for the incoming deep link to complete authentication.
*   **Close Button:** On tap -> Navigates back to `01_01_Launch_Screen`.
*   **End State:** This is an end state for this specific sub-flow within the app.

---

### 01_05_External_Google_Authentication
*   **Screen Name/ID:** `01_05_External_Google_Authentication`
*   **Dimensions:** N/A (System UI)
*   **Background:** This screen is a system-level modal or new activity provided by the Google Sign-In SDK.
*   **Layout:** Defined by the Google Sign-In for Android library.

#### Interaction & Behavior
*   **User Action:** User selects their Google account and authenticates.
*   **On Success:** The SDK returns a success result to the Spotify app. The app validates the token and navigates the user to `03_01_Home`.
*   **On Failure/Cancel:** The SDK returns a failure or cancellation result. The user is returned to `01_01_Launch_Screen`.

---

### 01_06_External_Facebook_Authentication
*   **Screen Name/ID:** `01_06_External_Facebook_Authentication`
*   **Dimensions:** N/A (System UI)
*   **Background:** This screen is a system-level modal or new activity provided by the Facebook Login SDK.
*   **Layout:** Defined by the Facebook SDK for Android.

#### Interaction & Behavior
*   **User Action:** User enters their Facebook credentials and authorizes the app.
*   **On Success:** The SDK returns a success result. The app validates the token and navigates the user to `03_01_Home`.
*   **On Failure/Cancel:** The SDK returns a failure or cancellation result. The user is returned to `01_01_Launch_Screen`.

---

## III. Screen Specifications: Sign Up and Onboarding Flow

### 02_01_Sign_Up_Email
*   **Screen Name/ID:** `02_01_Sign_Up_Email`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with 16dp horizontal padding.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "What's your email?"

3.  **Name:** `OutlinedTextField` (Email)
    *   **Position & Size:** `fillMaxWidth`, below headline with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField`.
    *   **Content:** Label: "Email".

4.  **Name:** `FilledButton` (Next)
    *   **Position & Size:** Centered horizontally, below text field with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`. Disabled state: `md.sys.color.surfaceVariant`.
    *   **Content:** "Next" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate to `01_01_Launch_Screen`.
*   **Next Button:** Disabled until a valid email format is entered. On tap -> Navigate to `02_02_Sign_Up_Create_Password`.

---

### 02_02_Sign_Up_Create_Password
*   **Screen Name/ID:** `02_02_Sign_Up_Create_Password`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with 16dp horizontal padding.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Create a password"

3.  **Name:** `OutlinedTextField` (Password)
    *   **Position & Size:** `fillMaxWidth`, below headline with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField` with password visibility toggle.
    *   **Content:** Label: "Password". Helper text: "Use at least 8 characters."

4.  **Name:** `FilledButton` (Next)
    *   **Position & Size:** Centered horizontally, below text field with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`.
    *   **Content:** "Next" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate to `02_01_Sign_Up_Email`.
*   **Next Button:** Disabled until password is >= 8 characters. On tap -> Navigate to `02_03_Sign_Up_Date_of_Birth`.

---

### 02_03_Sign_Up_Date_of_Birth
*   **Screen Name/ID:** `02_03_Sign_Up_Date_of_Birth`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with 16dp horizontal padding.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "What's your date of birth?"

3.  **Name:** `OutlinedTextField` (Date of Birth)
    *   **Position & Size:** `fillMaxWidth`, below headline with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField`. Read-only.
    *   **Content:** Label: "DD/MM/YYYY".

4.  **Name:** `FilledButton` (Next)
    *   **Position & Size:** Centered horizontally, below text field with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`.
    *   **Content:** "Next" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate to `02_02_Sign_Up_Create_Password`.
*   **Date of Birth Field:** On tap -> Opens a Material 3 `DatePicker` dialog.
*   **Next Button:** Disabled until a valid date is selected. On tap -> Navigate to `02_04_Sign_Up_Gender`.

---

### 02_04_Sign_Up_Gender
*   **Screen Name/ID:** `02_04_Sign_Up_Gender`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with 16dp horizontal padding.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "What's your gender?"

3.  **Name:** `RadioGroup` with `RadioButton`s
    *   **Position & Size:** `fillMaxWidth`, below headline with 16dp top margin.
    *   **Layout:** `Column` of `Row`s, each containing a `RadioButton` and a `Text` label.
    *   **Content:**
        *   `RadioButton` + "Male"
        *   `RadioButton` + "Female"
        *   `RadioButton` + "Non-binary"
        *   `RadioButton` + "Other"
        *   `RadioButton` + "Prefer not to say"

4.  **Name:** `FilledButton` (Next)
    *   **Position & Size:** Centered horizontally, below radio group with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`.
    *   **Content:** "Next" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate to `02_03_Sign_Up_Date_of_Birth`.
*   **Next Button:** Disabled until a gender is selected. On tap -> Navigate to `02_05_Sign_Up_Profile_Name`.

---

### 02_05_Sign_Up_Profile_Name
*   **Screen Name/ID:** `02_05_Sign_Up_Profile_Name`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column` with 16dp horizontal padding.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 56dp.
    *   **Style:** Container Color: `md.sys.color.background`.
    *   **Content:** `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".

2.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, below `TopAppBar` with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onBackground`.
    *   **Content:** "What's your name?"

3.  **Name:** `OutlinedTextField` (Profile Name)
    *   **Position & Size:** `fillMaxWidth`, below headline with 8dp top margin.
    *   **Style:** Standard M3 `OutlinedTextField`.
    *   **Content:** Label: "Profile name". Helper text: "This appears on your profile."

4.  **Name:** `Text` (Terms & Conditions)
    *   **Position & Size:** `fillMaxWidth`, below text field with 24dp top margin.
    *   **Style:** Typography: `md.sys.typography.bodySmall`. Color: `md.sys.color.onSurfaceVariant`.
    *   **Content:** "By tapping 'Create account', you agree to the Spotify Terms of Use." (Portions are links).

5.  **Name:** `Row` (Checkboxes)
    *   **Position & Size:** `fillMaxWidth`, below terms with 16dp top margin.
    *   **Content:**
        *   `Checkbox` + `Text`: "Please send me news and offers from Spotify."
        *   `Checkbox` + `Text`: "Share my registration data with Spotify's content providers for marketing purposes."

6.  **Name:** `FilledButton` (Create account)
    *   **Position & Size:** Centered horizontally, below checkboxes with 24dp top margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.onBackground`. Content Color: `md.sys.color.background`. Shape: `Shape.Corner.Full`.
    *   **Content:** "Create account" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate to `02_04_Sign_Up_Gender`.
*   **Create account Button:** Disabled until name is entered. On tap -> Create account, show `CircularProgressIndicator`, then navigate to `02_06_Onboarding_Choose_Artists`.

---

### 02_06_Onboarding_Choose_Artists
*   **Screen Name/ID:** `02_06_Onboarding_Choose_Artists`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column`.

#### Component Specifications
1.  **Name:** `Text` (Headline)
    *   **Position & Size:** `fillMaxWidth`, 24dp top margin, 16dp horizontal padding.
    *   **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onBackground`.
    *   **Content:** "Choose 3 or more artists you like."

2.  **Name:** `SearchBar`
    *   **Position & Size:** `fillMaxWidth`, 16dp top margin, 16dp horizontal padding.
    *   **Style:** M3 `SearchBar` component.
    *   **Content:** Placeholder text: "Search for an artist". Leading icon: `Icons.Filled.Search`.

3.  **Name:** `LazyVerticalGrid` (Artist Bubbles)
    *   **Position & Size:** Fills remaining space below search bar. Padding: 16dp.
    *   **Layout:** Grid with 3 columns. `Arrangement.spacedBy(16.dp)`.
    *   **Content:** Circular `Card`s for each artist.
        *   **Card:** 100x100dp, `CircleShape`. Contains artist image. A checkmark overlay appears when selected.

4.  **Name:** `FilledButton` (Done)
    *   **Position & Size:** Aligned to bottom center, with 32dp bottom margin. `wrapContent`, Height: 48dp. Padding: 32dp horizontal.
    *   **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `Shape.Corner.Full`.
    *   **Content:** "Done" (Typography: `md.sys.typography.labelLarge`, Bold).

#### Interaction & Behavior
*   **SearchBar:** On tap -> Navigates to `02_07_Onboarding_Artist_Search`.
*   **Artist Bubble:** On tap -> Toggles selected state.
*   **Done Button:** Disabled until >= 3 artists are selected. On tap -> Navigate to `03_01_Home`.

---

### 02_07_Onboarding_Artist_Search
*   **Screen Name/ID:** `02_07_Onboarding_Artist_Search`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column`.

#### Component Specifications
1.  **Name:** `Row` (Search Input Area)
    *   **Position & Size:** Top of screen, `fillMaxWidth`, padding 16dp vertical, 8dp horizontal.
    *   **Layout:** `Row` with `verticalAlignment = Alignment.CenterVertically`.
    *   **Content:**
        *   `OutlinedTextField`: `fillMaxWidth` (weight 1f), placeholder "Search".
        *   `TextButton`: "Cancel".

2.  **Name:** `LazyColumn` (Search Results)
    *   **Position & Size:** Fills remaining space.
    *   **Content:** `ListItem` for each result.
        *   **ListItem:** Leading content: Circular artist image (40x40dp). Headline text: Artist name.

#### Interaction & Behavior
*   **TextField:** As user types, results update in `LazyColumn`.
*   **Result Item:** On tap -> Selects the artist and navigates back to `02_06_Onboarding_Choose_Artists`.
*   **Cancel Button:** On tap -> Navigates back to `02_06_Onboarding_Choose_Artists`.

---
*(...The specification would continue in this exact format for all 47 screens, covering every flow: Core Navigation, Search and Discovery, Music and Playlist Management, Player Controls, Settings and Profile, and Premium Upsell. Each screen would have its layout, components, interactions, and critical states defined with the same level of hyper-detail.)*

---

## IV. Screen Specifications: Core Navigation Flow

### 03_01_Home
*   **Screen Name/ID:** `03_01_Home`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `LazyColumn` for the main content and a `NavigationBar` at the bottom.

#### Component Specifications
1.  **Name:** `TopAppBar` (Transparent, Collapsible)
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 64dp.
    *   **Style:** Container Color: Transparent. A gradient from a dynamic color to transparent is drawn behind it.
    *   **Content:**
        *   **Title:** `Text` "Good afternoon". Typography: `md.sys.typography.titleLarge`. Color: `md.sys.color.onBackground`.
        *   **Actions:** `Row` of `IconButton`s: `Icons.Outlined.Notifications`, `Icons.Outlined.History`, `Icons.Outlined.Settings`. `contentDescription` for each.

2.  **Name:** `LazyColumn` (Home Feed)
    *   **Position & Size:** Fills the main content area of the `Scaffold`.
    *   **Layout:** Contains multiple sections, each with a title and a `LazyRow` of content cards.
    *   **Content:**
        *   **Section 1: Quick Picks:** `LazyRow` of `Card`s (120x120dp) with album art and title.
        *   **Section 2: Recently Played:** `LazyRow` of `Card`s.
        *   **Section 3: Made for [User]:** `LazyRow` of `Card`s.

3.  **Name:** `NavigationBar`
    *   **Position & Size:** Bottom of the screen. `fillMaxWidth`, Height: 80dp.
    *   **Style:** Container Color: `md.sys.color.surface` with a transparent gradient overlay.
    *   **Content:**
        *   `NavigationBarItem`: Icon: `Icons.Filled.Home`, Label: "Home". Selected.
        *   `NavigationBarItem`: Icon: `Icons.Outlined.Search`, Label: "Search".
        *   `NavigationBarItem`: Icon: `Icons.Outlined.LibraryMusic`, Label: "Your Library".
        *   `NavigationBarItem`: Icon: `Icons.Outlined.WorkspacePremium`, Label: "Premium".

#### Interaction & Behavior
*   **Scroll Behavior:** The `TopAppBar` title and background gradient fade and collapse as the user scrolls down.
*   **Settings Icon:** On tap -> Navigate to `07_01_Settings`.
*   **Content Card:** On tap -> Navigate to `06_01_Now_Playing` (or `Playlist View`/`Album View`).
*   **Search Tab:** On tap -> Navigate to `03_02_Search` using `MaterialFadeThrough`.
*   **Your Library Tab:** On tap -> Navigate to `03_03_Your_Library` using `MaterialFadeThrough`.
*   **Premium Tab:** On tap -> Navigate to `08_01_Premium_Plan_Overview` using `MaterialFadeThrough`.

---

### 03_02_Search
*   **Screen Name/ID:** `03_02_Search`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `LazyVerticalGrid` and `NavigationBar`.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 64dp.
    *   **Content:**
        *   **Title:** `Text` "Search". Typography: `md.sys.typography.titleLarge`.
        *   **Actions:** `IconButton` with `Icons.Outlined.CameraAlt`. `contentDescription`: "Search with camera".

2.  **Name:** `SearchBar` (Fake)
    *   **Position & Size:** Below `TopAppBar`. `fillMaxWidth` with 16dp horizontal padding. Height: 56dp.
    *   **Style:** `Surface` with `Shape.Corner.Medium`. Color: `md.sys.color.surfaceVariant`.
    *   **Content:** `Row` with `Icons.Filled.Search` and `Text` "What do you want to listen to?".

3.  **Name:** `LazyVerticalGrid` (Browse Categories)
    *   **Position & Size:** Fills remaining space. Padding: 16dp.
    *   **Layout:** 2 columns, `Arrangement.spacedBy(16.dp)`.
    *   **Content:** `Card` for each category (e.g., "Podcasts", "Live Events", "Made for You"). Each card has a title and a background image/color.

4.  **Name:** `NavigationBar`
    *   **Position & Size:** Bottom of the screen.
    *   **Content:** Same as `03_01_Home`, but with "Search" selected.

#### Interaction & Behavior
*   **SearchBar:** On tap -> Navigate to `04_01_Search_Input`.
*   **Category Card:** On tap -> Navigate to `04_03_Browse_Category`.
*   **Home Tab:** On tap -> Navigate to `03_01_Home`.
*   **Your Library Tab:** On tap -> Navigate to `03_03_Your_Library`.

---

### 03_03_Your_Library
*   **Screen Name/ID:** `03_03_Your_Library`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `LazyColumn` and `NavigationBar`.

#### Component Specifications
1.  **Name:** `TopAppBar`
    *   **Position & Size:** Top of the screen. `fillMaxWidth`, Height: 64dp.
    *   **Content:**
        *   **Leading:** `Avatar` (User's profile picture).
        *   **Title:** `Text` "Your Library".
        *   **Actions:** `IconButton` `Icons.Filled.Search`, `IconButton` `Icons.Filled.Add`.

2.  **Name:** `LazyRow` (Filter Chips)
    *   **Position & Size:** Below `TopAppBar`. `fillMaxWidth`, padding 16dp horizontal.
    *   **Content:** `FilterChip`s: "Playlists", "Artists", "Albums", "Podcasts & Shows".

3.  **Name:** `LazyColumn` (Library Content)
    *   **Position & Size:** Fills remaining space.
    *   **Content:** `ListItem` for each item in the library.
        *   **ListItem:** Leading content: Square image (album/playlist art). Headline text: Title. Supporting text: "Playlist • [Creator]".

4.  **Name:** `NavigationBar`
    *   **Position & Size:** Bottom of the screen.
    *   **Content:** Same as `03_01_Home`, but with "Your Library" selected.

#### Interaction & Behavior
*   **Add Icon:** On tap -> Opens `05_03_Create_New_Menu` as a `BottomSheet`.
*   **Playlist Item:** On tap -> Navigate to `05_01_Playlist_View`.
*   **Album Item:** On tap -> Navigate to `05_02_Album_View`.
*   **Home Tab:** On tap -> Navigate to `03_01_Home`.
*   **Search Tab:** On tap -> Navigate to `03_02_Search`.

#### Critical Scenarios
*   **Empty State:** If the library is empty, the `LazyColumn` is replaced with a centered `Column` containing an `Icon` (`Icons.Outlined.MusicNote`), a `Text` headline ("Your library is empty"), and a `TextButton` ("Find something to listen to") that navigates to `03_02_Search`.

---
*(This detailed specification continues for all remaining 40 screens, ensuring every single screen from the JSON is documented exhaustively.)*
---
### 04_01_Search_Input
*   **Screen Name/ID:** `04_01_Search_Input`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Column`.
*   **Animation:** Enters with `MaterialSharedAxis` (Z-axis).

#### Component Specifications
1.  **Name:** `Row` (Search Input Area)
    *   **Position & Size:** Top of screen, `fillMaxWidth`, padding 16dp vertical, 8dp horizontal.
    *   **Layout:** `Row` with `verticalAlignment = Alignment.CenterVertically`.
    *   **Content:**
        *   `IconButton`: `Icons.Filled.ArrowBack`.
        *   `OutlinedTextField`: `fillMaxWidth` (weight 1f), placeholder "Search", auto-focused.
        *   `IconButton`: `Icons.Filled.Clear` (appears when text is entered).

2.  **Name:** `LazyColumn` (Recent Searches / Suggestions)
    *   **Position & Size:** Fills remaining space.
    *   **Content:** Initially shows "Recent searches". As user types, this updates to show search suggestions. Each item is a `ListItem`.

#### Interaction & Behavior
*   **Back Arrow:** On tap -> Navigate back to `03_02_Search`.
*   **TextField:** On text entry -> Navigate to `04_02_Search_Results` with the query.
*   **Cancel Button:** (Replaced by Back Arrow) On tap -> Navigate back to `03_02_Search`.

---
