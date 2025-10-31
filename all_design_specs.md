# Combined Android Design Specifications



============================================================
## APP 1: App_1
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Empower Personal Dashboard - Android Design Specification

## I. Global Specifications

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Modes**: Light and Dark themes are supported.
    *   **Dynamic Color**: Material You dynamic color theming is enabled, using the user's wallpaper colors on supported Android versions.
*   **Colors**:
    *   **Seed Color**: `#005E66` (Empower Teal)
    *   **Light Theme Color Roles**:
        *   `md.sys.color.primary`: `#006A6F`
        *   `md.sys.color.on-primary`: `#FFFFFF`
        *   `md.sys.color.primary-container`: `#9CF1F7`
        *   `md.sys.color.on-primary-container`: `#002022`
        *   `md.sys.color.secondary`: `#4A6364`
        *   `md.sys.color.on-secondary`: `#FFFFFF`
        *   `md.sys.color.secondary-container`: `#CDE8E9`
        *   `md.sys.color.on-secondary-container`: `#051F21`
        *   `md.sys.color.tertiary`: `#505E7D`
        *   `md.sys.color.on-tertiary`: `#FFFFFF`
        *   `md.sys.color.tertiary-container`: `#D8E2FF`
        *   `md.sys.color.on-tertiary-container`: `#0A1B36`
        *   `md.sys.color.error`: `#BA1A1A`
        *   `md.sys.color.on-error`: `#FFFFFF`
        *   `md.sys.color.error-container`: `#FFDAD6`
        *   `md.sys.color.on-error-container`: `#410002`
        *   `md.sys.color.background`: `#FAFDFD`
        *   `md.sys.color.on-background`: `#191C1C`
        *   `md.sys.color.surface`: `#FAFDFD`
        *   `md.sys.color.on-surface`: `#191C1C`
        *   `md.sys.color.surface-variant`: `#DAE4E5`
        *   `md.sys.color.on-surface-variant`: `#3F4949`
        *   `md.sys.color.outline`: `#6F797A`
        *   `md.sys.color.inverse-surface`: `#2E3131`
        *   `md.sys.color.inverse-on-surface`: `#F0F1F1`
        *   `md.sys.color.inverse-primary`: `#80D5DA`
        *   `md.sys.color.surface-tint`: `#006A6F`
    *   **Dark Theme Color Roles**:
        *   `md.sys.color.primary`: `#80D5DA`
        *   `md.sys.color.on-primary`: `#00373A`
        *   `md.sys.color.primary-container`: `#004F53`
        *   `md.sys.color.on-primary-container`: `#9CF1F7`
        *   `md.sys.color.secondary`: `#B1CCCD`
        *   `md.sys.color.on-secondary`: `#1B3536`
        *   `md.sys.color.secondary-container`: `#324B4C`
        *   `md.sys.color.on-secondary-container`: `#CDE8E9`
        *   `md.sys.color.tertiary`: `#B8C6E9`
        *   `md.sys.color.on-tertiary`: `#21304C`
        *   `md.sys.color.tertiary-container`: `#384664`
        *   `md.sys.color.on-tertiary-container`: `#D8E2FF`
        *   `md.sys.color.error`: `#FFB4AB`
        *   `md.sys.color.on-error`: `#690005`
        *   `md.sys.color.error-container`: `#93000A`
        *   `md.sys.color.on-error-container`: `#FFDAD6`
        *   `md.sys.color.background`: `#191C1C`
        *   `md.sys.color.on-background`: `#E1E3E3`
        *   `md.sys.color.surface`: `#191C1C`
        *   `md.sys.color.on-surface`: `#E1E3E3`
        *   `md.sys.color.surface-variant`: `#3F4949`
        *   `md.sys.color.on-surface-variant`: `#BFC8C9`
        *   `md.sys.color.outline`: `#899393`
        *   `md.sys.color.inverse-surface`: `#E1E3E3`
        *   `md.sys.color.inverse-on-surface`: `#191C1C`
        *   `md.sys.color.inverse-primary`: `#006A6F`
        *   `md.sys.color.surface-tint`: `#80D5DA`
*   **Typography**:
    *   **Font Family**: Roboto
    *   **Type Scale**:
        *   `displayLarge`: Roboto 57sp
        *   `displayMedium`: Roboto 45sp
        *   `displaySmall`: Roboto 36sp
        *   `headlineLarge`: Roboto 32sp
        *   `headlineMedium`: Roboto 28sp
        *   `headlineSmall`: Roboto 24sp
        *   `titleLarge`: Roboto 22sp
        *   `titleMedium`: Roboto 16sp, weight 500
        *   `titleSmall`: Roboto 14sp, weight 500
        *   `bodyLarge`: Roboto 16sp
        *   `bodyMedium`: Roboto 14sp
        *   `bodySmall`: Roboto 12sp
        *   `labelLarge`: Roboto 14sp, weight 500
        *   `labelMedium`: Roboto 12sp, weight 500
        *   `labelSmall`: Roboto 11sp, weight 500
*   **Spacing**:
    *   **Base Grid Unit**: 8dp
    *   **Standard Padding**: 16dp
    *   **Standard Margins**: 16dp
*   **Accessibility**:
    *   **Target Standard**: WCAG 2.1 Level AA
    *   **Minimum Touch Target**: 48dp x 48dp for all interactive elements.
    *   **Content Descriptions**: All icons and images must have descriptive content descriptions for screen readers.

---

## II. Screen Specifications

### Flow 1: Authentication

---

#### Screen 1: Welcome Screen
*   **Screen Name/ID**: `01_01_Welcome_Screen`
*   **Dimensions**: 393x852dp (Typical mobile viewport)
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered and horizontally aligned to the center.
    *   `verticalArrangement`: `Arrangement.Center`
    *   `horizontalAlignment`: `Alignment.CenterHorizontally`
    *   `modifier`: `fillMaxSize()`, `padding(32.dp)`

##### Components:
1.  **Name**: `Image` (App Logo)
    *   **Position & Size**: 120dp x 120dp. Centered horizontally. Margin bottom 24dp.
    *   **Style**: Placeholder for the Empower logo.
    *   **Content**: Empower app logo graphic.
2.  **Name**: `Text` (Tagline)
    *   **Position & Size**: `fillMaxWidth()`. Margin bottom 48dp.
    *   **Style**:
        *   `typography`: `md.sys.typography.headlineSmall`
        *   `color`: `md.sys.color.on-surface`
        *   `textAlign`: `TextAlign.Center`
    *   **Content**: "Clarity for your entire financial life."
3.  **Name**: `Filled Button`
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Margin bottom 16dp. Minimum touch target 48x48dp.
    *   **Style**:
        *   `colors`: `ButtonDefaults.buttonColors(containerColor = md.sys.color.primary, contentColor = md.sys.color.on-primary)`
        *   `shape`: `ShapeDefaults.Full` (Pill shape)
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.labelLarge`
        *   **Content**: "Log In"
4.  **Name**: `Outlined Button`
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Minimum touch target 48x48dp.
    *   **Style**:
        *   `colors`: `ButtonDefaults.outlinedButtonColors(contentColor = md.sys.color.primary)`
        *   `border`: `BorderStroke(1.dp, md.sys.color.outline)`
        *   `shape`: `ShapeDefaults.Full` (Pill shape)
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.labelLarge`
        *   **Content**: "Sign Up For Free"

##### Interaction & Behavior:
*   **Filled Button ('Log In')**:
    *   **States**: Standard Material 3 states (pressed, hover, focused, disabled) with state layer overlays.
    *   **Interaction**: On tap -> Navigate to `01_02_Log_In_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) forward transition.
*   **Outlined Button ('Sign Up For Free')**:
    *   **States**: Standard Material 3 states.
    *   **Interaction**: On tap -> Navigate to `01_03_Sign_Up_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) forward transition.

---

#### Screen 2: Log In Screen
*   **Screen Name/ID**: `01_02_Log_In_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout within a `Scaffold`.
    *   `modifier`: `fillMaxSize()`, `padding(16.dp)`

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**:
        *   `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`
        *   `navigationIcon`:
            *   **Name**: `IconButton`
            *   **Icon**: `Icons.Filled.ArrowBack`
            *   **Content Description**: "Back"
            *   **Tint**: `md.sys.color.on-surface`
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Log In"
2.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**:
        *   `label`: "Email address"
        *   `keyboardOptions`: `KeyboardType.Email`
        *   `singleLine`: `true`
    *   **Content**: User-entered email address.
3.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Style**:
        *   `label`: "Password"
        *   `visualTransformation`: `PasswordVisualTransformation`
        *   `keyboardOptions`: `KeyboardType.Password`
        *   `singleLine`: `true`
        *   `trailingIcon`: `IconButton` with visibility toggle (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`).
    *   **Content**: User-entered password.
4.  **Name**: `TextButton` (Forgot Password)
    *   **Position & Size**: Aligned to the end of the screen. Top margin 8dp.
    *   **Style**: `colors`: `ButtonDefaults.textButtonColors(contentColor = md.sys.color.primary)`
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.labelLarge`
        *   **Content**: "Forgot Password?"
5.  **Name**: `Filled Button` (Log In)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**:
        *   `colors`: `ButtonDefaults.buttonColors(containerColor = md.sys.color.primary)`
        *   `shape`: `ShapeDefaults.Full`
        *   **Initial State**: Disabled until both fields are non-empty.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.labelLarge`
        *   **Content**: "Log In"

##### Interaction & Behavior:
*   **TopAppBar Navigation Icon**:
    *   **Interaction**: On tap -> Navigate back to `01_01_Welcome_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) backward transition.
*   **Email/Password Fields**:
    *   **Interaction**: User enters text. The 'Log In' button becomes enabled when both fields contain valid input.
*   **'Forgot Password?' TextButton**:
    *   **Interaction**: On tap -> Navigate to `01_04_Forgot_Password_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.
*   **'Log In' Filled Button**:
    *   **Interaction**: On tap -> Authenticate user. On success, navigate to `02_01_Dashboard`.
    *   **Animation**: `MaterialFadeThrough` transition.

---

#### Screen 3: Sign Up Screen
*   **Screen Name/ID**: `01_03_Sign_Up_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` containing a `WebView`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**:
        *   `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`
        *   `navigationIcon`:
            *   **Name**: `IconButton`
            *   **Icon**: `Icons.Filled.Close`
            *   **Content Description**: "Close"
            *   **Tint**: `md.sys.color.on-surface`
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Create Account"
2.  **Name**: `WebView`
    *   **Position & Size**: `fillMaxSize()`. Occupies the entire area below the `TopAppBar`.
    *   **Style**: Displays the mobile web sign-up flow from the Empower website.
    *   **Content**: External web page for user registration.

##### Interaction & Behavior:
*   **TopAppBar Navigation Icon**:
    *   **Interaction**: On tap -> Navigate back to `01_01_Welcome_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) backward transition.
*   **WebView**:
    *   **Interaction**: User completes the sign-up form within the web view. Upon successful completion (detected via a URL redirect or JavaScript interface), the app navigates to the dashboard.
    *   **Resulting Navigation**: On success -> Navigate to `02_01_Dashboard`.
    *   **Animation**: `MaterialFadeThrough` transition.

---

#### Screen 4: Forgot Password Screen
*   **Screen Name/ID**: `01_04_Forgot_Password_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout within a `Scaffold`.
    *   `modifier`: `fillMaxSize()`, `padding(16.dp)`

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**:
        *   `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`
        *   `navigationIcon`:
            *   **Name**: `IconButton`
            *   **Icon**: `Icons.Filled.ArrowBack`
            *   **Content Description**: "Back"
            *   **Tint**: `md.sys.color.on-surface`
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Reset Password"
2.  **Name**: `Text` (Instruction)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**:
        *   `typography`: `md.sys.typography.bodyMedium`
        *   `color`: `md.sys.color.on-surface-variant`
    *   **Content**: "Enter the email address associated with your account, and we'll send you a link to reset your password."
3.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Style**:
        *   `label`: "Email address"
        *   `keyboardOptions`: `KeyboardType.Email`
        *   `singleLine`: `true`
    *   **Content**: User-entered email address.
4.  **Name**: `Filled Button` (Submit)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**:
        *   `colors`: `ButtonDefaults.buttonColors(containerColor = md.sys.color.primary)`
        *   `shape`: `ShapeDefaults.Full`
        *   **Initial State**: Disabled until the email field is non-empty and valid.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.labelLarge`
        *   **Content**: "Send Reset Link"

##### Interaction & Behavior:
*   **TopAppBar Navigation Icon**:
    *   **Interaction**: On tap -> Navigate back to `01_02_Log_In_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.
*   **'Send Reset Link' Filled Button**:
    *   **Interaction**: On tap -> Validate email, trigger password reset API call. Display a `Snackbar` with the message "If an account exists for this email, a reset link has been sent." Then, navigate back to the Log In screen.
    *   **Resulting Navigation**: Navigate to `01_02_Log_In_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.

---

### Flow 2: Main Navigation

---

#### Screen 5: Dashboard
*   **Screen Name/ID**: `02_01_Dashboard`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn` for content, and `NavigationBar` at the bottom.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**:
        *   `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface, scrolledContainerColor = md.sys.color.surface-tint)`
        *   `scrollBehavior`: `TopAppBarDefaults.enterAlwaysScrollBehavior()`
    *   **Content**:
        *   **Name**: `Image` (Logo)
        *   **Position**: Start of the `TopAppBar`.
        *   **Size**: 32dp x 32dp.
        *   **Content**: Empower app logo.
    *   **Actions**:
        *   **Name**: `IconButton`
        *   **Icon**: `Icons.Filled.Add`
        *   **Content Description**: "Link an Account"
        *   **Tint**: `md.sys.color.on-surface`
2.  **Name**: `LazyColumn` (Screen Content)
    *   **Position & Size**: Fills the space between `TopAppBar` and `NavigationBar`.
    *   **Layout**: `padding(horizontal = 16.dp)`. `Arrangement.spacedBy(16.dp)`.
    *   **Content**: A list of `Card` components.
        *   **Example Card 1**: `Card` for "Net Worth". Contains a title `Text` ("Net Worth"), a large amount `Text` ("$1,234,567.89"), and a smaller `Text` for change ("+$5,000.12 today").
        *   **Example Card 2**: `Card` for "Cash Flow". Contains a title, a bar chart visual, and summary figures.
        *   **Example Card 3**: `Card` for "Budget". Contains a title, a progress indicator, and spending categories.
3.  **Name**: `NavigationBar` (Bottom Navigation)
    *   **Position & Size**: `fillMaxWidth()`, height 80dp. Aligned to the bottom of the screen.
    *   **Style**: `containerColor`: `md.sys.color.surface-variant`
    *   **Content**: Five `NavigationBarItem` components.
        *   **Item 1 (Active)**: `label`: "Dashboard", `icon`: `Icons.Filled.Dashboard`, `selected`: `true`.
        *   **Item 2**: `label`: "Planning", `icon`: `Icons.Outlined.EditNote`, `selected`: `false`.
        *   **Item 3**: `label`: "Investing", `icon`: `Icons.Outlined.ShowChart`, `selected`: `false`.
        *   **Item 4**: `label`: "Spending", `icon`: `Icons.Outlined.AccountBalanceWallet`, `selected`: `false`.
        *   **Item 5**: `label`: "Wealth", `icon`: `Icons.Outlined.Diamond`, `selected`: `false`.

