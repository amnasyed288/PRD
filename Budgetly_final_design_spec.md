# Budgetly - Android Design Specification

This document provides a complete and hyper-detailed design specification for the Budgetly Android application, based on the provided app flow tree. It is intended to be used by an AI design generation model to create a high-fidelity, interactive prototype.

## I. Global Specifications

### Platform
- **Target Platform:** Android Mobile App
- **API Level:** Target API 34 (Android 14)

### Design System
- **System:** Material Design 3
- **Theming:** Supports Light and Dark modes. Implements dynamic color (Material You) where available, falling back to the defined brand theme.
- **Density:** Default screen density.

### Colors
- **Seed Color:** `#3662E0` (Budgetly Blue)
- **Light Theme Color Roles:**
  - `md.sys.color.primary`: `#3662E0`
  - `md.sys.color.onPrimary`: `#FFFFFF`
  - `md.sys.color.primaryContainer`: `#DCE1FF`
  - `md.sys.color.onPrimaryContainer`: `#001B3F`
  - `md.sys.color.secondary`: `#575E71`
  - `md.sys.color.onSecondary`: `#FFFFFF`
  - `md.sys.color.secondaryContainer`: `#DBE2F9`
  - `md.sys.color.onSecondaryContainer`: `#141B2C`
  - `md.sys.color.tertiary`: `#715573`
  - `md.sys.color.onTertiary`: `#FFFFFF`
  - `md.sys.color.tertiaryContainer`: `#FBD7FC`
  - `md.sys.color.onTertiaryContainer`: `#29132D`
  - `md.sys.color.error`: `#BA1A1A`
  - `md.sys.color.onError`: `#FFFFFF`
  - `md.sys.color.errorContainer`: `#FFDAD6`
  - `md.sys.color.onErrorContainer`: `#410002`
  - `md.sys.color.background`: `#FEFBFF`
  - `md.sys.color.onBackground`: `#1B1B1F`
  - `md.sys.color.surface`: `#FEFBFF`
  - `md.sys.color.onSurface`: `#1B1B1F`
  - `md.sys.color.surfaceVariant`: `#E1E2EC`
  - `md.sys.color.onSurfaceVariant`: `#44474F`
  - `md.sys.color.outline`: `#757780`
  - `md.sys.color.inverseSurface`: `#2F3033`
  - `md.sys.color.inverseOnSurface`: `#F2F0F4`
- **Dark Theme Color Roles:**
  - `md.sys.color.primary`: `#B5C4FF`
  - `md.sys.color.onPrimary`: `#002F65`
  - `md.sys.color.primaryContainer`: `#1948C7`
  - `md.sys.color.onPrimaryContainer`: `#DCE1FF`
  - `md.sys.color.secondary`: `#BFC6DC`
  - `md.sys.color.onSecondary`: `#293041`
  - `md.sys.color.secondaryContainer`: `#3F4759`
  - `md.sys.color.onSecondaryContainer`: `#DBE2F9`
  - `md.sys.color.tertiary`: `#DEBBDF`
  - `md.sys.color.onTertiary`: `#402843`
  - `md.sys.color.tertiaryContainer`: `#583E5B`
  - `md.sys.color.onTertiaryContainer`: `#FBD7FC`
  - `md.sys.color.error`: `#FFB4AB`
  - `md.sys.color.onError`: `#690005`
  - `md.sys.color.errorContainer`: `#93000A`
  - `md.sys.color.onErrorContainer`: `#FFDAD6`
  - `md.sys.color.background`: `#1B1B1F`
  - `md.sys.color.onBackground`: `#E4E2E6`
  - `md.sys.color.surface`: `#1B1B1F`
  - `md.sys.color.onSurface`: `#E4E2E6`
  - `md.sys.color.surfaceVariant`: `#44474F`
  - `md.sys.color.onSurfaceVariant`: `#C5C6D0`
  - `md.sys.color.outline`: `#8E9099`
  - `md.sys.color.inverseSurface`: `#E4E2E6`
  - `md.sys.color.inverseOnSurface`: `#1B1B1F`

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

### Flow 1: Authentication & Onboarding

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
    - **Content:** Budgetly app logo vector.
  - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered horizontally. Margin top: 32dp. Size: 48dp x 48dp.
    - **Style:** Color: `md.sys.color.primary`. Stroke width: 4dp.
    - **Content:** N/A.
- **Interaction & Behavior:**
  - **Interactions:** On successful initialization and authentication check, the app automatically navigates.
  - **Navigation:**
    - `On first open -> Navigate to 01_02_Welcome_&_Value_Prop_Screen`.
    - `If logged out -> Navigate to 01_04_Sign_In_Screen`.
    - `If logged in -> Navigate to 02_01_Dashboard_Screen`.
  - **Animations:** `MaterialFade` transition.

---

#### Screen 1.2: Welcome & Value Prop Screen
- **Screen Name/ID:** `01_02_Welcome_&_Value_Prop_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` layout with `verticalArrangement = Arrangement.SpaceBetween`. Padding: 24dp on all sides.
- **Component Specifications:**
  - **Name:** `Column` (Content Container)
    - **Position & Size:** Aligned to top-center. Margin top: 64dp.
    - **Layout:** `Column` with `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Components:**
      - **Name:** `Image` (App Logo)
        - **Position & Size:** Width: 96dp, Height: 96dp.
        - **Style:** No tint.
        - **Content:** Budgetly app logo vector.
      - **Name:** `Text` (Headline)
        - **Position & Size:** Centered horizontally. Margin top: 24dp.
        - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text align: Center.
        - **Content:** "Capture Every Expense, Effortlessly"
      - **Name:** `Text` (Body)
        - **Position & Size:** Centered horizontally. Margin top: 16dp.
        - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
        - **Content:** "From SMS and bank sync to voice notes and receipts, Budgetly is the smartest way to track your spending."
  - **Name:** `Column` (Button Container)
    - **Position & Size:** Aligned to bottom-center. Margin bottom: 32dp.
    - **Layout:** `Column` with `verticalArrangement = Arrangement.spacedBy(16dp)`.
    - **Components:**
      - **Name:** `FilledButton` (Get Started)
        - **Position & Size:** `fillMaxWidth()`. Height: 52dp.
        - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
        - **Content:** Text label: "Get Started" with style `md.sys.typography.labelLarge`.
      - **Name:** `TextButton` (I already have an account)
        - **Position & Size:** `fillMaxWidth()`. Height: 52dp.
        - **Style:** Content Color: `md.sys.color.primary`.
        - **Content:** Text label: "I already have an account" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton` (Get Started): `On tap -> Navigate to 01_03_Sign_Up_Screen`.
    - `TextButton` (I already have an account): `On tap -> Navigate to 01_04_Sign_In_Screen`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 1.3: Sign Up Screen
