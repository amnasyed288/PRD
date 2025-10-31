# WealthNest - Android Design Specification

## I. Global Specifications

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Modes**: Light and Dark themes are supported.
    *   **Dynamic Color**: Material You dynamic color theming is enabled, using the user's wallpaper colors on supported Android versions.
*   **Colors**:
    *   **Seed Color**: `#00A86B` (WealthNest Green)
    *   **Light Theme Color Roles**:
        *   `md.sys.color.primary`: `#006D3D`
        *   `md.sys.color.on-primary`: `#FFFFFF`
        *   `md.sys.color.primary-container`: `#8CF7B6`
        *   `md.sys.color.on-primary-container`: `#00210E`
        *   `md.sys.color.secondary`: `#4F6353`
        *   `md.sys.color.on-secondary`: `#FFFFFF`
        *   `md.sys.color.secondary-container`: `#D2E8D4`
        *   `md.sys.color.on-secondary-container`: `#0D1F13`
        *   `md.sys.color.tertiary`: `#3C6471`
        *   `md.sys.color.on-tertiary`: `#FFFFFF`
        *   `md.sys.color.tertiary-container`: `#BFE9F9`
        *   `md.sys.color.on-tertiary-container`: `#001F27`
        *   `md.sys.color.error`: `#BA1A1A`
        *   `md.sys.color.on-error`: `#FFFFFF`
        *   `md.sys.color.error-container`: `#FFDAD6`
        *   `md.sys.color.on-error-container`: `#410002`
        *   `md.sys.color.background`: `#FBFDF7`
        *   `md.sys.color.on-background`: `#1A1C1A`
        *   `md.sys.color.surface`: `#FBFDF7`
        *   `md.sys.color.on-surface`: `#1A1C1A`
        *   `md.sys.color.surface-variant`: `#DDE5DB`
        *   `md.sys.color.on-surface-variant`: `#414942`
        *   `md.sys.color.outline`: `#717971`
        *   `md.sys.color.inverse-surface`: `#2F312E`
        *   `md.sys.color.inverse-on-surface`: `#F0F1EC`
        *   `md.sys.color.inverse-primary`: `#70DA9C`
        *   `md.sys.color.surface-tint`: `#006D3D`
    *   **Dark Theme Color Roles**:
        *   `md.sys.color.primary`: `#70DA9C`
        *   `md.sys.color.on-primary`: `#00391C`
        *   `md.sys.color.primary-container`: `#00522B`
        *   `md.sys.color.on-primary-container`: `#8CF7B6`
        *   `md.sys.color.secondary`: `#B6CCB8`
        *   `md.sys.color.on-secondary`: `#223527`
        *   `md.sys.color.secondary-container`: `#384B3D`
        *   `md.sys.color.on-secondary-container`: `#D2E8D4`
        *   `md.sys.color.tertiary`: `#A4CDDC`
        *   `md.sys.color.on-tertiary`: `#053641`
        *   `md.sys.color.tertiary-container`: `#224C58`
        *   `md.sys.color.on-tertiary-container`: `#BFE9F9`
        *   `md.sys.color.error`: `#FFB4AB`
        *   `md.sys.color.on-error`: `#690005`
        *   `md.sys.color.error-container`: `#93000A`
        *   `md.sys.color.on-error-container`: `#FFDAD6`
        *   `md.sys.color.background`: `#1A1C1A`
        *   `md.sys.color.on-background`: `#E2E3DE`
        *   `md.sys.color.surface`: `#1A1C1A`
        *   `md.sys.color.on-surface`: `#E2E3DE`
        *   `md.sys.color.surface-variant`: `#414942`
        *   `md.sys.color.on-surface-variant`: `#C1C9BF`
        *   `md.sys.color.outline`: `#8B938A`
        *   `md.sys.color.inverse-surface`: `#E2E3DE`
        *   `md.sys.color.inverse-on-surface`: `#1A1C1A`
        *   `md.sys.color.inverse-primary`: `#006D3D`
        *   `md.sys.color.surface-tint`: `#70DA9C`
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

### Flow 1: Onboarding & Authentication

---