##### Interaction & Behavior:
*   **TopAppBar '+' IconButton**:
    *   **Interaction**: On tap -> Navigate to `03_02_Link_an_Account_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) forward transition (modal sheet style).
*   **Scroll Behavior**: The `TopAppBar` collapses on scroll up and reappears on scroll down.
*   **NavigationBar Items**:
    *   **Interaction**: Tapping an inactive item navigates to the corresponding screen.
    *   **'Planning'**: On tap -> Navigate to `02_02_Planning_Screen`.
    *   **'Investing'**: On tap -> Navigate to `02_03_Investing_Screen`.
    *   **'Spending'**: On tap -> Navigate to `02_04_Spending_Screen`.
    *   **'Wealth'**: On tap -> Navigate to `02_05_Wealth_Screen`.
    *   **Animation**: `MaterialFadeThrough` transition between tabs.

---

#### Screen 6: Planning Screen
*   **Screen Name/ID**: `02_02_Planning_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**: `scrollBehavior`: `TopAppBarDefaults.enterAlwaysScrollBehavior()`
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Planning"
2.  **Name**: `LazyColumn` (Screen Content)
    *   **Position & Size**: Fills the space between `TopAppBar` and `NavigationBar`.
    *   **Layout**: `padding(horizontal = 16.dp)`. `Arrangement.spacedBy(16.dp)`.
    *   **Content**: List of `Card` components for planning tools.
        *   **Example Card 1**: "Retirement Planner".
        *   **Example Card 2**: "Savings Goals".
        *   **Example Card 3**: "Education Planner".
3.  **Name**: `NavigationBar`
    *   **Position & Size**: `fillMaxWidth()`, height 80dp. Aligned to the bottom.
    *   **Content**:
        *   **Item 1**: `label`: "Dashboard", `icon`: `Icons.Outlined.Dashboard`, `selected`: `false`.
        *   **Item 2 (Active)**: `label`: "Planning", `icon`: `Icons.Filled.EditNote`, `selected`: `true`.
        *   **Item 3**: `label`: "Investing", `icon`: `Icons.Outlined.ShowChart`, `selected`: `false`.
        *   **Item 4**: `label`: "Spending", `icon`: `Icons.Outlined.AccountBalanceWallet`, `selected`: `false`.
        *   **Item 5**: `label`: "Wealth", `icon`: `Icons.Outlined.Diamond`, `selected`: `false`.

##### Interaction & Behavior:
*   **NavigationBar Items**:
    *   **Interaction**: Tapping an inactive item navigates to the corresponding screen.
    *   **Animation**: `MaterialFadeThrough` transition between tabs.

---

#### Screen 7: Investing Screen
*   **Screen Name/ID**: `02_03_Investing_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, content area with `TabRow`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Investing"
2.  **Name**: `PrimaryTabRow`
    *   **Position & Size**: `fillMaxWidth()`, height 48dp. Below `TopAppBar`.
    *   **Content**:
        *   **Tab 1**: `text`: "Holdings"
        *   **Tab 2**: `text`: "Allocation"
        *   **Tab 3**: `text`: "Performance"
3.  **Name**: `HorizontalPager` / Content Area
    *   **Position & Size**: Fills the space between `TabRow` and `NavigationBar`.
    *   **Content**: Displays content corresponding to the selected tab.
4.  **Name**: `NavigationBar`
    *   **Position & Size**: `fillMaxWidth()`, height 80dp. Aligned to the bottom.
    *   **Content**:
        *   **Item 1**: `label`: "Dashboard", `icon`: `Icons.Outlined.Dashboard`, `selected`: `false`.
        *   **Item 2**: `label`: "Planning", `icon`: `Icons.Outlined.EditNote`, `selected`: `false`.
        *   **Item 3 (Active)**: `label`: "Investing", `icon`: `Icons.Filled.ShowChart`, `selected`: `true`.
        *   **Item 4**: `label`: "Spending", `icon`: `Icons.Outlined.AccountBalanceWallet`, `selected`: `false`.
        *   **Item 5**: `label`: "Wealth", `icon`: `Icons.Outlined.Diamond`, `selected`: `false`.

##### Interaction & Behavior:
*   **TabRow**:
    *   **Interaction**: Tapping a tab switches the content displayed in the `HorizontalPager`.
    *   **'Holdings' Tab**: On tap -> Navigate to `05_02_Investment_Holdings_Screen`.
    *   **'Allocation' Tab**: On tap -> Navigate to `05_03_Investment_Allocation_Screen`.
*   **NavigationBar Items**:
    *   **Interaction**: Tapping an inactive item navigates to the corresponding screen.
    *   **Animation**: `MaterialFadeThrough` transition between tabs.

---

#### Screen 8: Spending Screen
*   **Screen Name/ID**: `02_04_Spending_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, content area with `TabRow`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Spending"
2.  **Name**: `PrimaryTabRow`
    *   **Position & Size**: `fillMaxWidth()`, height 48dp. Below `TopAppBar`.
    *   **Content**:
        *   **Tab 1**: `text`: "Overview"
        *   **Tab 2**: `text`: "Transactions"
        *   **Tab 3**: `text`: "Budgets"
3.  **Name**: `HorizontalPager` / Content Area
    *   **Position & Size**: Fills the space between `TabRow` and `NavigationBar`.
    *   **Content**: Displays content corresponding to the selected tab.
4.  **Name**: `NavigationBar`
    *   **Position & Size**: `fillMaxWidth()`, height 80dp. Aligned to the bottom.
    *   **Content**:
        *   **Item 1**: `label`: "Dashboard", `icon`: `Icons.Outlined.Dashboard`, `selected`: `false`.
        *   **Item 2**: `label`: "Planning", `icon`: `Icons.Outlined.EditNote`, `selected`: `false`.
        *   **Item 3**: `label`: "Investing", `icon`: `Icons.Outlined.ShowChart`, `selected`: `false`.
        *   **Item 4 (Active)**: `label`: "Spending", `icon`: `Icons.Filled.AccountBalanceWallet`, `selected`: `true`.
        *   **Item 5**: `label`: "Wealth", `icon`: `Icons.Outlined.Diamond`, `selected`: `false`.

##### Interaction & Behavior:
*   **TabRow**:
    *   **Interaction**: Tapping a tab switches the content.
    *   **'Transactions' Tab**: On tap -> Navigate to `04_02_Transactions_List_Screen`.
*   **NavigationBar Items**:
    *   **Interaction**: Tapping an inactive item navigates to the corresponding screen.
    *   **Animation**: `MaterialFadeThrough` transition between tabs.

---

#### Screen 9: Wealth Screen
*   **Screen Name/ID**: `02_05_Wealth_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Wealth"
2.  **Name**: `LazyColumn` (Screen Content)
    *   **Position & Size**: Fills the space between `TopAppBar` and `NavigationBar`.
    *   **Layout**: `padding(horizontal = 16.dp)`. `Arrangement.spacedBy(16.dp)`.
    *   **Content**: List of `Card` components detailing assets and liabilities.
        *   **Example Card 1**: "Assets" with a total value and a breakdown by type (Cash, Investments, Property).
        *   **Example Card 2**: "Liabilities" with a total value and a breakdown by type (Credit Cards, Loans, Mortgages).
3.  **Name**: `NavigationBar`
    *   **Position & Size**: `fillMaxWidth()`, height 80dp. Aligned to the bottom.
    *   **Content**:
        *   **Item 1**: `label`: "Dashboard", `icon`: `Icons.Outlined.Dashboard`, `selected`: `false`.
        *   **Item 2**: `label`: "Planning", `icon`: `Icons.Outlined.EditNote`, `selected`: `false`.
        *   **Item 3**: `label`: "Investing", `icon`: `Icons.Outlined.ShowChart`, `selected`: `false`.
        *   **Item 4**: `label`: "Spending", `icon`: `Icons.Outlined.AccountBalanceWallet`, `selected`: `false`.
        *   **Item 5 (Active)**: `label`: "Wealth", `icon`: `Icons.Filled.Diamond`, `selected`: `true`.

##### Interaction & Behavior:
*   **NavigationBar Items**:
    *   **Interaction**: Tapping an inactive item navigates to the corresponding screen.
    *   **Animation**: `MaterialFadeThrough` transition between tabs.

---

### Flow 3: Link Bank Account

---

#### Screen 10: Link an Account Screen
*   **Screen Name/ID**: `03_02_Link_an_Account_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Style**: `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.Close` icon.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Link an Account"
2.  **Name**: `OutlinedTextField` (Search Bar)
    *   **Position & Size**: `fillMaxWidth()`. Margin 16dp.
    *   **Style**:
        *   `placeholder`: "Search for your bank or brokerage"
        *   `leadingIcon`: `Icon` with `Icons.Filled.Search`.
        *   `shape`: `ShapeDefaults.Full`.
    *   **Content**: User-entered search query.
3.  **Name**: `Text` (Section Header)
    *   **Position & Size**: `fillMaxWidth()`. Margin horizontal 16dp, top 16dp.
    *   **Style**: `typography`: `md.sys.typography.titleMedium`, `color`: `md.sys.color.on-surface-variant`
    *   **Content**: "Popular Institutions"
4.  **Name**: `LazyColumn` (Institution List)
    *   **Position & Size**: Fills remaining space.
    *   **Content**: A list of institutions using `ListItem`.
        *   **Example ListItem**:
            *   `leadingContent`: `Image` of the institution's logo (e.g., Chase logo).
            *   `headlineContent`: `Text` with the institution's name (e.g., "Chase").
            *   `modifier`: `clickable()`

##### Interaction & Behavior:
*   **TopAppBar Close Icon**:
    *   **Interaction**: On tap -> Dismiss the screen and return to `02_01_Dashboard`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) backward transition.
*   **Search Bar**:
    *   **Interaction**: As the user types, the list below filters to show matching institutions. Tapping a result navigates to the login screen.
    *   **Resulting Navigation**: Navigate to `03_03_Institution_Login_Screen`.
*   **ListItem (Institution)**:
    *   **Interaction**: On tap -> Navigate to the login screen for the selected institution.
    *   **Resulting Navigation**: Navigate to `03_03_Institution_Login_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.

---

#### Screen 11: Institution Login Screen
*   **Screen Name/ID**: `03_03_Institution_Login_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**:
        *   **Name**: `Text`
        *   **Style**: `typography`: `md.sys.typography.titleLarge`
        *   **Content**: "Connect to [Institution Name]"
2.  **Name**: `Image` (Institution Logo)
    *   **Position & Size**: 80dp x 80dp. Centered horizontally. Top margin 32dp.
    *   **Content**: Logo of the selected institution (e.g., Chase).
3.  **Name**: `OutlinedTextField` (User ID)
    *   **Position & Size**: `fillMaxWidth()`. Margin horizontal 16dp, top 32dp.
    *   **Style**: `label`: "User ID"
    *   **Content**: User-entered institution User ID.
4.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**: `fillMaxWidth()`. Margin horizontal 16dp, top 16dp.
    *   **Style**: `label`: "Password", `visualTransformation`: `PasswordVisualTransformation`.
    *   **Content**: User-entered institution password.
5.  **Name**: `Filled Button` (Sign In)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Margin 16dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Sign In".

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `03_02_Link_an_Account_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.
*   **'Sign In' Button**:
    *   **Interaction**: On tap -> Initiate the account linking process.
    *   **Resulting Navigation**: Navigate to `03_04_Linking_Account_Progress_Screen`.
    *   **Animation**: `MaterialFadeThrough` transition.

---

#### Screen 12: Linking Account Progress Screen
*   **Screen Name/ID**: `03_04_Linking_Account_Progress_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `verticalArrangement = Arrangement.Center` and `horizontalAlignment = Alignment.CenterHorizontally`.

##### Components:
1.  **Name**: `CircularProgressIndicator`
    *   **Position & Size**: 64dp x 64dp. Centered on screen.
    *   **Style**: `strokeWidth`: 4.dp.
2.  **Name**: `Text` (Status Message)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.titleMedium`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Linking your account... This may take a moment."

##### Interaction & Behavior:
*   **Automatic Transition**:
    *   **Interaction**: This is a transient screen. The app performs the account linking in the background.
    *   **Resulting Navigation**: On successful linking -> Navigate to `03_05_Accounts_Found_Screen`. On failure, show an error dialog or `Snackbar` and return to `03_03_Institution_Login_Screen`.
    *   **Animation**: `MaterialFadeThrough` transition.

---

#### Screen 13: Accounts Found Screen
*   **Screen Name/ID**: `03_05_Accounts_Found_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `Column` and a bottom-aligned button.

##### Components:
1.  **Name**: `Icon` (Success Icon)
    *   **Position & Size**: 96dp x 96dp. Centered horizontally. Top margin 64dp.
    *   **Style**: `icon`: `Icons.Filled.CheckCircle`, `tint`: `md.sys.color.primary`.
2.  **Name**: `Text` (Success Title)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.headlineMedium`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Success!"
3.  **Name**: `Text` (Success Message)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 8dp. Padding horizontal 32dp.
    *   **Style**: `typography`: `md.sys.typography.bodyLarge`, `textAlign`: `TextAlign.Center`, `color`: `md.sys.color.on-surface-variant`.
    *   **Content**: "We found 3 accounts at [Institution Name] and have added them to your dashboard."
4.  **Name**: `Filled Button` (Continue)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Aligned to the bottom of the screen with 16dp margin.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Continue".

##### Interaction & Behavior:
*   **'Continue' Button**:
    *   **Interaction**: On tap -> Dismiss the entire linking flow and return to the dashboard.
    *   **Resulting Navigation**: Navigate to `02_01_Dashboard`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) backward transition, dismissing the modal flow.

---

### Flow 4: View Transactions

---

#### Screen 14: Transactions List Screen
*   **Screen Name/ID**: `04_02_Transactions_List_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with "Transactions".
    *   **Actions**: `IconButton` with `Icons.Filled.FilterList` icon.
2.  **Name**: `LazyColumn` (Transactions)
    *   **Position & Size**: Fills the remaining space.
    *   **Content**: List of transactions, grouped by date.
        *   **Date Header**: `Text` with date (e.g., "October 31, 2025"). `Modifier.padding(16.dp)`.
        *   **Transaction Item**: `ListItem` for each transaction.
            *   `leadingContent`: `Icon` representing the category (e.g., `Icons.Filled.Restaurant`).
            *   `headlineContent`: `Text` with merchant name (e.g., "Starbucks").
            *   `supportingContent`: `Text` with category name (e.g., "Food & Dining").
            *   `trailingContent`: `Text` with amount (e.g., "-$5.75").
            *   `modifier`: `clickable()`.

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `02_04_Spending_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.
*   **TopAppBar Filter Icon**:
    *   **Interaction**: On tap -> Navigate to `04_04_Filter_Transactions_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) forward transition.
*   **Transaction ListItem**:
    *   **Interaction**: On tap -> Navigate to `04_03_Transaction_Details_Screen` with the selected transaction's data.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.

---

#### Screen 15: Transaction Details Screen
*   **Screen Name/ID**: `04_03_Transaction_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with "Transaction Details".
2.  **Name**: `Column` (Details)
    *   **Position & Size**: `fillMaxWidth()`, `padding(16.dp)`.
    *   **Content**:
        *   `Text` (Merchant Name): `typography`: `headlineMedium`, content: "Starbucks".
        *   `Text` (Amount): `typography`: `headlineLarge`, `color`: `md.sys.color.error`, content: "-$5.75".
        *   `Divider`: `modifier.padding(vertical = 16.dp)`.
        *   `ListItem`: `headlineContent`: "Date", `trailingContent`: "October 31, 2025".
        *   `ListItem`: `headlineContent`: "Category", `trailingContent`: "Food & Dining".
        *   `ListItem`: `headlineContent`: "Account", `trailingContent`: "Chase Checking (...1234)".

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `04_02_Transactions_List_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.