- **Screen Name/ID:** `01_03_Sign_Up_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Create Your Account" and style `md.sys.typography.titleLarge`.
  - **Name:** `OutlinedTextField` (Email)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Shape: `ShapeDefaults.Medium`.
    - **Content:** Label: "Email". `singleLine = true`. `keyboardType = KeyboardType.Email`.
  - **Name:** `OutlinedTextField` (Password)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". `singleLine = true`. `keyboardType = KeyboardType.Password`.
  - **Name:** `FilledButton` (Sign Up)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until fields are valid.
    - **Content:** Text label: "Sign Up" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Sign In)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Already have an account? Sign In" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 01_05_Onboarding_Connect_Bank_Intro`.
    - `TextButton`: `On tap -> Navigate to 01_04_Sign_In_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 1.4: Sign In Screen
- **Screen Name/ID:** `01_04_Sign_In_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout. Padding: 16dp horizontally.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: `Text` with content "Welcome Back" and style `md.sys.typography.titleLarge`.
  - **Name:** `OutlinedTextField` (Email)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp.
    - **Style:** Shape: `ShapeDefaults.Medium`.
    - **Content:** Label: "Email". `singleLine = true`. `keyboardType = KeyboardType.Email`.
  - **Name:** `OutlinedTextField` (Password)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 16dp.
    - **Style:** Shape: `ShapeDefaults.Medium`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". `singleLine = true`. `keyboardType = KeyboardType.Password`.
  - **Name:** `FilledButton` (Sign In)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 24dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`. Disabled until fields are valid.
    - **Content:** Text label: "Sign In" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Sign Up)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Don't have an account? Sign Up" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
    - `TextButton`: `On tap -> Navigate to 01_03_Sign_Up_Screen`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 1.5: Onboarding - Connect Bank Intro
- **Screen Name/ID:** `01_05_Onboarding_Connect_Bank_Intro`
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
    - **Content:** "Automate Your Tracking"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "Connect your bank to automatically sync transactions and always stay up-to-date. It's secure and read-only."
  - **Name:** `FilledButton` (Connect Bank Account)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Connect Bank Account" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Skip for Now)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Skip for Now" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 07_02_Bank_Connection_Institution_Selection_Screen`.
    - `TextButton`: `On tap -> Navigate to 01_06_Onboarding_SMS_Parser_Intro`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 1.6: Onboarding - SMS Parser Intro
- **Screen Name/ID:** `01_06_Onboarding_SMS_Parser_Intro`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` layout, `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`. Padding: 24dp.
- **Component Specifications:**
  - **Name:** `Icon`
    - **Position & Size:** Centered. Size: 64dp x 64dp.
    - **Style:** `imageVector = Icons.Filled.Sms`. Tint: `md.sys.color.primary`.
    - **Content:** Content description: "SMS message".
  - **Name:** `Text` (Headline)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`. Text align: Center.
    - **Content:** "Capture Expenses from SMS"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "Allow Budgetly to read your transactional SMS messages to automatically create expense entries for you."
  - **Name:** `FilledButton` (Enable SMS Parsing)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Enable SMS Parsing" with style `md.sys.typography.labelLarge`.
  - **Name:** `TextButton` (Maybe Later)
    - **Position & Size:** Centered horizontally. Margin top: 16dp.
    - **Style:** Content Color: `md.sys.color.primary`.
    - **Content:** Text label: "Maybe Later" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Show 01_07_System_SMS_Permission_Dialog`.
    - `TextButton`: `On tap -> Navigate to 01_08_Onboarding_Complete`.
  - **Animations:** `MaterialSharedAxis.X` forward transition.

---

#### Screen 1.7: System SMS Permission Dialog
- **Screen Name/ID:** `01_07_System_SMS_Permission_Dialog`
- **Dimensions:** System Dialog.
- **Background:** System default.
- **Layout:** Standard Android runtime permission dialog.
- **Component Specifications:**
  - **Name:** `System Permission Dialog`
    - **Content:** Text explaining the app wants to "Read your text messages (SMS)". Buttons for "Allow" and "Deny".
- **Interaction & Behavior:**
  - **Interactions:**
    - `User taps 'Allow'`: `On tap -> Navigate to 01_08_Onboarding_Complete`.
    - `User taps 'Deny'`: `On tap -> Navigate to 01_08_Onboarding_Complete`.
  - **Animations:** System default.

---

#### Screen 1.8: Onboarding - Complete
- **Screen Name/ID:** `01_08_Onboarding_Complete`
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
    - **Content:** "You're All Set!"
  - **Name:** `Text` (Body)
    - **Position & Size:** Centered horizontally. Margin top: 8dp.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text align: Center.
    - **Content:** "You're ready to start taking control of your finances."
  - **Name:** `FilledButton` (Let's Go!)
    - **Position & Size:** `fillMaxWidth()`. Margin top: 32dp. Height: 52dp.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Shape: `ShapeDefaults.Full`.
    - **Content:** Text label: "Let's Go!" with style `md.sys.typography.labelLarge`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
  - **Animations:** `MaterialSharedAxis.Z` transition.

---

### Flow 2: Main App & Navigation

---

#### Screen 2.1: Dashboard Screen
- **Screen Name/ID:** `02_01_Dashboard_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `FloatingActionButton`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `fillMaxWidth()`. Height: 56dp.
    - **Style:** Container Color: `md.sys.color.surface`. `scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()`.
    - **Content:**
      - **Title:** `Text` with content "Dashboard" and style `md.sys.typography.titleLarge`.
      - **Actions:**
        - `IconButton` with `Icons.Filled.Inbox` and a `Badge` if there are items to review. Content description: "Review Inbox".
        - `IconButton` with `Icons.Filled.Settings`. Content description: "Settings".
  - **Name:** `LazyColumn` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp horizontal.
    - **Content:**
      - `ListSubheader`: `Text` "Smart Templates".
      - `LazyRow` of `SuggestionChip` components (e.g., "Coffee", "Groceries", "Fuel").
      - `ListSubheader`: `Text` "Recent Transactions".
      - `ListItem` for each transaction:
        - **Leading Content:** `Icon` for the category.
        - **Headline Content:** `Text` with merchant name.
        - **Supporting Content:** `Text` with category name. A `Text` with "Pending sync" if offline.
        - **Trailing Content:** `Text` with amount.
  - **Name:** `FloatingActionButton` (FAB)
    - **Position & Size:** Bottom right corner.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`.
    - **Content:** Icon: `Icons.Filled.Add`. Content description: "Add Transaction".
- **Interaction & Behavior:**
  - **Interactions:**
    - `FAB`: `On tap -> Show 02_02_Add_Transaction_Speed_Dial_Menu`.
    - `Inbox IconButton`: `On tap -> Navigate to 05_01_Review_Inbox_Screen`.
    - `Settings IconButton`: `On tap -> Navigate to 06_01_Settings_Screen`.
    - `Transaction ListItem`: `On tap -> Navigate to 02_04_Transaction_Detail_Screen`.
    - `SuggestionChip`: `On tap -> Create transaction, Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
  - **Animations:** `MaterialContainerTransform` for FAB expansion. `MaterialSharedAxis.Z` for Settings.