#### Screen 1: Splash Screen
*   **Screen Name/ID**: `01_01_Splash_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, vertically centered and horizontally aligned to the center.
    *   `verticalArrangement`: `Arrangement.Center`
    *   `horizontalAlignment`: `Alignment.CenterHorizontally`
    *   `modifier`: `fillMaxSize()`

##### Components:
1.  **Name**: `Image` (App Logo)
    *   **Position & Size**: 150dp x 150dp. Centered.
    *   **Style**: Placeholder for the WealthNest logo.
    *   **Content**: WealthNest app logo graphic.
2.  **Name**: `Text` (App Name)
    *   **Position & Size**: `fillMaxWidth()`. Margin top 16dp.
    *   **Style**:
        *   `typography`: `md.sys.typography.headlineMedium`
        *   `color`: `md.sys.color.primary`
        *   `textAlign`: `TextAlign.Center`
    *   **Content**: "WealthNest"

##### Interaction & Behavior:
*   **Automatic Transition**:
    *   **Interaction**: After a 2-second delay for app loading, automatically transition to the next screen.
    *   **Resulting Navigation**: Navigate to `01_02_Welcome_Screen`.
    *   **Animation**: `MaterialFadeThrough` transition.

---

#### Screen 2: Welcome Screen
*   **Screen Name/ID**: `01_02_Welcome_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` layout, with content pushed to the center and bottom.
    *   `modifier`: `fillMaxSize()`, `padding(24.dp)`

##### Components:
1.  **Name**: `Image` (Illustration)
    *   **Position & Size**: Centered horizontally, occupying the upper-middle portion of the screen. `240dp x 240dp`.
    *   **Content**: A welcoming illustration related to financial growth or planning.
2.  **Name**: `Text` (Headline)
    *   **Position & Size**: `fillMaxWidth()`. Margin top 24dp.
    *   **Style**: `typography`: `md.sys.typography.headlineLarge`, `color`: `md.sys.color.on-surface`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Build Your Financial Future"
3.  **Name**: `Text` (Body)
    *   **Position & Size**: `fillMaxWidth()`. Margin top 16dp, margin bottom 48dp.
    *   **Style**: `typography`: `md.sys.typography.bodyLarge`, `color`: `md.sys.color.on-surface-variant`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Take control of your finances with personalized plans and analysis."
4.  **Name**: `Filled Button`
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Aligned towards the bottom. Margin bottom 16dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Get Started".
5.  **Name**: `TextButton`
    *   **Position & Size**: `fillMaxWidth()`, height 48dp. Below the filled button.
    *   **Content**: `Text` with "Log In".

##### Interaction & Behavior:
*   **Filled Button ('Get Started')**:
    *   **Interaction**: On tap -> Navigate to `01_03_Sign_Up_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) forward transition.
*   **TextButton ('Log In')**:
    *   **Interaction**: On tap -> Navigate to `01_04_Log_In_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Z-axis) forward transition.

---

#### Screen 3: Sign Up Screen
*   **Screen Name/ID**: `01_03_Sign_Up_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and a `Column` with vertical scrolling.
    *   `modifier`: `fillMaxSize()`, `padding(16.dp)`

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`.
    *   **Style**: `colors`: `TopAppBarDefaults.topAppBarColors(containerColor = md.sys.color.surface)`.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Create Account".
2.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Content**: Label "Email".
3.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Style**: `visualTransformation`: `PasswordVisualTransformation`.
    *   **Content**: Label "Password", `trailingIcon` for visibility toggle.
4.  **Name**: `Filled Button` (Create Account)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Create Account".
5.  **Name**: `Row` (Divider)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 32dp.
    *   **Content**: `Divider`, `Text` "or", `Divider`.
6.  **Name**: `Outlined Button` (Sign Up with Google)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: Google logo `Icon`, `Text` "Sign Up with Google".
7.  **Name**: `Row` (Log In Prompt)
    *   **Position & Size**: Centered horizontally at the bottom of the view. Top margin 32dp.
    *   **Content**: `Text` "Already have an account?", `TextButton` "Log In".

##### Interaction & Behavior:
*   **'Create Account' Button**:
    *   **Interaction**: On tap -> Navigate to `01_06_Link_Account_Introduction_Screen`.
*   **'Sign Up with Google' Button**:
    *   **Interaction**: On tap -> Initiate Google Sign-Up flow, then navigate to `01_06_Link_Account_Introduction_Screen`.
*   **'Log In' TextButton**:
    *   **Interaction**: On tap -> Navigate to `01_04_Log_In_Screen`.

---

#### Screen 4: Log In Screen
*   **Screen Name/ID**: `01_04_Log_In_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.
    *   `modifier`: `fillMaxSize()`, `padding(16.dp)`

