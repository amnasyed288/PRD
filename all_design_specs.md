# Combined Android Design Specifications



============================================================
## APP 1: App_1
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Mint: Budget & Expense Tracker - Android Design Specification

This document provides a complete and hyper-detailed design specification for the Mint Android application, based on the provided app flow tree. It is intended to be used by an AI design generation model to create a high-fidelity, interactive prototype.

## I. Global Specifications

### Platform
- **Target Platform:** Android Mobile App
- **API Level:** Target API 34 (Android 14)

### Design System
- **System:** Material Design 3
- **Theming:** Supports Light and Dark modes. Implements dynamic color (Material You) where available, falling back to the defined brand theme.
- **Density:** Default screen density.

### Colors
- **Seed Color:** `#008445` (Mint Green)
- **Light Theme Color Roles:**
  - `md.sys.color.primary`: `#006C45`
  - `md.sys.color.onPrimary`: `#FFFFFF`
  - `md.sys.color.primaryContainer`: `#8BF8BE`
  - `md.sys.color.onPrimaryContainer`: `#002112`
  - `md.sys.color.secondary`: `#4D6356`
  - `md.sys.color.onSecondary`: `#FFFFFF`
  - `md.sys.color.secondaryContainer`: `#D0E8D8`
  - `md.sys.color.onSecondaryContainer`: `#0A1F15`
  - `md.sys.color.tertiary`: `#3D6473`
  - `md.sys.color.onTertiary`: `#FFFFFF`
  - `md.sys.color.tertiaryContainer`: `#C0E9FB`
  - `md.sys.color.onTertiaryContainer`: `#001F28`
  - `md.sys.color.error`: `#BA1A1A`
  - `md.sys.color.onError`: `#FFFFFF`
  - `md.sys.color.errorContainer`: `#FFDAD6`
  - `md.sys.color.onErrorContainer`: `#410002`
  - `md.sys.color.background`: `#FBFDF9`
  - `md.sys.color.onBackground`: `#191C1A`
  - `md.sys.color.surface`: `#FBFDF9`
  - `md.sys.color.onSurface`: `#191C1A`
  - `md.sys.color.surfaceVariant`: `#DDE5DE`
  - `md.sys.color.onSurfaceVariant`: `#414943`
  - `md.sys.color.outline`: `#717973`
  - `md.sys.color.inverseSurface`: `#2E312F`
  - `md.sys.color.inverseOnSurface`: `#F0F1ED`
- **Dark Theme Color Roles:**
  - `md.sys.color.primary`: `#6FDBA4`
  - `md.sys.color.onPrimary`: `#003822`
  - `md.sys.color.primaryContainer`: `#005233`
  - `md.sys.color.onPrimaryContainer`: `#8BF8BE`
  - `md.sys.color.secondary`: `#B4CCBC`
  - `md.sys.color.onSecondary`: `#203529`
  - `md.sys.color.secondaryContainer`: `#364B3F`
  - `md.sys.color.onSecondaryContainer`: `#D0E8D8`
  - `md.sys.color.tertiary`: `#A5CDDE`
  - `md.sys.color.onTertiary`: `#073542`
  - `md.sys.color.tertiaryContainer`: `#244C5A`
  - `md.sys.color.onTertiaryContainer`: `#C0E9FB`
  - `md.sys.color.error`: `#FFB4AB`
  - `md.sys.color.onError`: `#690005`
  - `md.sys.color.errorContainer`: `#93000A`
  - `md.sys.color.onErrorContainer`: `#FFDAD6`
  - `md.sys.color.background`: `#191C1A`
  - `md.sys.color.onBackground`: `#E1E3DF`
  - `md.sys.color.surface`: `#191C1A`
  - `md.sys.color.onSurface`: `#E1E3DF`
  - `md.sys.color.surfaceVariant`: `#414943`
  - `md.sys.color.onSurfaceVariant`: `#C1C9C2`
  - `md.sys.color.outline`: `#8B938C`
  - `md.sys.color.inverseSurface`: `#E1E3DF`
  - `md.sys.color.inverseOnSurface`: `#191C1A`

### Typography
- **Font Family:** Roboto
- **Type Scale Roles:**
  - `md.sys.typography.displayLarge`: `Roboto Regular, 57sp`
  - `md.sys.typography.displayMedium`: `Roboto Regular, 45sp`
  - `md.sys.typography.displaySmall`: `Roboto Regular, 36sp`
  - `md.sys.typography.headlineLarge`: `Roboto Regular, 32sp`
  - `md.sys.typography.headlineMedium`: `Roboto Regular, 28sp`
  - `md.sys.typography.headlineSmall`: `Roboto Regular, 24sp`
  - `md.sys.typography.titleLarge`: `Roboto Regular, 22sp`
  - `md.sys.typography.titleMedium`: `Roboto Medium, 16sp, Letter Spacing 0.15`
  - `md.sys.typography.titleSmall`: `Roboto Medium, 14sp, Letter Spacing 0.1`
  - `md.sys.typography.labelLarge`: `Roboto Medium, 14sp, Letter Spacing 0.1`
  - `md.sys.typography.labelMedium`: `Roboto Medium, 12sp, Letter Spacing 0.5`
  - `md.sys.typography.labelSmall`: `Roboto Medium, 11sp, Letter Spacing 0.5`
  - `md.sys.typography.bodyLarge`: `Roboto Regular, 16sp, Letter Spacing 0.5`
  - `md.sys.typography.bodyMedium`: `Roboto Regular, 14sp, Letter Spacing 0.25`
  - `md.sys.typography.bodySmall`: `Roboto Regular, 12sp, Letter Spacing 0.4`

### Spacing & Sizing
- **Base Grid Unit:** 8dp
- **Standard Padding:** 16dp
- **Standard Margins:** 16dp
- **Minimum Touch Target:** 48dp x 48dp

### Accessibility
- **Target Standard:** WCAG 2.1 Level AA
- **Requirements:**
  - All interactive elements must have a minimum touch target of 48x48dp.
  - Text contrast ratios must meet AA standards.
  - All images and icons that convey information must have content descriptions.
  - Form fields must have clear labels.

### Animations
- **Default Screen Transition:** `MaterialSharedAxis` (X-axis for forward/backward, Z-axis for top-level).
- **Dialog Transition:** `MaterialFade`.
- **Component Motion:** Standard Material 3 motion specs (e.g., easing, duration).

---

## II. Screen Specifications

### Flow 1: Authentication

---

#### Screen 1.1: App Launch Screen
- **Screen Name/ID:** `01_01_App_Launch_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, centered vertically and horizontally.
- **Component Specifications:**
  - **Name:** `Image` (App Logo)
    - **Position & Size:** Centered horizontally. Width: 120dp, Height: 120dp.
    - **Style:** No tint.
    - **Content:** Mint app logo vector.
  - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered horizontally. Margin top: 32dp. Size: 48dp x 48dp.
    - **Style:** Color: `md.sys.color.primary`. Stroke width: 4dp.
    - **Content:** N/A.
- **Interaction & Behavior:**
  - **Interactions:** On successful initialization/authentication check, the app automatically navigates.
  - **Navigation:** `On load complete -> Navigate to 01_02_Sign_Up_or_Sign_In_Screen` (if not logged in) or `03_01_Overview_Screen` (if logged in).
  - **Animations:** `MaterialFade` transition.

---

#### Screen 1.2: Sign Up or Sign In Screen
- **Screen Name/ID:** `01_02_Sign_Up_or_Sign_In_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout with `verticalArrangement = Arrangement.SpaceBetween`. Padding: 16dp on all sides.
- **Component Specifications:**
  - **Name:** `Image` (App Logo)
    - **Position & Size:** Aligned to top-center. Margin top: 64dp. Width: 96dp, Height: 96dp.
    - **Style:** No tint.
    - **Content:** Mint app logo vector.
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "Welcome to Mint"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "The #1 personal finance app"
  - **Name:** `Column` (Button Container)
    - **Position & Size:** Aligned to bottom-center. Margin bottom: 32dp.
    - **Layout:** `Column` with `verticalArrangement = Arrangement.spacedBy(16dp)`.
    - **Components:**
      - **Name:** `FilledButton` (Create Account)
        - **Position & Size:** `fillMaxWidth()`. Height: 52dp.
        - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
        - **Content:** Text label: "Create an account" with style `md.sys.typography.labelLarge`.
      - **Name:** `FilledTonalButton` (Sign In)
        - **Position & Size:** `fillMaxWidth()`. Height: 52dp.
        - **Style:** Container Color: `md.sys.color.secondaryContainer`. Content Color: `md.sys.color.onSecondaryContainer`. Shape: `ShapeDefaults.Full`.
        - **Content:** Text label: "Sign In" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton` (Create Account): `On tap -> Navigate to 02_01_Create_Account_Email_Screen`.
    - `FilledTonalButton` (Sign In): `On tap -> Navigate to 01_03_Sign_In_Screen`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 1.3: Sign In Screen
- **Screen Name/ID:** `01_03_Sign_In_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`. `scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior()`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Sign In" and style `md.sys.typography.titleLarge`.
  - **Name:** `OutlinedTextField` (User ID)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. Colors: Default `OutlinedTextField` colors.
    - **Content:** Label: "User ID". `singleLine = true`. `keyboardType = KeyboardType.Text`.
  - **Name:** `OutlinedTextField` (Password)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `visualTransformation = PasswordVisualTransformation()`. Trailing icon: `IconButton` to toggle password visibility.
    - **Content:** Label: "Password". `singleLine = true`. `keyboardType = KeyboardType.Password`.
  - **Name:** `FilledButton` (Sign In)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Initially disabled until both fields are non-empty.
    - **Content:** Text label: "Sign In" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Forgot Password)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Forgot your user ID or password?" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **States:** `FilledButton` is disabled (`containerColor` is `md.sys.color.onSurface` with 0.12 alpha, `contentColor` is `md.sys.color.onSurface` with 0.38 alpha) until both text fields are valid.
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 01_02_Sign_Up_or_Sign_In_Screen`.
    - `FilledButton`: `On tap -> Navigate to 01_04_Two_Factor_Authentication_Screen`.
    - `TextButton`: `On tap -> Navigate to 01_05_Password_Recovery_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 1.4: Two-Factor Authentication Screen
- **Screen Name/ID:** `01_04_Two_Factor_Authentication_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 24dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Verify Your Identity" and style `md.sys.typography.titleLarge`.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "For your security, please enter the 6-digit code we sent to your registered device."
  - **Name:** `OutlinedTextField` (Verification Code)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Text align: Center. `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword)`.
    - **Content:** Label: "Verification Code".
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until input length is 6.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Resend Code)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Didn't get a code? Resend" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `TextButton`: `On tap -> Show Snackbar with "New code sent" message. Stay on 01_04_Two_Factor_Authentication_Screen`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 1.5: Password Recovery Screen
- **Screen Name/ID:** `01_05_Password_Recovery_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Account Recovery" and style `md.sys.typography.titleLarge`.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`.
    - **Content:** "Enter the email or phone number associated with your account to receive recovery instructions."
  - **Name:** `OutlinedTextField` (Email or Phone)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`.
    - **Content:** Label: "Email or Phone Number". `singleLine = true`.
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until field is non-empty.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 01_03_Sign_In_Screen`.
    - `FilledButton`: `On tap -> Navigate to 01_06_Password_Recovery_Instructions_Sent_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 1.6: Password Recovery Instructions Sent Screen
- **Screen Name/ID:** `01_06_Password_Recovery_Instructions_Sent_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout, `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`. Padding: 24dp.
- **Component Specifications:**
  - **Name:** `Icon`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** `imageVector = Icons.Filled.MarkEmailRead`. Tint: `md.sys.color.primary`.
    - **Content:** Content description: "Email sent".
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "Check Your Inbox"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "We've sent password recovery instructions to your email address. Please follow the link to reset your password."
  - **Name:** `FilledButton` (Back to Sign In)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Back to Sign In" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 01_03_Sign_In_Screen`.
  - **Animations:** `MaterialFade` transition.

---

### Flow 2: Account Creation and Onboarding

---

#### Screen 2.1: Create Account - Email Screen
- **Screen Name/ID:** `02_01_Create_Account_Email_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Create Account (1/4)" and style `md.sys.typography.titleLarge`.
  - **Name:** `LinearProgressIndicator`
    - **Position & Size:** Below `TopAppBar`. `fillMaxWidth()`.
    - **Style:** Color: `md.sys.color.primary`. Progress: 0.25.
    - **Content:** N/A.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "What's your email address?"
  - **Name:** `OutlinedTextField` (Email)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `keyboardType = KeyboardType.Email`.
    - **Content:** Label: "Email Address". `singleLine = true`.
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until email is valid.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 01_02_Sign_Up_or_Sign_In_Screen`.
    - `FilledButton`: `On tap -> Navigate to 02_02_Create_Account_User_ID_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.2: Create Account - User ID Screen
- **Screen Name/ID:** `02_02_Create_Account_User_ID_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Create Account (2/4)" and style `md.sys.typography.titleLarge`.
  - **Name:** `LinearProgressIndicator`
    - **Position & Size:** Below `TopAppBar`. `fillMaxWidth()`.
    - **Style:** Color: `md.sys.color.primary`. Progress: 0.50.
    - **Content:** N/A.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "Create a User ID"
  - **Name:** `OutlinedTextField` (User ID)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`.
    - **Content:** Label: "User ID". `singleLine = true`. Helper text: "Must be at least 6 characters."
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until User ID is valid.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_01_Create_Account_Email_Screen`.
    - `FilledButton`: `On tap -> Navigate to 02_03_Create_Account_Phone_Number_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.3: Create Account - Phone Number Screen
- **Screen Name/ID:** `02_03_Create_Account_Phone_Number_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Create Account (3/4)" and style `md.sys.typography.titleLarge`.
  - **Name:** `LinearProgressIndicator`
    - **Position & Size:** Below `TopAppBar`. `fillMaxWidth()`.
    - **Style:** Color: `md.sys.color.primary`. Progress: 0.75.
    - **Content:** N/A.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "What's your phone number?"
  - **Name:** `OutlinedTextField` (Phone Number)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `keyboardType = KeyboardType.Phone`.
    - **Content:** Label: "Phone Number". `singleLine = true`.
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until phone number is valid.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_02_Create_Account_User_ID_Screen`.
    - `FilledButton`: `On tap -> Navigate to 02_04_Create_Account_Password_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.4: Create Account - Password Screen
- **Screen Name/ID:** `02_04_Create_Account_Password_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Create Account (4/4)" and style `md.sys.typography.titleLarge`.
  - **Name:** `LinearProgressIndicator`
    - **Position & Size:** Below `TopAppBar`. `fillMaxWidth()`.
    - **Style:** Color: `md.sys.color.primary`. Progress: 1.0.
    - **Content:** N/A.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "Create a secure password"
  - **Name:** `OutlinedTextField` (Password)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". `singleLine = true`. Helper text: "8+ characters, 1 uppercase, 1 number."
  - **Name:** `OutlinedTextField` (Confirm Password)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Confirm Password". `singleLine = true`.
  - **Name:** `FilledButton` (Create account)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until passwords are valid and match.
    - **Content:** Text label: "Create account" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_03_Create_Account_Phone_Number_Screen`.
    - `FilledButton`: `On tap -> Navigate to 02_05_Phone_Verification_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.5: Phone Verification Screen
- **Screen Name/ID:** `02_05_Phone_Verification_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 24dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Verify Your Phone" and style `md.sys.typography.titleLarge`.
  - **Name:** `Text` (Instruction)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "Please enter the 6-digit code we sent to your phone number to finish setting up your account."
  - **Name:** `OutlinedTextField` (Verification Code)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Text align: Center. `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.NumberPassword)`.
    - **Content:** Label: "Verification Code".
  - **Name:** `FilledButton` (Continue)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until input length is 6.
    - **Content:** Text label: "Continue" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 02_06_Onboarding_Connect_Account_Intro_Screen`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 2.6: Onboarding - Connect Account Intro Screen
- **Screen Name/ID:** `02_06_Onboarding_Connect_Account_Intro_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout, `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`. Padding: 24dp.
- **Component Specifications:**
  - **Name:** `Icon`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** `imageVector = Icons.Filled.AccountBalance`. Tint: `md.sys.color.primary`.
    - **Content:** Content description: "Bank account".
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "See your full financial picture"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "Connect your bank accounts to automatically track your spending, budgets, and net worth."
  - **Name:** `FilledButton` (Connect an account)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Connect an account" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Skip for now)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Skip for now" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 02_07_Search_For_Institution_Screen`.
    - `TextButton`: `On tap -> Navigate to 03_01_Overview_Screen`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 2.7: Search For Institution Screen
- **Screen Name/ID:** `02_07_Search_For_Institution_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Close".
      - **Title:** `Text` with content "Connect an account" and style `md.sys.typography.titleLarge`.
  - **Name:** `OutlinedTextField` (Search)
    - **Position & Size:** `fillMaxWidth()`. Padding: 16dp horizontally, 8dp vertically.
    - **Style:** Shape: `ShapeDefaults.Full`. Leading icon: `Icons.Filled.Search`.
    - **Content:** Placeholder text: "Search for your bank".
  - **Name:** `LazyColumn` (Institutions List)
    - **Position & Size:** `fillMaxWidth()`. Fills remaining space.
    - **Content:**
      - `ListSubheader`: `Text` with content "Popular Institutions".
      - `ListItem` (for each popular institution):
        - **Leading Content:** `Image` of the institution's logo (e.g., Chase, Bank of America). Size: 40dp x 40dp.
        - **Headline Content:** `Text` with the institution's name (e.g., "Chase Bank"). Style: `md.sys.typography.bodyLarge`.
        - **Trailing Content:** `Icon` with `Icons.Filled.ChevronRight`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_06_Onboarding_Connect_Account_Intro_Screen`.
    - `ListItem`: `On tap -> Navigate to 02_08_Institution_Login_Screen`.
    - `OutlinedTextField`: As user types, the `LazyColumn` content updates with search results.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.8: Institution Login Screen
- **Screen Name/ID:** `02_08_Institution_Login_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** This screen is primarily a `WebView` container for a third-party service like Plaid.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with the selected institution's name (e.g., "Chase Bank") and style `md.sys.typography.titleLarge`.
  - **Name:** `WebView`
    - **Position & Size:** Fills the remaining space below the `TopAppBar`.
    - **Content:** Loads the Plaid Link interface for the user to enter their banking credentials securely.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_07_Search_For_Institution_Screen`.
    - `WebView`: User interacts with the Plaid interface. `On successful submission -> Navigate to 02_09_Connecting_Account_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.9: Connecting Account Screen