---

#### Screen 2.2: Add Transaction Speed Dial Menu
- **Screen Name/ID:** `02_02_Add_Transaction_Speed_Dial_Menu`
- **Dimensions:** Overlay on `02_01_Dashboard_Screen`.
- **Background:** Semi-transparent scrim (`md.sys.color.scrim` with alpha).
- **Layout:** `Column` of `ExtendedFloatingActionButton`s positioned above the main FAB.
- **Component Specifications:**
  - **Name:** `Column` (Speed Dial Actions)
    - **Position & Size:** Aligned to bottom-right, above the main FAB.
    - **Layout:** `Column` with `verticalArrangement = Arrangement.spacedBy(16dp)`.
    - **Components:**
      - `ExtendedFloatingActionButton` (Scan QR): Icon `Icons.Filled.QrCodeScanner`, Text "Scan QR".
      - `ExtendedFloatingActionButton` (Attach & Parse): Icon `Icons.Filled.AttachFile`, Text "Attach & Parse".
      - `ExtendedFloatingActionButton` (Use Voice): Icon `Icons.Filled.Mic`, Text "Use Voice".
      - `ExtendedFloatingActionButton` (Add Manually): Icon `Icons.Filled.Edit`, Text "Add Manually".
  - **Name:** `FloatingActionButton` (Close)
    - **Position & Size:** Same position as the original FAB.
    - **Content:** Icon: `Icons.Filled.Close`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Add Manually FAB`: `On tap -> Navigate to 03_01_Add_Transaction_Form_Screen`.
    - `Use Voice FAB`: `On tap -> Show 03_03_Voice_Input_Bottom_Sheet`.
    - `Attach & Parse FAB`: `On tap -> Show 03_06_System_File_Picker`.
    - `Scan QR FAB`: `On tap -> Navigate to 03_09_QR_Scan_Screen`.
    - `Close FAB` or tap on scrim: `On tap -> Dismiss menu, return to 02_01_Dashboard_Screen`.
  - **Animations:** `MaterialFade` for scrim, `MaterialSharedAxis.Y` for FABs animating in.

---

#### Screen 2.3: Dashboard Screen with Undo Snackbar
- **Screen Name/ID:** `02_03_Dashboard_Screen_with_Undo_Snackbar`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** Same as `02_01_Dashboard_Screen`.
- **Component Specifications:**
  - **Name:** `Snackbar`
    - **Position & Size:** Bottom of the screen.
    - **Style:** Container color `md.sys.color.inverseSurface`, content color `md.sys.color.inverseOnSurface`.
    - **Content:** Message: "Transaction added." Action label: "Undo".
    - **Behavior:** Automatically dismisses after 5 seconds.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Undo Button`: `On tap -> Delete the last transaction, dismiss snackbar, stay on 02_01_Dashboard_Screen`.
    - `Snackbar timeout`: `After 5 seconds -> Dismiss snackbar, stay on 02_01_Dashboard_Screen`.

---

#### Screen 2.4: Transaction Detail Screen
- **Screen Name/ID:** `02_04_Transaction_Detail_Screen`
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
      - **Actions:**
        - `IconButton` with `Icons.Filled.Edit`. Content description: "Edit".
        - `IconButton` with `Icons.Filled.Delete`. Content description: "Delete".
  - **Name:** `Column` (Content)
    - **Position & Size:** Fills the content area. Padding: 16dp.
    - **Content:** A series of `ListItem`s for details.
      - `ListItem` (Amount): Headline `Text` "Amount", Supporting `Text` "-$5.75".
      - `ListItem` (Merchant): Headline `Text` "Merchant", Supporting `Text` "Starbucks".
      - `ListItem` (Category): Headline `Text` "Category", Supporting `Text` "Coffee Shops".
      - `ListItem` (Date): Headline `Text` "Date", Supporting `Text` "October 29, 2025".
      - `ListItem` (Source): Headline `Text` "Source", Supporting `Text` "Manual Entry".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
    - `Edit IconButton`: `On tap -> Navigate to 03_02_Edit_Transaction_Form_Screen`.
    - `Delete IconButton`: `On tap -> Show 02_05_Delete_Transaction_Confirmation_Dialog`.
  - **Animations:** `MaterialSharedAxis.X` for navigation.