##### Components:
1.  **Name**: `TopAppBar`
    *   **Position & Size**: `fillMaxWidth()`.
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Log In".
2.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Content**: Label "Email".
3.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Content**: Label "Password", `trailingIcon` for visibility toggle.
4.  **Name**: `TextButton` (Forgot Password)
    *   **Position & Size**: Aligned to the end of the screen. Top margin 8dp.
    *   **Content**: `Text` with "Forgot Password?".
5.  **Name**: `Filled Button` (Log In)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Log In".
6.  **Name**: `Row` (Sign Up Prompt)
    *   **Position & Size**: Centered horizontally at the bottom. Top margin 32dp.
    *   **Content**: `Text` "Don't have an account?", `TextButton` "Sign Up".

##### Interaction & Behavior:
*   **'Log In' Button**:
    *   **Interaction**: On tap -> Authenticate user, then navigate to `02_01_Dashboard_Screen`.
*   **'Forgot Password?' TextButton**:
    *   **Interaction**: On tap -> Navigate to `01_05_Forgot_Password_Screen`.
*   **'Sign Up' TextButton**:
    *   **Interaction**: On tap -> Navigate to `01_03_Sign_Up_Screen`.

---

#### Screen 5: Forgot Password Screen
*   **Screen Name/ID**: `01_05_Forgot_Password_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.
    *   `modifier`: `fillMaxSize()`, `padding(16.dp)`

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Reset Password".
2.  **Name**: `Text` (Instruction)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.bodyMedium`, `color`: `md.sys.color.on-surface-variant`.
    *   **Content**: "Enter your email and we'll send you a link to reset your password."
3.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Content**: Label "Email".
4.  **Name**: `Filled Button` (Send Reset Link)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Send Reset Link".

##### Interaction & Behavior:
*   **'Send Reset Link' Button**:
    *   **Interaction**: On tap -> Show `Snackbar` "Reset link sent", then navigate to `01_04_Log_In_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) backward transition.

---

#### Screen 6: Link Account Introduction Screen
*   **Screen Name/ID**: `01_06_Link_Account_Introduction_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` with `verticalArrangement = Arrangement.Center`, `horizontalAlignment = Alignment.CenterHorizontally`.
    *   `modifier`: `fillMaxSize()`, `padding(24.dp)`

##### Components:
1.  **Name**: `Icon`
    *   **Position & Size**: 80dp x 80dp.
    *   **Content**: `Icons.Filled.AccountBalance`, `tint`: `md.sys.color.primary`.
2.  **Name**: `Text` (Header)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.headlineMedium`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Connect Your First Account"
3.  **Name**: `Text` (Body)
    *   **Position & Size**: `fillMaxWidth()`. Top margin 16dp.
    *   **Style**: `typography`: `md.sys.typography.bodyLarge`, `color`: `md.sys.color.on-surface-variant`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Link your bank account to get a complete view of your finances. We use Plaid for secure, bank-level encryption."
4.  **Name**: `Filled Button` (Connect)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 48dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Connect Bank Account".