- **Screen Name/ID:** `02_09_Connecting_Account_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout, `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`. Padding: 24dp.
- **Component Specifications:**
  - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** Color: `md.sys.color.primary`. Stroke width: 5dp.
    - **Content:** N/A.
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 32dp.
    - **Style:** Typography: `md.sys.typography.titleLarge`. Color: `md.sys.color.onSurface`.
    - **Content:** "Connecting your account..."
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`.
    - **Content:** "This may take a moment. Please don't close the app."
- **Interaction & Behavior:**
  - **Interactions:** This is a transient screen. `On connection success -> Navigate to 02_10_Account_Connected_Success_Screen`.
  - **Animations:** `MaterialFade` transition.

---

#### Screen 2.10: Account Connected Success Screen
- **Screen Name/ID:** `02_10_Account_Connected_Success_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout, `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`. Padding: 24dp.
- **Component Specifications:**
  - **Name:** `Icon`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** `imageVector = Icons.Filled.CheckCircle`. Tint: `md.sys.color.primary`.
    - **Content:** Content description: "Success".
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "Account Connected!"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "We've successfully linked your account. Your transactions will now appear in Mint."
  - **Name:** `FilledButton` (Done)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Done" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 03_01_Overview_Screen`.
  - **Animations:** `MaterialFade` transition.

---

### Flow 3: Main Navigation

---

#### Screen 3.1: Overview Screen
- **Screen Name/ID:** `03_01_Overview_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`. `scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()`.
    - **Content:**
      - **Title:** `Text` with content "Overview" and style `md.sys.typography.titleLarge`.
      - **Actions:** `IconButton` with `Icons.Filled.Settings`. Content description: "Settings".
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp horizontal.
    - **Content:** A series of `Card` components for different modules.
      - **Card 1 (Net Worth):** `ElevatedCard` with `Text` "Net Worth", a large `Text` with amount (e.g., "$50,432.10"), and a small chart.
      - **Card 2 (Spending):** `FilledCard` with `Text` "This Month's Spending", a progress bar, and `Text` showing amount spent vs. budget.
      - **Card 3 (Recent Transactions):** `OutlinedCard` with a header `Row` containing `Text` "Recent Transactions" and a `TextButton` "See all". Below the header, a list of 3-4 `ListItem` components for each transaction.
  - **Name:** `BottomAppBar`
    - **Position & Size:** Bottom of the screen. `fillMaxWidth()`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** `NavigationBar` with 4 `NavigationBarItem`s:
      - **Item 1:** `selected = true`. Icon: `Icons.Filled.Home`. Label: "Overview".
      - **Item 2:** `selected = false`. Icon: `Icons.Outlined.CalendarMonth`. Label: "Monthly".
      - **Item 3:** `selected = false`. Icon: `Icons.Outlined.Storefront`. Label: "Marketplace".
      - **Item 4:** `selected = false`. Icon: `Icons.Outlined.Notifications`. Label: "Updates".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Settings IconButton`: `On tap -> Navigate to 03_05_Settings_Screen`.
    - `See all TextButton`: `On tap -> Navigate to 04_01_All_Transactions_Screen`.
    - `Transaction ListItem`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen`.
    - `Monthly NavigationBarItem`: `On tap -> Navigate to 03_02_Monthly_Budgets_Screen`.
    - `Marketplace NavigationBarItem`: `On tap -> Navigate to 03_03_Marketplace_Screen`.
    - `Updates NavigationBarItem`: `On tap -> Navigate to 03_04_Updates_Screen`.
  - **Animations:** `MaterialFadeThrough` for bottom navigation changes. `MaterialSharedAxis.Z` for navigating to Settings.

---

#### Screen 3.2: Monthly Budgets Screen
- **Screen Name/ID:** `03_02_Monthly_Budgets_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Monthly Budgets" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `Card` showing overall budget summary (e.g., "Left to spend").
      - `ListSubheader` with `Text` "Budgets".
      - A list of `ListItem`s for each budget category (e.g., "Shopping", "Groceries"). Each item shows the category name, a `LinearProgressIndicator` for spending, and text like "$150 of $500".
  - **Name:** `FloatingActionButton` (FAB)
    - **Position & Size:** Bottom right corner, overlapping `BottomAppBar`.
    - **Style:** Container Color: `md.sys.color.primaryContainer`. Content Color: `md.sys.color.onPrimaryContainer`.
    - **Content:** Icon: `Icons.Filled.Add`. Content description: "Create a budget".
  - **Name:** `BottomAppBar`
    - **Position & Size:** Bottom of the screen.
    - **Content:** `NavigationBar` with "Monthly" selected.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Overview NavigationBarItem`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `FAB`: `On tap -> Navigate to 05_01_Create_Budget_Select_Category_Screen`.
    - `Budget ListItem`: `On tap -> Navigate to 05_03_Budget_Detail_Screen`.
  - **Animations:** `MaterialFadeThrough` for bottom navigation changes.

---

#### Screen 3.3: Marketplace Screen
- **Screen Name/ID:** `03_03_Marketplace_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Marketplace" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:** A list of `Card` components, each representing an offer (e.g., "Find a better credit card", "Lower your loan payments"). Each card has an image, headline, and a short description.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Overview NavigationBarItem`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `Offer Card`: `On tap -> Navigate to 07_01_Offer_Detail_Screen`.
  - **Animations:** `MaterialFadeThrough` for bottom navigation changes.

---

#### Screen 3.4: Updates Screen
- **Screen Name/ID:** `03_04_Updates_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Updates" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area.
    - **Content:** A list of `ListItem`s, each representing a notification or update.
      - **Leading Content:** `Icon` relevant to the update (e.g., `Icons.Filled.Warning` for a bill due).
      - **Headline Content:** `Text` with the update title (e.g., "Upcoming Bill").
      - **Supporting Content:** `Text` with a short description and timestamp.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Overview NavigationBarItem`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `Update ListItem`: `On tap -> Navigate to 07_02_Update_Detail_Screen`.
  - **Animations:** `MaterialFadeThrough` for bottom navigation changes.

---

#### Screen 3.5: Settings Screen
- **Screen Name/ID:** `03_05_Settings_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Settings" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area.
    - **Content:** A series of `ListItem`s for settings options.
      - `ListItem` 1: Leading Icon `Icons.Filled.AccountBalance`, Headline `Text` "Accounts".
      - `ListItem` 2: Leading Icon `Icons.Filled.Notifications`, Headline `Text` "Notifications".
      - `ListItem` 3: Leading Icon `Icons.Filled.Person`, Headline `Text` "Profile".
      - `Divider`
      - `ListItem` 4: Leading Icon `Icons.Filled.Logout`, Headline `Text` "Sign Out", Color `md.sys.color.error`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `Accounts ListItem`: `On tap -> Navigate to 06_01_Accounts_List_Screen`.
    - `Notifications ListItem`: `On tap -> Navigate to 06_04_Notification_Settings_Screen`.
    - `Profile ListItem`: `On tap -> Navigate to 06_05_Profile_Screen`.
    - `Sign Out ListItem`: `On tap -> Show 06_07_Sign_Out_Confirmation_Dialog`.
  - **Animations:** `MaterialSharedAxis.X` for back navigation.

---

### Flow 4: Manage Transactions

---

#### Screen 4.1: All Transactions Screen
- **Screen Name/ID:** `04_01_All_Transactions_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "All Transactions" and style `md.sys.typography.titleLarge`.
      - **Actions:** `IconButton` with `Icons.Filled.FilterList`. Content description: "Filter".
  - **Name:** `LazyColumn` (Transactions List)
    - **Position & Size:** Fills the content area.
    - **Content:** Grouped by date.
      - `ListSubheader`: `Text` with date (e.g., "October 29, 2025").
      - `ListItem` for each transaction:
        - **Leading Content:** `Icon` for the category (e.g., `Icons.Filled.ShoppingCart`).
        - **Headline Content:** `Text` with merchant name.
        - **Supporting Content:** `Text` with category name.
        - **Trailing Content:** `Text` with amount (e.g., "-$45.50"). Color is `md.sys.color.error` for debits, `md.sys.color.primary` for credits.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_01_Overview_Screen`.
    - `Filter IconButton`: `On tap -> Navigate to 04_05_Filter_Transactions_Screen`.
    - `Transaction ListItem`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 4.2: Transaction Detail Screen
- **Screen Name/ID:** `04_02_Transaction_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Transaction Details" and style `md.sys.typography.titleLarge`.
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:** A series of `ListItem`s for details.
      - `ListItem` (Description): Headline `Text` "Description", Supporting `Text` "Starbucks".
      - `ListItem` (Amount): Headline `Text` "Amount", Supporting `Text` "-$5.75".
      - `ListItem` (Category): Headline `Text` "Category", Supporting `Text` "Coffee Shops", Trailing `Icon` `Icons.Filled.ChevronRight`.
      - `ListItem` (Date): Headline `Text` "Date", Supporting `Text` "October 29, 2025".
      - `ListItem` (Account): Headline `Text` "Account", Supporting `Text` "Chase Freedom (...1234)".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 04_01_All_Transactions_Screen`.
    - `Description ListItem`: `On tap -> Navigate to 04_04_Edit_Transaction_Description_Screen`.
    - `Category ListItem`: `On tap -> Navigate to 04_03_Edit_Transaction_Category_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 4.3: Edit Transaction - Category Screen
- **Screen Name/ID:** `04_03_Edit_Transaction_Category_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Cancel".
      - **Title:** `Text` with content "Edit Category" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Done".
  - **Name:** `LazyColumn` (Categories List)
    - **Position & Size:** Fills the content area.
    - **Content:** `ListItem`s for each category, grouped by parent category. The selected category has a `RadioButton` or checkmark.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Close IconButton`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen` (without saving).
    - `Done TextButton`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen` (with saved changes).
    - `Category ListItem`: Selects the category.
  - **Animations:** `MaterialSharedAxis.Y` (modal-like).

---

#### Screen 4.4: Edit Transaction - Description Screen
- **Screen Name/ID:** `04_04_Edit_Transaction_Description_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Cancel".
      - **Title:** `Text` with content "Edit Description" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Save".
  - **Name:** `OutlinedTextField` (Description)
    - **Position & Size:** `fillMaxWidth()`. Padding: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`.
    - **Content:** Label: "Description". Pre-filled with current description.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Close IconButton`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen` (without saving).
    - `Save TextButton`: `On tap -> Navigate to 04_02_Transaction_Detail_Screen` (with saved changes).
  - **Animations:** `MaterialSharedAxis.Y` (modal-like).

---

#### Screen 4.5: Filter Transactions Screen
- **Screen Name/ID:** `04_05_Filter_Transactions_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Close".
      - **Title:** `Text` with content "Filters" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Reset".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `ExposedDropdownMenuBox` for "Account".
      - `ExposedDropdownMenuBox` for "Category".
      - `DateRangePicker` input field.
  - **Name:** `FilledButton` (Apply Filters)
    - **Position & Size:** `fillMaxWidth()`. Aligned to bottom. Margin: 16dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Apply Filters".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Close IconButton`: `On tap -> Navigate to 04_01_All_Transactions_Screen`.
    - `Apply Filters Button`: `On tap -> Navigate to 04_01_All_Transactions_Screen` (with filters applied).
  - **Animations:** Full-screen dialog transition.

---

### Flow 5: Manage Budgets

---

#### Screen 5.1: Create Budget - Select Category Screen
- **Screen Name/ID:** `05_01_Create_Budget_Select_Category_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Select a Category" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Categories List)
    - **Position & Size:** Fills the content area.
    - **Content:** `ListItem`s for each available spending category (e.g., "Shopping", "Restaurants", "Gas & Fuel").
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_02_Monthly_Budgets_Screen`.
    - `Category ListItem`: `On tap -> Navigate to 05_02_Create_Budget_Set_Amount_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 5.2: Create Budget - Set Amount Screen
- **Screen Name/ID:** `05_02_Create_Budget_Set_Amount_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Set Budget Amount" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Save".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 24dp. `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Content:**
      - `Text` with the selected category name (e.g., "Shopping"). Style: `md.sys.typography.titleMedium`.
      - `OutlinedTextField` (Amount)
        - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
        - **Style:** `keyboardType = KeyboardType.Decimal`. Prefix: `Text` with "$".
        - **Content:** Label: "Budget Amount".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 05_01_Create_Budget_Select_Category_Screen`.
    - `Save TextButton`: `On tap -> Navigate to 03_02_Monthly_Budgets_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 5.3: Budget Detail Screen
- **Screen Name/ID:** `05_03_Budget_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with budget category name (e.g., "Shopping") and style `md.sys.typography.titleLarge`.
      - **Actions:** `IconButton` with `Icons.Filled.Edit`. Content description: "Edit Budget".
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area.
    - **Content:**
      - **Header Section (not in LazyColumn):** A `Column` with padding 16dp showing a large circular progress indicator, `Text` "Amount Spent", and `Text` "$150 of $500".
      - `ListSubheader`: `Text` with "Transactions in this budget".
      - `ListItem`s for each transaction in this category (same format as All Transactions screen).
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_02_Monthly_Budgets_Screen`.
    - `Edit IconButton`: `On tap -> Navigate to 05_04_Edit_Budget_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 5.4: Edit Budget Screen
- **Screen Name/ID:** `05_04_Edit_Budget_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Cancel".
      - **Title:** `Text` with content "Edit Budget" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Save".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `OutlinedTextField` (Amount) - same as Set Amount screen.
      - `OutlinedButton` (Delete Budget)
        - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
        - **Style:** Border color: `md.sys.color.error`. Content color: `md.sys.color.error`.
        - **Content:** Text label: "Delete Budget".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Close IconButton`: `On tap -> Navigate to 05_03_Budget_Detail_Screen`.
    - `Save TextButton`: `On tap -> Navigate to 05_03_Budget_Detail_Screen`.
    - `Delete Budget Button`: `On tap -> Show 05_05_Delete_Budget_Confirmation_Dialog`.
  - **Animations:** `MaterialSharedAxis.Y` (modal-like).

---