---

#### Screen 2.5: Delete Transaction Confirmation Dialog
- **Screen Name/ID:** `02_05_Delete_Transaction_Confirmation_Dialog`
- **Dimensions:** Dialog, typically 280dp width.
- **Background:** `md.sys.color.surface` with elevation.
- **Layout:** `AlertDialog` component.
- **Component Specifications:**
  - **Name:** `AlertDialog`
    - **Style:** Shape: `ShapeDefaults.ExtraLarge`.
    - **Content:**
      - **Icon:** `Icon` with `Icons.Filled.DeleteForever`, tint `md.sys.color.error`.
      - **Title:** `Text` with content "Delete Transaction?".
      - **Text:** `Text` with content "This action cannot be undone. Are you sure you want to delete this transaction?".
      - **Confirm Button:** `TextButton` with text "Delete".
      - **Dismiss Button:** `TextButton` with text "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Delete Button`: `On tap -> Dismiss dialog, Navigate to 02_01_Dashboard_Screen`.
    - `Cancel Button`: `On tap -> Dismiss dialog, Stay on 02_04_Transaction_Detail_Screen`.
  - **Animations:** `MaterialFade`.

---

### Flow 3: Manual Capture Flows

---

#### Screen 3.1: Add Transaction Form Screen
- **Screen Name/ID:** `03_01_Add_Transaction_Form_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
      - **Title:** `Text` with content "Add Transaction".
  - **Name:** `Column` (Form)
    - **Position & Size:** Padding 16dp.
    - **Content:**
      - `OutlinedTextField` (Amount): Label "Amount", `keyboardType = KeyboardType.Decimal`.
      - `OutlinedTextField` (Merchant): Label "Merchant (Optional)".
      - `ExposedDropdownMenuBox` (Category): Label "Category".
      - `DatePicker` input field (Date): Label "Date".
  - **Name:** `FilledButton` (Save)
    - **Position & Size:** `fillMaxWidth()`. Aligned to bottom. Margin: 16dp. Height: 52dp.
    - **Content:** Text label: "Save".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
    - `Save Button`: `On tap -> If valid, Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`. If invalid, show error state on required fields.
  - **Animations:** `MaterialSharedAxis.Y` (modal-like).

---

#### Screen 3.2: Edit Transaction Form Screen
- **Screen Name/ID:** `03_02_Edit_Transaction_Form_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `Column`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
      - **Title:** `Text` with content "Edit Transaction".
  - **Name:** `Column` (Form)
    - **Position & Size:** Padding 16dp.
    - **Content:** Same as `03_01_Add_Transaction_Form_Screen`, but pre-filled with existing data.
  - **Name:** `FilledButton` (Save Changes)
    - **Position & Size:** `fillMaxWidth()`. Aligned to bottom. Margin: 16dp. Height: 52dp.
    - **Content:** Text label: "Save Changes".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Navigation Icon`: `On tap -> Navigate to 02_04_Transaction_Detail_Screen`.
    - `Save Changes Button`: `On tap -> Navigate to 02_04_Transaction_Detail_Screen`.
  - **Animations:** `MaterialSharedAxis.X`.

---

#### Screen 3.3: Voice Input Bottom Sheet
- **Screen Name/ID:** `03_03_Voice_Input_Bottom_Sheet`
- **Dimensions:** Modal Bottom Sheet.
- **Background:** `md.sys.color.surfaceContainer`.
- **Layout:** `Column` with `horizontalAlignment = Alignment.CenterHorizontally`. Padding 24dp.
- **Component Specifications:**
  - **Name:** `Text` (Title)
    - **Style:** `md.sys.typography.titleLarge`.
    - **Content:** "What did you spend?"
  - **Name:** `Text` (Instruction)
    - **Style:** `md.sys.typography.bodyMedium`, `color = md.sys.color.onSurfaceVariant`. Margin top 8dp.
    - **Content:** "e.g., 'Spent 500 on petrol' or type it below."
  - **Name:** `Icon` (Microphone)
    - **Position & Size:** 64dp x 64dp. Margin 32dp.
    - **Style:** `tint = md.sys.color.primary`. Pulsating animation while listening.
    - **Content:** `Icons.Filled.Mic`.
  - **Name:** `OutlinedTextField` (Text Input)
    - **Position & Size:** `fillMaxWidth()`.
    - **Content:** Placeholder "Or type here...".
- **Interaction & Behavior:**
  - **Interactions:**
    - `On successful speech recognition`: `Navigate to 03_04_NL_Parse_Confirmation_Screen`.
    - `On text input submission`: `Navigate to 03_04_NL_Parse_Confirmation_Screen`.
    - `On dismiss`: `Navigate to 02_01_Dashboard_Screen`.
  - **Animations:** `MaterialFade`.

---

#### Screen 3.4: NL Parse Confirmation Screen
- **Screen Name/ID:** `03_04_NL_Parse_Confirmation_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with padding 24dp.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Confirm Transaction".
  - **Name:** `Card` (Parsed Details)
    - **Style:** `ElevatedCard`.
    - **Content:** `ListItem`s showing parsed Amount, Merchant, and Category.
  - **Name:** `Card` (Low Confidence Warning)
    - **Style:** `FilledCard` with `containerColor = md.sys.color.tertiaryContainer`.
    - **Content:** `Text` "We weren't sure about the category. Please check if it's correct."
    - **Visibility:** Only visible in 'yellow state'.
  - **Name:** `Row` (Action Buttons)
    - **Position & Size:** `fillMaxWidth()`. Margin top 24dp.
    - **Content:**
      - `OutlinedButton` (Edit Details): `modifier = Modifier.weight(1f)`.
      - `FilledButton` (Confirm): `modifier = Modifier.weight(1f)`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Confirm Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Edit Details Button`: `On tap -> Navigate to 03_05_Edit_Parsed_Transaction_Screen`.
  - **Animations:** `MaterialSharedAxis.X`.

---

#### Screen 3.5: Edit Parsed Transaction Screen
- **Screen Name/ID:** `03_05_Edit_Parsed_Transaction_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a mini-form.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`.
      - **Title:** `Text` "Edit Details".
  - **Name:** `Column` (Mini-Form)
    - **Position & Size:** Padding 16dp.
    - **Content:** `OutlinedTextField` for Amount, Merchant, and a dropdown for Category, pre-filled with parsed data.
  - **Name:** `FilledButton` (Save)
    - **Position & Size:** Aligned to bottom. Margin 16dp.
    - **Content:** "Save".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Save Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Close Icon`: `On tap -> Navigate to 03_04_NL_Parse_Confirmation_Screen`.
  - **Animations:** `MaterialSharedAxis.Y`.