##### Interaction & Behavior:
*   **'Connect Bank Account' Button**:
    *   **Interaction**: On tap -> Navigate to `01_07_Select_Institution_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) forward transition.

---

#### Screen 7: Select Institution Screen
*   **Screen Name/ID**: `01_07_Select_Institution_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.Close`.
    *   **Content**: `Text` with "Link an Account".
2.  **Name**: `OutlinedTextField` (Search)
    *   **Position & Size**: `fillMaxWidth()`. Margin 16dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: Placeholder "Search for your bank", `leadingIcon`: `Icons.Filled.Search`.
3.  **Name**: `LazyColumn` (Institution List)
    *   **Position & Size**: Fills remaining space.
    *   **Content**: A list of popular institutions using `ListItem`.
        *   **Example ListItem**: `leadingContent`: Bank Logo `Image`, `headlineContent`: Bank Name `Text`.

##### Interaction & Behavior:
*   **ListItem (Institution)**:
    *   **Interaction**: On tap -> Navigate to `01_08_Enter_Bank_Credentials_Screen`.
    *   **Animation**: `MaterialSharedAxis` (X-axis) forward transition.

---

#### Screen 8: Enter Bank Credentials Screen
*   **Screen Name/ID**: `01_08_Enter_Bank_Credentials_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: This screen represents the Plaid SDK modal flow.
*   **Components**:
    1.  **Name**: `WebView` (Plaid UI)
        *   **Position & Size**: `fillMaxSize()`.
        *   **Content**: The Plaid Link UI for entering institution credentials.

##### Interaction & Behavior:
*   **'Submit' (within Plaid UI)**:
    *   **Interaction**: User enters credentials and submits.
    *   **Resulting Navigation**: Navigate to `01_09_Connecting_Account_Screen`.

---

#### Screen 9: Connecting Account Screen
*   **Screen Name/ID**: `01_09_Connecting_Account_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` centered on the screen.

##### Components:
1.  **Name**: `CircularProgressIndicator`
    *   **Position & Size**: 64dp x 64dp.
2.  **Name**: `Text` (Status)
    *   **Position & Size**: Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.titleMedium`.
    *   **Content**: "Connecting securely..."

##### Interaction & Behavior:
*   **Automatic Transition**:
    *   **Interaction**: After connection completes.
    *   **Resulting Navigation**: Navigate to `01_10_Analyzing_Data_Screen`.
    *   **Animation**: `MaterialFadeThrough`.

---

#### Screen 10: Analyzing Data Screen
*   **Screen Name/ID**: `01_10_Analyzing_Data_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` centered on the screen.

##### Components:
1.  **Name**: `CircularProgressIndicator`
    *   **Position & Size**: 64dp x 64dp.
2.  **Name**: `Text` (Status)
    *   **Position & Size**: Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.titleMedium`.
    *   **Content**: "Analyzing your income and expenses..."

##### Interaction & Behavior:
*   **Automatic Transition**:
    *   **Interaction**: After analysis completes.
    *   **Resulting Navigation**: Navigate to `01_11_Initial_Plan_Ready_Screen`.
    *   **Animation**: `MaterialFadeThrough`.

---

#### Screen 11: Initial Plan Ready Screen
*   **Screen Name/ID**: `01_11_Initial_Plan_Ready_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` centered on the screen. `padding(24.dp)`.

##### Components:
1.  **Name**: `Icon`
    *   **Position & Size**: 80dp x 80dp.
    *   **Content**: `Icons.Filled.CheckCircle`, `tint`: `md.sys.color.primary`.
2.  **Name**: `Text` (Header)
    *   **Position & Size**: Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.headlineMedium`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Your Initial Plan is Ready!"
3.  **Name**: `Filled Button` (View Plan)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "View My Plan".

##### Interaction & Behavior:
*   **'View My Plan' Button**:
    *   **Interaction**: On tap -> Navigate to `02_01_Dashboard_Screen`.
    *   **Animation**: `MaterialFadeThrough`.

---

### Flow 2: Main Navigation

---

#### Screen 12: Dashboard Screen
*   **Screen Name/ID**: `02_01_Dashboard_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Content**: `Text` with "Dashboard".
    *   **Actions**: `IconButton` with `Icons.Filled.Add` and content description "Link an Account".
2.  **Name**: `LazyColumn` (Content)
    *   **Position & Size**: Fills space between `TopAppBar` and `NavigationBar`. `padding(16.dp)`.
    *   **Content**: A list of `Card` components.
        *   **Card 1**: "Net Worth" with a large value and a small chart.
        *   **Card 2**: "Savings Plans" with a summary of goals.
        *   **Card 3**: "Investment Plans" with a summary of portfolio performance.