#### Screen 5.5: Delete Budget Confirmation Dialog
- **Screen Name/ID:** `05_05_Delete_Budget_Confirmation_Dialog`
- **Dimensions:** Dialog, typically 280dp width.
- **Background:** `md.sys.color.surface` with elevation.
- **Layout:** `AlertDialog` component.
- **Component Specifications:**
  - **Name:** `AlertDialog`
    - **Style:** Shape: `ShapeDefaults.ExtraLarge`.
    - **Content:**
      - **Icon:** `Icon` with `Icons.Filled.DeleteForever`, tint `md.sys.color.error`.
      - **Title:** `Text` with content "Delete Budget?".
      - **Text:** `Text` with content "This action cannot be undone. Are you sure you want to delete this budget?".
      - **Confirm Button:** `TextButton` with text "Delete".
      - **Dismiss Button:** `TextButton` with text "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Delete Button`: `On tap -> Dismiss dialog, Navigate to 03_02_Monthly_Budgets_Screen`.
    - `Cancel Button`: `On tap -> Dismiss dialog, Stay on 05_04_Edit_Budget_Screen`.
  - **Animations:** `MaterialFade`.

---

### Flow 6: Settings and Profile Management

---

#### Screen 6.1: Accounts List Screen
- **Screen Name/ID:** `06_01_Accounts_List_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `FAB`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Accounts" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Accounts List)
    - **Position & Size:** Fills the content area.
    - **Content:** `ListItem`s for each connected account.
      - **Leading Content:** `Image` of institution logo.
      - **Headline Content:** `Text` with account name (e.g., "Chase Freedom").
      - **Supporting Content:** `Text` with last 4 digits and current balance.
  - **Name:** `FloatingActionButton` (FAB)
    - **Position & Size:** Bottom right corner.
    - **Style:** Container Color: `md.sys.color.primaryContainer`. Content Color: `md.sys.color.onPrimaryContainer`.
    - **Content:** Icon: `Icons.Filled.Add`. Content description: "Add account".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_05_Settings_Screen`.
    - `Account ListItem`: `On tap -> Navigate to 06_02_Account_Detail_Screen`.
    - `FAB`: `On tap -> Navigate to 02_07_Search_For_Institution_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 6.2: Account Detail Screen
- **Screen Name/ID:** `06_02_Account_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with account name and style `md.sys.typography.titleLarge`.
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `ListItem`s showing account details (Nickname, Account Number, Balance).
      - `OutlinedButton` (Delete Account)
        - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp.
        - **Style:** Border color: `md.sys.color.error`. Content color: `md.sys.color.error`.
        - **Content:** Text label: "Delete Account".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 06_01_Accounts_List_Screen`.
    - `Delete Account Button`: `On tap -> Show 06_03_Delete_Account_Confirmation_Dialog`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 6.3: Delete Account Confirmation Dialog
- **Screen Name/ID:** `06_03_Delete_Account_Confirmation_Dialog`
- **Dimensions:** Dialog, typically 280dp width.
- **Background:** `md.sys.color.surface` with elevation.
- **Layout:** `AlertDialog` component.
- **Component Specifications:**
  - **Name:** `AlertDialog`
    - **Style:** Shape: `ShapeDefaults.ExtraLarge`.
    - **Content:**
      - **Icon:** `Icon` with `Icons.Filled.Warning`, tint `md.sys.color.error`.
      - **Title:** `Text` with content "Delete Account?".
      - **Text:** `Text` with content "This will remove the account and all its transactions from Mint. This action cannot be undone.".
      - **Confirm Button:** `TextButton` with text "Delete".
      - **Dismiss Button:** `TextButton` with text "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Delete Button`: `On tap -> Dismiss dialog, Navigate to 06_01_Accounts_List_Screen`.
    - `Cancel Button`: `On tap -> Dismiss dialog, Stay on 06_02_Account_Detail_Screen`.
  - **Animations:** `MaterialFade`.

---

#### Screen 6.4: Notification Settings Screen
- **Screen Name/ID:** `06_04_Notification_Settings_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Notifications" and style `md.sys.typography.titleLarge`.
  - **Name:** `LazyColumn` (Settings List)
    - **Position & Size:** Fills the content area.
    - **Content:** `ListItem`s for each notification type.
      - `ListItem` (e.g., "Bill Reminders"):
        - **Headline Content:** `Text` "Bill Reminders".
        - **Supporting Content:** `Text` "Get notified when bills are due".
        - **Trailing Content:** `Switch` component.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_05_Settings_Screen`.
    - `Switch`: `On toggle -> Update setting. Stay on 06_04_Notification_Settings_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 6.5: Profile Screen
- **Screen Name/ID:** `06_05_Profile_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Profile" and style `md.sys.typography.titleLarge`.
      - **Actions:** `IconButton` with `Icons.Filled.Edit`. Content description: "Edit Profile".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:** `ListItem`s showing user info.
      - `ListItem`: Headline `Text` "Name", Supporting `Text` "Jane Doe".
      - `ListItem`: Headline `Text` "Email", Supporting `Text` "jane.doe@email.com".
      - `ListItem`: Headline `Text` "Phone", Supporting `Text` "(555) 123-4567".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_05_Settings_Screen`.
    - `Edit IconButton`: `On tap -> Navigate to 06_06_Edit_Profile_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 6.6: Edit Profile Screen
- **Screen Name/ID:** `06_06_Edit_Profile_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Cancel".
      - **Title:** `Text` with content "Edit Profile" and style `md.sys.typography.titleLarge`.
      - **Actions:** `TextButton` with text "Save".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `OutlinedTextField` for "Name".
      - `OutlinedTextField` for "Email".
      - `OutlinedTextField` for "Phone".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Close IconButton`: `On tap -> Navigate to 06_05_Profile_Screen`.
    - `Save TextButton`: `On tap -> Navigate to 06_05_Profile_Screen`.
  - **Animations:** `MaterialSharedAxis.Y` (modal-like).

---

#### Screen 6.7: Sign Out Confirmation Dialog
- **Screen Name/ID:** `06_07_Sign_Out_Confirmation_Dialog`
- **Dimensions:** Dialog, typically 280dp width.
- **Background:** `md.sys.color.surface` with elevation.
- **Layout:** `AlertDialog` component.
- **Component Specifications:**
  - **Name:** `AlertDialog`
    - **Style:** Shape: `ShapeDefaults.ExtraLarge`.
    - **Content:**
      - **Title:** `Text` with content "Sign Out?".
      - **Text:** `Text` with content "Are you sure you want to sign out?".
      - **Confirm Button:** `TextButton` with text "Sign Out".
      - **Dismiss Button:** `TextButton` with text "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Sign Out Button`: `On tap -> Dismiss dialog, Navigate to 01_02_Sign_Up_or_Sign_In_Screen`.
    - `Cancel Button`: `On tap -> Dismiss dialog, Stay on 03_05_Settings_Screen`.
  - **Animations:** `MaterialFade`.

---

### Flow 7: Placeholder Screens for Navigation

---

#### Screen 7.1: Offer Detail Screen
- **Screen Name/ID:** `07_01_Offer_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with content "Offer Details" and style `md.sys.typography.titleLarge`.
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `Image` for the offer.
      - `Text` headline.
      - `Text` body with detailed information.
      - `FilledButton` with "Learn More" or "Apply Now".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_03_Marketplace_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 7.2: Update Detail Screen
- **Screen Name/ID:** `07_02_Update_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
      - **Title:** `Text` with update title and style `md.sys.typography.titleLarge`.
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:**
      - `Text` headline.
      - `Text` body with detailed information about the update.
      - `TextButton` for any relevant action (e.g., "View Transaction").
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 03_04_Updates_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

## V. Critical Scenarios & States

### Error States
- **No Internet Connection:**
  - **UI:** A `Snackbar` appears at the bottom of the screen.
  - **Style:** Container color `md.sys.color.inverseSurface`, content color `md.sys.color.inverseOnSurface`.
  - **Content:** Message: "No internet connection." Action label: "Retry".
  - **Behavior:** The "Retry" action re-attempts the last network request. The Snackbar can be swiped away to be dismissed.
- **Input Validation Error:**
  - **UI:** `OutlinedTextField` components will show an error state.
  - **Style:** The outline, label, and helper text turn to `md.sys.color.error`. A leading error icon (`Icons.Filled.Error`) appears.
  - **Content:** Helper text changes to describe the error (e.g., "Please enter a valid email address").
- **API Error:**
  - **UI:** A `Snackbar` appears with a generic error message.
  - **Content:** Message: "Something went wrong. Please try again."

### Empty States
- **Applies to:** `All Transactions Screen`, `Monthly Budgets Screen`, `Updates Screen`.
- **Layout:** `Column` layout, centered vertically and horizontally. Padding: 32dp.
- **Components:**
  - **Name:** `Icon`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** Tint: `md.sys.color.secondary`. Icon varies by screen (e.g., `Icons.Outlined.ReceiptLong` for transactions).
    - **Content:** Content description provided.
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.titleLarge`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** Example: "No transactions yet".
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** Example: "Connect an account to see your transactions here."
  - **Name:** `FilledButton` (Primary CTA)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Standard filled button style.
    - **Content:** Example: "Connect Account".

### Loading States
- **Initial Screen Load:**
  - **UI:** A centered `CircularProgressIndicator` is displayed over the screen content area while data is being fetched.
  - **Style:** Color: `md.sys.color.primary`. Size: 48dp x 48dp.
- **In-Progress Action:**
  - **UI:** For actions like connecting an account or saving data, a `LinearProgressIndicator` appears at the top of the screen, just below the `TopAppBar`.
  - **Style:** Indeterminate. Color: `md.sys.color.primary`.
- **Button Loading:**
  - **UI:** When a button triggers an async action, the button text is replaced by a `CircularProgressIndicator` (sized appropriately, e.g., 24dp) and the button is disabled.
```

---


============================================================
## APP 2: App_2
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Android Design Specification: Wallet: Budget & Expense Tracker

This document provides a complete and hyper-detailed design specification for the "Wallet: Budget & Expense Tracker" Android application. It is intended to be used by an AI design generation model to create a high-fidelity, interactive prototype.

## I. Global Specifications

### Platform
- **Platform:** Android Mobile App
- **Target SDK:** 34+

### Design System
- **System:** Material Design 3
- **Dynamic Color:** Enabled (Material You). The specified colors serve as the baseline for users with dynamic color disabled.
- **Modes:** Light and Dark themes are supported. All color roles are defined for both.

### Colors
- **Seed Color:** #4CAF50 (A trustworthy green for finance)
- **Key Color Roles (Light Theme):**
  - **Primary:** #386A20
  - **On Primary:** #FFFFFF
  - **Primary Container:** #B7F397
  - **On Primary Container:** #042100
  - **Secondary:** #55624C
  - **On Secondary:** #FFFFFF
  - **Secondary Container:** #D9E7CB
  - **On Secondary Container:** #131F0D
  - **Tertiary:** #386666
  - **On Tertiary:** #FFFFFF
  - **Tertiary Container:** #BBEBEB
  - **On Tertiary Container:** #002020
  - **Error:** #BA1A1A
  - **On Error:** #FFFFFF
  - **Error Container:** #FFDAD6
  - **On Error Container:** #410002
  - **Background:** #FCFDF6
  - **On Background:** #1A1C18
  - **Surface:** #FCFDF6
  - **On Surface:** #1A1C18
  - **Surface Variant:** #DFE4D7
  - **On Surface Variant:** #43483F
  - **Outline:** #73796E
  - **Outline Variant:** #C3C8BC
- **Key Color Roles (Dark Theme):**
  - **Primary:** #9CD67E
  - **On Primary:** #0A3900
  - **Primary Container:** #1F5107
  - **On Primary Container:** #B7F397
  - **Secondary:** #BDCBAF
  - **On Secondary:** #283420
  - **Secondary Container:** #3E4A35
  - **On Secondary Container:** #D9E7CB
  - **Tertiary:** #A0CFCF
  - **On Tertiary:** #003737
  - **Tertiary Container:** #1E4E4E
  - **On Tertiary Container:** #BBEBEB
  - **Error:** #FFB4AB
  - **On Error:** #690005
  - **Error Container:** #93000A
  - **On Error Container:** #FFDAD6
  - **Background:** #1A1C18
  - **On Background:** #E2E3DC
  - **Surface:** #1A1C18
  - **On Surface:** #E2E3DC
  - **Surface Variant:** #43483F
  -  **On Surface Variant:** #C3C8BC
  - **Outline:** #8D9387
  - **Outline Variant:** #43483F

### Typography
- **Font Family:** Roboto
- **Type Scale Roles:**
  - **Display Large:** 57sp
  - **Display Medium:** 45sp
  - **Display Small:** 36sp
  - **Headline Large:** 32sp
  - **Headline Medium:** 28sp
  - **Headline Small:** 24sp
  - **Title Large:** 22sp
  - **Title Medium:** 16sp, Letter Spacing 0.15
  - **Title Small:** 14sp, Letter Spacing 0.1
  - **Label Large:** 14sp, Letter Spacing 0.1
  - **Label Medium:** 12sp, Letter Spacing 0.5
  - **Label Small:** 11sp, Letter Spacing 0.5
  - **Body Large:** 16sp, Letter Spacing 0.5
  - **Body Medium:** 14sp, Letter Spacing 0.25
  - **Body Small:** 12sp, Letter Spacing 0.4

### Spacing
- **Base Grid Unit:** 8dp
- **Standard Padding:** 16dp
- **Standard Margins:** 16dp
- **Minimum Touch Target:** 48dp x 48dp

### Accessibility
- **Target Standard:** WCAG 2.1 Level AA
- **Requirements:** All interactive elements must have content descriptions. Color contrast ratios must meet the standard. Font sizes should be scalable with system settings.

---

## II. Screen Specifications

### Flow 1: Authentication and Onboarding

---

#### Screen 1.1: Welcome Screen
- **Screen Name/ID:** `01_01_Welcome_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.SpaceBetween`, `horizontalAlignment = Alignment.CenterHorizontally`, and padding of 24dp.

##### Components:
1.  **Component: App Logo & Title**
    - **Name:** `Column`
    - **Position & Size:** Top-center of the screen. `padding(top = 64dp)`.
    - **Layout:** Contains an `Icon` and a `Text` element.
    - **Component 1.1: App Logo**
        - **Name:** `Icon`
        - **Position & Size:** 72dp x 72dp.
        - **Style:** `icon = Icons.Filled.AccountBalanceWallet`, `tint = md.sys.color.primary`.
    - **Component 1.2: App Name Text**
        - **Name:** `Text`
        - **Position & Size:** `padding(top = 16dp)`.
        - **Style:** `typography = md.sys.typography.headlineMedium`, `color = md.sys.color.onSurface`.
        - **Content:** "Welcome to Wallet"
    - **Component 1.3: Subtitle Text**
        - **Name:** `Text`
        - **Position & Size:** `padding(top = 8dp)`.
        - **Style:** `typography = md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = TextAlign.Center`.
        - **Content:** "Your personal finance manager."

2.  **Component: Action Buttons Group**
    - **Name:** `Column`
    - **Position & Size:** Bottom-center of the screen. `padding(bottom = 32dp)`. `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Component 2.1: Google Sign-In Button**
        - **Name:** `FilledTonalButton`
        - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `minTouchTarget = 48x48dp`. `margin(bottom = 16dp)`.
        - **Style:** `containerColor = md.sys.color.surfaceContainerHighest`, `contentColor = md.sys.color.onSurface`. Shape is `ShapeDefaults.Medium`.
        - **Content:** `Row` containing a Google logo `Icon` and `Text`.
            - **Icon:** Google logo, 24x24dp.
            - **Text:** "Continue with Google", `typography = md.sys.typography.labelLarge`. `padding(start = 12dp)`.
    - **Component 2.2: Facebook Sign-In Button**
        - **Name:** `FilledTonalButton`
        - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `minTouchTarget = 48x48dp`. `margin(bottom = 16dp)`.
        - **Style:** `containerColor = #1877F2`, `contentColor = #FFFFFF`. Shape is `ShapeDefaults.Medium`.
        - **Content:** `Row` containing a Facebook logo `Icon` and `Text`.
            - **Icon:** Facebook logo, 24x24dp.
            - **Text:** "Continue with Facebook", `typography = md.sys.typography.labelLarge`. `padding(start = 12dp)`.
    - **Component 2.3: Email Sign-In Button**
        - **Name:** `FilledButton`
        - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `minTouchTarget = 48x48dp`.
        - **Style:** `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`. Shape is `ShapeDefaults.Medium`.
        - **Content:** "Continue with email", `typography = md.sys.typography.labelLarge`.

##### Interaction & Behavior:
- **Google Button:** On tap -> Navigate to `02_01_Dashboard` (simulating successful social login). Animation: `MaterialSharedAxis(Z)`.
- **Facebook Button:** On tap -> Navigate to `02_01_Dashboard` (simulating successful social login). Animation: `MaterialSharedAxis(Z)`.
- **Email Button:** On tap -> Navigate to `01_02_Sign_Up_with_Email`. Animation: `MaterialSharedAxis(X)`.
- **States:** All buttons show a `0.12` opacity `onSurface` color overlay when pressed (state layer).