---

#### Screen 3.6: System File Picker
- **Screen Name/ID:** `03_06_System_File_Picker`
- **Dimensions:** System UI.
- **Background:** System default.
- **Layout:** Standard Android file/document picker.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Selects image/PDF receipt`: `Navigate to 03_07_Parse_Preview_Screen_Image_PDF`.
    - `Selects CSV/PDF statement`: `Navigate to 03_08_Parse_Preview_Screen_CSV_Statement`.
    - `Cancels`: `Navigate to 02_01_Dashboard_Screen`.

---

#### Screen 3.7: Parse Preview Screen (Image/PDF)
- **Screen Name/ID:** `03_07_Parse_Preview_Screen_Image_PDF`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Column` with an image preview and a form.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Confirm from Receipt".
  - **Name:** `Image` (Receipt Preview)
    - **Position & Size:** `fillMaxWidth()`, `height = 300dp`.
  - **Name:** `Column` (Parsed Data Form)
    - **Content:** `OutlinedTextField`s for Amount, Merchant, Date. Tapping a field highlights the corresponding area on the image preview.
  - **Name:** `Card` (Parse Failure)
    - **Content:** `Text` "Couldn't read the receipt." and a `FilledButton` "Fix Manually".
    - **Visibility:** Only on parse failure.
  - **Name:** `FilledButton` (Save)
    - **Position & Size:** Aligned to bottom. Margin 16dp.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Save Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Fix Manually Button`: `On tap -> Navigate to 03_01_Add_Transaction_Form_Screen`.
  - **Animations:** `MaterialSharedAxis.X`.

---

#### Screen 3.8: Parse Preview Screen (CSV/Statement)
- **Screen Name/ID:** `03_08_Parse_Preview_Screen_CSV_Statement`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Import Transactions".
  - **Name:** `LazyColumn` (Transaction Rows)
    - **Content:** `ListItem` for each row in the CSV/statement.
      - **Leading Content:** `Checkbox`.
      - **Headline Content:** `Text` with description.
      - **Trailing Content:** `Text` with amount.
      - **Supporting Content:** `Chip` with "Possible duplicate" if flagged.
  - **Name:** `FilledButton` (Import X Transactions)
    - **Position & Size:** Aligned to bottom. Margin 16dp.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Import Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Checkbox`: Toggles inclusion of the row.
  - **Animations:** `MaterialSharedAxis.X`.

---

#### Screen 3.9: QR Scan Screen
- **Screen Name/ID:** `03_09_QR_Scan_Screen`
- **Dimensions:** 393x852dp
- **Background:** Black.
- **Layout:** Camera preview fills the screen with an overlay.
- **Component Specifications:**
  - **Name:** `CameraPreview`
  - **Name:** `Box` (Overlay)
    - **Content:** A semi-transparent overlay with a clear square in the center for scanning.
  - **Name:** `TextButton` (Enter Manually)
    - **Position & Size:** Bottom center.
- **Interaction & Behavior:**
  - **Interactions:**
    - `On successful scan`: `Navigate to 03_10_QR_Scan_Confirmation_Screen`.
    - `Enter Manually Button`: `On tap -> Navigate to 03_01_Add_Transaction_Form_Screen`.
    - `Back Navigation`: `On tap -> Navigate to 02_01_Dashboard_Screen`.

---

#### Screen 3.10: QR Scan Confirmation Screen
- **Screen Name/ID:** `03_10_QR_Scan_Confirmation_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** Similar to `03_04_NL_Parse_Confirmation_Screen`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Confirm Scanned Data".
  - **Name:** `Card` (Pre-filled Details)
    - **Content:** `ListItem`s showing Amount, Merchant, etc.
  - **Name:** `Row` (Action Buttons)
    - **Content:** `OutlinedButton` "Edit", `FilledButton` "Save".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Save Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Edit Button`: `On tap -> Navigate to 03_05_Edit_Parsed_Transaction_Screen`.

---

### Flow 4: Home Screen Widget & Share Sheet Capture

---

#### Screen 4.1: Home Screen Widget
- **Screen Name/ID:** `04_01_Home_Screen_Widget`
- **Dimensions:** Android App Widget (e.g., 4x2).
- **Background:** `md.sys.color.surfaceContainer`.
- **Layout:** `Column` layout.
- **Component Specifications:**
  - **Name:** `TextField` (Amount)
  - **Name:** `Dropdown` (Category)
  - **Name:** `Button` (Log)
- **Interaction & Behavior:**
  - **Interactions:**
    - `Log Button`: `On tap -> Trigger 04_02_App_Quick_Add_Confirmation`.
    - `Tap widget background`: `On tap -> Navigate to 02_01_Dashboard_Screen`.

---