3.  **Name**: `NavigationBar`
    *   **Position & Size**: Bottom of the screen.
    *   **Content**: Four `NavigationBarItem`s.
        *   **Item 1 (Active)**: `label`: "Dashboard", `icon`: `Icons.Filled.Dashboard`.
        *   **Item 2**: `label`: "Plans", `icon`: `Icons.Outlined.Description`.
        *   **Item 3**: `label`: "Analysis", `icon`: `Icons.Outlined.PieChart`.
        *   **Item 4**: `label`: "Settings", `icon`: `Icons.Outlined.Settings`.

##### Interaction & Behavior:
*   **'+' IconButton**:
    *   **Interaction**: On tap -> Navigate to `01_07_Select_Institution_Screen`.
*   **NavigationBar Items**:
    *   **'Plans'**: On tap -> Navigate to `02_02_Plans_Screen`.
    *   **'Analysis'**: On tap -> Navigate to `02_03_Analysis_Screen`.
    *   **'Settings'**: On tap -> Navigate to `02_04_Settings_Screen`.
    *   **Animation**: `MaterialFadeThrough` between tabs.

---

#### Screen 13: Plans Screen
*   **Screen Name/ID**: `02_02_Plans_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Content**: `Text` with "Plans".
2.  **Name**: `LazyColumn` (Content)
    *   **Content**: List of `Card` components for different financial plans.
        *   **Card 1**: "Savings Plan: Emergency Fund". Clickable.
        *   **Card 2**: "Investment Plan: Retirement". Clickable.
3.  **Name**: `NavigationBar`
    *   **Content**: Same as Dashboard, but with "Plans" selected.

##### Interaction & Behavior:
*   **Savings Plan Card**:
    *   **Interaction**: On tap -> Navigate to `03_01_Savings_Plan_Details_Screen`.
*   **Investment Plan Card**:
    *   **Interaction**: On tap -> Navigate to `03_02_Investment_Plan_Details_Screen`.
*   **NavigationBar Items**: Navigate to other main screens.

---

#### Screen 14: Analysis Screen
*   **Screen Name/ID**: `02_03_Analysis_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Content**: `Text` with "Analysis".
2.  **Name**: `LazyColumn` (Content)
    *   **Content**:
        *   `Card` with a pie chart for "Spending by Category".
        *   `Card` with a list of "Recent Transactions".
        *   `TextButton` with "View All Transactions".
3.  **Name**: `NavigationBar`
    *   **Content**: Same as Dashboard, but with "Analysis" selected.

##### Interaction & Behavior:
*   **'View All Transactions' Button**:
    *   **Interaction**: On tap -> Navigate to `04_01_Transactions_List_Screen`.
*   **Transaction ListItem**:
    *   **Interaction**: On tap -> Navigate to `04_02_Transaction_Details_Screen`.
*   **NavigationBar Items**: Navigate to other main screens.

---

#### Screen 15: Settings Screen
*   **Screen Name/ID**: `02_04_Settings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `NavigationBar`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Content**: `Text` with "Settings".
2.  **Name**: `LazyColumn` (Settings List)
    *   **Content**: `ListItem`s for navigation.
        *   `ListItem` "Profile".
        *   `ListItem` "Linked Accounts".
        *   `ListItem` "Notifications".
        *   `ListItem` "Security".
        *   `ListItem` "Log Out".
3.  **Name**: `NavigationBar`
    *   **Content**: Same as Dashboard, but with "Settings" selected.

##### Interaction & Behavior:
*   **'Profile'**: On tap -> Navigate to `05_01_Profile_Details_Screen`.
*   **'Linked Accounts'**: On tap -> Navigate to `05_02_Linked_Accounts_Screen`.
*   **'Notifications'**: On tap -> Navigate to `05_05_Notifications_Screen`.
*   **'Security'**: On tap -> Navigate to `05_06_Security_Screen`.
*   **'Log Out'**: On tap -> Show `05_07_Log_Out_Confirmation_Modal`.

---

### Flow 3: View Financial Plans

---

#### Screen 16: Savings Plan Details Screen
*   **Screen Name/ID**: `03_01_Savings_Plan_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Savings Plan".
2.  **Name**: `LazyColumn`
    *   **Content**: `Card`s detailing the plan's goal, progress, and contribution history.

##### Interaction & Behavior:
*   **Back Icon**: On tap -> Navigate back to `02_02_Plans_Screen`.