---

#### Screen 1.2: Sign Up with Email
- **Screen Name/ID:** `01_02_Sign_Up_with_Email`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`. Content is a `Column` with vertical padding of 16dp and horizontal padding of 24dp.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Sign Up". `typography = md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `width = fillMaxWidth`, `margin(top = 24dp)`.
    - **Style:** `label = { Text("Email") }`, `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Email)`.
    - **Content:** User-entered email address.

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `width = fillMaxWidth`, `margin(top = 16dp)`.
    - **Style:** `label = { Text("Password") }`, `visualTransformation = PasswordVisualTransformation()`, `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Password)`.
    - **Content:** User-entered password.

4.  **Component: Sign Up Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 32dp)`.
    - **Style:** `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
    - **Content:** "Sign up", `typography = md.sys.typography.labelLarge`.

5.  **Component: Login Link**
    - **Name:** `Row`
    - **Position & Size:** Centered horizontally, `margin(top = 24dp)`.
    - **Content:**
        - **Text 1:** "Already have an account? " `color = md.sys.color.onSurfaceVariant`, `typography = md.sys.typography.bodyMedium`.
        - **Text 2 (Clickable):** "Log in" `color = md.sys.color.primary`, `typography = md.sys.typography.bodyMedium`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `01_01_Welcome_Screen`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Sign Up Button:** On tap -> Validate fields. If valid, navigate to `01_04_Onboarding_Set_Currency`. Animation: `MaterialSharedAxis(X)`.
- **'Log in' Link:** On tap -> Navigate to `01_03_Login_Screen`. Animation: `MaterialFadeThrough`.

---

#### Screen 1.3: Login Screen
- **Screen Name/ID:** `01_03_Login_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar`. Content is a `Column` with vertical padding of 16dp and horizontal padding of 24dp.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Log In". `typography = md.sys.typography.titleLarge`.

2.  **Component: Email Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `width = fillMaxWidth`, `margin(top = 24dp)`.
    - **Style:** `label = { Text("Email") }`.
    - **Content:** User-entered email address.

3.  **Component: Password Text Field**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `width = fillMaxWidth`, `margin(top = 16dp)`.
    - **Style:** `label = { Text("Password") }`, `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** User-entered password.

4.  **Component: Log In Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 32dp)`.
    - **Style:** `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
    - **Content:** "Log in", `typography = md.sys.typography.labelLarge`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `01_02_Sign_Up_with_Email`. Animation: `MaterialFadeThrough`.
- **Log In Button:** On tap -> Validate fields. If valid, navigate to `02_01_Dashboard`. Animation: `MaterialSharedAxis(Z)`.

---

#### Screen 1.4: Onboarding - Set Currency
- **Screen Name/ID:** `01_04_Onboarding_Set_Currency`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar` and a `FilledButton` at the bottom. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Title:** `Text` with content "What's your main currency?". `typography = md.sys.typography.titleLarge`.

2.  **Component: Currency List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the space between the `TopAppBar` and the bottom button. `padding(horizontal = 16dp)`.
    - **Content:** A list of `ListItem` components for each currency.
    - **ListItem Component:**
        - **Name:** `ListItem`
        - **Layout:** `Row` with `verticalAlignment = Alignment.CenterVertically`.
        - **Content:**
            - **Headline Text:** Currency name (e.g., "United States Dollar"). `typography = md.sys.typography.bodyLarge`.
            - **Supporting Text:** Currency code (e.g., "USD"). `typography = md.sys.typography.bodyMedium`.
            - **Trailing Content:** `RadioButton` to indicate selection.
        - **Style:** `colors = ListItemDefaults.colors(containerColor = Color.Transparent)`.

3.  **Component: Next Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of the screen, `width = fillMaxWidth`, `height = 52dp`. `padding(16dp)`.
    - **Style:** Initially disabled. Enabled once a currency is selected.
    - **Content:** "Next", `typography = md.sys.typography.labelLarge`.

##### Interaction & Behavior:
- **Currency ListItem:** On tap -> Selects the associated `RadioButton`. Enables the "Next" button.
- **Next Button:** On tap -> Navigate to `01_05_Onboarding_Create_First_Account`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 1.5: Onboarding - Create First Account
- **Screen Name/ID:** `01_05_Onboarding_Create_First_Account`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with a `TopAppBar` and a bottom button. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Create your first account". `typography = md.sys.typography.titleLarge`.

2.  **Component: Content Column**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - **Account Name Field:** `OutlinedTextField`, `width = fillMaxWidth`, `label = { Text("Account name") }`, `placeholder = { Text("e.g., Cash, Bank Account") }`.
        - **Account Balance Field:** `OutlinedTextField`, `width = fillMaxWidth`, `margin(top = 16dp)`, `label = { Text("Current balance") }`, `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)`.

3.  **Component: Next Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of the screen, `width = fillMaxWidth`, `height = 52dp`. `padding(16dp)`.
    - **Style:** Enabled when both fields are non-empty.
    - **Content:** "Next", `typography = md.sys.typography.labelLarge`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `01_04_Onboarding_Set_Currency`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Next Button:** On tap -> Navigate to `01_06_Onboarding_Connect_Bank_Prompt`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 1.6: Onboarding - Connect Bank Prompt
- **Screen Name/ID:** `01_06_Onboarding_Connect_Bank_Prompt`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding(24dp)`.

##### Components:
1.  **Component: Illustration**
    - **Name:** `Icon`
    - **Position & Size:** 120dp x 120dp.
    - **Style:** `icon = Icons.Outlined.SyncAlt`, `tint = md.sys.color.primary`.

2.  **Component: Headline Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 32dp)`.
    - **Style:** `typography = md.sys.typography.headlineSmall`, `textAlign = TextAlign.Center`.
    - **Content:** "Automate your tracking"

3.  **Component: Body Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 16dp)`.
    - **Style:** `typography = md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = TextAlign.Center`.
    - **Content:** "Connect your bank account to automatically sync transactions and always stay up-to-date."

4.  **Component: Connect Bank Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 32dp)`.
    - **Content:** "Connect bank"

5.  **Component: Maybe Later Button**
    - **Name:** `TextButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 8dp)`.
    - **Content:** "Maybe later"

##### Interaction & Behavior:
- **Connect Bank Button:** On tap -> Navigate to `03_03_Connect_a_Bank`. Animation: `MaterialSharedAxis(X)`.
- **Maybe Later Button:** On tap -> Navigate to `01_07_Onboarding_Complete`. Animation: `MaterialFadeThrough`.

---

#### Screen 1.7: Onboarding - Complete
- **Screen Name/ID:** `01_07_Onboarding_Complete`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding(24dp)`.

##### Components:
1.  **Component: Illustration**
    - **Name:** `Icon`
    - **Position & Size:** 120dp x 120dp.
    - **Style:** `icon = Icons.Outlined.CheckCircleOutline`, `tint = md.sys.color.primary`.

2.  **Component: Headline Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 32dp)`.
    - **Style:** `typography = md.sys.typography.headlineSmall`, `textAlign = TextAlign.Center`.
    - **Content:** "You're all set!"

3.  **Component: Body Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 16dp)`.
    - **Style:** `typography = md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = TextAlign.Center`.
    - **Content:** "You are ready to start managing your finances. Let's make it happen."

4.  **Component: Let's Go Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 32dp)`.
    - **Content:** "Let's go!"

##### Interaction & Behavior:
- **Let's Go Button:** On tap -> Navigate to `02_01_Dashboard`. Animation: `MaterialSharedAxis(Z)`.

---
### Flow 2: Add Record

---

#### Screen 2.1: Dashboard
- **Screen Name/ID:** `02_01_Dashboard`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `FloatingActionButton`, and `BottomAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`. `scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()`.
    - **Content:**
        - **Title:** `Text` with content "Dashboard".
        - **Actions:** `IconButton` with `Icons.Filled.Notifications`.

2.  **Component: Main Content**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the screen area. `padding(horizontal = 16dp)`.
    - **Content:** Placeholder for dashboard widgets like "Total Balance", "Recent Transactions", "Spending by Category". (Detailed widget specs omitted for brevity as they are not part of the flow tree).

3.  **Component: Floating Action Button**
    - **Name:** `LargeFloatingActionButton`
    - **Position & Size:** Bottom right, inside the `Scaffold`.
    - **Style:** `containerColor = md.sys.color.primaryContainer`, `contentColor = md.sys.color.onPrimaryContainer`.
    - **Content:** `Icon` with `Icons.Filled.Add`.

4.  **Component: Bottom Navigation Bar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the screen.
    - **Style:** `containerColor = md.sys.color.surfaceContainer`.
    - **Content:**
        - `NavigationBarItem` (Selected): `icon = Icons.Filled.Dashboard`, `label = { Text("Dashboard") }`.
        - `NavigationBarItem`: `icon = Icons.Outlined.AccountBalanceWallet`, `label = { Text("Accounts") }`.
        - `NavigationBarItem`: `icon = Icons.Outlined.DonutLarge`, `label = { Text("Budgets") }`.
        - `NavigationBarItem`: `icon = Icons.Outlined.Flag`, `label = { Text("Goals") }`.
        - `NavigationBarItem`: `icon = Icons.Outlined.MoreHoriz`, `label = { Text("More") }`.

##### Interaction & Behavior:
- **FAB:** On tap -> Navigate to `02_02_Add_Record`. Animation: `MaterialContainerTransform`.
- **Bottom Nav Items:** See Flow 5 for navigation details.

---

#### Screen 2.2: Add Record
- **Screen Name/ID:** `02_02_Add_Record`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Style:** `colors = TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`.
        - **Title:** `Text` with content "Add Record".

2.  **Component: Record Type Tabs**
    - **Name:** `TabRow`
    - **Position & Size:** Below `TopAppBar`, `width = fillMaxWidth`.
    - **Content:**
        - `Tab` (Selected): Text "Expense".
        - `Tab`: Text "Income".
        - `Tab`: Text "Transfer".

3.  **Component: Input Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - **Amount Field:** `OutlinedTextField`, `label = { Text("Amount") }`, `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)`.
        - **Category Field (Clickable):** `ListItem` with `headlineContent = { Text("Category") }`, `supportingContent = { Text("Select a category") }`, `trailingContent = { Icon(Icons.Filled.ChevronRight) }`.
        - **Account Field (Clickable):** `ListItem` with `headlineContent = { Text("Account") }`, `supportingContent = { Text("Select an account") }`, `trailingContent = { Icon(Icons.Filled.ChevronRight) }`.
        - **Date Field (Clickable):** `ListItem` with `headlineContent = { Text("Date") }`, `supportingContent = { Text("Today") }`, `trailingContent = { Icon(Icons.Filled.CalendarToday) }`.
        - **Note Field:** `OutlinedTextField`, `label = { Text("Note (Optional)") }`.

4.  **Component: Save Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of the screen, `width = fillMaxWidth`, `height = 52dp`, `padding(16dp)`.
    - **Content:** "Save"

##### Interaction & Behavior:
- **Close Icon:** On tap -> Navigate back to `02_01_Dashboard`. Animation: `MaterialContainerTransform(backward)`.
- **'Income' Tab:** On tap -> Switch view, navigate to `02_03_Add_Record_Income`. Animation: `Crossfade`.
- **'Transfer' Tab:** On tap -> Switch view, navigate to `02_04_Add_Record_Transfer`. Animation: `Crossfade`.
- **Category Field:** On tap -> Navigate to `02_05_Select_Category`. Animation: `MaterialSharedAxis(X)`.
- **Account Field:** On tap -> Navigate to `02_07_Select_Account`. Animation: `MaterialSharedAxis(X)`.
- **Date Field:** On tap -> Show `02_08_Date_Picker` dialog.
- **Save Button:** On tap -> Save record, navigate to `02_01_Dashboard`. Animation: `MaterialSharedAxis(Z, backward)`.

---

#### Screen 2.3: Add Record (Income)
- **Screen Name/ID:** `02_03_Add_Record_Income`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** Identical to `02_02_Add_Record`, but with the 'Income' tab selected.

##### Components:
1.  **Component: Top App Bar:** Same as `02_02`.
2.  **Component: Record Type Tabs**
    - **Name:** `TabRow`
    - **Content:**
        - `Tab`: Text "Expense".
        - `Tab` (Selected): Text "Income".
        - `Tab`: Text "Transfer".
3.  **Component: Input Form:** Same as `02_02`.
4.  **Component: Save Button:** Same as `02_02`.

##### Interaction & Behavior:
- **'Expense' Tab:** On tap -> Switch view, navigate to `02_02_Add_Record`. Animation: `Crossfade`.
- **'Transfer' Tab:** On tap -> Switch view, navigate to `02_04_Add_Record_Transfer`. Animation: `Crossfade`.
- **Category Field:** On tap -> Navigate to `02_05_Select_Category`. Animation: `MaterialSharedAxis(X)`.
- **Save Button:** On tap -> Save record, navigate to `02_01_Dashboard`. Animation: `MaterialSharedAxis(Z, backward)`.

---

#### Screen 2.4: Add Record (Transfer)
- **Screen Name/ID:** `02_04_Add_Record_Transfer`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** Identical to `02_02_Add_Record`, but with the 'Transfer' tab selected and a modified form.

##### Components:
1.  **Component: Top App Bar:** Same as `02_02`.
2.  **Component: Record Type Tabs**
    - **Name:** `TabRow`
    - **Content:**
        - `Tab`: Text "Expense".
        - `Tab`: Text "Income".
        - `Tab` (Selected): Text "Transfer".
3.  **Component: Input Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - **Amount Field:** `OutlinedTextField`, `label = { Text("Amount") }`.
        - **From Account Field (Clickable):** `ListItem` with `headlineContent = { Text("From Account") }`, `supportingContent = { Text("Select source account") }`, `trailingContent = { Icon(Icons.Filled.ChevronRight) }`.
        - **To Account Field (Clickable):** `ListItem` with `headlineContent = { Text("To Account") }`, `supportingContent = { Text("Select destination account") }`, `trailingContent = { Icon(Icons.Filled.ChevronRight) }`.
        - **Date Field (Clickable):** `ListItem` with `headlineContent = { Text("Date") }`, `supportingContent = { Text("Today") }`.
        - **Note Field:** `OutlinedTextField`, `label = { Text("Note (Optional)") }`.
4.  **Component: Save Button:** Same as `02_02`.

##### Interaction & Behavior:
- **'Expense' Tab:** On tap -> Switch view, navigate to `02_02_Add_Record`. Animation: `Crossfade`.
- **'Income' Tab:** On tap -> Switch view, navigate to `02_03_Add_Record_Income`. Animation: `Crossfade`.
- **'From'/'To' Account Fields:** On tap -> Navigate to `02_07_Select_Account`. Animation: `MaterialSharedAxis(X)`.
- **Save Button:** On tap -> Save record, navigate to `02_01_Dashboard`. Animation: `MaterialSharedAxis(Z, backward)`.

---

#### Screen 2.5: Select Category
- **Screen Name/ID:** `02_05_Select_Category`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Select Category".
        - **Actions:** `IconButton` with `Icons.Filled.Add`.

2.  **Component: Category List**
    - **Name:** `LazyColumn`
    - **Content:** List of categories, grouped by parent category (e.g., "Food & Drink", "Shopping"). Each group has a `ListSubheader`. Each category is a `ListItem`.
    - **ListItem Component:**
        - **Name:** `ListItem`
        - **Content:**
            - **Leading Content:** `Icon` representing the category (e.g., `Icons.Filled.ShoppingCart`).
            - **Headline Text:** Category name (e.g., "Groceries").

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `02_02_Add_Record`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Add Icon:** On tap -> Navigate to `02_06_Create_New_Category`. Animation: `MaterialSharedAxis(Y)`.
- **Category ListItem:** On tap -> Select category, navigate back to `02_02_Add_Record` with data. Animation: `MaterialSharedAxis(X, backward = true)`.

---