#### Screen 4.2: App Quick Add Confirmation
- **Screen Name/ID:** `04_02_App_Quick_Add_Confirmation`
- **Dimensions:** System Toast.
- **Layout:** A short-lived system toast message.
- **Component Specifications:**
  - **Name:** `Toast`
    - **Content:** "Transaction logged".
- **Interaction & Behavior:**
  - **Interactions:** `After showing toast -> Return to 08_01_Home_Screen`.

---

#### Screen 4.3: OS Share Sheet
- **Screen Name/ID:** `04_03_OS_Share_Sheet`
- **Dimensions:** System UI.
- **Layout:** Standard Android share sheet.
- **Interaction & Behavior:**
  - **Interactions:** `User shares text/image to Budgetly -> Navigate to 04_04_Chat_Share_Confirmation_Screen`.

---

#### Screen 4.4: Chat Share Confirmation Screen
- **Screen Name/ID:** `04_04_Chat_Share_Confirmation_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** Similar to `03_04_NL_Parse_Confirmation_Screen`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "Confirm from Chat".
  - **Name:** `Card` (Original Content)
    - **Content:** `Text` showing the shared text/image.
  - **Name:** `Card` (Parsed Details)
    - **Content:** `ListItem`s for Amount, Merchant, Category.
  - **Name:** `Chip` (Potential IOU)
    - **Content:** "Potential IOU". Visible if keywords like "owe" or "lend" are detected.
  - **Name:** `Row` (Action Buttons)
    - **Content:** `OutlinedButton` "Edit", `FilledButton` "Confirm", `TextButton` "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Confirm Button`: `On tap -> Navigate to 02_03_Dashboard_Screen_with_Undo_Snackbar`.
    - `Edit Button`: `On tap -> Navigate to 03_05_Edit_Parsed_Transaction_Screen`.
    - `Cancel Button`: `On tap -> Close app, return to 04_03_OS_Share_Sheet`.

---

### Flow 5: Review Inbox Management

---

#### Screen 5.1: Review Inbox Screen
- **Screen Name/ID:** `05_01_Review_Inbox_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a stack of swipeable cards.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:**
      - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
      - **Title:** `Text` "Review Inbox".
      - **Actions:** `IconButton` with `Icons.Filled.Add`.
  - **Name:** `Box` (Card Stack)
    - **Layout:** A stack of `Card` components. Only the top card is interactive.
    - **Card Content:** Shows parsed transaction details (Amount, Merchant, Source Icon).
- **Interaction & Behavior:**
  - **Interactions:**
    - `Swipe Right`: Confirms transaction, animates card away, shows next card.
    - `Swipe Left`: Navigates to `05_02_Review_Item_Edit_Screen` for the current card.
    - `Tap Card`: Navigates to `05_03_Review_Item_Detail_Screen`.
    - `Long-press Card`: Shows a context menu with a "Delete" option.
    - `Add IconButton`: `On tap -> Navigate to 03_01_Add_Transaction_Form_Screen`.
    - `Back Navigation`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
    - `On last item resolved`: `Navigate to 05_04_Review_Inbox_Zero_Screen`.

---

#### Screen 5.2: Review Item Edit Screen
- **Screen Name/ID:** `05_02_Review_Item_Edit_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** Same as `03_02_Edit_Transaction_Form_Screen`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Save Button`: `On tap -> Navigate to 05_01_Review_Inbox_Screen`.
    - `Cancel Button`: `On tap -> Navigate to 05_01_Review_Inbox_Screen`.

---

#### Screen 5.3: Review Item Detail Screen
- **Screen Name/ID:** `05_03_Review_Item_Detail_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and action buttons at the bottom.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Review Item".
  - **Name:** `Column` (Details)
    - **Content:** `ListItem`s showing all transaction details.
  - **Name:** `Row` (Action Buttons)
    - **Position & Size:** Aligned to bottom.
    - **Content:** `OutlinedButton` "Fix", `FilledButton` "Confirm".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Confirm Button`: `On tap -> Navigate to 05_01_Review_Inbox_Screen`.
    - `Fix Button`: `On tap -> Navigate to 05_02_Review_Item_Edit_Screen`.
    - `Back Navigation`: `On tap -> Navigate to 05_01_Review_Inbox_Screen`.

---

#### Screen 5.4: Review Inbox Zero Screen
- **Screen Name/ID:** `05_04_Review_Inbox_Zero_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** Centered `Column`.
- **Component Specifications:**
  - **Name:** `Icon`
    - **Size:** 64dp x 64dp.
    - **Content:** `Icons.Filled.AllInbox`.
  - **Name:** `Text` (Headline)
    - **Content:** "Inbox Cleared!".
  - **Name:** `FilledButton`
    - **Content:** "Back to Dashboard".
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 02_01_Dashboard_Screen`.

---

### Flow 6: Settings & Data Source Management

---

#### Screen 6.1: Settings Screen
- **Screen Name/ID:** `06_01_Settings_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Settings".
  - **Name:** `LazyColumn`
    - **Content:**
      - `ListItem`: `headlineContent = "Profile"`, `leadingContent = Icon(Icons.Filled.Person)`.
      - `ListItem`: `headlineContent = "Data Sources & Connections"`, `leadingContent = Icon(Icons.Filled.Sync)`.
      - `ListItem`: `headlineContent = "Notifications"`, `leadingContent = Icon(Icons.Filled.Notifications)`.
      - `Divider`.
      - `ListItem`: `headlineContent = "Sign Out"`, `headlineContentColor = md.sys.color.error`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Profile ListItem`: `On tap -> Navigate to 06_03_Profile_Screen`.
    - `Data Sources ListItem`: `On tap -> Navigate to 06_02_Data_Sources_&_Connections_Screen`.
    - `Notifications ListItem`: `On tap -> Navigate to 06_04_Notification_Settings_Screen`.
    - `Sign Out ListItem`: `On tap -> Show 06_05_Sign_Out_Confirmation_Dialog`.
    - `Back Navigation`: `On tap -> Navigate to 02_01_Dashboard_Screen`.

---

#### Screen 6.2: Data Sources & Connections Screen
- **Screen Name/ID:** `06_02_Data_Sources_&_Connections_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`. Content is a `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Data Sources".
  - **Name:** `LazyColumn`
    - **Content:**
      - `ListSubheader`: `Text` "Connections".
      - `ListItem`: `headlineContent = "Bank Accounts"`.
      - `ListItem`: `headlineContent = "Email Accounts"`.
      - `ListSubheader`: `Text` "On-Device Parsers".
      - `ListItem`: `headlineContent = "SMS Parser"`, `trailingContent = Switch`.
      - `ListItem`: `headlineContent = "Auto Gallery Scan"`, `trailingContent = Switch`.
      - `ListItem`: `headlineContent = "Location for Merchants"`, `trailingContent = Switch`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Bank Accounts ListItem`: `On tap -> Navigate to 07_01_Connected_Banks_Screen`.
    - `Email Accounts ListItem`: `On tap -> Navigate to 07_08_Connected_Emails_Screen`.
    - `SMS Parser Switch`: `On toggle -> Show 01_07_System_SMS_Permission_Dialog`.
    - `Gallery Scan Switch`: `On toggle -> Show 07_13_System_Gallery_Permission_Dialog`.
    - `Location Switch`: `On toggle -> Show 07_14_System_Location_Permission_Dialog`.
    - `Back Navigation`: `On tap -> Navigate to 06_01_Settings_Screen`.

---

#### Screen 6.3: Profile Screen
- **Screen Name/ID:** `06_03_Profile_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Profile".
  - **Name:** `Column`
    - **Content:** `ListItem`s for Name, Email, etc.