---

#### Screen 16: Filter Transactions Screen
*   **Screen Name/ID**: `04_04_Filter_Transactions_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.Close` icon.
    *   **Content**: `Text` with "Filter Transactions".
    *   **Actions**: `TextButton` with "Reset".
2.  **Name**: `Column` (Filter Options)
    *   **Position & Size**: `fillMaxWidth()`, `padding(16.dp)`.
    *   **Content**:
        *   `Text` (Section Header): "Date Range".
        *   `OutlinedButton` with `Icons.Filled.DateRange` to open a date picker.
        *   `Text` (Section Header): "Categories".
        *   `FilterChip` components for each category (e.g., "Food", "Shopping", "Travel").
        *   `Text` (Section Header): "Accounts".
        *   `FilterChip` components for each account.
3.  **Name**: `Filled Button` (Apply)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Aligned to bottom with 16dp margin.
    *   **Content**: `Text` with "Apply Filters".

##### Interaction & Behavior:
*   **TopAppBar Close Icon**:
    *   **Interaction**: On tap -> Dismiss screen without applying filters, return to `04_02_Transactions_List_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) backward transition.
*   **'Reset' TextButton**:
    *   **Interaction**: On tap -> Clear all selected filters to their default state.
*   **'Apply Filters' Button**:
    *   **Interaction**: On tap -> Apply the selected filters and return to the transactions list.
    *   **Resulting Navigation**: Navigate to `04_02_Transactions_List_Screen` (with filtered data).
    *   **Animation**: `MaterialSharedAxis` (Y-axis) backward transition.

---

### Flow 5: View Investment Portfolio

---

#### Screen 17: Investment Holdings Screen
*   **Screen Name/ID**: `05_02_Investment_Holdings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with "Investment Holdings".
2.  **Name**: `LazyColumn` (Holdings)
    *   **Position & Size**: Fills the remaining space.
    *   **Content**: List of investment holdings.
        *   **Holding Item**: `ListItem` for each holding.
            *   `headlineContent`: `Text` with holding name (e.g., "Apple Inc.").
            *   `supportingContent`: `Text` with ticker and shares (e.g., "AAPL - 10 shares").
            *   `trailingContent`: `Column` with `Text` for total value (e.g., "$1,500.00") and `Text` for today's change (e.g., "+$12.50").
            *   `modifier`: `clickable()`.

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `02_03_Investing_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.
*   **Holding ListItem**:
    *   **Interaction**: On tap -> Navigate to `05_04_Holding_Details_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.

---

#### Screen 18: Investment Allocation Screen
*   **Screen Name/ID**: `05_03_Investment_Allocation_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with "Investment Allocation".
2.  **Name**: `Card` (Pie Chart)
    *   **Position & Size**: `fillMaxWidth()`, `height(250.dp)`. Margin 16dp.
    *   **Content**: A pie chart visual representing asset allocation.
3.  **Name**: `LazyColumn` (Asset Classes)
    *   **Position & Size**: Fills remaining space below the chart.
    *   **Content**: List of asset classes.
        *   **Asset Class Item**: `ListItem`.
            *   `leadingContent`: `Box` with a color swatch matching the pie chart slice.
            *   `headlineContent`: `Text` with asset class name (e.g., "U.S. Stocks").
            *   `trailingContent`: `Text` with percentage (e.g., "45.0%").
            *   `modifier`: `clickable()`.

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `02_03_Investing_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.
*   **Asset Class ListItem**:
    *   **Interaction**: On tap -> Navigate to `05_05_Asset_Class_Details_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.

---

#### Screen 19: Holding Details Screen
*   **Screen Name/ID**: `05_04_Holding_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with holding name (e.g., "Apple Inc.").
2.  **Name**: `Column` (Details)
    *   **Position & Size**: `fillMaxWidth()`, `padding(16.dp)`.
    *   **Content**:
        *   `Text` (Ticker): `typography`: `titleMedium`, `color`: `on-surface-variant`, content: "AAPL".
        *   `Text` (Value): `typography`: `headlineLarge`, content: "$1,500.00".
        *   `Text` (Change): `typography`: `titleMedium`, `color`: `green` (custom), content: "+$12.50 (+0.84%) Today".
        *   `Divider`: `modifier.padding(vertical = 16.dp)`.
        *   `ListItem`: `headlineContent`: "Market Price", `trailingContent`: "$150.00".
        *   `ListItem`: `headlineContent`: "Quantity", `trailingContent`: "10 shares".
        *   `ListItem`: `headlineContent`: "Cost Basis", `trailingContent`: "$1,200.00".

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `05_02_Investment_Holdings_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.

---

#### Screen 20: Asset Class Details Screen
*   **Screen Name/ID**: `05_05_Asset_Class_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`, height 64dp.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack` icon.
    *   **Content**: `Text` with asset class name (e.g., "U.S. Stocks").
2.  **Name**: `LazyColumn` (Holdings in Class)
    *   **Position & Size**: Fills the remaining space.
    *   **Content**: A list of holdings that fall under this asset class, using the same `ListItem` component defined in `05_02_Investment_Holdings_Screen`.

##### Interaction & Behavior:
*   **TopAppBar Back Icon**:
    *   **Interaction**: On tap -> Navigate back to `05_03_Investment_Allocation_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.

---
*The remaining two screens are duplicates from other flows, included here to complete the count of 22 as per the input JSON structure.*

#### Screen 21: Dashboard (from Link Bank Account flow)
*   **Screen Name/ID**: `03_01_Dashboard`
*   **Specification**: This screen is identical to `02_01_Dashboard`. Please refer to its specification. The only difference is the initiating action.
*   **Interaction**: Tapping the '+' icon in the `TopAppBar` initiates the "Link Bank Account" flow.
    *   **User Action**: Taps '+' icon in top right.
    *   **Resulting Navigation**: Navigate to `03_02_Link_an_Account_Screen`.

#### Screen 22: Spending Screen (from View Transactions flow)
*   **Screen Name/ID**: `04_01_Spending_Screen`
*   **Specification**: This screen is identical to `02_04_Spending_Screen`. Please refer to its specification. The only difference is the initiating action.
*   **Interaction**: Tapping the 'Transactions' sub-tab initiates the "View Transactions" flow.
    *   **User Action**: Taps 'Transactions' sub-tab.
    *   **Resulting Navigation**: Navigate to `04_02_Transactions_List_Screen`.

---

## V. Critical Scenarios & States

#### Error States
1.  **No Internet Connection**:
    *   **UI**: A `Snackbar` appears at the bottom of the screen.
    *   **Style**: `containerColor`: `md.sys.color.error-container`, `contentColor`: `md.sys.color.on-error-container`.
    *   **Message**: "No internet connection. Please check your network and try again."
    *   **Action**: Optional "Retry" `TextButton` on the `Snackbar`.
2.  **API/Server Error**:
    *   **UI**: A `Snackbar` appears.
    *   **Message**: "Something went wrong. Please try again later."
3.  **Form Validation Error**:
    *   **UI**: The `OutlinedTextField` that fails validation will show an error state.
    *   **Style**: The outline and label color change to `md.sys.color.error`.
    *   **Message**: Helper text appears below the field with a descriptive error (e.g., "Please enter a valid email address.").

#### Empty States
1.  **Empty Dashboard (New User)**:
    *   **UI**: The main content area of the `02_01_Dashboard` screen will display a centered `Column`.
    *   **Content**:
        *   `Icon`: `Icons.Outlined.AccountBalance`, size 64dp, `tint`: `md.sys.color.secondary`.
        *   `Text` (Title): "Welcome to Empower", `typography`: `headlineSmall`.
        *   `Text` (Body): "Link an account to see your complete financial picture.", `typography`: `bodyMedium`, `textAlign`: `TextAlign.Center`.
        *   `FilledButton`: "Link First Account", `modifier.padding(top = 24.dp)`. On tap, navigates to `03_02_Link_an_Account_Screen`.
2.  **Empty Transactions List**:
    *   **UI**: The `LazyColumn` in `04_02_Transactions_List_Screen` will display a centered `Column`.
    *   **Content**:
        *   `Icon`: `Icons.Outlined.ReceiptLong`, size 64dp, `tint`: `md.sys.color.secondary`.
        *   `Text` (Title): "No Transactions Found".
        *   `Text` (Body): "We couldn't find any transactions for the selected filters."

#### Loading States
1.  **Initial App Load / Dashboard Refresh**:
    *   **UI**: A full-screen `CircularProgressIndicator` is displayed centered over the `02_01_Dashboard` content area while initial data is fetched.
2.  **LazyColumn Item Loading**:
    *   **UI**: When paginating or loading more items in a `LazyColumn` (e.g., Transactions), a `CircularProgressIndicator` is shown as the last item in the list.
3.  **Screen-Specific Loading**:
    *   **UI**: For screens that fetch data upon entry (e.g., `04_03_Transaction_Details_Screen`), a centered `CircularProgressIndicator` is shown in the content area until the data is ready to be displayed.

```

---


============================================================
## APP 2: App_2
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Rocket Money - Android App Design Specification

## I. Global Specifications

### Platform
- **Target:** Android Mobile App
- **Minimum SDK:** API 26 (Android 8.0 Oreo)
- **Target SDK:** API 34 (Android 14)

### Design System
- **System:** Material Design 3
- **Theming:** Supports Light and Dark modes. Utilizes Material You dynamic theming where available, falling back to the defined brand theme.
- **Density:** Default density scale.

### Colors
- **Seed Color:** `#5D55FE` (A vibrant purple, representative of the Rocket Money brand)
- **Generated Material 3 Color Roles (Light Theme):**
  - `md.sys.color.primary`: `#5D55FE`
  - `md.sys.color.onPrimary`: `#FFFFFF`
  - `md.sys.color.primaryContainer`: `#E4DFFF`
  - `md.sys.color.onPrimaryContainer`: `#190065`
  - `md.sys.color.secondary`: `#5F5C71`
  - `md.sys.color.onSecondary`: `#FFFFFF`
  - `md.sys.color.secondaryContainer`: `#E5DFF9`
  - `md.sys.color.onSecondaryContainer`: `#1C192B`
  - `md.sys.color.tertiary`: `#7B5266`
  - `md.sys.color.onTertiary`: `#FFFFFF`
  - `md.sys.color.tertiaryContainer`: `#FFD8E8`
  - `md.sys.color.onTertiaryContainer`: `#311021`
  - `md.sys.color.error`: `#BA1A1A`
  - `md.sys.color.onError`: `#FFFFFF`
  - `md.sys.color.errorContainer`: `#FFDAD6`
  - `md.sys.color.onErrorContainer`: `#410002`
  - `md.sys.color.background`: `#FFFBFF`
  - `md.sys.color.onBackground`: `#1C1B1F`
  - `md.sys.color.surface`: `#FFFBFF`
  - `md.sys.color.onSurface`: `#1C1B1F`
  - `md.sys.color.surfaceVariant`: `#E6E0EC`
  - `md.sys.color.onSurfaceVariant`: `#48454E`
  - `md.sys.color.outline`: `#79757F`
  - `md.sys.color.inverseOnSurface`: `#F4EFF4`
  - `md.sys.color.inverseSurface`: `#313033`
  - `md.sys.color.inversePrimary`: `#C6BFFF`
- **Generated Material 3 Color Roles (Dark Theme):**
  - `md.sys.color.primary`: `#C6BFFF`
  - `md.sys.color.onPrimary`: `#2E217D`
  - `md.sys.color.primaryContainer`: `#453B95`
  - `md.sys.color.onPrimaryContainer`: `#E4DFFF`
  - `md.sys.color.secondary`: `#C8C3DC`
  - `md.sys.color.onSecondary`: `#312E41`
  - `md.sys.color.secondaryContainer`: `#474459`
  - `md.sys.color.onSecondaryContainer`: `#E5DFF9`
  - `md.sys.color.tertiary`: `#ECB8CF`
  - `md.sys.color.onTertiary`: `#482537`
  - `md.sys.color.tertiaryContainer`: `#613B4D`
  - `md.sys.color.onTertiaryContainer`: `#FFD8E8`
  - `md.sys.color.error`: `#FFB4AB`
  - `md.sys.color.onError`: `#690005`
  - `md.sys.color.errorContainer`: `#93000A`
  - `md.sys.color.onErrorContainer`: `#FFDAD6`
  - `md.sys.color.background`: `#1C1B1F`
  - `md.sys.color.onBackground`: `#E6E1E5`
  - `md.sys.color.surface`: `#1C1B1F`
  - `md.sys.color.onSurface`: `#E6E1E5`
  - `md.sys.color.surfaceVariant`: `#48454E`
  - `md.sys.color.onSurfaceVariant`: `#CAC4D0`
  - `md.sys.color.outline`: `#938F99`
  - `md.sys.color.inverseOnSurface`: `#1C1B1F`
  - `md.sys.color.inverseSurface`: `#E6E1E5`
  - `md.sys.color.inversePrimary`: `#5D55FE`

### Typography
- **Font Family:** Roboto
- **Material 3 Type Scale:**
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
- **Standard Margins:** 16dp horizontal, 24dp vertical.
- **Standard Padding:** 16dp for cards and containers.
- **Minimum Touch Target:** 48dp x 48dp for all interactive elements.

### Accessibility
- **Target Standard:** WCAG 2.1 Level AA.
- **Requirements:**
  - All images and icons must have content descriptions.
  - Text elements must meet minimum contrast ratios.
  - All interactive elements must be focusable and clearly state their purpose.

---

## II. Screen Specifications

### Flow 1: Authentication

---

#### Screen 1: Splash Screen
- **Screen Name/ID:** `01_01_Splash_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.SpaceBetween`, filling max size.

##### Components:
1.  **Component: Spacer**
    - **Name:** `Spacer`
    - **Position & Size:** Fills top space to push content down. `weight = 1f`.
2.  **Component: Image (App Logo)**
    - **Name:** `Image`
    - **Position & Size:** Centered horizontally. `width = 120dp`, `height = 120dp`.
    - **Style:** No tint.
    - **Content:** `rocket_money_logo.svg`. Content description: "Rocket Money Logo".
3.  **Component: Text (Tagline)**
    - **Name:** `Text`
    - **Position & Size:** Centered horizontally. `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.headlineSmall`. Color: `md.sys.color.onSurface`. Text alignment: Center.
    - **Content:** "Take control of your money."
4.  **Component: Spacer**
    - **Name:** `Spacer`
    - **Position & Size:** Fills space between logo and buttons. `weight = 1f`.
5.  **Component: Button Container**
    - **Name:** `Column`
    - **Position & Size:** Aligned to bottom center. `padding = 16dp` horizontal, `32dp` bottom.
    - **Layout:** Contains the Sign Up and Log In buttons.
6.  **Component: Filled Button (Sign Up)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** "Sign Up for Free"
7.  **Component: Text Button (Log In)**
    - **Name:** `TextButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 8dp`.
    - **Style:** Content Color: `md.sys.color.primary`. Typography: `md.sys.typography.labelLarge`.
    - **Content:** "Log In"

##### Interaction & Behavior:
- **Sign Up Button:** On tap -> Navigate to `01_02_Sign_Up_Screen` using `MaterialSharedAxis(Z, forward = true)`.
- **Log In Button:** On tap -> Navigate to `01_03_Log_In_Screen` using `MaterialSharedAxis(Z, forward = true)`.

---