#### Screen 2.6: Create New Category
- **Screen Name/ID:** `02_06_Create_New_Category`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`.
        - **Title:** `Text` with content "New Category".
        - **Actions:** `TextButton` with text "Save".

2.  **Component: Input Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - **Category Name Field:** `OutlinedTextField`, `label = { Text("Category name") }`.
        - **Icon Selector:** A `Row` with a selected `Icon` and a "Change" `TextButton`. Tapping it opens an icon picker grid.
        - **Parent Category Selector:** `ExposedDropdownMenuBox` to select a parent category.

##### Interaction & Behavior:
- **Close Icon:** On tap -> Discard changes, navigate back to `02_05_Select_Category`. Animation: `MaterialSharedAxis(Y, backward = true)`.
- **Save Button:** On tap -> Save category, navigate back to `02_05_Select_Category`. Animation: `MaterialSharedAxis(Y, backward = true)`.

---

#### Screen 2.7: Select Account
- **Screen Name/ID:** `02_07_Select_Account`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Content:**
        - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        - **Title:** `Text` with content "Select Account".

2.  **Component: Account List**
    - **Name:** `LazyColumn`
    - **Content:** List of `ListItem` components for each user account.
    - **ListItem Component:**
        - **Name:** `ListItem`
        - **Content:**
            - **Leading Content:** `Icon` for account type (e.g., `Icons.Filled.CreditCard`).
            - **Headline Text:** Account name (e.g., "Checking Account").
            - **Supporting Text:** Current balance (e.g., "$1,234.56").

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to the previous screen (e.g., `02_02_Add_Record`). Animation: `MaterialSharedAxis(X, backward = true)`.
- **Account ListItem:** On tap -> Select account, navigate back to the previous screen with data. Animation: `MaterialSharedAxis(X, backward = true)`.

---

#### Screen 2.8: Date Picker
- **Screen Name/ID:** `02_08_Date_Picker`
- **Dimensions:** Displayed as a modal dialog over the current screen.
- **Background:** `md.sys.color.surfaceContainerHigh`.
- **Layout:** Material 3 `DatePickerDialog`.

##### Components:
1.  **Component: Date Picker Dialog**
    - **Name:** `DatePickerDialog`
    - **Content:** Standard Material 3 calendar view.
    - **Actions:**
        - `TextButton` with text "Cancel".
        - `TextButton` with text "OK".

##### Interaction & Behavior:
- **"OK" Button:** On tap -> Confirms date selection, dismisses dialog, and updates the date field on `02_02_Add_Record`.
- **"Cancel" Button:** On tap -> Discards selection and dismisses dialog.

---
### Flow 3: Connect Bank

---

#### Screen 3.1: Accounts
- **Screen Name/ID:** `03_01_Accounts`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`, `FloatingActionButton`, and `BottomAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen, `height = 64dp`.
    - **Content:**
        - **Title:** `Text` with content "Accounts".

2.  **Component: Account List**
    - **Name:** `LazyColumn`
    - **Content:** List of `Card` components for each account.
    - **Card Component:**
        - **Name:** `ElevatedCard`
        - **Position & Size:** `width = fillMaxWidth`, `margin(horizontal = 16dp, vertical = 8dp)`.
        - **Content:** `Column` with account name, type, and balance.

3.  **Component: Floating Action Button**
    - **Name:** `FloatingActionButton`
    - **Position & Size:** Bottom right, inside the `Scaffold`.
    - **Content:** `Icon` with `Icons.Filled.Add`.

4.  **Component: Bottom Navigation Bar:**
    - **Name:** `NavigationBar`
    - **Content:** `NavigationBarItem` for "Accounts" is selected. Other items are the same as `02_01_Dashboard`.

##### Interaction & Behavior:
- **FAB:** On tap -> Navigate to `03_02_Add_Account`. Animation: `MaterialContainerTransform`.

---

#### Screen 3.2: Add Account
- **Screen Name/ID:** `03_02_Add_Account`
- **Dimensions:** Displayed as a `ModalBottomSheet`.
- **Background:** `md.sys.color.surfaceContainer`.
- **Layout:** `Column` with padding.

##### Components:
1.  **Component: Title**
    - **Name:** `Text`
    - **Position & Size:** `padding(16dp)`.
    - **Style:** `typography = md.sys.typography.titleLarge`.
    - **Content:** "Add Account"

2.  **Component: Bank Connection Option**
    - **Name:** `ListItem`
    - **Content:**
        - **Leading Content:** `Icon(Icons.Filled.Sync)`.
        - **Headline Text:** "Bank connection".
        - **Supporting Text:** "Connect with your bank automatically".

3.  **Component: Manual Account Options**
    - **Name:** `ListItem`
    - **Content:**
        - **Leading Content:** `Icon(Icons.Filled.Money)`.
        - **Headline Text:** "Cash".
        - **Supporting Text:** "For cash expenses".
    - *(Other manual types like "Savings", "Credit Card" would follow the same ListItem pattern)*

##### Interaction & Behavior:
- **Bank Connection ListItem:** On tap -> Dismiss sheet, navigate to `03_03_Connect_a_Bank`. Animation: `MaterialSharedAxis(X)`.
- **Cash ListItem:** On tap -> Dismiss sheet, navigate to `01_05_Onboarding_Create_First_Account` (re-using the manual creation screen). Animation: `MaterialSharedAxis(X)`.

---

#### Screen 3.3: Connect a Bank
- **Screen Name/ID:** `03_03_Connect_a_Bank`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column` centered vertically and horizontally.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** `NavigationIcon` with `Icons.Filled.ArrowBack`.
2.  **Component: Content**
    - **Name:** `Column`
    - **Position & Size:** `padding(24dp)`, `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Content:**
        - **Icon:** `Icon(Icons.Filled.Security)`, size 96dp, `tint = md.sys.color.primary`.
        - **Headline:** `Text("Connect with your bank")`, `typography = md.sys.typography.headlineSmall`, `margin(top = 24dp)`.
        - **Body:** `Text("We partner with a secure provider to link your bank account. Your credentials will not be stored by us.")`, `typography = md.sys.typography.bodyMedium`, `textAlign = TextAlign.Center`, `margin(top = 16dp)`.
        - **Continue Button:** `FilledButton("Continue")`, `width = fillMaxWidth`, `margin(top = 32dp)`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to previous screen. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Continue Button:** On tap -> Navigate to `03_04_Select_Your_Country`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 3.4: Select Your Country
- **Screen Name/ID:** `03_04_Select_Your_Country`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Select Your Country".
2.  **Component: Country List**
    - **Name:** `LazyColumn`
    - **Content:** A list of `ListItem`s for each country.
    - **ListItem:** `headlineContent = { Text("Country Name") }`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `03_03_Connect_a_Bank`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Country ListItem:** On tap -> Navigate to `03_05_Select_Your_Bank`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 3.5: Select Your Bank
- **Screen Name/ID:** `03_05_Select_Your_Bank`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn` with a search bar.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Select Your Bank".
2.  **Component: Search Bar**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `width = fillMaxWidth`, `padding(16dp)`.
    - **Style:** `placeholder = { Text("Search for your bank") }`, `leadingIcon = { Icon(Icons.Filled.Search) }`.
3.  **Component: Bank List**
    - **Name:** `LazyColumn`
    - **Content:** A grid or list of popular banks, followed by an alphabetical list of `ListItem`s.
    - **ListItem:** `leadingContent = { Image(bank_logo) }`, `headlineContent = { Text("Bank Name") }`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `03_04_Select_Your_Country`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Bank ListItem:** On tap -> Navigate to `03_06_Bank_Login`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 3.6: Bank Login
- **Screen Name/ID:** `03_06_Bank_Login`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** This screen would typically be a `WebView` loading the bank's secure portal. The spec below is a fallback native UI.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.Close`.
        - `Title` with text of the selected bank name.
2.  **Component: Login Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - `OutlinedTextField` for "Username" or "Customer ID".
        - `OutlinedTextField` for "Password".
        - `FilledButton` with text "Log In".

##### Interaction & Behavior:
- **Close Icon:** On tap -> Cancel flow, navigate back to `03_01_Accounts`. Animation: `MaterialSharedAxis(Y, backward = true)`.
- **Log In Button:** On tap -> Simulate authentication, navigate to `03_07_Connecting`. Animation: `MaterialFadeThrough`.

---

#### Screen 3.7: Connecting
- **Screen Name/ID:** `03_07_Connecting`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.

##### Components:
1.  **Component: Progress Indicator**
    - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered, `size = 64dp`.
2.  **Component: Status Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 24dp)`.
    - **Style:** `typography = md.sys.typography.bodyLarge`.
    - **Content:** "Connecting to your bank..."

##### Interaction & Behavior:
- **System Process:** After a simulated delay, automatically navigate to `03_08_Connection_Successful`. Animation: `MaterialFadeThrough`.

---

#### Screen 3.8: Connection Successful
- **Screen Name/ID:** `03_08_Connection_Successful`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding(24dp)`.

##### Components:
1.  **Component: Illustration**
    - **Name:** `Icon`
    - **Position & Size:** 120dp x 120dp.
    - **Style:** `icon = Icons.Outlined.CheckCircleOutline`, `tint = md.sys.color.primary`.
2.  **Component: Headline Text**
    - **Name:** `Text`
    - **Position & Size:** `margin(top = 32dp)`.
    - **Style:** `typography = md.sys.typography.headlineSmall`.
    - **Content:** "Connection Successful!"
3.  **Component: Continue Button**
    - **Name:** `FilledButton`
    - **Position & Size:** `width = fillMaxWidth`, `height = 52dp`, `margin(top = 32dp)`.
    - **Content:** "Continue"

##### Interaction & Behavior:
- **Continue Button:** On tap -> Navigate to `03_01_Accounts`. Animation: `MaterialSharedAxis(Z)`.

---
### Flow 4: Create Budget

---

#### Screen 4.1: Budgets
- **Screen Name/ID:** `04_01_Budgets`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** `Title` with text "Budgets".
2.  **Component: Budget List / Empty State**
    - **Name:** `LazyColumn` or `Column` (for empty state).
    - **Content (With Data):** List of `Card`s, each showing a budget's name, progress bar, and amount remaining.
    - **Content (Empty State):**
        - `Icon(Icons.Outlined.DonutLarge)`, size 96dp, `tint = md.sys.color.onSurfaceVariant`.
        - `Text("No budgets yet")`, `typography = md.sys.typography.titleLarge`, `margin(top = 24dp)`.
        - `Text("Create a budget to keep your spending in check.")`, `typography = md.sys.typography.bodyMedium`, `color = md.sys.color.onSurfaceVariant`, `margin(top = 8dp)`.
        - `FilledButton("Create a budget")`, `margin(top = 24dp)`.
3.  **Component: Bottom Navigation Bar:**
    - **Name:** `NavigationBar`
    - **Content:** `NavigationBarItem` for "Budgets" is selected.

##### Interaction & Behavior:
- **'Create a budget' Button:** On tap -> Navigate to `04_02_Create_Budget_Step_1_Category`. Animation: `MaterialSharedAxis(Y)`.

---

#### Screen 4.2: Create Budget - Step 1: Category
- **Screen Name/ID:** `04_02_Create_Budget_Step_1_Category`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and a bottom button. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.Close`.
        - `Title` with text "Create Budget (1/4)".
2.  **Component: Category List**
    - **Name:** `LazyColumn`
    - **Content:** List of categories, similar to `02_05_Select_Category`, but with `Checkbox`es as trailing content.
3.  **Component: Next Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of screen, `width = fillMaxWidth`, `padding(16dp)`.
    - **Style:** Disabled until at least one category is selected.
    - **Content:** "Next"

##### Interaction & Behavior:
- **Close Icon:** On tap -> Discard, navigate back to `04_01_Budgets`. Animation: `MaterialSharedAxis(Y, backward = true)`.
- **Next Button:** On tap -> Navigate to `04_03_Create_Budget_Step_2_Amount`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 4.3: Create Budget - Step 2: Amount
- **Screen Name/ID:** `04_03_Create_Budget_Step_2_Amount`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and a bottom button. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Create Budget (2/4)".
2.  **Component: Amount Input**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - `Text("Set the budget amount")`, `typography = md.sys.typography.titleMedium`.
        - `OutlinedTextField`, `label = { Text("Amount") }`, `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)`.
3.  **Component: Next Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of screen, `width = fillMaxWidth`, `padding(16dp)`.
    - **Content:** "Next"

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `04_02`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Next Button:** On tap -> Navigate to `04_04_Create_Budget_Step_3_Period`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 4.4: Create Budget - Step 3: Period
- **Screen Name/ID:** `04_04_Create_Budget_Step_3_Period`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and a bottom button. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Create Budget (3/4)".
2.  **Component: Period Selector**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:** A list of `ListItem`s with `RadioButton`s for periods like "Monthly", "Weekly", "Quarterly", "Yearly".
3.  **Component: Next Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of screen, `width = fillMaxWidth`, `padding(16dp)`.
    - **Content:** "Next"

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `04_03`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Next Button:** On tap -> Navigate to `04_05_Create_Budget_Step_4_Accounts`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 4.5: Create Budget - Step 4: Accounts
- **Screen Name/ID:** `04_05_Create_Budget_Step_4_Accounts`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and a bottom button. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Create Budget (4/4)".
2.  **Component: Account List**
    - **Name:** `LazyColumn`
    - **Content:** List of user accounts with `Checkbox`es. A "Select All" option is at the top.
3.  **Component: Create Budget Button**
    - **Name:** `FilledButton`
    - **Position & Size:** Bottom of screen, `width = fillMaxWidth`, `padding(16dp)`.
    - **Content:** "Create budget"

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `04_04`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Create Budget Button:** On tap -> Save budget, navigate to `04_01_Budgets`. Animation: `MaterialSharedAxis(Y, backward = true)`.

---
### Flow 5: Main Navigation

---

#### Screen 5.1: Main Navigation Base
- **Screen Name/ID:** `05_01_Main_Navigation_Base`
- **Note:** This is not a distinct screen but represents the persistent navigation structure (`Scaffold` with `BottomAppBar`) present on the main app sections.

##### Interaction & Behavior:
- **'Dashboard' Tab:** On tap -> Navigate to `02_01_Dashboard`. Animation: `MaterialFadeThrough`.
- **'Accounts' Tab:** On tap -> Navigate to `03_01_Accounts`. Animation: `MaterialFadeThrough`.
- **'Budgets' Tab:** On tap -> Navigate to `04_01_Budgets`. Animation: `MaterialFadeThrough`.
- **'Goals' Tab:** On tap -> Navigate to `05_02_Goals`. Animation: `MaterialFadeThrough`.
- **'More' Tab:** On tap -> Navigate to `05_04_More_Menu`. Animation: `MaterialFadeThrough`.

---

#### Screen 5.2: Goals
- **Screen Name/ID:** `05_02_Goals`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** `Title` with text "Goals".
2.  **Component: Goals List / Empty State**
    - **Name:** `LazyColumn` or `Column` (for empty state).
    - **Content (Empty State):**
        - `Icon(Icons.Outlined.Flag)`, size 96dp.
        - `Text("No goals yet")`.
        - `FilledButton("Create a goal")`.
3.  **Component: Bottom Navigation Bar:**
    - **Name:** `NavigationBar`
    - **Content:** `NavigationBarItem` for "Goals" is selected.

##### Interaction & Behavior:
- **'Create a goal' Button:** On tap -> Navigate to `05_03_Create_Goal`. Animation: `MaterialSharedAxis(Y)`.

---

#### Screen 5.3: Create Goal
- **Screen Name/ID:** `05_03_Create_Goal`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.Close`.
        - `Title` with text "Create Goal".
        - `Actions` with `TextButton("Save")`.
2.  **Component: Goal Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - `OutlinedTextField` for "Goal Name".
        - `OutlinedTextField` for "Target Amount".
        - `OutlinedTextField` for "Initial Amount".
        - Date picker field for "Target Date".

##### Interaction & Behavior:
- **Close Icon:** On tap -> Discard, navigate back to `05_02_Goals`. Animation: `MaterialSharedAxis(Y, backward = true)`.
- **Save Button:** On tap -> Save goal, navigate back to `05_02_Goals`. Animation: `MaterialSharedAxis(Y, backward = true)`.

---

#### Screen 5.4: More Menu
- **Screen Name/ID:** `05_04_More_Menu`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar` and `BottomAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:** `Title` with text "More".
2.  **Component: Menu List**
    - **Name:** `LazyColumn`
    - **Content:**
        - `ListItem` for "My Profile". `leadingContent = { Icon(Icons.Outlined.Person) }`.
        - `ListItem` for "Settings". `leadingContent = { Icon(Icons.Outlined.Settings) }`.
        - `ListItem` for "Export Data".
        - `ListItem` for "Help & Support".
3.  **Component: Bottom Navigation Bar:**
    - **Name:** `NavigationBar`
    - **Content:** `NavigationBarItem` for "More" is selected.