---

#### Screen 17: Investment Plan Details Screen
*   **Screen Name/ID**: `03_02_Investment_Plan_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Investment Plan".
2.  **Name**: `LazyColumn`
    *   **Content**: `Card`s detailing portfolio value, performance charts, and buttons.
        *   `FilledTonalButton` "View Holdings".
        *   `FilledTonalButton` "View Allocation".

##### Interaction & Behavior:
*   **'View Holdings' Button**: On tap -> Navigate to `03_03_Investment_Holdings_Screen`.
*   **'View Allocation' Button**: On tap -> Navigate to `03_04_Investment_Allocation_Screen`.
*   **Back Icon**: On tap -> Navigate back to `02_02_Plans_Screen`.

---

#### Screen 18: Investment Holdings Screen
*   **Screen Name/ID**: `03_03_Investment_Holdings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Holdings".
2.  **Name**: `LazyColumn`
    *   **Content**: A list of `ListItem`s, each representing an investment holding.

##### Interaction & Behavior:
*   **Holding ListItem**: On tap -> Navigate to `03_05_Holding_Details_Screen`.
*   **Back Icon**: On tap -> Navigate back to `03_02_Investment_Plan_Details_Screen`.

---

#### Screen 19: Investment Allocation Screen
*   **Screen Name/ID**: `03_04_Investment_Allocation_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Allocation".
2.  **Name**: `Column`
    *   **Content**: A `Card` containing a large pie chart visualization of asset allocation.

##### Interaction & Behavior:
*   **Back Icon**: On tap -> Navigate back to `03_02_Investment_Plan_Details_Screen`.

---

#### Screen 20: Holding Details Screen
*   **Screen Name/ID**: `03_05_Holding_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "[Holding Name]".
2.  **Name**: `Column`
    *   **Content**: `ListItem`s detailing the holding's value, quantity, cost basis, etc.

##### Interaction & Behavior:
*   **Back Icon**: On tap -> Navigate back to `03_03_Investment_Holdings_Screen`.

---

### Flow 4: Analyze Spending & Transactions

---

#### Screen 21: Transactions List Screen
*   **Screen Name/ID**: `04_01_Transactions_List_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Transactions".
    *   **Actions**: `IconButton` with `Icons.Filled.FilterList`.
2.  **Name**: `LazyColumn`
    *   **Content**: A list of all transactions, grouped by date.

##### Interaction & Behavior:
*   **Transaction ListItem**: On tap -> Navigate to `04_02_Transaction_Details_Screen`.
*   **Filter Icon**: On tap -> Navigate to `04_03_Filter_Transactions_Screen`.
*   **Back Icon**: On tap -> Navigate back to `02_03_Analysis_Screen`.

---

#### Screen 22: Transaction Details Screen
*   **Screen Name/ID**: `04_02_Transaction_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Transaction Details".
    *   **Actions**: `TextButton` with "Edit".
2.  **Name**: `Column`
    *   **Content**: `ListItem`s detailing merchant, amount, date, category, and account.

##### Interaction & Behavior:
*   **'Edit' Button**: On tap -> Navigate to `04_04_Edit_Transaction_Screen`.
*   **Back Icon**: On tap -> Navigate back to `04_01_Transactions_List_Screen`.

---

#### Screen 23: Filter Transactions Screen
*   **Screen Name/ID**: `04_03_Filter_Transactions_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`. Presented modally.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.Close`.
    *   **Content**: `Text` with "Filter Transactions".
2.  **Name**: `Column`
    *   **Content**: Filter options for date range, categories, accounts using `FilterChip`s.
3.  **Name**: `Filled Button` (Apply)
    *   **Position & Size**: Aligned to bottom with 16dp margin.
    *   **Content**: `Text` with "Apply".

##### Interaction & Behavior:
*   **'Apply' Button**: On tap -> Dismiss screen and return to `04_01_Transactions_List_Screen` with filters applied.
*   **Close Icon**: On tap -> Dismiss screen without applying filters.

---

#### Screen 24: Edit Transaction Screen
*   **Screen Name/ID**: `04_04_Edit_Transaction_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.Close` (Cancel).
    *   **Content**: `Text` with "Edit Transaction".
    *   **Actions**: `TextButton` with "Save".
2.  **Name**: `Column`
    *   **Content**: `OutlinedTextField`s for merchant and amount, `ExposedDropdownMenuBox` for category.

##### Interaction & Behavior:
*   **'Save' Button**: On tap -> Save changes and navigate back to `04_02_Transaction_Details_Screen`.
*   **'Cancel' Icon**: On tap -> Navigate back to `04_02_Transaction_Details_Screen` without saving.

---

### Flow 5: Manage Accounts & Settings

---

#### Screen 25: Profile Details Screen
*   **Screen Name/ID**: `05_01_Profile_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Profile".
2.  **Name**: `Column`
    *   **Content**: `OutlinedTextField` for Name, read-only `OutlinedTextField` for Email.