#### Screen 2: Sign Up Screen
- **Screen Name/ID:** `01_02_Sign_Up_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with vertical scroll enabled. `padding = 16dp` horizontal.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `height = 56dp`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** No title. Contains a back navigation icon.
    - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.headlineLarge`. Color: `md.sys.color.onSurface`.
    - **Content:** "Create your account"
3.  **Component: Outlined Text Field (Email)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`.
    - **Content:** Label: "Email". Leading Icon: `Icons.Filled.Email`.
4.  **Component: Outlined Text Field (Password)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". Leading Icon: `Icons.Filled.Lock`. Trailing Icon: `IconButton` to toggle password visibility.
5.  **Component: Filled Button (Create Account)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** "Create account"
6.  **Component: Divider with Text**
    - **Name:** `Row` containing `Divider`, `Text`, `Divider`.
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`, `verticalAlignment = Alignment.CenterVertically`.
    - **Style:** `Divider` color: `md.sys.color.outline`. `Text` typography: `md.sys.typography.bodyMedium`, color: `md.sys.color.onSurfaceVariant`.
    - **Content:** Text: "or"
7.  **Component: Outlined Button (Continue with Google)**
    - **Name:** `OutlinedButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 32dp`.
    - **Style:** Outline Color: `md.sys.color.outline`. Content Color: `md.sys.color.onSurface`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** Icon: Google logo (`google_logo.svg`). Text: "Continue with Google".
8.  **Component: Outlined Button (Continue with Apple)**
    - **Name:** `OutlinedButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 16dp`.
    - **Style:** Outline Color: `md.sys.color.outline`. Content Color: `md.sys.color.onSurface`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** Icon: Apple logo (`apple_logo.svg`). Text: "Continue with Apple".
9.  **Component: Row (Log In Prompt)**
    - **Name:** `Row`
    - **Position & Size:** Centered horizontally, `marginTop = 32dp`.
    - **Content:** `Text` ("Already have an account?") and `TextButton` ("Log In").
    - **Style:** `Text` color: `md.sys.color.onSurface`. `TextButton` content color: `md.sys.color.primary`.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `01_01_Splash_Screen`.
- **Create Account Button:** On tap -> Validate fields. If valid, show `CircularProgressIndicator` and navigate to `02_01_Connect_Your_Bank_Screen`. If invalid, show error message on `TextField`.
- **Continue with Google/Apple:** On tap -> Initiate social sign-in flow. On success, navigate to `02_01_Connect_Your_Bank_Screen`.
- **Log In TextButton:** On tap -> Navigate to `01_03_Log_In_Screen`.

---

#### Screen 3: Log In Screen
- **Screen Name/ID:** `01_03_Log_In_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with vertical scroll enabled. `padding = 16dp` horizontal.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `height = 56dp`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** No title. Contains a back navigation icon.
    - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.headlineLarge`. Color: `md.sys.color.onSurface`.
    - **Content:** "Welcome back"
3.  **Component: Outlined Text Field (Email)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`.
    - **Content:** Label: "Email". Leading Icon: `Icons.Filled.Email`.
4.  **Component: Outlined Text Field (Password)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". Leading Icon: `Icons.Filled.Lock`. Trailing Icon: `IconButton` to toggle password visibility.
5.  **Component: Text Button (Forgot Password)**
    - **Name:** `TextButton`
    - **Position & Size:** Aligned to the end of the password field row. `marginTop = 8dp`.
    - **Style:** Content Color: `md.sys.color.primary`. Typography: `md.sys.typography.labelLarge`.
    - **Content:** "Forgot password?"
6.  **Component: Filled Button (Log In)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** "Log In"
7.  **Component: Row (Sign Up Prompt)**
    - **Name:** `Row`
    - **Position & Size:** Centered horizontally, `marginTop = 32dp`.
    - **Content:** `Text` ("Don't have an account?") and `TextButton` ("Sign Up").
    - **Style:** `Text` color: `md.sys.color.onSurface`. `TextButton` content color: `md.sys.color.primary`.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `01_01_Splash_Screen`.
- **Log In Button:** On tap -> Validate fields. On success, navigate to `03_01_Dashboard_Screen`. On failure, show `Snackbar` with "Invalid email or password."
- **Forgot Password? Button:** On tap -> Navigate to `01_04_Forgot_Password_Screen`.
- **Sign Up TextButton:** On tap -> Navigate to `01_02_Sign_Up_Screen`.

---

#### Screen 4: Forgot Password Screen
- **Screen Name/ID:** `01_04_Forgot_Password_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`. `padding = 16dp` horizontal.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `height = 56dp`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: "Reset Password". Contains a back navigation icon.
    - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
2.  **Component: Text (Instruction)**
    - **Name:** `Text`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`.
    - **Content:** "Enter the email address associated with your account and we'll send you a link to reset your password."
3.  **Component: Outlined Text Field (Email)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`.
    - **Content:** Label: "Email". Leading Icon: `Icons.Filled.Email`.
4.  **Component: Filled Button (Send Reset Link)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** "Send Reset Link"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `01_03_Log_In_Screen`.
- **Send Reset Link Button:** On tap -> Validate email. If valid, show a `Snackbar` with "Password reset link sent." and navigate back to `01_03_Log_In_Screen`.

---

### Flow 2: Onboarding & Account Linking

---

#### Screen 5: Connect Your Bank Screen
- **Screen Name/ID:** `02_01_Connect_Your_Bank_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding = 24dp`.

##### Components:
1.  **Component: Image (Illustration)**
    - **Name:** `Image`
    - **Position & Size:** Centered. `width = 200dp`, `height = 200dp`.
    - **Content:** `secure_connection_illustration.svg`. Content description: "Illustration of a secure bank connection."
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text alignment: Center.
    - **Content:** "Connect your bank to see the full picture"
3.  **Component: Text (Body)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    - **Content:** "We use Plaid to securely connect to over 11,000 institutions with bank-level security."
4.  **Component: Filled Button (Connect Account)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 48dp`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`. Typography: `md.sys.typography.labelLarge`. Shape: `ShapeDefaults.Full`.
    - **Content:** "Connect my main account"

##### Interaction & Behavior:
- **Connect Button:** On tap -> Navigate to `02_02_Select_Institution_Screen` using `MaterialSharedAxis(X, forward = true)`.

---

#### Screen 6: Select Institution Screen
- **Screen Name/ID:** `02_02_Select_Institution_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `height = 56dp`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: "Select your bank". Contains a close icon.
    - **Navigation Icon:** `IconButton` with `Icons.Filled.Close`. Content description: "Close".
2.  **Component: Search Bar**
    - **Name:** `SearchBar` (or `OutlinedTextField` styled as a search bar)
    - **Position & Size:** `fillMaxWidth`, `padding = 16dp` horizontal, `8dp` vertical.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** Placeholder text: "Search for your bank". Leading Icon: `Icons.Filled.Search`.
3.  **Component: LazyColumn (Bank List)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space. `contentPadding = 16dp` horizontal.
    - **Content:** A list of popular financial institutions. Each item is a `ListItem`.
4.  **Component: ListItem (Bank Item)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Clickable.
    - **Content:**
        - `leadingContent`: `Image` of the bank logo (e.g., Chase, Bank of America), `size = 40dp`.
        - `headlineContent`: `Text` with the bank name. Typography: `md.sys.typography.bodyLarge`.
        - `trailingContent`: `Icon` `Icons.Filled.ChevronRight`.

##### Interaction & Behavior:
- **Close Icon:** On tap -> Abort flow and navigate to `03_01_Dashboard_Screen`.
- **Search Bar:** On tap -> Navigate to `02_03_Search_Institution_Screen`.
- **Bank ListItem:** On tap -> Navigate to `02_04_Enter_Bank_Credentials_Screen`, passing the selected institution's ID.

---

#### Screen 7: Search Institution Screen
- **Screen Name/ID:** `02_03_Search_Institution_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: Search Bar**
    - **Name:** `SearchBar` (Active state)
    - **Position & Size:** Top of the screen, `fillMaxWidth`.
    - **Style:** Automatically focused with keyboard visible.
    - **Content:** Leading Icon: `Icons.Filled.ArrowBack`. Trailing Icon: `Icons.Filled.Clear` (when text is present).
2.  **Component: LazyColumn (Search Results)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space.
    - **Content:**
        - **Initial State:** Empty.
        - **No Results State:** A `Column` with an `Icon` and `Text` ("No results found").
        - **Results State:** A list of `ListItem` components for each matching institution, identical in style to `02_02_Select_Institution_Screen`.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `02_02_Select_Institution_Screen`.
- **Text Input:** As user types, dynamically filter and display results in the `LazyColumn`.
- **Clear Icon:** On tap -> Clear the text in the search bar.
- **Result ListItem:** On tap -> Navigate to `02_04_Enter_Bank_Credentials_Screen`, passing the selected institution's ID.

---

#### Screen 8: Enter Bank Credentials Screen
- **Screen Name/ID:** `02_04_Enter_Bank_Credentials_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`. `padding = 16dp` horizontal.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen. `height = 56dp`.
    - **Style:** Container Color: `md.sys.color.surface`.
    - **Content:** Title: "[Institution Name]". Contains a back navigation icon.
    - **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`. Content description: "Back".
2.  **Component: Image (Bank Logo)**
    - **Name:** `Image`
    - **Position & Size:** Centered horizontally, `marginTop = 32dp`. `size = 64dp`.
    - **Content:** Logo of the selected institution.
3.  **Component: Text (Instruction)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`. Text alignment: Center.
    - **Style:** Typography: `md.sys.typography.bodyMedium`. Color: `md.sys.color.onSurfaceVariant`.
    - **Content:** "Enter your credentials for [Institution Name]. Your information is encrypted and will not be shared."
4.  **Component: Outlined Text Field (Username)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`.
    - **Content:** Label: "Username" or "User ID".
5.  **Component: Outlined Text Field (Password)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Style:** `visualTransformation = PasswordVisualTransformation()`.
    - **Content:** Label: "Password". Trailing Icon: `IconButton` to toggle password visibility.
6.  **Component: Filled Button (Submit)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Submit"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `02_02_Select_Institution_Screen`.
- **Submit Button:** On tap -> Navigate to `02_05_Connecting_Account_Screen`.

---

#### Screen 9: Connecting Account Screen
- **Screen Name/ID:** `02_05_Connecting_Account_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.

##### Components:
1.  **Component: Circular Progress Indicator**
    - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered. `size = 64dp`.
    - **Style:** Color: `md.sys.color.primary`.
2.  **Component: Text (Status)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "Connecting securely..."

##### Interaction & Behavior:
- **System Action:** After a simulated delay (2-5 seconds), automatically navigate to `02_06_Connection_Successful_Screen`.
- **Error State:** If connection fails, show an `AlertDialog` with an error message and buttons to "Try Again" (returns to `02_04`) or "Cancel" (returns to `02_02`).

---

#### Screen 10: Connection Successful Screen
- **Screen Name/ID:** `02_06_Connection_Successful_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding = 24dp`.

##### Components:
1.  **Component: Icon**
    - **Name:** `Icon`
    - **Position & Size:** Centered. `size = 80dp`.
    - **Style:** Tint: A success color (e.g., `#2E7D32`).
    - **Content:** `Icons.Filled.CheckCircle`. Content description: "Success".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text alignment: Center.
    - **Content:** "Account Connected!"
3.  **Component: Text (Body)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    - **Content:** "You have successfully linked your [Institution Name] account."
4.  **Component: Filled Button (Continue)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 48dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Continue"

##### Interaction & Behavior:
- **Continue Button:** On tap -> Navigate to `02_07_Analyzing_Transactions_Screen`.

---

#### Screen 11: Analyzing Transactions Screen
- **Screen Name/ID:** `02_07_Analyzing_Transactions_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.

##### Components:
1.  **Component: Circular Progress Indicator**
    - **Name:** `CircularProgressIndicator`
    - **Position & Size:** Centered. `size = 64dp`.
    - **Style:** Color: `md.sys.color.primary`.
2.  **Component: Text (Status)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.titleMedium`. Color: `md.sys.color.onSurface`.
    - **Content:** "Analyzing your transactions..."

##### Interaction & Behavior:
- **System Action:** After a simulated delay (2-5 seconds), automatically navigate to `02_08_Found_Recurring_Bills_Screen`.

---

#### Screen 12: Found Recurring Bills Screen
- **Screen Name/ID:** `02_08_Found_Recurring_Bills_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding = 24dp`.

##### Components:
1.  **Component: Icon**
    - **Name:** `Icon`
    - **Position & Size:** Centered. `size = 80dp`.
    - **Style:** Tint: `md.sys.color.primary`.
    - **Content:** `Icons.Filled.ReceiptLong`. Content description: "Bills".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text alignment: Center.
    - **Content:** "We found 7 recurring bills"
3.  **Component: Text (Body)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    - **Content:** "We'll help you track them so you never miss a payment."
4.  **Component: Filled Button (Continue)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 48dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Continue"

##### Interaction & Behavior:
- **Continue Button:** On tap -> Navigate to `02_09_Found_Subscriptions_Screen`.

---

#### Screen 13: Found Subscriptions Screen
- **Screen Name/ID:** `02_09_Found_Subscriptions_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding = 24dp`.

##### Components:
1.  **Component: Icon**
    - **Name:** `Icon`
    - **Position & Size:** Centered. `size = 80dp`.
    - **Style:** Tint: `md.sys.color.primary`.
    - **Content:** `Icons.Filled.Autorenew`. Content description: "Subscriptions".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Color: `md.sys.color.onSurface`. Text alignment: Center.
    - **Content:** "And 4 subscriptions you might have forgotten"
3.  **Component: Text (Body)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    - **Content:** "Let us cancel the ones you don't want anymore."
4.  **Component: Filled Button (Continue)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 48dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Continue"

##### Interaction & Behavior:
- **Continue Button:** On tap -> Navigate to `03_01_Dashboard_Screen` using `MaterialFadeThrough`.

---

### Flow 3: Main Navigation

---

#### Screen 14: Dashboard Screen
- **Screen Name/ID:** `03_01_Dashboard_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn` for content, and `NavigationBar`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Style:** `scrollBehavior = TopAppBarDefaults.enterAlwaysScrollBehavior()`.
    - **Content:**
        - `title`: `Text` "Hi, [User Name]".
        - `actions`: `IconButton` with `Icons.Filled.Settings`. Content description: "Settings".
2.  **Component: LazyColumn (Dashboard Content)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the content area of the `Scaffold`. `contentPadding = 16dp` horizontal.
    - **Content:** A series of `Card` components.
3.  **Component: Card (Spending Overview)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Style:** `CardDefaults.elevatedCardColors()`.
    - **Content:** `Column` with a title ("Spending This Month"), a large amount (`$1,234.56`), a progress bar, and a `TextButton` ("View all spending").
4.  **Component: Card (Recurring Bills)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Style:** `CardDefaults.outlinedCardColors()`.
    - **Content:** `Column` with a title ("Upcoming Bills"), a list of 2-3 upcoming bills (`ListItem`), and a `TextButton` ("View all recurring").
5.  **Component: Card (Budget Overview)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Style:** `CardDefaults.outlinedCardColors()`.
    - **Content:** `Column` with a title ("Budgets"), a summary of budget progress, and a `TextButton` ("Manage budgets").