##### Interaction & Behavior:
- **'Settings' ListItem:** On tap -> Navigate to `05_05_Settings`. Animation: `MaterialSharedAxis(X)`.
- **'My Profile' ListItem:** On tap -> Navigate to `05_07_Profile`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 5.5: Settings
- **Screen Name/ID:** `05_05_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Settings".
2.  **Component: Settings List**
    - **Name:** `LazyColumn`
    - **Content:**
        - `ListItem` for "Security".
        - `ListItem` for "Notifications".
        - `ListItem` for "Appearance" (with a trailing switch for Dark Mode).
        - `ListItem` for "Currency".

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `05_04_More_Menu`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **'Security' ListItem:** On tap -> Navigate to `05_06_Security_Settings`. Animation: `MaterialSharedAxis(X)`.
- **'Notifications' ListItem:** On tap -> Navigate to `05_09_Notification_Settings`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 5.6: Security Settings
- **Screen Name/ID:** `05_06_Security_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Security".
2.  **Component: Security Options**
    - **Name:** `LazyColumn`
    - **Content:**
        - `ListItem` with `headlineContent = { Text("PIN Lock") }` and `trailingContent = { Switch() }`.
        - `ListItem` with `headlineContent = { Text("Biometric Lock") }` and `trailingContent = { Switch() }`.
        - `ListItem` for "Change Password".

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `05_05_Settings`. Animation: `MaterialSharedAxis(X, backward = true)`.

---

#### Screen 5.7: Profile
- **Screen Name/ID:** `05_07_Profile`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "My Profile".
        - `Actions` with `TextButton("Edit")`.
2.  **Component: Profile Details**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`, `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Content:**
        - `Avatar` (CircleShape Image), size 96dp.
        - `Text` for User Name, `typography = md.sys.typography.titleLarge`.
        - `Text` for User Email, `typography = md.sys.typography.bodyMedium`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `05_04_More_Menu`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **'Edit' Button:** On tap -> Navigate to `05_08_Edit_Profile`. Animation: `MaterialSharedAxis(X)`.

---

#### Screen 5.8: Edit Profile
- **Screen Name/ID:** `05_08_Edit_Profile`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.Close`.
        - `Title` with text "Edit Profile".
        - `Actions` with `TextButton("Save")`.
2.  **Component: Edit Form**
    - **Name:** `Column`
    - **Position & Size:** `padding(16dp)`.
    - **Content:**
        - `OutlinedTextField` for "Name".
        - `OutlinedTextField` for "Email" (disabled).

##### Interaction & Behavior:
- **Close Icon:** On tap -> Discard, navigate back to `05_07_Profile`. Animation: `MaterialSharedAxis(X, backward = true)`.
- **Save Button:** On tap -> Save changes, navigate back to `05_07_Profile`. Animation: `MaterialSharedAxis(X, backward = true)`.

---

#### Screen 5.9: Notification Settings
- **Screen Name/ID:** `05_09_Notification_Settings`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.

##### Components:
1.  **Component: Top App Bar**
    - **Name:** `TopAppBar`
    - **Content:**
        - `NavigationIcon` with `Icons.Filled.ArrowBack`.
        - `Title` with text "Notifications".
2.  **Component: Notification Options**
    - **Name:** `LazyColumn`
    - **Content:**
        - `ListItem` with `headlineContent = { Text("Upcoming Bills") }` and `trailingContent = { Switch() }`.
        - `ListItem` with `headlineContent = { Text("Budget Alerts") }` and `trailingContent = { Switch() }`.
        - `ListItem` with `headlineContent = { Text("Promotions") }` and `trailingContent = { Switch() }`.

##### Interaction & Behavior:
- **Back Arrow:** On tap -> Navigate back to `05_05_Settings`. Animation: `MaterialSharedAxis(X, backward = true)`.

---

## V. Critical Scenarios & States

### Error States
- **Type:** No Internet Connection
  - **UI:** `Snackbar`
  - **Position:** Appears at the bottom of the screen.
  - **Style:** `containerColor = md.sys.color.errorContainer`, `contentColor = md.sys.color.onErrorContainer`.
  - **Content:** "No internet connection. Please check your network."
  - **Action:** Optional "Retry" `TextButton`.

- **Type:** Form Validation Error
  - **UI:** `OutlinedTextField` error state.
  - **Style:** Border and label color change to `md.sys.color.error`.
  - **Content:** Helper text below the field appears, colored with `md.sys.color.error`. Example: "Please enter a valid email."

### Empty States
- **Applicable Screens:** `02_01_Dashboard` (no transactions), `03_01_Accounts` (no accounts), `04_01_Budgets`, `05_02_Goals`.
- **Layout:** Centered `Column` with `padding(32dp)`.
- **Components:**
  1.  **Icon:** A relevant outlined Material Icon (e.g., `Icons.Outlined.ReceiptLong` for transactions), size 96dp, `tint = md.sys.color.onSurfaceVariant`.
  2.  **Headline:** `Text` with a short, descriptive title (e.g., "No transactions yet"). `typography = md.sys.typography.titleLarge`, `textAlign = TextAlign.Center`.
  3.  **Body:** `Text` with a helpful prompt (e.g., "Tap the '+' button to add your first expense or income."). `typography = md.sys.typography.bodyMedium`, `color = md.sys.color.onSurfaceVariant`, `textAlign = TextAlign.Center`.
  4.  **CTA (Optional):** A `FilledButton` to guide the user to the primary creation action (e.g., "Create a budget").

### Loading States
- **Type:** Full Screen Load (e.g., initial app load)
  - **UI:** A centered `CircularProgressIndicator` on a `md.sys.color.surface` background.

- **Type:** Partial/Widget Load (e.g., a card on the dashboard refreshing)
  - **UI:** A smaller `CircularProgressIndicator` centered within the component's bounds. Alternatively, use shimmer placeholders (a `Surface` with an animated gradient brush) that match the shape of the content being loaded.

- **Type:** Pull-to-Refresh
  - **UI:** Standard `PullToRefresh` indicator at the top of a scrollable list.
  - **Style:** Uses `md.sys.color.primary` for the indicator.
```

---


============================================================
## APP 3: App_3
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

# Spendee - Android App Design Specification

## I. Global Specifications

This document outlines the design specifications for the Spendee Android application, based on Google's Material Design 3 system.

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Dynamic Color**: Enabled (Material You). The color scheme adapts to the user's wallpaper.
    *   **Modes**: Light and Dark themes are fully supported.
*   **Colors**:
    *   **Seed Color**: `#06A77D` (Spendee Green)
    *   **Light Theme Color Roles**:
        *   `md.sys.color.primary`: `#006C4F`
        *   `md.sys.color.onPrimary`: `#FFFFFF`
        *   `md.sys.color.primaryContainer`: `#86F8CA`
        *   `md.sys.color.onPrimaryContainer`: `#002116`
        *   `md.sys.color.secondary`: `#4C6358`
        *   `md.sys.color.onSecondary`: `#FFFFFF`
        *   `md.sys.color.secondaryContainer`: `#CFE9DA`
        *   `md.sys.color.onSecondaryContainer`: `#092017`
        *   `md.sys.color.tertiary`: `#3E6374`
        *   `md.sys.color.onTertiary`: `#FFFFFF`
        *   `md.sys.color.tertiaryContainer`: `#C1E8FC`
        *   `md.sys.color.onTertiaryContainer`: `#001F2A`
        *   `md.sys.color.error`: `#BA1A1A`
        *   `md.sys.color.onError`: `#FFFFFF`
        *   `md.sys.color.background`: `#FBFDF9`
        *   `md.sys.color.onBackground`: `#191C1A`
        *   `md.sys.color.surface`: `#FBFDF9`
        *   `md.sys.color.onSurface`: `#191C1A`
        *   `md.sys.color.surfaceVariant`: `#DCE5DE`
        *   `md.sys.color.onSurfaceVariant`: `#404944`
        *   `md.sys.color.outline`: `#707974`
    *   **Dark Theme Color Roles**:
        *   `md.sys.color.primary`: `#69DBAF`
        *   `md.sys.color.onPrimary`: `#003828`
        *   `md.sys.color.primaryContainer`: `#00513B`
        *   `md.sys.color.onPrimaryContainer`: `#86F8CA`
        *   `md.sys.color.secondary`: `#B3CCBF`
        *   `md.sys.color.onSecondary`: `#1F352B`
        *   `md.sys.color.secondaryContainer`: `#354B41`
        *   `md.sys.color.onSecondaryContainer`: `#CFE9DA`
        *   `md.sys.color.tertiary`: `#A6CCE0`
        *   `md.sys.color.onTertiary`: `#093544`
        *   `md.sys.color.tertiaryContainer`: `#254B5C`
        *   `md.sys.color.onTertiaryContainer`: `#C1E8FC`
        *   `md.sys.color.error`: `#FFB4AB`
        *   `md.sys.color.onError`: `#690005`
        *   `md.sys.color.background`: `#191C1A`
        *   `md.sys.color.onBackground`: `#E1E3DF`
        *   `md.sys.color.surface`: `#191C1A`
        *   `md.sys.color.onSurface`: `#E1E3DF`
        *   `md.sys.color.surfaceVariant`: `#404944`
        *   `md.sys.color.onSurfaceVariant`: `#C0C9C2`
        *   `md.sys.color.outline`: `#8A938D`
*   **Typography**:
    *   **Font Family**: Roboto
    *   **Type Scale**: Material 3 Default Scale
        *   `md.sys.typography.displayLarge`
        *   `md.sys.typography.headlineLarge`
        *   `md.sys.typography.headlineMedium`
        *   `md.sys.typography.headlineSmall`
        *   `md.sys.typography.titleLarge`
        *   `md.sys.typography.titleMedium`
        *   `md.sys.typography.titleSmall`
        *   `md.sys.typography.labelLarge`
        *   `md.sys.typography.labelMedium`
        *   `md.sys.typography.labelSmall`
        *   `md.sys.typography.bodyLarge`
        *   `md.sys.typography.bodyMedium`
        *   `md.sys.typography.bodySmall`
*   **Spacing**:
    *   **Base Grid Unit**: 8dp. All spacing, padding, and margins are multiples of 8dp (e.g., 8dp, 16dp, 24dp).
*   **Accessibility**:
    *   **Target Standard**: WCAG 2.1 Level AA.
    *   **Touch Targets**: All interactive elements must have a minimum touch target size of 48x48dp.
    *   **Content Descriptions**: All icons and images must have descriptive content descriptions for screen readers.

---

## II. Screen Specifications

### Flow 1: Onboarding and Account Creation

#### **Screen 1: Welcome**
*   **Screen Name/ID**: `01_01_Welcome`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered, horizontally aligned to `CenterHorizontally`. Padding of 24dp on all sides.
*   **Components**:
    *   **Name**: `Image` (App Logo)
        *   **Position & Size**: Top of the column, 120x120dp. Margin bottom 24dp.
        *   **Content**: Spendee app logo graphic.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: Below logo. `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineLarge`, `color = md.sys.color.onSurface`, `textAlign = Center`.
        *   **Content**: "See where your money goes"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: Below headline. `fillMaxWidth`. Margin bottom 48dp.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Spendee is a free budget app that helps you analyze your income and spending."
    *   **Name**: `FilledButton`
        *   **Position & Size**: Bottom of the column. `fillMaxWidth`, height 56dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: "Continue"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `01_02_Onboarding_Step_1`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis).

---

#### **Screen 2: Onboarding Step 1**
*   **Screen Name/ID**: `01_02_Onboarding_Step_1`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout. Padding of 24dp on all sides.
*   **Components**:
    *   **Name**: `Image` (Illustration)
        *   **Position & Size**: Top of the column, centered horizontally. `fillMaxWidth`, height 300dp. Margin top 32dp, margin bottom 32dp.
        *   **Content**: Illustration depicting connecting bank accounts.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: Below illustration. `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `color = md.sys.color.onSurface`, `textAlign = Center`.
        *   **Content**: "Connect Your Bank"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: Below headline. `fillMaxWidth`.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Automatically import transactions from your bank accounts and have them categorized."
    *   **Name**: `Row` (Page Indicator)
        *   **Position & Size**: Above the button, centered horizontally. `wrapContentSize`. Margin bottom 32dp.
        *   **Layout**: Contains three `Canvas` dots.
        *   **Components**:
            *   Dot 1: `Circle`, size 8dp, `color = md.sys.color.primary`.
            *   Dot 2: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
            *   Dot 3: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
    *   **Name**: `FilledButton`
        *   **Position & Size**: Bottom of the screen, anchored. `fillMaxWidth`, height 56dp. Margin bottom 24dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: "Continue"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `01_03_Onboarding_Step_2`.
    *   **Animation**: `MaterialSharedAxis` (X-axis).

---

#### **Screen 3: Onboarding Step 2**
*   **Screen Name/ID**: `01_03_Onboarding_Step_2`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout. Padding of 24dp on all sides.
*   **Components**:
    *   **Name**: `Image` (Illustration)
        *   **Position & Size**: Top of the column, centered horizontally. `fillMaxWidth`, height 300dp. Margin top 32dp, margin bottom 32dp.
        *   **Content**: Illustration depicting budgets and saving money.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: Below illustration. `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `color = md.sys.color.onSurface`, `textAlign = Center`.
        *   **Content**: "Create Smart Budgets"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: Below headline. `fillMaxWidth`.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Stick to your budget goals to save more money for things that matter."
    *   **Name**: `Row` (Page Indicator)
        *   **Position & Size**: Above the button, centered horizontally. `wrapContentSize`. Margin bottom 32dp.
        *   **Layout**: Contains three `Canvas` dots.
        *   **Components**:
            *   Dot 1: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
            *   Dot 2: `Circle`, size 8dp, `color = md.sys.color.primary`.
            *   Dot 3: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
    *   **Name**: `FilledButton`
        *   **Position & Size**: Bottom of the screen, anchored. `fillMaxWidth`, height 56dp. Margin bottom 24dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: "Continue"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `01_04_Onboarding_Step_3`.
    *   **Animation**: `MaterialSharedAxis` (X-axis).

---