##### Interaction & Behavior:
*   **Back Icon**: On tap -> Navigate back to `02_04_Settings_Screen`.

---

#### Screen 26: Linked Accounts Screen
*   **Screen Name/ID**: `05_02_Linked_Accounts_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `TopAppBar`, `LazyColumn`, and `FloatingActionButton`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Linked Accounts".
2.  **Name**: `LazyColumn`
    *   **Content**: A list of `Card`s, each representing a linked account.
3.  **Name**: `FloatingActionButton`
    *   **Content**: `Icon` `Icons.Filled.Add`.

##### Interaction & Behavior:
*   **Account Card**: On tap -> Navigate to `05_03_Account_Details_Screen`.
*   **FAB**: On tap -> Navigate to `01_07_Select_Institution_Screen`.
*   **Back Icon**: On tap -> Navigate back to `02_04_Settings_Screen`.

---

#### Screen 27: Account Details Screen
*   **Screen Name/ID**: `05_03_Account_Details_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `Column`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "[Account Name]".
2.  **Name**: `Column`
    *   **Content**: `ListItem`s with account details.
3.  **Name**: `OutlinedButton` (Unlink)
    *   **Style**: `borderColor`: `md.sys.color.error`, `contentColor`: `md.sys.color.error`.
    *   **Content**: `Text` with "Unlink Account".

##### Interaction & Behavior:
*   **'Unlink Account' Button**: On tap -> Show `05_04_Unlink_Confirmation_Modal`.
*   **Back Icon**: On tap -> Navigate back to `05_02_Linked_Accounts_Screen`.

---

#### Screen 28: Unlink Confirmation Modal
*   **Screen Name/ID**: `05_04_Unlink_Confirmation_Modal`
*   **Dimensions**: Modal dialog (280dp width).
*   **Background**: `md.sys.color.surface`.
*   **Layout**: `AlertDialog`.

##### Components:
1.  **Name**: `AlertDialog`
    *   **Content**:
        *   `icon`: `Icon` `Icons.Filled.Warning`, `tint`: `md.sys.color.error`.
        *   `title`: `Text` "Unlink Account?".
        *   `text`: `Text` "Are you sure? This will remove the account and its data.".
        *   `confirmButton`: `TextButton` with text "Unlink".
        *   `dismissButton`: `TextButton` with text "Cancel".

##### Interaction & Behavior:
*   **'Unlink' Button**: On tap -> Dismiss modal, perform unlink, navigate to `05_02_Linked_Accounts_Screen`.
*   **'Cancel' Button**: On tap -> Dismiss modal, return to `05_03_Account_Details_Screen`.

---