6.  **Component: NavigationBar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`.
    - **Style:** Container Color: `md.sys.color.surfaceVariant`.
    - **Content:** Four `NavigationBarItem`s.
        - **Item 1 (Dashboard):** Selected. Icon: `Icons.Filled.Dashboard`. Label: "Dashboard".
        - **Item 2 (Spending):** Icon: `Icons.Outlined.PieChart`. Label: "Spending".
        - **Item 3 (Recurring):** Icon: `Icons.Outlined.Autorenew`. Label: "Recurring".
        - **Item 4 (Budget):** Icon: `Icons.Outlined.Savings`. Label: "Budget".

##### Interaction & Behavior:
- **Settings Icon:** On tap -> Navigate to `07_01_Settings_Screen`.
- **View all spending Button:** On tap -> Navigate to `03_02_Spending_Screen`.
- **Recurring Bill ListItem:** On tap -> Navigate to `05_01_Subscription_Details_Screen`.
- **Spending Tab:** On tap -> Navigate to `03_02_Spending_Screen`.
- **Recurring Tab:** On tap -> Navigate to `03_03_Recurring_Screen`.
- **Budget Tab:** On tap -> Navigate to `03_04_Budget_Screen`.

---

#### Screen 15: Spending Screen
- **Screen Name/ID:** `03_02_Spending_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Spending".
2.  **Component: LazyColumn (Spending Content)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills content area. `contentPadding = 16dp`.
    - **Content:**
        - A `Card` containing a pie chart visualization of spending by category.
        - A `Text` header "Spending by Category".
        - A list of `ListItem`s, one for each category.
3.  **Component: ListItem (Category)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Clickable.
    - **Content:**
        - `leadingContent`: `Icon` for the category (e.g., `Icons.Filled.ShoppingCart` for Shopping).
        - `headlineContent`: `Text` with category name.
        - `supportingContent`: `LinearProgressIndicator` showing spending vs. total.
        - `trailingContent`: `Text` with amount spent (e.g., "$250.75").
4.  **Component: NavigationBar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`.
    - **Content:**
        - **Item 1 (Dashboard):** Icon: `Icons.Outlined.Dashboard`. Label: "Dashboard".
        - **Item 2 (Spending):** Selected. Icon: `Icons.Filled.PieChart`. Label: "Spending".
        - **Item 3 (Recurring):** Icon: `Icons.Outlined.Autorenew`. Label: "Recurring".
        - **Item 4 (Budget):** Icon: `Icons.Outlined.Savings`. Label: "Budget".

##### Interaction & Behavior:
- **Category ListItem:** On tap -> Navigate to `06_01_Category_Spending_Details_Screen`.
- **Navigation Tabs:** Navigate to corresponding screens (`Dashboard`, `Recurring`, `Budget`).

---

#### Screen 16: Recurring Screen
- **Screen Name/ID:** `03_03_Recurring_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Recurring".
2.  **Component: LazyColumn (Recurring Content)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills content area.
    - **Content:**
        - A `Text` subheader "Upcoming this month".
        - A list of `ListItem`s for upcoming bills.
        - A `Divider`.
        - A `Text` subheader "All recurring".
        - A list of `ListItem`s for all subscriptions and bills.
3.  **Component: ListItem (Subscription)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Clickable.
    - **Content:**
        - `leadingContent`: `Image` of the service logo (e.g., Netflix).
        - `headlineContent`: `Text` with service name.
        - `supportingContent`: `Text` with next payment date.
        - `trailingContent`: `Text` with amount.
4.  **Component: NavigationBar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`.
    - **Content:**
        - **Item 1 (Dashboard):** Icon: `Icons.Outlined.Dashboard`. Label: "Dashboard".
        - **Item 2 (Spending):** Icon: `Icons.Outlined.PieChart`. Label: "Spending".
        - **Item 3 (Recurring):** Selected. Icon: `Icons.Filled.Autorenew`. Label: "Recurring".
        - **Item 4 (Budget):** Icon: `Icons.Outlined.Savings`. Label: "Budget".

##### Interaction & Behavior:
- **Subscription ListItem:** On tap -> Navigate to `05_01_Subscription_Details_Screen`.
- **Navigation Tabs:** Navigate to corresponding screens.

---

#### Screen 17: Budget Screen
- **Screen Name/ID:** `03_04_Budget_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`, content area, `FloatingActionButton`, and `NavigationBar`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Budget".
2.  **Component: Content Area**
    - **Name:** `Box`
    - **Position & Size:** Fills content area.
    - **Content:** Displays either the `Empty State` or the `Budget List`.
3.  **Component: Empty State**
    - **Name:** `Column`
    - **Position & Size:** Centered in the `Box`. `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Content:**
        - `Icon`: `Icons.Outlined.Savings`, `size = 80dp`, tint: `md.sys.color.onSurfaceVariant`.
        - `Text`: "Create your first budget", typography: `md.sys.typography.titleLarge`, `marginTop = 16dp`.
        - `Text`: "Track your spending by category to stay on top of your goals.", typography: `md.sys.typography.bodyMedium`, color: `md.sys.color.onSurfaceVariant`, `marginTop = 8dp`, text alignment: Center.
4.  **Component: Budget List**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills the `Box`. `contentPadding = 16dp`.
    - **Content:** A list of `Card` components, one for each budget.
5.  **Component: Card (Budget Item)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Content:** `Column` with `padding = 16dp`. Includes category name, amount spent vs. total (e.g., "$150 / $400"), and a `LinearProgressIndicator`.
6.  **Component: FloatingActionButton**
    - **Name:** `FloatingActionButton`
    - **Position & Size:** Bottom right corner of the `Scaffold`.
    - **Style:** Container Color: `md.sys.color.primary`. Content Color: `md.sys.color.onPrimary`.
    - **Content:** `Icon` `Icons.Filled.Add`. Content description: "Create Budget".
7.  **Component: NavigationBar**
    - **Name:** `NavigationBar`
    - **Position & Size:** Bottom of the `Scaffold`.
    - **Content:**
        - **Item 1 (Dashboard):** Icon: `Icons.Outlined.Dashboard`. Label: "Dashboard".
        - **Item 2 (Spending):** Icon: `Icons.Outlined.PieChart`. Label: "Spending".
        - **Item 3 (Recurring):** Icon: `Icons.Outlined.Autorenew`. Label: "Recurring".
        - **Item 4 (Budget):** Selected. Icon: `Icons.Filled.Savings`. Label: "Budget".

##### Interaction & Behavior:
- **FAB (+ Create Budget):** On tap -> Navigate to `04_01_Choose_Category_Screen`.
- **Navigation Tabs:** Navigate to corresponding screens.

---

### Flow 4: Creating a Budget

---

#### Screen 18: Choose Category Screen
- **Screen Name/ID:** `04_01_Choose_Category_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Choose a category". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Category List)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space.
    - **Content:** A list of selectable categories.
3.  **Component: ListItem (Selectable Category)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Clickable.
    - **Content:**
        - `leadingContent`: `Icon` for the category.
        - `headlineContent`: `Text` with the category name.
        - `trailingContent`: `Icon` `Icons.Filled.ChevronRight`.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `03_04_Budget_Screen`.
- **Category ListItem:** On tap -> Navigate to `04_02_Set_Budget_Amount_Screen`, passing the selected category.

---

#### Screen 19: Set Budget Amount Screen
- **Screen Name/ID:** `04_02_Set_Budget_Amount_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`, `padding = 16dp`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Set Budget for [Category]". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Text (Instruction)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.titleLarge`.
    - **Content:** "How much do you want to budget for [Category] per month?"
3.  **Component: Outlined Text Field (Amount)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 32dp`.
    - **Style:** `keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)`.
    - **Content:** Label: "Budget Amount". Leading content: `Text`("$").
4.  **Component: Filled Button (Create Budget)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Create Budget"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `04_01_Choose_Category_Screen`.
- **Create Budget Button:** On tap -> Validate amount. On success, navigate to `04_03_Budget_Details_Screen`.

---

#### Screen 20: Budget Details Screen
- **Screen Name/ID:** `04_03_Budget_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "[Category] Budget". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Budget Details)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills content area. `contentPadding = 16dp`.
    - **Content:**
        - A `Card` showing the budget overview (progress bar, amount remaining).
        - A `Text` subheader "Transactions in this budget".
        - A list of `ListItem`s for each transaction.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `03_04_Budget_Screen`.

---

### Flow 5: Canceling a Subscription

---

#### Screen 21: Subscription Details Screen
- **Screen Name/ID:** `05_01_Subscription_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** No title. Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Header Section**
    - **Name:** `Column`
    - **Position & Size:** `padding = 24dp`, `horizontalAlignment = Alignment.CenterHorizontally`.
    - **Content:**
        - `Image`: Service logo, `size = 80dp`.
        - `Text`: Service name (e.g., "Netflix"), typography: `md.sys.typography.headlineMedium`, `marginTop = 16dp`.
        - `Text`: Amount (e.g., "$15.99 / month"), typography: `md.sys.typography.titleMedium`, `marginTop = 4dp`.
3.  **Component: Divider**
    - **Name:** `Divider`
    - **Position & Size:** `fillMaxWidth`.
4.  **Component: Details List**
    - **Name:** `Column`
    - **Position & Size:** `padding = 16dp`.
    - **Content:** `ListItem`s for "Next Payment Date", "Category", "Payment History".
5.  **Component: Filled Button (Cancel Service)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `margin = 16dp`.
    - **Style:** Container Color: `md.sys.color.primary`.
    - **Content:** "Cancel this service for me"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `03_03_Recurring_Screen`.
- **Cancel Button:** On tap -> Navigate to `05_02_Cancellation_Method_Screen`.

---

#### Screen 22: Cancellation Method Screen
- **Screen Name/ID:** `05_02_Cancellation_Method_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "How to Cancel". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Methods)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space. `contentPadding = 16dp`.
    - **Content:** A list of selectable `Card`s for cancellation methods.
3.  **Component: Card (Selectable Method)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Style:** `CardDefaults.outlinedCardColors()`, clickable.
    - **Content:** `ListItem` with `headlineContent` ("Let Rocket Money cancel for you"), `supportingContent` ("We contact the provider and handle everything."), and `trailingContent` (`RadioButton`).

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `05_01_Subscription_Details_Screen`.
- **Select Method:** On tap of a card/radio button -> Navigate to `05_03_Cancellation_Confirmation_Screen`.

---

#### Screen 23: Cancellation Confirmation Screen
- **Screen Name/ID:** `05_03_Cancellation_Confirmation_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`, `padding = 16dp`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Confirm Cancellation". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Text (Summary)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`.
    - **Content:** "You are requesting Rocket Money to cancel your [Service Name] subscription. We will notify you once the cancellation is complete. This process can take up to 48 hours."
3.  **Component: Filled Button (Confirm)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 32dp`.
    - **Style:** Container Color: `md.sys.color.error`. Content Color: `md.sys.color.onError`.
    - **Content:** "Confirm Cancellation Request"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `05_02_Cancellation_Method_Screen`.
- **Confirm Button:** On tap -> Navigate to `05_04_Cancellation_In_Progress_Screen`.

---

#### Screen 24: Cancellation In Progress Screen
- **Screen Name/ID:** `05_04_Cancellation_In_Progress_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`, `padding = 24dp`.

##### Components:
1.  **Component: Icon**
    - **Name:** `Icon`
    - **Position & Size:** Centered. `size = 80dp`.
    - **Style:** Tint: `md.sys.color.primary`.
    - **Content:** `Icons.Filled.HourglassTop`. Content description: "In Progress".
2.  **Component: Text (Header)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 32dp`.
    - **Style:** Typography: `md.sys.typography.headlineMedium`. Text alignment: Center.
    - **Content:** "Cancellation in Progress"
3.  **Component: Text (Body)**
    - **Name:** `Text`
    - **Position & Size:** `marginTop = 16dp`.
    - **Style:** Typography: `md.sys.typography.bodyLarge`. Color: `md.sys.color.onSurfaceVariant`. Text alignment: Center.
    - **Content:** "We've started the cancellation process for [Service Name]. We'll update you on the status in the app and via email."
4.  **Component: Filled Button (Done)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 48dp`.
    - **Style:** Shape: `ShapeDefaults.Full`.
    - **Content:** "Done"

##### Interaction & Behavior:
- **Done Button:** On tap -> Navigate to `03_03_Recurring_Screen`.

---

### Flow 6: Viewing Spending

---

#### Screen 25: Category Spending Details Screen
- **Screen Name/ID:** `06_01_Category_Spending_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "[Category Name] Spending". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Transaction List)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills content area.
    - **Content:**
        - A `Card` with a bar chart showing spending over time for this category.
        - A `Text` subheader "Transactions".
        - A list of `ListItem`s for each transaction in the category.
3.  **Component: ListItem (Transaction)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Style:** Clickable.
    - **Content:**
        - `leadingContent`: `Icon` for the merchant.
        - `headlineContent`: `Text` with merchant name.
        - `supportingContent`: `Text` with transaction date.
        - `trailingContent`: `Text` with amount.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `03_02_Spending_Screen`.
- **Transaction ListItem:** On tap -> Navigate to `06_02_Transaction_Details_Screen`.

---

#### Screen 26: Transaction Details Screen
- **Screen Name/ID:** `06_02_Transaction_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Transaction Details". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Details Section**
    - **Name:** `Column`
    - **Position & Size:** `padding = 16dp`.
    - **Content:**
        - `ListItem` with `headlineContent`: "Merchant", `supportingContent`: "[Merchant Name]".
        - `ListItem` with `headlineContent`: "Amount", `supportingContent`: "[Amount]".
        - `ListItem` with `headlineContent`: "Date", `supportingContent`: "[Date]".
        - `ListItem` with `headlineContent`: "Category", `supportingContent`: "[Category Name]", with a trailing "Edit" `TextButton`.
        - `ListItem` with `headlineContent`: "Account", `supportingContent`: "[Account Name]".

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `06_01_Category_Spending_Details_Screen`.

---

### Flow 7: Settings

---

#### Screen 27: Settings Screen
- **Screen Name/ID:** `07_01_Settings_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Settings". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Settings List)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space.
    - **Content:**
        - `ListItem` for "Profile". Leading Icon: `Icons.Filled.Person`. Trailing Icon: `Icons.Filled.ChevronRight`.
        - `ListItem` for "Linked Accounts". Leading Icon: `Icons.Filled.AccountBalance`. Trailing Icon: `Icons.Filled.ChevronRight`.
        - `ListItem` for "Notifications". Leading Icon: `Icons.Filled.Notifications`. Trailing Icon: `Icons.Filled.ChevronRight`.
        - `Divider`.
        - `ListItem` for "Log Out". Leading Icon: `Icons.Filled.Logout`. Text color: `md.sys.color.error`.

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `03_01_Dashboard_Screen`.
- **Profile:** On tap -> Navigate to `07_02_Profile_Screen`.
- **Linked Accounts:** On tap -> Navigate to `07_03_Linked_Accounts_Screen`.
- **Notifications:** On tap -> Navigate to `07_06_Notifications_Screen`.
- **Log Out:** On tap -> Show confirmation dialog. On confirm, clear session and navigate to `01_01_Splash_Screen`.

---

#### Screen 28: Profile Screen
- **Screen Name/ID:** `07_02_Profile_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`, `padding = 16dp`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Profile". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Outlined Text Field (Name)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Content:** Label: "Name", pre-filled with user's name.
3.  **Component: Outlined Text Field (Email)**
    - **Name:** `OutlinedTextField`
    - **Position & Size:** `fillMaxWidth`, `marginTop = 16dp`.
    - **Content:** Label: "Email", pre-filled with user's email, `enabled = false`.
4.  **Component: Filled Button (Save Changes)**
    - **Name:** `FilledButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 24dp`.
    - **Content:** "Save Changes"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `07_01_Settings_Screen`.

---