- **Interaction & Behavior:**
  - **Interactions:** `Back Navigation`: `On tap -> Navigate to 06_01_Settings_Screen`.

---

#### Screen 6.4: Notification Settings Screen
- **Screen Name/ID:** `06_04_Notification_Settings_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Notifications".
  - **Name:** `LazyColumn`
    - **Content:** `ListItem`s with `Switch` controls for various notification types.
- **Interaction & Behavior:**
  - **Interactions:** `Back Navigation`: `On tap -> Navigate to 06_01_Settings_Screen`.

---

#### Screen 6.5: Sign Out Confirmation Dialog
- **Screen Name/ID:** `06_05_Sign_Out_Confirmation_Dialog`
- **Dimensions:** Dialog.
- **Layout:** `AlertDialog`.
- **Component Specifications:**
  - **Name:** `AlertDialog`
    - **Content:** Title "Sign Out?", Text "Are you sure you want to sign out?", Confirm Button "Sign Out", Dismiss Button "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Sign Out Button`: `On tap -> Navigate to 01_01_App_Launch_Screen`.
    - `Cancel Button`: `On tap -> Dismiss dialog, stay on 06_01_Settings_Screen`.

---

### Flow 7: Automatic Capture Setup Flows

---

#### Screen 7.1: Connected Banks Screen
- **Screen Name/ID:** `07_01_Connected_Banks_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Connected Banks".
  - **Name:** `LazyColumn`
    - **Content:** `ListItem` for each connected bank.
  - **Name:** `FilledButton` (Connect a New Bank)
    - **Position & Size:** Aligned to bottom. Margin 16dp.
- **Interaction & Behavior:**
  - **Interactions:**
    - `FilledButton`: `On tap -> Navigate to 07_02_Bank_Connection_Institution_Selection_Screen`.
    - `ListItem`: `On tap -> Navigate to 07_06_Bank_Detail_Screen`.
    - `Back Navigation`: `On tap -> Navigate to 06_02_Data_Sources_&_Connections_Screen`.

---

#### Screen 7.2: Bank Connection - Institution Selection Screen
- **Screen Name/ID:** `07_02_Bank_Connection_Institution_Selection_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn` with a search bar.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "Select Your Bank".
  - **Name:** `OutlinedTextField` (Search)
  - **Name:** `LazyColumn` of bank `ListItem`s.
- **Interaction & Behavior:**
  - **Interactions:** `Select a bank -> Navigate to 07_03_Bank_Connection_WebView_Login`.

---

#### Screen 7.3: Bank Connection - WebView Login
- **Screen Name/ID:** `07_03_Bank_Connection_WebView_Login`
- **Dimensions:** 393x852dp
- **Layout:** `Scaffold` with `TopAppBar` and `WebView`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Close), `Text` "Connect to [Bank Name]".
  - **Name:** `WebView`
- **Interaction & Behavior:**
  - **Interactions:**
    - `On success`: `Navigate to 07_04_Bank_Connection_Success_Screen`.
    - `On failure/cancel`: `Navigate to 07_05_Bank_Connection_Failure_Screen`.

---

#### Screen 7.4: Bank Connection - Success Screen
- **Screen Name/ID:** `07_04_Bank_Connection_Success_Screen`
- **Dimensions:** 393x852dp
- **Layout:** Centered `Column`.
- **Component Specifications:**
  - **Name:** `Icon` (`Icons.Filled.CheckCircle`).
  - **Name:** `Text` "Bank Connected Successfully!".
  - **Name:** `FilledButton` "Done".
- **Interaction & Behavior:**
  - **Interactions:** `Done Button -> Navigate to 07_01_Connected_Banks_Screen`.

---

#### Screen 7.5: Bank Connection - Failure Screen
- **Screen Name/ID:** `07_05_Bank_Connection_Failure_Screen`
- **Dimensions:** 393x852dp
- **Layout:** Centered `Column`.
- **Component Specifications:**
  - **Name:** `Icon` (`Icons.Filled.Error`, `tint = md.sys.color.error`).
  - **Name:** `Text` "Connection Failed".
  - **Name:** `FilledButton` "Try Again", `OutlinedButton` "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Try Again Button`: `On tap -> Navigate to 07_02_Bank_Connection_Institution_Selection_Screen`.
    - `Cancel Button`: `On tap -> Navigate to 07_01_Connected_Banks_Screen`.