#### Screen 29: Notifications Screen
*   **Screen Name/ID**: `05_05_Notifications_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Notifications".
2.  **Name**: `LazyColumn`
    *   **Content**: `ListItem`s with `Switch` controls for various notification preferences.

##### Interaction & Behavior:
*   **Switch**: On toggle -> Update preferences.
*   **Back Icon**: On tap -> Navigate back to `02_04_Settings_Screen`.

---

#### Screen 30: Security Screen
*   **Screen Name/ID**: `05_06_Security_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Scaffold` with `TopAppBar` and `LazyColumn`.

##### Components:
1.  **Name**: `TopAppBar`
    *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Content**: `Text` with "Security".
2.  **Name**: `LazyColumn`
    *   **Content**: `ListItem` with a `Switch` for "Biometric Unlock".

##### Interaction & Behavior:
*   **Switch**: On toggle -> Enable/disable biometric authentication.
*   **Back Icon**: On tap -> Navigate back to `02_04_Settings_Screen`.

---

#### Screen 31: Log Out Confirmation Modal
*   **Screen Name/ID**: `05_07_Log_Out_Confirmation_Modal`
*   **Dimensions**: Modal dialog (280dp width).
*   **Background**: `md.sys.color.surface`.
*   **Layout**: `AlertDialog`.

##### Components:
1.  **Name**: `AlertDialog`
    *   **Content**:
        *   `title`: `Text` "Log Out?".
        *   `text`: `Text` "Are you sure you want to log out?".
        *   `confirmButton`: `TextButton` with text "Log Out".
        *   `dismissButton`: `TextButton` with text "Cancel".

##### Interaction & Behavior:
*   **'Log Out' Button**: On tap -> Log user out, navigate to `01_02_Welcome_Screen`.
*   **'Cancel' Button**: On tap -> Dismiss modal, return to `02_04_Settings_Screen`.

---

### Flow 6: Add New Account (Post-Onboarding)

---

#### Screen 32: Connection Successful Screen
*   **Screen Name/ID**: `06_01_Connection_Successful_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column` centered on the screen. `padding(24.dp)`.

##### Components:
1.  **Name**: `Icon`
    *   **Position & Size**: 80dp x 80dp.
    *   **Content**: `Icons.Filled.CheckCircle`, `tint`: `md.sys.color.primary`.
2.  **Name**: `Text` (Header)
    *   **Position & Size**: Top margin 24dp.
    *   **Style**: `typography`: `md.sys.typography.headlineMedium`, `textAlign`: `TextAlign.Center`.
    *   **Content**: "Account Connected!"
3.  **Name**: `Filled Button` (Done)
    *   **Position & Size**: `fillMaxWidth()`, height 56dp. Top margin 32dp.
    *   **Style**: `shape`: `ShapeDefaults.Full`.
    *   **Content**: `Text` with "Done".

##### Interaction & Behavior:
*   **'Done' Button**:
    *   **Interaction**: On tap -> Navigate to `02_01_Dashboard_Screen`.
    *   **Animation**: `MaterialSharedAxis` (Y-axis) backward transition, dismissing the modal flow.

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
    *   **UI**: The main content area of the `02_01_Dashboard_Screen` will display a centered `Column`.
    *   **Content**:
        *   `Icon`: `Icons.Outlined.AccountBalance`, size 64dp, `tint`: `md.sys.color.secondary`.
        *   `Text` (Title): "Welcome to WealthNest", `typography`: `headlineSmall`.
        *   `Text` (Body): "Link an account to see your complete financial picture.", `typography`: `bodyMedium`, `textAlign`: `TextAlign.Center`.
        *   `FilledButton`: "Link First Account", `modifier.padding(top = 24.dp)`. On tap, navigates to `01_07_Select_Institution_Screen`.
2.  **Empty Transactions List**:
    *   **UI**: The `LazyColumn` in `04_01_Transactions_List_Screen` will display a centered `Column`.
    *   **Content**:
        *   `Icon`: `Icons.Outlined.ReceiptLong`, size 64dp, `tint`: `md.sys.color.secondary`.
        *   `Text` (Title): "No Transactions Found".
        *   `Text` (Body): "Your transactions will appear here once they are synced."

#### Loading States
1.  **Initial App Load / Dashboard Refresh**:
    *   **UI**: A full-screen `CircularProgressIndicator` is displayed centered over the `02_01_Dashboard_Screen` content area while initial data is fetched.
2.  **LazyColumn Item Loading**:
    *   **UI**: When paginating or loading more items in a `LazyColumn` (e.g., Transactions), a `CircularProgressIndicator` is shown as the last item in the list.
3.  **Screen-Specific Loading**:
    *   **UI**: For screens that fetch data upon entry, a centered `CircularProgressIndicator` is shown in the content area until the data is ready to be displayed.
4.  **Shimmer Placeholders**:
    *   **UI**: On initial load of card-based screens like the Dashboard, gray placeholder shapes matching the card layouts will be shown with a shimmering animation to improve perceived performance.