#### Screen 29: Linked Accounts Screen
- **Screen Name/ID:** `07_03_Linked_Accounts_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.background`
- **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `FloatingActionButton`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Linked Accounts". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Account List)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills content area. `contentPadding = 16dp`.
    - **Content:** A list of `Card`s, one for each linked account.
3.  **Component: Card (Linked Account)**
    - **Name:** `Card`
    - **Position & Size:** `fillMaxWidth`, `marginBottom = 16dp`.
    - **Style:** Clickable.
    - **Content:** `ListItem` with bank logo, bank name, and account type (e.g., "Chase Checking").
4.  **Component: FloatingActionButton**
    - **Name:** `FloatingActionButton`
    - **Position & Size:** Bottom right corner.
    - **Content:** `Icon` `Icons.Filled.Add`. Content description: "Link another account".

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `07_01_Settings_Screen`.
- **Account Card:** On tap -> Navigate to `07_04_Account_Details_Screen`.
- **FAB:** On tap -> Navigate to `02_02_Select_Institution_Screen`.

---

#### Screen 30: Account Details Screen
- **Screen Name/ID:** `07_04_Account_Details_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`, `padding = 16dp`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "[Account Name]". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: Details Section**
    - **Name:** `Column`
    - **Position & Size:** `marginTop = 16dp`.
    - **Content:** `ListItem`s showing account details like "Institution", "Account Type", "Last Updated".
3.  **Component: Outlined Button (Unlink Account)**
    - **Name:** `OutlinedButton`
    - **Position & Size:** `fillMaxWidth`, `height = 52dp`, `marginTop = 32dp`.
    - **Style:** Outline Color: `md.sys.color.error`. Content Color: `md.sys.color.error`.
    - **Content:** "Unlink Account"

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `07_03_Linked_Accounts_Screen`.
- **Unlink Button:** On tap -> Show `07_05_Unlink_Confirmation_Modal`.

---

#### Screen 31: Unlink Confirmation Modal
- **Screen Name/ID:** `07_05_Unlink_Confirmation_Modal`
- **Dimensions:** Modal dialog, typically 280dp width.
- **Background:** `md.sys.color.surface` with elevation.
- **Layout:** `AlertDialog`.

##### Components:
1.  **Component: AlertDialog**
    - **Name:** `AlertDialog`
    - **Content:**
        - `icon`: `Icon` `Icons.Filled.Warning`, tint: `md.sys.color.error`.
        - `title`: `Text` "Unlink Account?".
        - `text`: `Text` "Are you sure you want to unlink this account? All associated data will be removed.".
        - `confirmButton`: `TextButton` with text "Unlink". Text color: `md.sys.color.error`.
        - `dismissButton`: `TextButton` with text "Cancel".

##### Interaction & Behavior:
- **Unlink Button:** On tap -> Dismiss modal, perform unlink action, and navigate back to `07_03_Linked_Accounts_Screen`.
- **Cancel Button:** On tap -> Dismiss modal, returning to `07_04_Account_Details_Screen`.

---

#### Screen 32: Notifications Screen
- **Screen Name/ID:** `07_06_Notifications_Screen`
- **Dimensions:** 393x852dp
- **Background:** `md.sys.color.surface`
- **Layout:** `Column`.

##### Components:
1.  **Component: TopAppBar**
    - **Name:** `TopAppBar`
    - **Position & Size:** Top of the screen.
    - **Content:** Title: "Notifications". Navigation Icon: `Icons.Filled.ArrowBack`.
2.  **Component: LazyColumn (Notification Toggles)**
    - **Name:** `LazyColumn`
    - **Position & Size:** Fills remaining space.
    - **Content:** A list of `ListItem`s for different notification types.
3.  **Component: ListItem (Notification Toggle)**
    - **Name:** `ListItem`
    - **Position & Size:** `fillMaxWidth`.
    - **Content:**
        - `headlineContent`: `Text` with notification type (e.g., "Upcoming Bill Reminders").
        - `supportingContent`: `Text` with a brief description.
        - `trailingContent`: `Switch` component (toggled on/off).

##### Interaction & Behavior:
- **Back Icon:** On tap -> Navigate back to `07_01_Settings_Screen`.
- **Switch:** On toggle -> Update user's notification preferences. The state is persistent.

---

## V. Critical Scenarios & States

### Error States
- **No Internet:** A `Snackbar` appears at the bottom of the screen with the message "No internet connection." and an optional "Retry" action.
- **API Error:** A `Snackbar` appears with a generic message like "Something went wrong. Please try again."
- **Text Field Validation:** The `OutlinedTextField` border and label color change to `md.sys.color.error`. `supportingText` appears below the field with a specific error message (e.g., "Invalid email format").

### Empty States
- **General Pattern:** An empty state consists of a central `Column` containing:
    1.  An `Icon` from Material Symbols (e.g., `Icons.Outlined.Inbox`), sized at `80dp`, tinted with `md.sys.color.onSurfaceVariant`.
    2.  A `Text` headline using `md.sys.typography.titleLarge`.
    3.  A `Text` body using `md.sys.typography.bodyMedium` and `md.sys.color.onSurfaceVariant`.
    4.  (Optional) A primary `FilledButton` or `TextButton` as a call to action.
- **Specific Screens:**
    - **Budget Screen:** As specified in `03_04_Budget_Screen`.
    - **Recurring Screen:** If no recurring bills are found, show a message "No recurring payments found yet."

### Loading States
- **Initial Screen Load:** A centered `CircularProgressIndicator` is displayed while initial data is fetched.
- **Button-triggered Load:** The button that triggered the action becomes disabled, and a small `CircularProgressIndicator` (`size = 24dp`) appears within the button, replacing the text label until the action is complete.
- **Pull-to-Refresh:** Standard `PullToRefresh` indicator is used on lists like the Dashboard, Spending, and Recurring screens.
```

---


============================================================
## APP 3: App_3
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

# Monarch Money: Android Design Specification

## I. Global Specifications

### Platform
*   **Target:** Android Mobile App
*   **API Level:** 34+ (Android 14)

### Design System
*   **System:** Material Design 3
*   **Theming:** Supports Light and Dark modes. Implements dynamic color (Material You) where available, falling back to the defined brand theme.
*   **Density:** Default screen density.

### Colors
*   **Seed Color:** `#00A86B` (Monarch Green)
*   **Generated Color Roles (Light Theme):**
    *   `md.sys.color.primary`: `#006D3D`
    *   `md.sys.color.onPrimary`: `#FFFFFF`
    *   `md.sys.color.primaryContainer`: `#8CF7B6`
    *   `md.sys.color.onPrimaryContainer`: `#00210E`
    *   `md.sys.color.secondary`: `#4F6353`
    *   `md.sys.color.onSecondary`: `#FFFFFF`
    *   `md.sys.color.secondaryContainer`: `#D2E8D4`
    *   `md.sys.color.onSecondaryContainer`: `#0D1F13`
    *   `md.sys.color.tertiary`: `#3C6471`
    *   `md.sys.color.onTertiary`: `#FFFFFF`
    *   `md.sys.color.tertiaryContainer`: `#BFE9F9`
    *   `md.sys.color.onTertiaryContainer`: `#001F27`
    *   `md.sys.color.error`: `#BA1A1A`
    *   `md.sys.color.onError`: `#FFFFFF`
    *   `md.sys.color.errorContainer`: `#FFDAD6`
    *   `md.sys.color.onErrorContainer`: `#410002`
    *   `md.sys.color.background`: `#FBFDF7`
    *   `md.sys.color.onBackground`: `#1A1C1A`
    *   `md.sys.color.surface`: `#FBFDF7`
    *   `md.sys.color.onSurface`: `#1A1C1A`
    *   `md.sys.color.surfaceVariant`: `#DDE5DB`
    *   `md.sys.color.onSurfaceVariant`: `#414942`
    *   `md.sys.color.outline`: `#717971`
    *   `md.sys.color.outlineVariant`: `#C1C9BF`
*   **Generated Color Roles (Dark Theme):**
    *   `md.sys.color.primary`: `#70DA9C`
    *   `md.sys.color.onPrimary`: `#00391C`
    *   `md.sys.color.primaryContainer`: `#00522B`
    *   `md.sys.color.onPrimaryContainer`: `#8CF7B6`
    *   `md.sys.color.secondary`: `#B6CCB8`
    *   `md.sys.color.onSecondary`: `#223527`
    *   `md.sys.color.secondaryContainer`: `#384B3D`
    *   `md.sys.color.onSecondaryContainer`: `#D2E8D4`
    *   `md.sys.color.tertiary`: `#A4CDDC`
    *   `md.sys.color.onTertiary`: `#053641`
    *   `md.sys.color.tertiaryContainer`: `#224C58`
    *   `md.sys.color.onTertiaryContainer`: `#BFE9F9`
    *   `md.sys.color.error`: `#FFB4AB`
    *   `md.sys.color.onError`: `#690005`
    *   `md.sys.color.errorContainer`: `#93000A`
    *   `md.sys.color.onErrorContainer`: `#FFDAD6`
    *   `md.sys.color.background`: `#1A1C1A`
    *   `md.sys.color.onBackground`: `#E2E3DE`
    *   `md.sys.color.surface`: `#1A1C1A`
    *   `md.sys.color.onSurface`: `#E2E3DE`
    *   `md.sys.color.surfaceVariant`: `#414942`
    *   `md.sys.color.onSurfaceVariant`: `#C1C9BF`
    *   `md.sys.color.outline`: `#8B938A`
    *   `md.sys.color.outlineVariant`: `#414942`

### Typography
*   **Font Family:** Roboto
*   **Type Scale:**
    *   `displayLarge`: Roboto 57
    *   `displayMedium`: Roboto 45
    *   `displaySmall`: Roboto 36
    *   `headlineLarge`: Roboto 32
    *   `headlineMedium`: Roboto 28
    *   `headlineSmall`: Roboto 24
    *   `titleLarge`: Roboto 22
    *   `titleMedium`: Roboto Medium 16, Letter Spacing 0.15
    *   `titleSmall`: Roboto Medium 14, Letter Spacing 0.1
    *   `labelLarge`: Roboto Medium 14, Letter Spacing 0.1
    *   `labelMedium`: Roboto Medium 12, Letter Spacing 0.5
    *   `labelSmall`: Roboto Medium 11, Letter Spacing 0.5
    *   `bodyLarge`: Roboto 16, Letter Spacing 0.5
    *   `bodyMedium`: Roboto 14, Letter Spacing 0.25
    *   `bodySmall`: Roboto 12, Letter Spacing 0.4

### Spacing & Sizing
*   **Base Grid Unit:** 8dp
*   **Standard Margins:** 16dp
*   **Standard Padding:** 16dp
*   **Minimum Touch Target:** 48dp x 48dp

### Accessibility
*   **Target Standard:** WCAG 2.1 Level AA
*   **Requirements:** All interactive elements must have content descriptions. Color contrast ratios must meet the standard. Font sizes should be scalable with user system settings.

---

## Flow 1: Connecting an Account

### 01_01_Accounts_Screen
*   **Screen Name/ID:** `01_01_Accounts_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar`, `LazyColumn` for content, and an `ExtendedFloatingActionButton`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Position & Size:** Top of the screen, `height: 64dp`, `width: fillMaxWidth`.
        *   **Style:** `containerColor: md.sys.color.surface`, `titleContentColor: md.sys.color.onSurface`, `elevation: Elevation.Level2` when content is scrolled beneath.
        *   **Content:** Title text "Accounts". `typography: md.sys.typescale.titleLarge`.
    *   **Component 2: Account List**
        *   **Name:** `LazyColumn`
        *   **Position & Size:** Below Top App Bar, fills remaining space. `padding: 16dp` horizontal.
        *   **Content:** Contains a list of `Card` components, one for each account type (e.g., "Cash", "Credit Cards", "Investments").
        *   **Sub-Component: Account Type Card**
            *   **Name:** `Card`
            *   **Position & Size:** `width: fillMaxWidth`, `marginBottom: 16dp`.
            *   **Style:** `containerColor: md.sys.color.surfaceVariant`, `shape: Shape.Corner.Medium`.
            *   **Content:** A `Column` containing a header `ListItem` and subsequent `ListItem`s for each account.
            *   **Sub-Component: Card Header**
                *   **Name:** `ListItem`
                *   **Content:** Headline text (e.g., "Cash"), supporting text (total balance, e.g., "$10,500.00").
                *   **Style:** `headlineColor: md.sys.color.onSurfaceVariant`, `supportingTextColor: md.sys.color.primary`. `headlineTypography: md.sys.typescale.titleMedium`, `supportingTypography: md.sys.typescale.titleMedium`.
            *   **Sub-Component: Account Item**
                *   **Name:** `ListItem`
                *   **Content:** Headline text (e.g., "Chase Checking"), supporting text (e.g., "$5,500.00"), leading icon (bank logo).
                *   **Style:** `headlineColor: md.sys.color.onSurfaceVariant`, `supportingTextColor: md.sys.color.onSurfaceVariant`. `headlineTypography: md.sys.typescale.bodyLarge`, `supportingTypography: md.sys.typescale.bodyMedium`.
    *   **Component 3: Add Account Button**
        *   **Name:** `ExtendedFloatingActionButton`
        *   **Position & Size:** Bottom right corner, `margin: 16dp`.
        *   **Style:** `containerColor: md.sys.color.primaryContainer`, `contentColor: md.sys.color.onPrimaryContainer`.
        *   **Content:** Icon `Icons.Filled.Add`, Text "Add account".
*   **Interaction & Behavior:**
    *   **Action:** User taps 'Add account' button.
    *   **Result:** Navigate to `01_02_Add_Account_Screen`.
    *   **Animation:** `MaterialSharedAxis` (Z-axis).
    *   **Scroll Behavior:** `TopAppBar` scrolls off-screen.

### 01_02_Add_Account_Screen
*   **Screen Name/ID:** `01_02_Add_Account_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Scaffold` with a `TopAppBar` and a central `Column`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Position & Size:** Top, `height: 64dp`, `width: fillMaxWidth`.
        *   **Style:** `containerColor: md.sys.color.surface`.
        *   **Content:** Title text "Add Account", `typography: md.sys.typescale.titleLarge`. Navigation icon `Icons.Filled.ArrowBack`.
    *   **Component 2: Content Layout**
        *   **Name:** `Column`
        *   **Position & Size:** Centered vertically and horizontally. `padding: 24dp`.
        *   **Style:** `horizontalAlignment: CenterHorizontally`.
    *   **Component 3: Illustration**
        *   **Name:** `Image` (Vector Graphic)
        *   **Position & Size:** Top of the `Column`, `size: 120dp`.
        *   **Content:** A vector graphic representing security or linking accounts.
    *   **Component 4: Headline Text**
        *   **Name:** `Text`
        *   **Position & Size:** Below illustration, `marginTop: 24dp`.
        *   **Style:** `typography: md.sys.typescale.headlineSmall`, `color: md.sys.color.onSurface`, `textAlign: Center`.
        *   **Content:** "Connect an account securely"
    *   **Component 5: Body Text**
        *   **Name:** `Text`
        *   **Position & Size:** Below headline, `marginTop: 16dp`.
        *   **Style:** `typography: md.sys.typescale.bodyMedium`, `color: md.sys.color.onSurfaceVariant`, `textAlign: Center`.
        *   **Content:** "Monarch uses Plaid to connect to over 11,000 financial institutions with bank-level security."
    *   **Component 6: Connect Button**
        *   **Name:** `FilledButton`
        *   **Position & Size:** Bottom of the `Column`, `marginTop: 32dp`, `width: fillMaxWidth`, `height: 52dp`.
        *   **Style:** `containerColor: md.sys.color.primary`, `contentColor: md.sys.color.onPrimary`.
        *   **Content:** Text "Connect with Plaid".