---

#### Screen 7.6: Bank Detail Screen
- **Screen Name/ID:** `07_06_Bank_Detail_Screen`
- **Dimensions:** 393x852dp
- **Layout:** `Scaffold` with `TopAppBar`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** `IconButton` (Back), `Text` "[Bank Name]".
  - **Name:** `OutlinedButton` (Delete Connection)
    - **Style:** Border and content color `md.sys.color.error`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Delete Button`: `On tap -> Show 07_07_Disconnect_Confirmation_Dialog`.
    - `Back Navigation`: `On tap -> Navigate to 07_01_Connected_Banks_Screen`.

---

#### Screen 7.7: Disconnect Confirmation Dialog
- **Screen Name/ID:** `07_07_Disconnect_Confirmation_Dialog`
- **Layout:** `AlertDialog`.
- **Component Specifications:**
  - **Content:** Title "Disconnect Bank?", Text "This will stop new transactions from syncing.", Confirm Button "Disconnect", Dismiss Button "Cancel".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Disconnect Button`: `On tap -> Navigate to 07_01_Connected_Banks_Screen`.
    - `Cancel Button`: `On tap -> Stay on 07_06_Bank_Detail_Screen`.

---

#### Screen 7.8: Connected Emails Screen
- **Screen Name/ID:** `07_08_Connected_Emails_Screen`
- **Layout:** Similar to `07_01_Connected_Banks_Screen`.
- **Interaction & Behavior:**
  - **Interactions:**
    - `Connect New Email Button`: `On tap -> Navigate to 07_09_Email_Connection_Provider_Selection`.
    - `Back Navigation`: `On tap -> Navigate to 06_02_Data_Sources_&_Connections_Screen`.

---

#### Screen 7.9: Email Connection - Provider Selection
- **Screen Name/ID:** `07_09_Email_Connection_Provider_Selection`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
- **Component Specifications:**
  - **Content:** `ListItem` for "Gmail", "Outlook", etc.
- **Interaction & Behavior:**
  - **Interactions:** `Tap Gmail -> Navigate to 07_10_Email_Connection_OAuth_Screen`.

---

#### Screen 7.10: Email Connection - OAuth Screen
- **Screen Name/ID:** `07_10_Email_Connection_OAuth_Screen`
- **Layout:** System `WebView` or browser for OAuth flow.
- **Interaction & Behavior:**
  - **Interactions:**
    - `On success`: `Navigate to 07_11_Email_Connection_Success_Screen`.
    - `On failure/cancel`: `Navigate to 07_08_Connected_Emails_Screen`.

---

#### Screen 7.11: Email Connection - Success Screen
- **Screen Name/ID:** `07_11_Email_Connection_Success_Screen`
- **Layout:** Centered `Column` with success icon, text, and "Done" button.
- **Interaction & Behavior:**
  - **Interactions:** `Done Button -> Navigate to 07_08_Connected_Emails_Screen`.

---

#### Screen 7.12: First Email Sender Import Screen
- **Screen Name/ID:** `07_12_First_Email_Sender_Import_Screen`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
- **Component Specifications:**
  - **Name:** `TopAppBar`
    - **Content:** Title `Text` "New Receipts Found".
  - **Name:** `LazyColumn`
    - **Content:** Preview of transactions parsed from a new email sender.
  - **Name:** `FilledButton` "Confirm & Create Rule".
- **Interaction & Behavior:**
  - **Interactions:**
    - `Confirm Button`: `On tap -> Navigate to 02_01_Dashboard_Screen`.
    - `Cancel Button`: `On tap -> Navigate to 02_01_Dashboard_Screen`.

---

#### Screen 7.13: System Gallery Permission Dialog
- **Screen Name/ID:** `07_13_System_Gallery_Permission_Dialog`
- **Layout:** System permission dialog for media/storage access.
- **Interaction & Behavior:**
  - **Interactions:** `Allow/Deny -> Navigate to 06_02_Data_Sources_&_Connections_Screen`.

---

#### Screen 7.14: System Location Permission Dialog
- **Screen Name/ID:** `07_14_System_Location_Permission_Dialog`
- **Layout:** System permission dialog for location access.
- **Interaction & Behavior:**
  - **Interactions:** `Allow/Deny -> Navigate to 06_02_Data_Sources_&_Connections_Screen`.

---

### Flow 8: Placeholder Screens

---

#### Screen 8.1: Home Screen
- **Screen Name/ID:** `08_01_Home_Screen`
- **Description:** This represents the device's home screen, which is outside the app's control but hosts the widget.
- **Interaction & Behavior:**
  - **Interactions:** `User interacts with home screen -> Can access 04_01_Home_Screen_Widget`.

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
- **Applies to:** `Dashboard Screen`, `Review Inbox Screen`, `Connected Banks Screen`.
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
    - **Content:** Example: "Tap the '+' button to add your first expense."
  - **Name:** `FilledButton` (Primary CTA)
    - **Position & Size:** Centered horizontally. Margin top: 24dp.
    - **Style:** Standard filled button style.
    - **Content:** Example: "Add Transaction".

### Loading States
- **Initial Screen Load:**
  - **UI:** A centered `CircularProgressIndicator` is displayed over the screen content area while data is being fetched.
  - **Style:** Color: `md.sys.color.primary`. Size: 48dp x 48dp.
- **In-Progress Action:**
  - **UI:** For actions like connecting an account or saving data, a `LinearProgressIndicator` appears at the top of the screen, just below the `TopAppBar`.
  - **Style:** Indeterminate. Color: `md.sys.color.primary`.
- **Button Loading:**
  - **UI:** When a button triggers an async action, the button text is replaced by a `CircularProgressIndicator` (sized appropriately, e.g., 24dp) and the button is disabled.