#### **Screen 4: Onboarding Step 3**
*   **Screen Name/ID**: `01_04_Onboarding_Step_3`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout. Padding of 24dp on all sides.
*   **Components**:
    *   **Name**: `Image` (Illustration)
        *   **Position & Size**: Top of the column, centered horizontally. `fillMaxWidth`, height 300dp. Margin top 32dp, margin bottom 32dp.
        *   **Content**: Illustration depicting charts and financial analysis.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: Below illustration. `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `color = md.sys.color.onSurface`, `textAlign = Center`.
        *   **Content**: "Understand Your Habits"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: Below headline. `fillMaxWidth`.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Get a clear overview of your finances with insightful charts and reports."
    *   **Name**: `Row` (Page Indicator)
        *   **Position & Size**: Above the button, centered horizontally. `wrapContentSize`. Margin bottom 32dp.
        *   **Layout**: Contains three `Canvas` dots.
        *   **Components**:
            *   Dot 1: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
            *   Dot 2: `Circle`, size 8dp, `color = md.sys.color.surfaceVariant`.
            *   Dot 3: `Circle`, size 8dp, `color = md.sys.color.primary`.
    *   **Name**: `FilledButton`
        *   **Position & Size**: Bottom of the screen, anchored. `fillMaxWidth`, height 56dp. Margin bottom 24dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: "Get Started"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `01_05_Sign_Up_Options`.
    *   **Animation**: `MaterialSharedAxis` (X-axis).

---

#### **Screen 5: Sign Up Options**
*   **Screen Name/ID**: `01_05_Sign_Up_Options`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, padding 24dp horizontal, 32dp vertical. Elements are arranged from bottom to top.
*   **Components**:
    *   **Name**: `Image` (App Logo)
        *   **Position & Size**: Top of the screen, centered horizontally. 80x80dp. Margin top 64dp, margin bottom 32dp.
        *   **Content**: Spendee app logo graphic.
    *   **Name**: `FilledTonalButton` (Continue with Google)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin bottom 16dp.
        *   **Style**: `containerColor = md.sys.color.secondaryContainer`, `contentColor = md.sys.color.onSecondaryContainer`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: `Icon` (Google logo) on the left, `Text` "Continue with Google" centered.
    *   **Name**: `FilledTonalButton` (Continue with Apple)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin bottom 16dp.
        *   **Style**: `containerColor = md.sys.color.secondaryContainer`, `contentColor = md.sys.color.onSecondaryContainer`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: `Icon` (Apple logo) on the left, `Text` "Continue with Apple" centered.
    *   **Name**: `OutlinedButton` (Continue with Email)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin bottom 32dp.
        *   **Style**: `borderColor = md.sys.color.outline`, `contentColor = md.sys.color.primary`. Typography: `md.sys.typography.labelLarge`.
        *   **Content**: "Continue with Email"
    *   **Name**: `Row` (Log In prompt)
        *   **Position & Size**: Centered horizontally at the bottom of the main content area.
        *   **Components**:
            *   `Text`: "Already have an account? " (`style = md.sys.typography.bodyMedium`, `color = md.sys.color.onSurfaceVariant`)
            *   `TextButton`: "Log in" (`style = md.sys.typography.bodyMedium`, `contentColor = md.sys.color.primary`)
*   **Interaction & Behavior**:
    *   **Action**: Tap `OutlinedButton` "Continue with Email".
    *   **Navigation**: Navigate to `01_06_Sign_Up_with_Email`.
    *   **Action**: Tap `FilledTonalButton` "Continue with Google".
    *   **Navigation**: Navigate to `01_08_Google_Authentication`.
    *   **Action**: Tap `FilledTonalButton` "Continue with Apple".
    *   **Navigation**: Navigate to `01_09_Apple_Authentication`.
    *   **Action**: Tap `TextButton` "Log in".
    *   **Navigation**: Navigate to `01_07_Log_In_with_Email`.

---

#### **Screen 6: Sign Up with Email**
*   **Screen Name/ID**: `01_06_Sign_Up_with_Email`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `TopAppBar` and a `Column` in the content area. Padding 24dp horizontal.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Style**: `containerColor = md.sys.color.surface`.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Sign Up" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `OutlinedTextField` (Email)
        *   **Position & Size**: `fillMaxWidth`. Margin top 24dp.
        *   **Style**: Standard M3 `OutlinedTextField`.
        *   **Content**: Label: "Email". `keyboardType = Email`.
    *   **Name**: `OutlinedTextField` (Password)
        *   **Position & Size**: `fillMaxWidth`. Margin top 16dp.
        *   **Style**: Standard M3 `OutlinedTextField`.
        *   **Content**: Label: "Password". `keyboardType = Password`. `visualTransformation = PasswordVisualTransformation`. Trailing icon: `Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`.
    *   **Name**: `FilledButton` (Sign Up)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin top 32dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
        *   **Content**: "Sign Up"
*   **Interaction & Behavior**:
    *   **Action**: Enter valid email and password, tap `FilledButton`.
    *   **Navigation**: Navigate to `01_10_Set_Main_Currency`.
*   **Critical Scenarios**:
    *   **Error State**: If email is invalid or password is too short, the `OutlinedTextField` shows an error state: border and label color change to `md.sys.color.error`, and helper text appears below (e.g., "Enter a valid email"). The "Sign Up" button is disabled until both fields are valid.

---

#### **Screen 7: Log In with Email**
*   **Screen Name/ID**: `01_07_Log_In_with_Email`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `TopAppBar` and a `Column` in the content area. Padding 24dp horizontal.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Style**: `containerColor = md.sys.color.surface`.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Log In" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `OutlinedTextField` (Email)
        *   **Position & Size**: `fillMaxWidth`. Margin top 24dp.
        *   **Style**: Standard M3 `OutlinedTextField`.
        *   **Content**: Label: "Email".
    *   **Name**: `OutlinedTextField` (Password)
        *   **Position & Size**: `fillMaxWidth`. Margin top 16dp.
        *   **Style**: Standard M3 `OutlinedTextField`.
        *   **Content**: Label: "Password". `visualTransformation = PasswordVisualTransformation`.
    *   **Name**: `FilledButton` (Log In)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin top 32dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
        *   **Content**: "Log In"
*   **Interaction & Behavior**:
    *   **Action**: Enter credentials, tap `FilledButton`.
    *   **Navigation**: Navigate to `02_01_Dashboard`.
*   **Critical Scenarios**:
    *   **Error State**: On failed login, a `Snackbar` appears at the bottom of the screen with the message "Invalid email or password."

---

#### **Screen 8: Google Authentication**
*   **Screen Name/ID**: `01_08_Google_Authentication`
*   **Dimensions**: N/A (System UI)
*   **Background**: System-defined modal sheet.
*   **Layout**: This screen is a system-provided UI component for Google Sign-In. It is not custom-designed. It typically appears as a bottom sheet or a full-screen modal.
*   **Components**:
    *   Standard Google account selector UI.
*   **Interaction & Behavior**:
    *   **Action**: User selects a Google account and authenticates successfully.
    *   **Navigation**: The app navigates to `01_10_Set_Main_Currency`.
*   **Critical Scenarios**:
    *   **Error State**: If the user cancels or authentication fails, they are returned to the `01_05_Sign_Up_Options` screen. An optional `Snackbar` can show a message like "Authentication failed."

---

#### **Screen 9: Apple Authentication**
*   **Screen Name/ID**: `01_09_Apple_Authentication`
*   **Dimensions**: N/A (System UI)
*   **Background**: System-defined modal sheet.
*   **Layout**: This screen is a system-provided UI component for Sign in with Apple.
*   **Components**:
    *   Standard Apple ID authentication UI.
*   **Interaction & Behavior**:
    *   **Action**: User authenticates with their Apple ID successfully.
    *   **Navigation**: The app navigates to `01_10_Set_Main_Currency`.
*   **Critical Scenarios**:
    *   **Error State**: If the user cancels or authentication fails, they are returned to the `01_05_Sign_Up_Options` screen.

---

#### **Screen 10: Set Main Currency**
*   **Screen Name/ID**: `01_10_Set_Main_Currency`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with a `Column` layout. Padding 24dp horizontal.
*   **Components**:
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: Top of the column, `fillMaxWidth`. Margin top 64dp, margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `textAlign = Center`.
        *   **Content**: "Set Your Main Currency"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: `fillMaxWidth`. Margin bottom 32dp.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "This will be the default currency for your wallets and budgets. You can change it later."
    *   **Name**: `OutlinedTextField` (Currency Selector)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Style**: `ExposedDropdownMenuBox` style. Read-only. Trailing icon: `Icons.Filled.ArrowDropDown`.
        *   **Content**: Label: "Currency". Default value: "USD - United States Dollar".
    *   **Name**: `FilledButton` (Continue)
        *   **Position & Size**: Anchored to the bottom. `fillMaxWidth`, height 56dp. Margin 24dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
        *   **Content**: "Continue"
*   **Interaction & Behavior**:
    *   **Action**: Tap `OutlinedTextField` opens a full-screen list (`LazyColumn` of currencies) for selection.
    *   **Action**: Select a currency and tap `FilledButton`.
    *   **Navigation**: Navigate to `01_11_Connect_Bank_Introduction`.

---

#### **Screen 11: Connect Bank Introduction**
*   **Screen Name/ID**: `01_11_Connect_Bank_Introduction`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered, padding 24dp.
*   **Components**:
    *   **Name**: `Icon`
        *   **Position & Size**: Centered horizontally, 64x64dp. Margin bottom 24dp.
        *   **Style**: `tint = md.sys.color.primary`.
        *   **Content**: `Icons.Filled.AccountBalance`.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `textAlign = Center`.
        *   **Content**: "Connect Your Bank Account"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: `fillMaxWidth`. Margin bottom 32dp.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Save time by automatically importing your transactions. It's secure and you can disconnect anytime."
    *   **Name**: `FilledButton` (Connect Bank)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin bottom 16dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
        *   **Content**: "Connect Bank"
    *   **Name**: `TextButton` (Skip)
        *   **Position & Size**: `fillMaxWidth`, height 48dp.
        *   **Style**: `contentColor = md.sys.color.primary`.
        *   **Content**: "I'll do it later"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `01_12_Select_Country_Onboarding`.
    *   **Action**: Tap `TextButton`.
    *   **Navigation**: Navigate to `02_01_Dashboard`.

---

#### **Screen 12: Select Country (Onboarding)**
*   **Screen Name/ID**: `01_12_Select_Country_Onboarding`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Style**: `containerColor = md.sys.color.surface`.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Select Country" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `OutlinedTextField` (Search)
        *   **Position & Size**: `fillMaxWidth`. Padding 16dp horizontal, 8dp vertical.
        *   **Style**: Standard M3 `OutlinedTextField`.
        *   **Content**: Label: "Search country". Leading icon: `Icons.Filled.Search`.
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**: List of `ListItem` components.
    *   **Name**: `ListItem` (for each country)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Style**: `headlineContentColor = md.sys.color.onSurface`.
        *   **Content**:
            *   `LeadingContent`: Country flag image (24x24dp).
            *   `HeadlineText`: Country name (e.g., "United States").
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Navigate to `01_13_Select_Bank`.

---

#### **Screen 13: Select Bank**
*   **Screen Name/ID**: `01_13_Select_Bank`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Select Bank" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `OutlinedTextField` (Search)
        *   **Position & Size**: `fillMaxWidth`. Padding 16dp horizontal, 8dp vertical.
        *   **Content**: Label: "Search bank". Leading icon: `Icons.Filled.Search`.
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**: List of `ListItem` components for popular banks.
    *   **Name**: `ListItem` (for each bank)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**:
            *   `LeadingContent`: Bank logo image (40x40dp, rounded corners).
            *   `HeadlineText`: Bank name (e.g., "Chase Bank").
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Navigate to `01_14_Bank_Login`.

---

#### **Screen 14: Bank Login**
*   **Screen Name/ID**: `01_14_Bank_Login`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and a `WebView` component.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.Close`. On tap -> Cancel flow, navigate back to `01_11_Connect_Bank_Introduction`.
            *   `Text` (Title): "Connect to [Bank Name]" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `LinearProgressIndicator`
        *   **Position & Size**: Directly below the `TopAppBar`. `fillMaxWidth`.
        *   **Style**: Visible while the WebView is loading. `color = md.sys.color.primary`.
    *   **Name**: `WebView`
        *   **Position & Size**: Fills the entire content area.
        *   **Content**: Loads the secure bank login portal (via a service like Plaid or Stripe).
*   **Interaction & Behavior**:
    *   **Action**: User enters their bank credentials and submits the form within the `WebView`.
    *   **Navigation**: On successful authentication, navigate to `01_15_Select_Accounts`.

---

#### **Screen 15: Select Accounts**
*   **Screen Name/ID**: `01_15_Select_Accounts`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and a bottom `FilledButton`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Content**: `Text` (Title): "Select Accounts" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills space between `TopAppBar` and button.
        *   **Content**: List of `ListItem` components for each available bank account.
    *   **Name**: `ListItem` (for each account)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**:
            *   `HeadlineText`: Account Name (e.g., "Checking (...1234)").
            *   `SupportingText`: Account Type (e.g., "Checking").
            *   `TrailingContent`: `Checkbox` component.
    *   **Name**: `FilledButton` (Continue)
        *   **Position & Size**: Anchored to the bottom. `fillMaxWidth`, height 56dp. Margin 24dp.
        *   **Style**: `containerColor = md.sys.color.primary`, `contentColor = md.sys.color.onPrimary`.
        *   **Content**: "Continue"
*   **Interaction & Behavior**:
    *   **Action**: User selects one or more accounts via `Checkbox` and taps `FilledButton`.
    *   **Navigation**: Navigate to `01_16_Enable_Notifications`.

---

#### **Screen 16: Enable Notifications**
*   **Screen Name/ID**: `01_16_Enable_Notifications`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered, padding 24dp.
*   **Components**:
    *   **Name**: `Icon`
        *   **Position & Size**: Centered horizontally, 64x64dp. Margin bottom 24dp.
        *   **Style**: `tint = md.sys.color.primary`.
        *   **Content**: `Icons.Filled.Notifications`.
    *   **Name**: `Text` (Headline)
        *   **Position & Size**: `fillMaxWidth`. Margin bottom 16dp.
        *   **Style**: `md.sys.typography.headlineMedium`, `textAlign = Center`.
        *   **Content**: "Enable Notifications"
    *   **Name**: `Text` (Body)
        *   **Position & Size**: `fillMaxWidth`. Margin bottom 32dp.
        *   **Style**: `md.sys.typography.bodyLarge`, `color = md.sys.color.onSurfaceVariant`, `textAlign = Center`.
        *   **Content**: "Get reminders for upcoming bills and alerts when you're over budget."
    *   **Name**: `FilledButton` (Enable Notifications)
        *   **Position & Size**: `fillMaxWidth`, height 56dp. Margin bottom 16dp.
        *   **Content**: "Enable Notifications"
    *   **Name**: `TextButton` (Skip)
        *   **Position & Size**: `fillMaxWidth`, height 48dp.
        *   **Content**: "Not now"
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`. Triggers system permission dialog for notifications.
    *   **Navigation**: After dialog dismissal, navigate to `02_01_Dashboard`.
    *   **Action**: Tap `TextButton`.
    *   **Navigation**: Navigate to `02_01_Dashboard`.

---

### Flow 2: Add Transaction

#### **Screen 17: Dashboard**
*   **Screen Name/ID**: `02_01_Dashboard`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, `FloatingActionButton`, and `NavigationBar`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Style**: `scrollBehavior = ExitUntilCollapsedScrollBehavior`.
        *   **Content**:
            *   `Text` (Title): "Overview" (`style = md.sys.typography.titleLarge`).
            *   `Actions`: `IconButton` with `Icons.Filled.Notifications`.
    *   **Name**: `LazyColumn` (Main Content)
        *   **Position & Size**: Fills the content area. Padding 16dp horizontal.
        *   **Content**:
            *   Header item: A `Card` showing current balance, income, and expenses for the month.
            *   List items: `ListItem` or custom `Card` for each recent transaction, showing category icon, name, amount, and date.
    *   **Name**: `FloatingActionButton`
        *   **Position & Size**: Bottom right corner, inside the `Scaffold`.
        *   **Style**: `containerColor = md.sys.color.primaryContainer`, `contentColor = md.sys.color.onPrimaryContainer`.
        *   **Content**: `Icon` `Icons.Filled.Add`.
    *   **Name**: `NavigationBar` (Bottom Nav)
        *   **Position & Size**: Bottom of the screen. `fillMaxWidth`.
        *   **Style**: `containerColor = md.sys.color.surfaceVariant`.
        *   **Content**:
            *   `NavigationBarItem` 1: Selected. `Icon = Icons.Filled.Dashboard`, Label = "Dashboard".
            *   `NavigationBarItem` 2: `Icon = Icons.Filled.PieChart`, Label = "Analysis".
            *   `NavigationBarItem` 3: `Icon = Icons.Filled.AccountBalanceWallet`, Label = "Budgets".
            *   `NavigationBarItem` 4: `Icon = Icons.Filled.MoreHoriz`, Label = "More".
*   **Interaction & Behavior**:
    *   **Action**: Tap `FloatingActionButton`.
    *   **Navigation**: Navigate to `02_02_Add_Transaction`.
    *   **Action**: Tap "Analysis" `NavigationBarItem`.
    *   **Navigation**: Navigate to `04_01_Analysis`.
    *   **Action**: Tap "Budgets" `NavigationBarItem`.
    *   **Navigation**: Navigate to `03_01_Budgets`.
    *   **Action**: Tap "More" `NavigationBarItem`.
    *   **Navigation**: Navigate to `05_01_More`.

---

#### **Screen 18: Add Transaction**
*   **Screen Name/ID**: `02_02_Add_Transaction`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.tertiaryContainer` (for the top part), `md.sys.color.surface` (for the bottom part).
*   **Layout**: `Scaffold` with `TopAppBar`. The content is a `Column` split into a number pad area and a details area.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Style**: `containerColor = md.sys.color.tertiaryContainer`.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.Close`. On tap -> Navigate back.
            *   `Text` (Title): "Add Transaction".
            *   `Actions`: `TextButton` "Save".
    *   **Name**: `Row` (Amount Input)
        *   **Position & Size**: Top content area. `fillMaxWidth`, padding 32dp.
        *   **Style**: `backgroundColor = md.sys.color.tertiaryContainer`.
        *   **Content**:
            *   `Text` (Currency Symbol): e.g., "$". `style = md.sys.typography.headlineLarge`, `color = md.sys.color.onTertiaryContainer`.
            *   `Text` (Amount): "0". `style = md.sys.typography.displayLarge`, `color = md.sys.color.onTertiaryContainer`.
    *   **Name**: `Column` (Transaction Details)
        *   **Position & Size**: Below amount input. Padding 16dp.
        *   **Content**:
            *   `ListItem` (Category): `headlineContent = "Category"`, `leadingContent = Icon(Icons.Filled.Category)`, `trailingContent = Text("Select")`.
            *   `ListItem` (Wallet): `headlineContent = "Wallet"`, `leadingContent = Icon(Icons.Filled.AccountBalanceWallet)`, `trailingContent = Text("Cash")`.
            *   `ListItem` (Note): `headlineContent = "Add note"`, `leadingContent = Icon(Icons.Filled.Notes)`.
    *   **Name**: `Grid` (Number Pad)
        *   **Position & Size**: Bottom of the screen.
        *   **Content**: `TextButton`s for digits 0-9, a decimal point, and a backspace `Icon`.
*   **Interaction & Behavior**:
    *   **Action**: Tap number pad buttons to enter an amount.
    *   **Action**: Tap "Category" `ListItem`.
    *   **Navigation**: Navigate to `02_03_Select_Category`.
    *   **Action**: Tap "Wallet" `ListItem`.
    *   **Navigation**: Navigate to `02_05_Select_Wallet`.
    *   **Action**: Tap "Add note" `ListItem`.
    *   **Navigation**: Navigate to `02_04_Add_Note`.
    *   **Action**: Tap "Save" `TextButton`.
    *   **Navigation**: Save the transaction and navigate back to `02_01_Dashboard`.

---

#### **Screen 19: Select Category**
*   **Screen Name/ID**: `02_03_Select_Category`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Select Category".
    *   **Name**: `TabRow`
        *   **Position & Size**: Below `TopAppBar`.
        *   **Content**: `Tab` "Expenses", `Tab` "Income".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**: List of `ListItem` components, grouped by super-category (e.g., "Food & Drink").
    *   **Name**: `ListItem` (for each category)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**:
            *   `LeadingContent`: `Icon` for the category (e.g., `Icons.Filled.Restaurant`).
            *   `HeadlineText`: Category name (e.g., "Restaurants").
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Return to `02_02_Add_Transaction` with the selected category.

---

#### **Screen 20: Add Note**
*   **Screen Name/ID**: `02_04_Add_Note`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `TextField`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.Close`. On tap -> Navigate back without saving.
            *   `Text` (Title): "Add Note".
            *   `Actions`: `TextButton` "Save".
    *   **Name**: `TextField` (Note Input)
        *   **Position & Size**: Fills the content area. Padding 16dp.
        *   **Style**: `colors = TextFieldDefaults.colors(containerColor = Color.Transparent)`. No border/underline.
        *   **Content**: Placeholder text: "Add a note...".