*   **Interaction & Behavior:**
    *   **Action:** User taps 'Connect with Plaid' button.
    *   **Result:** Navigate to `01_03_Plaid_Consent_Screen`.
    *   **Action:** User taps back arrow in `TopAppBar`.
    *   **Result:** Navigate back to `01_01_Accounts_Screen`.
    *   **Animation:** `MaterialSharedAxis` (X-axis).

### 01_03_Plaid_Consent_Screen
*   **Screen Name/ID:** `01_03_Plaid_Consent_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** This screen is a WebView or a custom activity provided by the Plaid SDK, presented modally. The specification describes the container and expected content.
*   **Components:**
    *   **Component 1: Modal Container**
        *   **Name:** `Scaffold` or Full-Screen Dialog.
        *   **Position & Size:** Fills the entire screen.
    *   **Component 2: Plaid Header**
        *   **Name:** `View` (Plaid UI)
        *   **Position & Size:** Top of the screen.
        *   **Content:** Plaid logo and Monarch Money logo, with text "Monarch Money uses Plaid to connect your accounts."
    *   **Component 3: Consent Information**
        *   **Name:** `WebView` Content
        *   **Position & Size:** Fills the main body.
        *   **Content:** Detailed information about the data being shared, privacy policy links, and terms of service.
    *   **Component 4: Continue Button**
        *   **Name:** `Button` (Plaid UI)
        *   **Position & Size:** Pinned to the bottom of the screen.
        *   **Style:** Styled according to Plaid's branding.
        *   **Content:** Text "Continue".
*   **Interaction & Behavior:**
    *   **Action:** User taps 'Continue' button.
    *   **Result:** Navigate to `01_04_Select_Your_Institution_Screen`.
    *   **Animation:** Modal slide-up transition.

### 01_04_Select_Your_Institution_Screen
*   **Screen Name/ID:** `01_04_Select_Your_Institution_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** Plaid SDK UI. `Scaffold` with a search bar at the top and a `LazyColumn` of institutions.
*   **Components:**
    *   **Component 1: Top Bar**
        *   **Name:** `View` (Plaid UI)
        *   **Position & Size:** Top of the screen.
        *   **Content:** Title "Select your institution" and a close button (`Icons.Filled.Close`).
    *   **Component 2: Search Bar**
        *   **Name:** `TextField` (Plaid UI)
        *   **Position & Size:** Below the top bar.
        *   **Style:** Outlined style with a leading search icon.
        *   **Content:** Placeholder text "Search".
    *   **Component 3: Institution Grid/List**
        *   **Name:** `LazyColumn` or `LazyVerticalGrid` (Plaid UI)
        *   **Position & Size:** Fills the remaining space.
        *   **Content:** A list of popular financial institutions, each represented by a logo and name.
*   **Interaction & Behavior:**
    *   **Action:** User taps on a financial institution.
    *   **Result:** Navigate to `01_05_Enter_Credentials_Screen`.
    *   **Action:** User types in the search bar.
    *   **Result:** The institution list is filtered in real-time. The screen remains `01_04_Select_Your_Institution_Screen`.

### 01_05_Enter_Credentials_Screen
*   **Screen Name/ID:** `01_05_Enter_Credentials_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** Plaid SDK UI. `Scaffold` with a `TopAppBar` and a `Column` containing input fields.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar` (Plaid UI)
        *   **Position & Size:** Top of the screen.
        *   **Content:** Title is the name of the selected institution (e.g., "Chase"). Navigation icon `Icons.Filled.ArrowBack`.
    *   **Component 2: Username Field**
        *   **Name:** `OutlinedTextField` (Plaid UI)
        *   **Position & Size:** In `Column`, `width: fillMaxWidth`, `marginTop: 32dp`.
        *   **Content:** Label "Username".
    *   **Component 3: Password Field**
        *   **Name:** `OutlinedTextField` (Plaid UI)
        *   **Position & Size:** Below username field, `width: fillMaxWidth`, `marginTop: 16dp`.
        *   **Content:** Label "Password", with a trailing icon to toggle password visibility.
    *   **Component 4: Submit Button**
        *   **Name:** `FilledButton` (Plaid UI)
        *   **Position & Size:** Below password field, `width: fillMaxWidth`, `marginTop: 24dp`.
        *   **Content:** Text "Submit".
*   **Interaction & Behavior:**
    *   **Action:** User enters credentials and taps 'Submit'.
    *   **Result:** Navigate to `01_06_Connecting_Screen`.

### 01_06_Connecting_Screen
*   **Screen Name/ID:** `01_06_Connecting_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface` with a scrim overlay (`#000000` at 30% opacity).
*   **Layout:** Full-screen modal dialog. A central `Column` with a progress indicator and text.
*   **Components:**
    *   **Component 1: Progress Indicator**
        *   **Name:** `CircularProgressIndicator`
        *   **Position & Size:** Centered on screen, `size: 64dp`.
        *   **Style:** `color: md.sys.color.primary`.
    *   **Component 2: Status Text**
        *   **Name:** `Text`
        *   **Position & Size:** Below progress indicator, `marginTop: 24dp`.
        *   **Style:** `typography: md.sys.typescale.titleMedium`, `color: md.sys.color.onSurface`.
        *   **Content:** "Connecting to [Institution Name]..."
*   **Interaction & Behavior:**
    *   **Action:** Automatic transition after the connection process completes successfully.
    *   **Result:** Navigate to `01_07_Success_Screen`.
    *   **Error State:** If connection fails, a `Snackbar` appears on the previous screen (`01_05_Enter_Credentials_Screen`) with the message "Connection failed. Please check your credentials and try again." The connecting screen is dismissed.

### 01_07_Success_Screen
*   **Screen Name/ID:** `01_07_Success_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** Full-screen modal dialog. A central `Column` with an icon, text, and a button.
*   **Components:**
    *   **Component 1: Success Icon**
        *   **Name:** `Icon`
        *   **Position & Size:** Centered, top of the `Column`, `size: 80dp`.
        *   **Style:** `tint: md.sys.color.primary`.
        *   **Content:** `Icons.Filled.CheckCircle`.
    *   **Component 2: Headline Text**
        *   **Name:** `Text`
        *   **Position & Size:** Below icon, `marginTop: 24dp`.
        *   **Style:** `typography: md.sys.typescale.headlineMedium`, `color: md.sys.color.onSurface`.
        *   **Content:** "Success!"
    *   **Component 3: Body Text**
        *   **Name:** `Text`
        *   **Position & Size:** Below headline, `marginTop: 8dp`.
        *   **Style:** `typography: md.sys.typescale.bodyLarge`, `color: md.sys.color.onSurfaceVariant`.
        *   **Content:** "Your account has been connected."
    *   **Component 4: Continue Button**
        *   **Name:** `FilledButton`
        *   **Position & Size:** Bottom of the `Column`, `marginTop: 32dp`, `width: fillMaxWidth`, `padding: 0dp 32dp`.
        *   **Style:** `containerColor: md.sys.color.primary`, `contentColor: md.sys.color.onPrimary`.
        *   **Content:** Text "Continue".
*   **Interaction & Behavior:**
    *   **Action:** User taps 'Continue' button.
    *   **Result:** Dismisses the entire Plaid flow and navigates to `01_08_Accounts_Updated_Screen`.
    *   **Animation:** Modal slide-down.

### 01_08_Accounts_Updated_Screen
*   **Screen Name/ID:** `01_08_Accounts_Updated_Screen`
*   **Description:** This is the same screen as `01_01_Accounts_Screen`, but the `LazyColumn` now includes the newly added account.
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar`, `LazyColumn`, and `ExtendedFloatingActionButton`.
*   **Components:**
    *   Identical to `01_01_Accounts_Screen`, but the `LazyColumn` now contains a new `ListItem` for the connected account under the appropriate `Card` (e.g., a new "Bank of America Checking" item under the "Cash" card).
*   **Interaction & Behavior:**
    *   **Action:** User views the newly added account.
    *   **Result:** End of flow.

---

## Flow 2: Main Navigation

### 02_01_Dashboard_Screen
*   **Screen Name/ID:** `02_01_Dashboard_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, `FloatingActionButton`, and `NavigationBar`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Position & Size:** Top, `height: 64dp`, `width: fillMaxWidth`.
        *   **Style:** `containerColor: md.sys.color.surface`.
        *   **Content:** Title is the Monarch Money logo/wordmark. `actions` contains an `IconButton` with `Icons.Filled.Person` for profile/settings.
    *   **Component 2: Dashboard Content**
        *   **Name:** `LazyColumn`
        *   **Position & Size:** Fills space between `TopAppBar` and `NavigationBar`. `contentPadding: 16dp`.
        *   **Content:** A series of `Card` components for different dashboard widgets.
        *   **Sub-Component: Net Worth Card**
            *   **Name:** `Card`
            *   **Style:** `containerColor: md.sys.color.surfaceVariant`.
            *   **Content:** Title "Net Worth", a large value (e.g., "$150,000.00"), and a small line chart.
        *   **Sub-Component: Cash Flow Card**
            *   **Name:** `Card`
            *   **Style:** `containerColor: md.sys.color.surfaceVariant`.
            *   **Content:** Title "Cash Flow", income vs. expenses summary, and a bar chart.
        *   **Sub-Component: Recent Transactions Card**
            *   **Name:** `Card`
            *   **Style:** `containerColor: md.sys.color.surfaceVariant`.
            *   **Content:** Title "Recent Transactions", and 3-4 `ListItem`s showing recent transactions.
    *   **Component 3: Add FAB**
        *   **Name:** `FloatingActionButton`
        *   **Position & Size:** Bottom right, anchored above the `NavigationBar`. `margin: 16dp`.
        *   **Style:** `containerColor: md.sys.color.primary`, `contentColor: md.sys.color.onPrimary`.
        *   **Content:** Icon `Icons.Filled.Add`.
    *   **Component 4: Bottom Navigation Bar**
        *   **Name:** `NavigationBar`
        *   **Position & Size:** Bottom of the screen, `height: 80dp`, `width: fillMaxWidth`.
        *   **Style:** `containerColor: md.sys.color.surfaceVariant`.
        *   **Content:** Four `NavigationBarItem`s:
            *   1: `selected: true`, `icon: Icons.Filled.Dashboard`, `label: "Dashboard"`
            *   2: `selected: false`, `icon: Icons.Outlined.AccountBalanceWallet`, `label: "Accounts"`
            *   3: `selected: false`, `icon: Icons.Outlined.ReceiptLong`, `label: "Transactions"`
            *   4: `selected: false`, `icon: Icons.Outlined.PieChart`, `label: "Plan"`
*   **Interaction & Behavior:**
    *   **Action:** Tap 'Accounts' tab -> Navigate to `01_01_Accounts_Screen`.
    *   **Action:** Tap 'Transactions' tab -> Navigate to `02_02_Transactions_Screen`.
    *   **Action:** Tap 'Plan' tab -> Navigate to `02_03_Plan_Screen`.
    *   **Action:** Tap 'Profile' icon -> Navigate to `05_01_Settings_Screen`.
    *   **Action:** Tap 'Add' FAB -> Open `02_08_Add_Menu_Screen` as a `ModalBottomSheet`.
    *   **Animation:** `MaterialFadeThrough` for tab navigation. `MaterialSharedAxis` (X-axis) for profile navigation.

### 02_02_Transactions_Screen
*   **Screen Name/ID:** `02_02_Transactions_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Position & Size:** Top, `height: 64dp`, `width: fillMaxWidth`.
        *   **Content:** Title "Transactions". `actions` contains `IconButton`s for Search (`Icons.Filled.Search`) and Filter (`Icons.Filled.FilterList`).
    *   **Component 2: Transaction List**
        *   **Name:** `LazyColumn`
        *   **Position & Size:** Fills space between `TopAppBar` and `NavigationBar`.
        *   **Content:** List items are grouped by date. Each group has a date header.
        *   **Sub-Component: Date Header**
            *   **Name:** `ListItem`
            *   **Style:** `containerColor: md.sys.color.surface`.
            *   **Content:** Headline text "October 31, 2025". `typography: md.sys.typescale.titleSmall`.
        *   **Sub-Component: Transaction Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: Icon for category. `headlineContent`: Merchant name (e.g., "Starbucks"). `supportingContent`: Category name (e.g., "Coffee Shops"). `trailingContent`: Amount (e.g., "-$5.75").
            *   **Style:** Amount is colored `md.sys.color.error` for debits and `md.sys.color.primary` for credits.
    *   **Component 3: Bottom Navigation Bar**
        *   **Name:** `NavigationBar`
        *   **Content:** Same as `02_01_Dashboard_Screen`, but with "Transactions" selected.
*   **Interaction & Behavior:**
    *   **Action:** Tap on a transaction `ListItem`.
    *   **Result:** Navigate to `03_01_Transaction_Detail_Screen`.
    *   **Action:** Tap other navigation tabs -> Navigate to respective screens.

### 02_03_Plan_Screen
*   **Screen Name/ID:** `02_03_Plan_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar`, `TabRow`, a content area, and `NavigationBar`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Position & Size:** Top, `height: 64dp`, `width: fillMaxWidth`.
        *   **Content:** Title "Plan".
    *   **Component 2: Sub-Navigation Tabs**
        *   **Name:** `PrimaryTabRow`
        *   **Position & Size:** Below `TopAppBar`, `height: 48dp`, `width: fillMaxWidth`.
        *   **Content:** Three `Tab`s: "Budget", "Recurring", "Goals".
    *   **Component 3: Tab Content Area**
        *   **Name:** `HorizontalPager` or similar.
        *   **Position & Size:** Fills space between `TabRow` and `NavigationBar`.
        *   **Content:** Displays the content for the currently selected tab (`02_04_Budget_Screen`, `02_05_Recurring_Screen`, or `02_06_Goals_Screen`). Initially shows `02_04_Budget_Screen`.
    *   **Component 4: Bottom Navigation Bar**
        *   **Name:** `NavigationBar`
        *   **Content:** Same as `02_01_Dashboard_Screen`, but with "Plan" selected.
*   **Interaction & Behavior:**
    *   **Action:** Tap 'Budget' sub-tab -> Display `02_04_Budget_Screen` content.
    *   **Action:** Tap 'Recurring' sub-tab -> Display `02_05_Recurring_Screen` content.
    *   **Action:** Tap 'Goals' sub-tab -> Display `02_06_Goals_Screen` content.
    *   **Action:** Swipe left/right on content area -> Change tabs.

### 02_04_Budget_Screen
*   **Screen Name/ID:** `02_04_Budget_Screen`
*   **Description:** This is the content displayed within the "Plan" screen when the "Budget" tab is active. It is not a full, separate screen with its own `Scaffold`.
*   **Layout:** `LazyColumn` with `contentPadding: 16dp`.
*   **Components:**
    *   **Component 1: Budget Summary Card**
        *   **Name:** `Card`
        *   **Content:** A summary of the monthly budget, showing "Spent vs. Budgeted" with a `LinearProgressIndicator`.
    *   **Component 2: Budget Category List**
        *   **Name:** `Column`
        *   **Content:** A list of budget categories.
        *   **Sub-Component: Category Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: Category icon. `headlineContent`: Category name (e.g., "Groceries"). `trailingContent`: Text showing amount spent vs. budgeted (e.g., "$350 / $500"). Below the `ListItem` is a `LinearProgressIndicator` showing the progress for that category.
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow or 'Plan' tab.
    *   **Result:** No navigation, as this is part of the Plan screen. The user would tap another main navigation tab to leave.

### 02_05_Recurring_Screen
*   **Screen Name/ID:** `02_05_Recurring_Screen`
*   **Description:** Content for the "Recurring" tab on the "Plan" screen.
*   **Layout:** `LazyColumn` with `contentPadding: 16dp`.
*   **Components:**
    *   **Component 1: Upcoming Bills Card**
        *   **Name:** `Card`
        *   **Content:** Title "Upcoming Bills" and a list of `ListItem`s for upcoming recurring transactions (e.g., "Netflix", "Rent").
    *   **Component 2: Subscriptions Card**
        *   **Name:** `Card`
        *   **Content:** Title "All Subscriptions" and a `LazyColumn` of all detected recurring payments.
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow or 'Plan' tab.
    *   **Result:** No navigation.

### 02_06_Goals_Screen
*   **Screen Name/ID:** `02_06_Goals_Screen`
*   **Description:** Content for the "Goals" tab on the "Plan" screen.
*   **Layout:** `LazyColumn` with `contentPadding: 16dp`.
*   **Components:**
    *   **Component 1: Add Goal Button**
        *   **Name:** `FilledTonalButton`
        *   **Position & Size:** Top of the list, `width: fillMaxWidth`.
        *   **Content:** `leadingIcon: Icons.Filled.Add`, Text "Create a Goal".
    *   **Component 2: Goal Card**
        *   **Name:** `Card`
        *   **Position & Size:** `marginBottom: 16dp`.
        *   **Content:** A `Column` showing the goal name (e.g., "House Down Payment"), a progress bar, and text showing amount saved vs. goal (e.g., "$5,000 / $50,000").
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow or 'Plan' tab.
    *   **Result:** No navigation.

### 02_08_Add_Menu_Screen
*   **Screen Name/ID:** `02_08_Add_Menu_Screen`
*   **Description:** A modal bottom sheet that appears on top of the current screen.
*   **Layout:** `ModalBottomSheet`
*   **Components:**
    *   **Component 1: Drag Handle**
        *   **Name:** `DragHandle`
        *   **Position & Size:** Top center of the sheet.
    *   **Component 2: Menu Items**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`.
        *   **Content:** A list of `ListItem` components.
        *   **Sub-Component: Menu Item 1**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.PostAdd)`, `headlineContent`: "Add Transaction".
        *   **Sub-Component: Menu Item 2**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.AccountBalance)`, `headlineContent`: "Add Account".
        *   **Sub-Component: Menu Item 3**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Flag)`, `headlineContent`: "Add Goal".
*   **Interaction & Behavior:**
    *   **Action:** Tap 'Add Transaction'.
    *   **Result:** Dismiss sheet and navigate to `04_01_Add_Transaction_Screen`.
    *   **Action:** Tap 'Add Account'.
    *   **Result:** Dismiss sheet and navigate to `01_02_Add_Account_Screen`.
    *   **Action:** Tap 'Add Goal'.
    *   **Result:** Dismiss sheet, navigate to `02_03_Plan_Screen` and switch to the `02_06_Goals_Screen` tab.
    *   **Action:** User taps outside the sheet or swipes it down.
    *   **Result:** Dismisses the menu, returning to `02_01_Dashboard_Screen`.

---

## Flow 3: View and Edit Transaction

### 03_01_Transaction_Detail_Screen
*   **Screen Name/ID:** `03_01_Transaction_Detail_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Transaction Detail", `actions`: `IconButton` with `Icons.Filled.Edit`.
    *   **Component 2: Detail List**
        *   **Name:** `LazyColumn`
        *   **Position & Size:** Fills the screen, `padding: 16dp`.
        *   **Content:** A series of `ListItem`s displaying transaction data.
        *   **Sub-Component: Merchant & Amount**
            *   **Name:** `ListItem`
            *   **Content:** `headlineContent`: Merchant Name (e.g., "Amazon"), `trailingContent`: Amount (e.g., "-$49.99").
            *   **Style:** `headlineTypography: md.sys.typescale.headlineSmall`, `trailingTypography: md.sys.typescale.headlineSmall`.
        *   **Sub-Component: Date**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.CalendarToday)`, `headlineContent`: "Date", `trailingContent`: "October 30, 2025".
        *   **Sub-Component: Category**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Label)`, `headlineContent`: "Category", `trailingContent`: "Shopping".
        *   **Sub-Component: Account**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.AccountBalanceWallet)`, `headlineContent`: "Account", `trailingContent`: "Chase Sapphire".
*   **Interaction & Behavior:**
    *   **Action:** Tap 'Edit' button.
    *   **Result:** Navigate to `03_02_Edit_Transaction_Screen`.
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `02_02_Transactions_Screen`.
    *   **Animation:** `MaterialSharedAxis` (X-axis).

### 03_02_Edit_Transaction_Screen
*   **Screen Name/ID:** `03_02_Edit_Transaction_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Scaffold` with `TopAppBar` and `Column` in a `verticalScroll`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.Close` (for Cancel), Title "Edit Transaction", `actions`: a `TextButton` with text "Save".
    *   **Component 2: Form Fields**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`.
        *   **Content:**
            *   `OutlinedTextField` for Merchant Name.
            *   `OutlinedTextField` for Amount (with currency prefix).
            *   `OutlinedTextField` for Date (tappable, opens a `DatePickerDialog`).
            *   `ExposedDropdownMenuBox` for Category.
            *   `ExposedDropdownMenuBox` for Account.
*   **Interaction & Behavior:**
    *   **Action:** User modifies details and taps 'Save'.
    *   **Result:** Data is saved, navigate back to `03_01_Transaction_Detail_Screen` with updated information.
    *   **Action:** User taps 'Cancel' (Close icon) or the system back button.
    *   **Result:** A confirmation `AlertDialog` appears: "Discard changes?". If "Yes", navigate back to `03_01_Transaction_Detail_Screen`. If "No", dialog dismisses.

---

## Flow 4: Add Transaction

### 04_01_Add_Transaction_Screen
*   **Screen Name/ID:** `04_01_Add_Transaction_Screen`
*   **Description:** This screen is functionally identical to `03_02_Edit_Transaction_Screen`, but for creating a new entry. It is presented as a full-screen dialog.
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Scaffold` with `TopAppBar` and `Column` in a `verticalScroll`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.Close` (for Cancel), Title "Add Transaction", `actions`: a `TextButton` with text "Add". The "Add" button is disabled until all required fields are filled.
    *   **Component 2: Form Fields**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`.
        *   **Content:**
            *   `OutlinedTextField` for Merchant Name.
            *   `OutlinedTextField` for Amount.
            *   `OutlinedTextField` for Date (opens `DatePickerDialog`).
            *   `ExposedDropdownMenuBox` for Category.
            *   `ExposedDropdownMenuBox` for Account.
            *   `SegmentedButton` to select transaction type (Expense, Income, Transfer).
*   **Interaction & Behavior:**
    *   **Action:** User fills out details and taps 'Add'.
    *   **Result:** Transaction is created, screen is dismissed, user returns to `02_02_Transactions_Screen` where the new transaction is visible at the top of the list. A `Snackbar` confirms "Transaction added".
    *   **Action:** User taps 'Cancel' (Close icon) or system back button.
    *   **Result:** Screen is dismissed, user returns to the previous screen (e.g., `02_02_Transactions_Screen`).

---

## Flow 5: Settings and Profile

### 05_01_Settings_Screen
*   **Screen Name/ID:** `05_01_Settings_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Settings".
    *   **Component 2: Settings List**
        *   **Name:** `LazyColumn`
        *   **Content:** A list of `ListItem`s for navigation.
        *   **Sub-Component: Profile Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Person)`, `headlineContent`: "Profile", `trailingContent`: `Icon(Icons.Filled.ChevronRight)`.
        *   **Sub-Component: Notifications Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Notifications)`, `headlineContent`: "Notifications", `trailingContent`: `Icon(Icons.Filled.ChevronRight)`.
        *   **Sub-Component: Data & Privacy Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Security)`, `headlineContent`: "Data & Privacy", `trailingContent`: `Icon(Icons.Filled.ChevronRight)`.
        *   **Sub-Component: Appearance Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.Palette)`, `headlineContent`: "Appearance", `trailingContent`: `Icon(Icons.Filled.ChevronRight)`.
        *   **Sub-Component: Subscription Item**
            *   **Name:** `ListItem`
            *   **Content:** `leadingContent`: `Icon(Icons.Filled.CreditCard)`, `headlineContent`: "Subscription", `trailingContent`: `Icon(Icons.Filled.ChevronRight)`.
    *   **Component 3: Log Out Button**
        *   **Name:** `FilledTonalButton`
        *   **Position & Size:** In the `LazyColumn` after the list items, `padding: 16dp`, `width: fillMaxWidth`.
        *   **Style:** `containerColor: md.sys.color.secondaryContainer`, `contentColor: md.sys.color.onSecondaryContainer`.
        *   **Content:** Text "Log Out".
*   **Interaction & Behavior:**
    *   **Action:** Tap 'Profile' -> Navigate to `05_02_Profile_Screen`.
    *   **Action:** Tap 'Notifications' -> Navigate to `05_03_Notifications_Screen`.
    *   **Action:** Tap 'Data & Privacy' -> Navigate to `05_04_Data_Privacy_Screen`.
    *   **Action:** Tap 'Appearance' -> Navigate to `05_05_Appearance_Screen`.
    *   **Action:** Tap 'Subscription' -> Navigate to `05_06_Subscription_Screen`.
    *   **Action:** Tap 'Log Out' -> Show confirmation `AlertDialog`. On confirm, log out and navigate to `05_07_Welcome_Screen`.
    *   **Action:** Tap back arrow -> Navigate to `02_01_Dashboard_Screen`.

### 05_02_Profile_Screen
*   **Screen Name/ID:** `05_02_Profile_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `Column`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Profile".
    *   **Component 2: Profile Form**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`.
        *   **Content:** `OutlinedTextField` for "Name", `OutlinedTextField` for "Email" (read-only), and a `Button` for "Change Password".
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `05_01_Settings_Screen`.

### 05_03_Notifications_Screen
*   **Screen Name/ID:** `05_03_Notifications_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Notifications".
    *   **Component 2: Notification Toggles**
        *   **Name:** `LazyColumn`
        *   **Content:** A list of `ListItem`s with `Switch` controls.
        *   **Sub-Component: Push Notifications Toggle**
            *   **Name:** `ListItem`
            *   **Content:** `headlineContent`: "Push Notifications", `supportingContent`: "Allow all notifications", `trailingContent`: `Switch` (checked/unchecked).
        *   **Sub-Component: Large Transaction Toggle**
            *   **Name:** `ListItem`
            *   **Content:** `headlineContent`: "Large Transactions", `supportingContent`: "Notify for transactions over $100", `trailingContent`: `Switch`.
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `05_01_Settings_Screen`.

### 05_04_Data_Privacy_Screen
*   **Screen Name/ID:** `05_04_Data_Privacy_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `LazyColumn`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Data & Privacy".
    *   **Component 2: Privacy Options**
        *   **Name:** `LazyColumn`
        *   **Content:** `ListItem`s for "Privacy Policy", "Terms of Service", and a `Button` for "Delete Account".
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `05_01_Settings_Screen`.

### 05_05_Appearance_Screen
*   **Screen Name/ID:** `05_05_Appearance_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `Column`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Appearance".
    *   **Component 2: Theme Options**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`.
        *   **Content:** A `Text` label "Theme" followed by a `Row` of `FilterChip`s or a `SegmentedButton` for "System", "Light", and "Dark".
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `05_01_Settings_Screen`.

### 05_06_Subscription_Screen
*   **Screen Name/ID:** `05_06_Subscription_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with `TopAppBar` and `Column`.
*   **Components:**
    *   **Component 1: Top App Bar**
        *   **Name:** `TopAppBar`
        *   **Content:** `navigationIcon: Icons.Filled.ArrowBack`, Title "Subscription".
    *   **Component 2: Subscription Details**
        *   **Name:** `Column`
        *   **Position & Size:** `padding: 16dp`, `horizontalAlignment: CenterHorizontally`.
        *   **Content:** A `Card` displaying the current plan (e.g., "Monarch Premium"), renewal date, and a `Button` to "Manage Subscription" which opens the Google Play subscription management screen.
*   **Interaction & Behavior:**
    *   **Action:** Tap back arrow.
    *   **Result:** Navigate back to `05_01_Settings_Screen`.

### 05_07_Welcome_Screen
*   **Screen Name/ID:** `05_07_Welcome_Screen`
*   **Description:** The initial screen for logged-out users.
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Column` centered on the screen.
*   **Components:**
    *   **Component 1: App Logo**
        *   **Name:** `Image`
        *   **Position & Size:** Top of the `Column`, `size: 150dp`.
        *   **Content:** Monarch Money logo.
    *   **Component 2: Tagline**
        *   **Name:** `Text`
        *   **Position & Size:** `marginTop: 24dp`.
        *   **Style:** `typography: md.sys.typescale.headlineSmall`, `textAlign: Center`.
        *   **Content:** "Your modern financial manager."
    *   **Component 3: Sign Up Button**
        *   **Name:** `FilledButton`
        *   **Position & Size:** `marginTop: 48dp`, `width: fillMaxWidth`, `padding: 0dp 32dp`.
        *   **Content:** "Get Started".
    *   **Component 4: Log In Button**
        *   **Name:** `TextButton`
        *   **Position & Size:** `marginTop: 16dp`.
        *   **Content:** "Already have an account? Log In".
*   **Interaction & Behavior:**
    *   **Action:** User is logged out and arrives here.
    *   **Result:** End of flow.

---

## V. Critical Scenarios & States

### Error States
*   **No Internet Connection:** A `Snackbar` appears at the bottom of the screen.
    *   **Message:** "No internet connection. Please check your network."
    *   **Action:** "Retry" button on the Snackbar.
*   **API/Server Error:** A `Snackbar` appears.
    *   **Message:** "Something went wrong. Please try again later."
*   **Form Validation Error:** `TextField` components enter an error state.
    *   **Style:** The outline and label color change to `md.sys.color.error`.
    *   **Content:** `supportingText` appears below the field with a descriptive error message (e.g., "Invalid email address").

### Empty States
*   **Accounts Screen (No Accounts):**
    *   **Layout:** A centered `Column`.
    *   **Content:** An `Icon` (`Icons.Outlined.AccountBalance`, `size: 96dp`, `tint: md.sys.color.surfaceVariant`), a `Text` headline "No accounts yet", a `Text` body "Add your first account to get started.", and a `FilledButton` with text "Add Account".
*   **Transactions Screen (No Transactions):**
    *   **Layout:** A centered `Column`.
    *   **Content:** An `Icon` (`Icons.Outlined.ReceiptLong`, `size: 96dp`, `tint: md.sys.color.surfaceVariant`), a `Text` headline "No transactions found", and a `Text` body "Your transactions will appear here once you connect an account.".

### Loading States
*   **Initial App Load / Data Fetch:**
    *   **Indicator:** A centered `CircularProgressIndicator` is displayed over the screen content area.
*   **Pull-to-Refresh:**
    *   **Behavior:** Swiping down from the top of any `LazyColumn` will trigger a refresh.
    *   **Indicator:** A standard `SwipeRefreshIndicator` appears at the top.
*   **Shimmer/Placeholder UI:**
    *   **Usage:** On screens like Dashboard and Accounts, while data is loading for the first time, placeholder `Card`s with a shimmering animation are shown to represent the layout before content is available. The shimmer effect uses animated gradients moving across light gray shapes.

---