*   **Interaction & Behavior**:
    *   **Action**: Enter text and tap "Save".
    *   **Navigation**: Return to `02_02_Add_Transaction` with the entered note.

---

#### **Screen 21: Select Wallet**
*   **Screen Name/ID**: `02_05_Select_Wallet`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Select Wallet".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**: List of `ListItem` components.
    *   **Name**: `ListItem` (for each wallet)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**:
            *   `LeadingContent`: `Icon(Icons.Filled.AccountBalanceWallet)`.
            *   `HeadlineText`: Wallet name (e.g., "Cash", "Bank Account").
            *   `TrailingContent`: `RadioButton` to show selection.
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Return to `02_02_Add_Transaction` with the selected wallet.

---

### Flow 3: Create Budget

#### **Screen 22: Budgets**
*   **Screen Name/ID**: `03_01_Budgets`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, content area, and `NavigationBar`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**: `Text` (Title): "Budgets". `Actions`: `IconButton` with `Icons.Filled.Add`.
    *   **Name**: `NavigationBar` (Bottom Nav)
        *   **Position & Size**: Bottom of the screen.
        *   **Content**: `NavigationBarItem` "Budgets" is selected.
*   **Interaction & Behavior**:
    *   **Action**: Tap `IconButton` `Add`.
    *   **Navigation**: Navigate to `03_02_Create_Budget`.
*   **Critical Scenarios**:
    *   **Empty State**: If no budgets exist, the content area shows:
        *   `Icon(Icons.Filled.AccountBalanceWallet, size = 64dp, tint = md.sys.color.surfaceVariant)`.
        *   `Text` headline: "Create Your First Budget".
        *   `Text` body: "Track your spending for specific categories.".
        *   `FilledButton`: "Create Budget". On tap -> Navigate to `03_02_Create_Budget`.
    *   **Populated State**: The content area is a `LazyColumn` of `Card`s, each representing a budget with its name, progress bar, and amount remaining.

---

#### **Screen 23: Create Budget**
*   **Screen Name/ID**: `03_02_Create_Budget`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back.
            *   `Text` (Title): "Create Budget".
    *   **Name**: `OutlinedTextField` (Amount)
        *   **Position & Size**: `fillMaxWidth`, padding 16dp.
        *   **Content**: Label: "Budget Amount", `keyboardType = Number`.
    *   **Name**: `ListItem` (Categories)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "Categories"`, `supportingContent = "All Expenses"`, `trailingContent = Icon(Icons.Filled.ChevronRight)`.
    *   **Name**: `ListItem` (Period)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "Period"`, `supportingContent = "Monthly"`, `trailingContent = Icon(Icons.Filled.ChevronRight)`.
    *   **Name**: `FilledButton` (Create Budget)
        *   **Position & Size**: Anchored to bottom. `fillMaxWidth`, height 56dp, margin 16dp.
        *   **Content**: "Create Budget".
*   **Interaction & Behavior**:
    *   **Action**: Tap "Categories" `ListItem`.
    *   **Navigation**: Navigate to `03_03_Select_Budget_Category`.
    *   **Action**: Tap "Period" `ListItem`.
    *   **Navigation**: Navigate to `03_04_Select_Budget_Period`.
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Save budget and navigate back to `03_01_Budgets`.

---

#### **Screen 24: Select Budget Category**
*   **Screen Name/ID**: `03_03_Select_Budget_Category`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`.
            *   `Text` (Title): "Select Categories".
            *   `Actions`: `TextButton` "Done".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills the content area.
        *   **Content**: List of `ListItem`s for each expense category.
    *   **Name**: `ListItem` (for each category)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "Category Name"`, `trailingContent = Checkbox`.
*   **Interaction & Behavior**:
    *   **Action**: Select categories, tap "Done".
    *   **Navigation**: Return to `03_02_Create_Budget`.

---

#### **Screen 25: Select Budget Period**
*   **Screen Name/ID**: `03_04_Select_Budget_Period`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`.
            *   `Text` (Title): "Select Period".
    *   **Name**: `Column`
        *   **Position & Size**: Fills the content area.
        *   **Content**: `ListItem`s with `RadioButton`s.
    *   **Name**: `ListItem` (for each period)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "Weekly"`, `trailingContent = RadioButton`. (Repeated for Monthly, Yearly, Custom).
*   **Interaction & Behavior**:
    *   **Action**: Select a period.
    *   **Navigation**: Automatically return to `03_02_Create_Budget`.

---

### Flow 4: View Analysis

#### **Screen 26: Analysis**
*   **Screen Name/ID**: `04_01_Analysis`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**: `Text` (Title): "Analysis".
    *   **Name**: `Row` (Filters)
        *   **Position & Size**: Below `TopAppBar`. `fillMaxWidth`, padding 16dp.
        *   **Content**:
            *   `FilterChip` (Time Period): "This Month".
            *   `FilterChip` (Category): "All Categories".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**:
            *   `Card` with a Pie Chart visualization of expenses by category.
            *   `Card` with a Bar Chart of income vs. expenses over time.
            *   List of `ListItem`s showing top spending categories.
    *   **Name**: `NavigationBar` (Bottom Nav)
        *   **Position & Size**: Bottom of the screen.
        *   **Content**: `NavigationBarItem` "Analysis" is selected.
*   **Interaction & Behavior**:
    *   **Action**: Tap Time Period `FilterChip`.
    *   **Navigation**: Navigate to `04_02_Select_Time_Period`.
    *   **Action**: Tap Category `FilterChip`.
    *   **Navigation**: Navigate to `04_03_Select_Category_Filter`.

---

#### **Screen 27: Select Time Period**
*   **Screen Name/ID**: `04_02_Select_Time_Period`
*   **Dimensions**: N/A (Modal Bottom Sheet)
*   **Background**: `md.sys.color.surface`
*   **Layout**: `ModalBottomSheet` with a `Column` of `ListItem`s.
*   **Components**:
    *   **Name**: `Text` (Title)
        *   **Position & Size**: Top of sheet, padding 16dp.
        *   **Style**: `md.sys.typography.titleMedium`.
        *   **Content**: "Select Time Period".
    *   **Name**: `ListItem` (e.g., "This Month")
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "This Month"`, `trailingContent = RadioButton`.
    *   (Repeated for "Last Month", "Last 3 Months", "All Time", "Custom Range").
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Dismiss sheet and return to `04_01_Analysis` with the new filter applied.

---

#### **Screen 28: Select Category Filter**
*   **Screen Name/ID**: `04_03_Select_Category_Filter`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`.
            *   `Text` (Title): "Filter by Category".
            *   `Actions`: `TextButton` "Apply".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills the content area.
        *   **Content**: List of `ListItem`s for each expense category.
    *   **Name**: `ListItem` (for each category)
        *   **Position & Size**: `fillMaxWidth`.
        *   **Content**: `headlineContent = "Category Name"`, `trailingContent = Checkbox`.
*   **Interaction & Behavior**:
    *   **Action**: Select categories, tap "Apply".
    *   **Navigation**: Return to `04_01_Analysis` with filter applied.

---

### Flow 5: Settings and Management

#### **Screen 29: More**
*   **Screen Name/ID**: `05_01_More`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen.
        *   **Content**: `Text` (Title): "More".
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills content area.
        *   **Content**:
            *   `ListItem`: `headlineContent = "My Profile"`, `leadingContent = Icon(Icons.Filled.Person)`.
            *   `ListItem`: `headlineContent = "Wallets"`, `leadingContent = Icon(Icons.Filled.AccountBalanceWallet)`.
            *   `ListItem`: `headlineContent = "Bank Accounts"`, `leadingContent = Icon(Icons.Filled.AccountBalance)`.
            *   `ListItem`: `headlineContent = "Categories"`, `leadingContent = Icon(Icons.Filled.Category)`.
            *   `ListItem`: `headlineContent = "Settings"`, `leadingContent = Icon(Icons.Filled.Settings)`.
    *   **Name**: `NavigationBar` (Bottom Nav)
        *   **Position & Size**: Bottom of the screen.
        *   **Content**: `NavigationBarItem` "More" is selected.
*   **Interaction & Behavior**:
    *   Tap "My Profile" -> Navigate to `05_02_My_Profile`.
    *   Tap "Wallets" -> Navigate to `05_03_Wallets`.
    *   Tap "Bank Accounts" -> Navigate to `05_04_Bank_Accounts`.
    *   Tap "Categories" -> Navigate to `05_05_Categories`.
    *   Tap "Settings" -> Navigate to `05_06_App_Settings`.

---

#### **Screen 30: My Profile**
*   **Screen Name/ID**: `05_02_My_Profile`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Content**: `IconButton` (Back), `Text` (Title): "My Profile".
    *   **Name**: `Column` (Content)
        *   **Position & Size**: Padding 16dp.
        *   **Content**:
            *   `ListItem`: `headlineContent = "Name"`, `supportingContent = "User's Name"`.
            *   `ListItem`: `headlineContent = "Email"`, `supportingContent = "user@email.com"`.
            *   `TextButton`: "Log Out".
*   **Interaction & Behavior**: View and edit profile details.

---

#### **Screen 31: Wallets**
*   **Screen Name/ID**: `05_03_Wallets`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `FloatingActionButton`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Content**: `IconButton` (Back), `Text` (Title): "Wallets".
    *   **Name**: `LazyColumn`
        *   **Content**: List of `ListItem`s, each showing a wallet name and its balance.
    *   **Name**: `FloatingActionButton`
        *   **Content**: `Icon(Icons.Filled.Add)`.
*   **Interaction & Behavior**: Tap FAB to add a new wallet. Tap a list item to edit an existing wallet.

---

#### **Screen 32: Bank Accounts**
*   **Screen Name/ID**: `05_04_Bank_Accounts`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Content**: `IconButton` (Back), `Text` (Title): "Bank Accounts".
    *   **Name**: `LazyColumn`
        *   **Content**: List of `ListItem`s, each showing a connected bank and its status.
    *   **Name**: `FilledButton` (Connect a bank)
        *   **Position & Size**: Anchored to bottom, margin 16dp.
        *   **Content**: "Connect a bank".
*   **Interaction & Behavior**:
    *   **Action**: Tap `FilledButton`.
    *   **Navigation**: Navigate to `06_01_Select_Country_Settings`.

---

#### **Screen 33: Categories**
*   **Screen Name/ID**: `05_05_Categories`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`, `TabRow`, and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Content**: `IconButton` (Back), `Text` (Title): "Categories". `Actions`: `IconButton(Icons.Filled.Add)`.
    *   **Name**: `TabRow`
        *   **Content**: `Tab` "Expenses", `Tab` "Income".
    *   **Name**: `LazyColumn`
        *   **Content**: List of user-created and default categories.
*   **Interaction & Behavior**: View, add, or edit transaction categories.

---

#### **Screen 34: App Settings**
*   **Screen Name/ID**: `05_06_App_Settings`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Content**: `IconButton` (Back), `Text` (Title): "Settings".
    *   **Name**: `LazyColumn`
        *   **Content**:
            *   `ListItem`: `headlineContent = "Notifications"`, `trailingContent = Switch`.
            *   `ListItem`: `headlineContent = "Main Currency"`, `supportingContent = "USD"`.
            *   `ListItem`: `headlineContent = "Theme"`, `supportingContent = "System Default"`.
            *   `ListItem`: `headlineContent = "Passcode Lock"`, `trailingContent = Switch`.
*   **Interaction & Behavior**: Adjust application settings.

---

### Flow 6: Connect Bank Account from Settings

#### **Screen 35: Select Country (Settings)**
*   **Screen Name/ID**: `06_01_Select_Country_Settings`
*   **Description**: This screen is functionally identical to `01_12_Select_Country_Onboarding` but is initiated from the settings flow. The context and back-stack navigation are different.
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components**:
    *   **Name**: `TopAppBar`
        *   **Position & Size**: Top of the screen. `fillMaxWidth`, height 64dp.
        *   **Content**:
            *   `IconButton` (Navigation Icon): `Icons.Filled.ArrowBack`. On tap -> Navigate back to `05_04_Bank_Accounts`.
            *   `Text` (Title): "Select Country" (`style = md.sys.typography.titleLarge`).
    *   **Name**: `OutlinedTextField` (Search)
        *   **Position & Size**: `fillMaxWidth`. Padding 16dp horizontal, 8dp vertical.
        *   **Content**: Label: "Search country". Leading icon: `Icons.Filled.Search`.
    *   **Name**: `LazyColumn`
        *   **Position & Size**: Fills remaining space.
        *   **Content**: List of `ListItem` components for each country.
*   **Interaction & Behavior**:
    *   **Action**: Tap a `ListItem`.
    *   **Navigation**: Navigate to `01_13_Select_Bank`. The subsequent flow (Select Bank, Bank Login, etc.) is reused from the onboarding flow.

---

## V. Critical Scenarios & States

*   **Error States**:
    *   **Text Field Validation**: Invalid input in `OutlinedTextField` components will trigger an error state. The outline, label, and supporting text will turn `md.sys.color.error`. A descriptive error message will appear as supporting text (e.g., "Invalid email format").
    *   **Network Errors**: If an API call fails due to no internet, a `Snackbar` will appear at the bottom of the screen.
        *   **Style**: `containerColor = md.sys.color.inverseSurface`, `contentColor = md.sys.color.inverseOnSurface`.
        *   **Content**: "No internet connection. Please try again."
        *   **Action**: Optional "Retry" `TextButton`.
*   **Empty States**:
    *   Screens that display lists of user-generated content (e.g., `02_01_Dashboard`, `03_01_Budgets`, `05_04_Bank_Accounts`) must have a dedicated empty state.
    *   **Layout**: Centered `Column` with an `Icon`, a `Text` headline, a `Text` body, and a primary `FilledButton` CTA.
    *   **Example (Budgets)**: `Icon(Icons.Filled.AccountBalanceWallet)`, Headline: "No Budgets Yet", Body: "Create budgets to keep your spending in check.", Button: "Create a Budget".
*   **Loading States**:
    *   **Full-Screen Loading**: For initial data loads or screen transitions that require fetching data (e.g., after login), a centered `CircularProgressIndicator` is displayed over a semi-transparent scrim.
    *   **Inline Loading**: When refreshing content within a list (e.g., pull-to-refresh on the Dashboard), a `CircularProgressIndicator` will appear at the top of the list.
    *   **Button Loading**: When a `FilledButton` triggers an action that requires a network call (e.g., "Save"), the button text is replaced by a `CircularProgressIndicator` (size 24x24dp) and the button is disabled until the operation completes.

---
