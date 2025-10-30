# Combined Android Design Specifications



============================================================
## APP 1: App_1
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Android Design Specification: Spotify

## I. Global Specifications

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Dynamic Color**: Enabled (Material You). The specified colors serve as the baseline when dynamic color is unavailable.
    *   **Themes**: Light and Dark modes are fully supported.
*   **Colors**:
    *   **Seed Color**: `#1DB954` (Spotify Green)
    *   **Light Theme Color Roles**:
        *   `md.sys.color.primary`: `#006e25`
        *   `md.sys.color.onPrimary`: `#ffffff`
        *   `md.sys.color.primaryContainer`: `#8ef89c`
        *   `md.sys.color.onPrimaryContainer`: `#002106`
        *   `md.sys.color.secondary`: `#516350`
        *   `md.sys.color.onSecondary`: `#ffffff`
        *   `md.sys.color.secondaryContainer`: `#d4e8d0`
        *   `md.sys.color.onSecondaryContainer`: `#0f1f11`
        *   `md.sys.color.tertiary`: `#39656c`
        *   `md.sys.color.onTertiary`: `#ffffff`
        *   `md.sys.color.tertiaryContainer`: `#bdeaf2`
        *   `md.sys.color.onTertiaryContainer`: `#001f24`
        *   `md.sys.color.error`: `#ba1a1a`
        *   `md.sys.color.onError`: `#ffffff`
        *   `md.sys.color.background`: `#fcfdf7`
        *   `md.sys.color.onBackground`: `#1a1c19`
        *   `md.sys.color.surface`: `#fcfdf7`
        *   `md.sys.color.onSurface`: `#1a1c19`
        *   `md.sys.color.surfaceVariant`: `#dee5d9`
        *   `md.sys.color.onSurfaceVariant`: `#424940`
        *   `md.sys.color.outline`: `#72796f`
    *   **Dark Theme Color Roles**:
        *   `md.sys.color.primary`: `#73db83`
        *   `md.sys.color.onPrimary`: `#00390f`
        *   `md.sys.color.primaryContainer`: `#005319`
        *   `md.sys.color.onPrimaryContainer`: `#8ef89c`
        *   `md.sys.color.secondary`: `#b8ccb5`
        *   `md.sys.color.onSecondary`: `#243425`
        *   `md.sys.color.secondaryContainer`: `#3a4b3a`
        *   `md.sys.color.onSecondaryContainer`: `#d4e8d0`
        *   `md.sys.color.tertiary`: `#a1ced6`
        *   `md.sys.color.onTertiary`: `#00363d`
        *   `md.sys.color.tertiaryContainer`: `#1f4d54`
        *   `md.sys.color.onTertiaryContainer`: `#bdeaf2`
        *   `md.sys.color.error`: `#ffb4ab`
        *   `md.sys.color.onError`: `#690005`
        *   `md.sys.color.background`: `#1a1c19`
        *   `md.sys.color.onBackground`: `#e2e3de`
        *   `md.sys.color.surface`: `#1a1c19`
        *   `md.sys.color.onSurface`: `#e2e3de`
        *   `md.sys.color.surfaceVariant`: `#424940`
        *   `md.sys.color.onSurfaceVariant`: `#c2c9be`
        *   `md.sys.color.outline`: `#8c9388`
*   **Typography**:
    *   **Font Family**: Roboto
    *   **Type Scale**:
        *   `md.sys.typescale.displayLarge`: Roboto, 57sp
        *   `md.sys.typescale.displayMedium`: Roboto, 45sp
        *   `md.sys.typescale.displaySmall`: Roboto, 36sp
        *   `md.sys.typescale.headlineLarge`: Roboto, 32sp
        *   `md.sys.typescale.headlineMedium`: Roboto, 28sp
        *   `md.sys.typescale.headlineSmall`: Roboto, 24sp
        *   `md.sys.typescale.titleLarge`: Roboto, 22sp, FontWeight.Bold
        *   `md.sys.typescale.titleMedium`: Roboto, 16sp, FontWeight.Bold
        *   `md.sys.typescale.titleSmall`: Roboto, 14sp, FontWeight.Bold
        *   `md.sys.typescale.labelLarge`: Roboto, 14sp, FontWeight.Medium
        *   `md.sys.typescale.labelMedium`: Roboto, 12sp, FontWeight.Medium
        *   `md.sys.typescale.labelSmall`: Roboto, 11sp, FontWeight.Medium
        *   `md.sys.typescale.bodyLarge`: Roboto, 16sp
        *   `md.sys.typescale.bodyMedium`: Roboto, 14sp
        *   `md.sys.typescale.bodySmall`: Roboto, 12sp
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

### **Screen Name/ID**: 01_Splash_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background` (Dark Theme: `#121212`, Light Theme: `#FFFFFF`)
*   **Layout**: `Column`
    *   `verticalArrangement`: `Arrangement.Center`
    *   `horizontalAlignment`: `Alignment.CenterHorizontally`
    *   `modifier`: `fillMaxSize()`

#### III. Component Specifications
1.  **Name**: `Icon` (App Logo)
    *   **Position & Size**:
        *   Size: 120dp x 120dp
        *   Alignment: Centered in parent `Column`.
    *   **Style**:
        *   Icon: Custom Spotify logo vector.
        *   Tint: `md.sys.color.primary` (Light Theme), `#1DB954` (Dark Theme).
    *   **Content**:
        *   `contentDescription`: "Spotify Logo"

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On screen load, display for 2 seconds.
    *   After 2 seconds, automatically navigate to `02_Onboarding_Welcome_Screen`.
*   **Animations**:
    *   **Screen Transition (Exit)**: `MaterialFade` transition to the next screen.

---

### **Screen Name/ID**: 02_Onboarding_Welcome_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize()`, `padding(horizontal = 24dp, vertical = 48dp)`
    *   `verticalArrangement`: `Arrangement.SpaceBetween`
    *   `horizontalAlignment`: `Alignment.CenterHorizontally`

#### III. Component Specifications
1.  **Name**: `Icon` (App Logo)
    *   **Position & Size**:
        *   Size: 80dp x 80dp
        *   Alignment: Top center of the screen.
        *   Margin: `marginBottom = 64dp`
    *   **Style**:
        *   Icon: Custom Spotify logo vector.
        *   Tint: `md.sys.color.onBackground`.
    *   **Content**:
        *   `contentDescription`: "Spotify Logo"

2.  **Name**: `Text` (Headline)
    *   **Position & Size**:
        *   Alignment: Center of the screen.
        *   `modifier`: `fillMaxWidth()`
    *   **Style**:
        *   Typography: `md.sys.typescale.displaySmall`
        *   Color: `md.sys.color.onBackground`
        *   Text Alignment: `TextAlign.Center`
    *   **Content**: "Millions of songs.\nFree on Spotify."

3.  **Name**: `Column` (Button Container)
    *   **Position & Size**:
        *   Alignment: Bottom of the screen.
        *   `modifier`: `fillMaxWidth()`
    *   **Layout**:
        *   `verticalArrangement`: `Arrangement.spacedBy(8dp)`
        *   `horizontalAlignment`: `Alignment.CenterHorizontally`

4.  **Name**: `FilledButton` (Sign up free)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `height(48dp)`
    *   **Style**:
        *   Container Color: `md.sys.color.primary`
        *   Content Color: `md.sys.color.onPrimary`
        *   Typography: `md.sys.typescale.labelLarge`
        *   Shape: `Shape.Corner.Full` (Pill shape)
    *   **Content**:
        *   Text: "Sign up free"

5.  **Name**: `OutlinedButton` (Continue with Google)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `height(48dp)`
    *   **Style**:
        *   Outline Color: `md.sys.color.outline`
        *   Content Color: `md.sys.color.onBackground`
        *   Typography: `md.sys.typescale.labelLarge`
        *   Shape: `Shape.Corner.Full` (Pill shape)
    *   **Content**:
        *   Text: "Continue with Google"
        *   Icon (leading): Google 'G' logo, size 24dp.

6.  **Name**: `OutlinedButton` (Continue with Facebook)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `height(48dp)`
    *   **Style**:
        *   Outline Color: `md.sys.color.outline`
        *   Content Color: `md.sys.color.onBackground`
        *   Typography: `md.sys.typescale.labelLarge`
        *   Shape: `Shape.Corner.Full` (Pill shape)
    *   **Content**:
        *   Text: "Continue with Facebook"
        *   Icon (leading): Facebook 'f' logo, size 24dp.

7.  **Name**: `TextButton` (Log in)
    *   **Position & Size**:
        *   `modifier`: `height(48dp)`
    *   **Style**:
        *   Content Color: `md.sys.color.onBackground`
        *   Typography: `md.sys.typescale.labelLarge`
    *   **Content**:
        *   Text: "Log in"

#### IV. Interaction & Behavior
*   **States**:
    *   All buttons use Material Design state layers for pressed, hovered, and focused states (e.g., on press, apply a 12% opacity overlay of the content color).
*   **Interactions**:
    *   On tap of "Sign up free" button -> Navigate to `03_Signup_Screen`.
    *   On tap of "Continue with Google" button -> Initiate Google Sign-In flow (OAuth). On success, navigate to `05_Home_Screen`.
    *   On tap of "Continue with Facebook" button -> Initiate Facebook Sign-In flow (OAuth). On success, navigate to `05_Home_Screen`.
    *   On tap of "Log in" button -> Navigate to `04_Login_Screen`.
*   **Animations**:
    *   **Screen Transition (Enter)**: `MaterialSharedAxis(Z)` from `01_Splash_Screen`.
    *   **Screen Transition (Exit)**: `MaterialSharedAxis(X)` to `03_Signup_Screen` or `04_Login_Screen`.

---

### **Screen Name/ID**: 03_Signup_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize()`

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`
        *   Height: 56dp
    *   **Style**:
        *   Container Color: `md.sys.color.surface`
        *   Elevation: `Elevation.Level0`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   **Title**: `Text` component.
            *   Content: "Create account"
            *   Style: `md.sys.typescale.titleLarge`, color `md.sys.color.onSurface`.
            *   Alignment: Centered horizontally within the TopAppBar.

2.  **Name**: `Column` (Form Fields)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `padding(16dp)`, `verticalScroll(rememberScrollState())`
    *   **Layout**:
        *   `verticalArrangement`: `Arrangement.spacedBy(16dp)`

3.  **Name**: `Text` (Email Label)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`
    *   **Style**:
        *   Typography: `md.sys.typescale.bodyLarge`
        *   Color: `md.sys.color.onSurface`
    *   **Content**: "What's your email?"

4.  **Name**: `OutlinedTextField` (Email Input)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`
    *   **Style**:
        *   Typography: `md.sys.typescale.bodyLarge`
        *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors()`
        *   Shape: `Shape.Corner.Medium`
    *   **Content**:
        *   `label`: `Text` with content "Email".
        *   `keyboardOptions`: `KeyboardType.Email`

5.  **Name**: `TextButton` (Next Button)
    *   **Position & Size**:
        *   Alignment: `Alignment.CenterHorizontally`
        *   `modifier`: `wrapContentWidth()`, `height(48dp)`
    *   **Style**:
        *   Container Color: `md.sys.color.onBackground`
        *   Content Color: `md.sys.color.background`
        *   Shape: `Shape.Corner.Full`
        *   Initially disabled.
    *   **Content**:
        *   Text: "Next"

#### IV. Interaction & Behavior
*   **States**:
    *   "Next" button is disabled until a valid email format is entered in the `OutlinedTextField`.
    *   `OutlinedTextField` shows an error state (red border, helper text) if the input is not a valid email format after losing focus.
*   **Interactions**:
    *   On tap of Navigation Icon (`ArrowBack`) -> Navigate back to `02_Onboarding_Welcome_Screen`.
    *   User types in the email field. The "Next" button becomes enabled when the text is a valid email pattern.
    *   On tap of "Next" button -> Navigate to the next step of the signup flow (e.g., create password, not detailed in tree but implied). For this spec, assume on success it navigates to `05_Home_Screen`.
*   **Animations**:
    *   **Screen Transition (Enter/Exit)**: `MaterialSharedAxis(X)`.

#### V. Critical Scenarios & States
*   **Error State**:
    *   If the user enters an invalid email (e.g., "test@test") and taps "Next" or the field loses focus, the `OutlinedTextField` border turns to `md.sys.color.error`.
    *   A supporting `Text` component appears below the field with `typography = md.sys.typescale.bodySmall`, `color = md.sys.color.error`, and content "Please enter a valid email address."
*   **Loading State**:
    *   On tap of "Next", the button can show a `CircularProgressIndicator` (size 24dp) inside it while validating the email with the backend.

---

### **Screen Name/ID**: 04_Login_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize()`

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`
        *   Height: 56dp
    *   **Style**:
        *   Container Color: `md.sys.color.surface`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   **Title**: `Text` component, centered.
            *   Content: "Log in"
            *   Style: `md.sys.typescale.titleLarge`, color `md.sys.color.onSurface`.

2.  **Name**: `Column` (Form Fields)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `padding(16dp)`, `verticalScroll(rememberScrollState())`
    *   **Layout**:
        *   `verticalArrangement`: `Arrangement.spacedBy(8dp)`

3.  **Name**: `Text` (Email Label)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`
    *   **Style**: `md.sys.typescale.bodyLarge`, `md.sys.color.onSurface`
    *   **Content**: "Email or username"

4.  **Name**: `OutlinedTextField` (Email/Username Input)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`
    *   **Style**: Standard `OutlinedTextField` styles.
    *   **Content**: `label`: `Text` with content "Email or username".

5.  **Name**: `Text` (Password Label)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`, `padding(top = 8dp)`
    *   **Style**: `md.sys.typescale.bodyLarge`, `md.sys.color.onSurface`
    *   **Content**: "Password"

6.  **Name**: `OutlinedTextField` (Password Input)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`
    *   **Style**: Standard `OutlinedTextField` styles.
    *   **Content**:
        *   `label`: `Text` with content "Password".
        *   `visualTransformation`: `PasswordVisualTransformation()`
        *   `keyboardOptions`: `KeyboardType.Password`
        *   `trailingIcon`: `IconButton` with a toggleable eye icon (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`) to show/hide password. `contentDescription`: "Toggle password visibility".

7.  **Name**: `FilledButton` (Log In Button)
    *   **Position & Size**:
        *   Alignment: `Alignment.CenterHorizontally`
        *   `modifier`: `wrapContentWidth()`, `height(48dp)`, `margin(top = 16dp)`
    *   **Style**:
        *   Container Color: `md.sys.color.onBackground`
        *   Content Color: `md.sys.color.background`
        *   Shape: `Shape.Corner.Full`
        *   Initially disabled.
    *   **Content**:
        *   Text: "Log In"

8.  **Name**: `TextButton` (Forgot Password)
    *   **Position & Size**:
        *   Alignment: `Alignment.CenterHorizontally`
        *   `modifier`: `height(48dp)`, `margin(top = 8dp)`
    *   **Style**:
        *   Content Color: `md.sys.color.onBackground`
        *   Typography: `md.sys.typescale.labelLarge`
    *   **Content**:
        *   Text: "Log in without password"

#### IV. Interaction & Behavior
*   **States**:
    *   "Log In" button is disabled until both fields are non-empty.
*   **Interactions**:
    *   On tap of Navigation Icon (`ArrowBack`) -> Navigate back to `02_Onboarding_Welcome_Screen`.
    *   On tap of "Log In" button -> Authenticate user. On success, navigate to `05_Home_Screen`. On failure, show an error.
    *   On tap of "Log in without password" -> Navigate to a password recovery flow (not specified in tree).
*   **Animations**:
    *   **Screen Transition (Enter/Exit)**: `MaterialSharedAxis(X)`.

#### V. Critical Scenarios & States
*   **Error State**:
    *   If login fails, a `Snackbar` appears at the bottom of the screen.
    *   **Snackbar Style**: Container color `md.sys.color.errorContainer`, text color `md.sys.color.onErrorContainer`.
    *   **Snackbar Content**: "Incorrect username or password."
*   **Loading State**:
    *   On tap of "Log In", the button shows a `CircularProgressIndicator` (size 24dp) inside it while authenticating.

---

### **Screen Name/ID**: 05_Home_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold`
    *   `topBar`: `TopAppBar`
    *   `bottomBar`: `NavigationBar`
    *   `content`: `LazyColumn`

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**: Top of the `Scaffold`. Height 64dp.
    *   **Style**:
        *   Container Color: `md.sys.color.surface` (transparent gradient to background).
        *   `scrollBehavior`: `TopAppBarDefaults.enterAlwaysScrollBehavior()`
    *   **Content**:
        *   **Title**: `Text` with content "Good morning" (or afternoon/evening). Style: `md.sys.typescale.titleLarge`, `FontWeight.Bold`.
        *   **Actions**: `Row` containing three `IconButton`s.
            *   `IconButton` 1: `Icons.Outlined.Notifications`, `contentDescription`: "Notifications".
            *   `IconButton` 2: `Icons.Outlined.History`, `contentDescription`: "Recently played".
            *   `IconButton` 3: `Icons.Outlined.Settings`, `contentDescription`: "Settings".

2.  **Name**: `LazyColumn` (Main Content)
    *   **Position & Size**: Fills the content area of the `Scaffold`. `padding(horizontal = 16dp)`.
    *   **Layout**: `Arrangement.spacedBy(24dp)`.

3.  **Name**: `Row` (Filter Chips)
    *   **Position & Size**: First item in the `LazyColumn`.
    *   **Layout**: `Arrangement.spacedBy(8dp)`.
    *   **Content**:
        *   `AssistChip` 1: Label "Music".
        *   `AssistChip` 2: Label "Podcasts & Shows".
        *   Style: `AssistChipDefaults.assistChipColors(containerColor = md.sys.color.surfaceVariant)`.

4.  **Name**: `Text` (Section Header 1)
    *   **Position & Size**: Item in `LazyColumn`.
    *   **Style**: `md.sys.typescale.titleMedium`, `FontWeight.Bold`.
    *   **Content**: "Recently played"

5.  **Name**: `LazyRow` (Recently Played)
    *   **Position & Size**: Item in `LazyColumn`. `fillMaxWidth()`.
    *   **Layout**: `Arrangement.spacedBy(16dp)`.
    *   **Content**: A horizontal list of `Column` items.
        *   **Item**: `Column` containing:
            *   `Image`: 120x120dp, `shape = Shape.Corner.Medium`, `contentScale = ContentScale.Crop`. Placeholder for album/playlist art.
            *   `Text`: `maxLines = 2`, `overflow = TextOverflow.Ellipsis`. Style `md.sys.typescale.bodyMedium`. Content: "Liked Songs" or playlist name.

6.  **Name**: `Text` (Section Header 2)
    *   **Position & Size**: Item in `LazyColumn`.
    *   **Style**: `md.sys.typescale.titleMedium`, `FontWeight.Bold`.
    *   **Content**: "Made for You"

7.  **Name**: `LazyRow` (Made for You)
    *   **Position & Size**: Item in `LazyColumn`. `fillMaxWidth()`.
    *   **Layout**: `Arrangement.spacedBy(16dp)`.
    *   **Content**: Similar to "Recently Played" row, displaying personalized playlists like "Discover Weekly".

8.  **Name**: `NavigationBar`
    *   **Position & Size**: Bottom of the `Scaffold`. `modifier`: `fillMaxWidth()`.
    *   **Style**: `md.sys.color.surfaceVariant`.
    *   **Content**:
        *   `NavigationBarItem` 1:
            *   `selected`: `true`
            *   `icon`: `Icon` with `Icons.Filled.Home`, `contentDescription`: "Home".
            *   `label`: `Text` with "Home".
        *   `NavigationBarItem` 2:
            *   `selected`: `false`
            *   `icon`: `Icon` with `Icons.Outlined.Search`, `contentDescription`: "Search".
            *   `label`: `Text` with "Search".
        *   `NavigationBarItem` 3:
            *   `selected`: `false`
            *   `icon`: `Icon` with `Icons.Outlined.LibraryMusic`, `contentDescription`: "Your Library".
            *   `label`: `Text` with "Your Library".

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of a playlist/album item in any `LazyRow` -> Navigate to `07_Playlist_Screen`.
    *   On tap of "Search" `NavigationBarItem` -> Navigate to `06_Search_Screen`.
    *   On tap of "Your Library" `NavigationBarItem` -> Navigate to `08_Library_Screen`.
    *   On tap of Settings icon -> Navigate to `10_Settings_Screen`.
*   **Animations**:
    *   **Screen Transition (Bottom Nav)**: `MaterialFadeThrough`.
*   **Scroll Behavior**:
    *   As the user scrolls down, the `TopAppBar` scrolls out of view.
    *   As the user scrolls up, the `TopAppBar` scrolls back into view.

#### V. Critical Scenarios & States
*   **Empty State**:
    *   If a new user has no "Recently played" items, the section is hidden or replaced with a message like "Start listening to see your history here."
*   **Loading State**:
    *   The screen displays shimmer placeholders for the `LazyRow` items while data is being fetched. Each placeholder is a grey box matching the dimensions of the content it represents.

---

### **Screen Name/ID**: 06_Search_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `Column` content.

#### III. Component Specifications
1.  **Name**: `Column` (Main Content)
    *   **Position & Size**: Fills content area. `modifier`: `fillMaxSize()`, `padding(16dp)`.
    *   **Layout**: `verticalArrangement`: `Arrangement.spacedBy(16dp)`.

2.  **Name**: `Text` (Screen Title)
    *   **Position & Size**: Top of the column.
    *   **Style**: `md.sys.typescale.headlineMedium`, `FontWeight.Bold`.
    *   **Content**: "Search"

3.  **Name**: `SearchBar` (Docked)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`.
    *   **Style**: `SearchBarDefaults` with container color `md.sys.color.surfaceVariant`.
    *   **Content**:
        *   `placeholder`: `Text` with "What do you want to listen to?".
        *   `leadingIcon`: `Icon` with `Icons.Filled.Search`.
        *   `trailingIcon`: `Icon` with `Icons.Outlined.CameraAlt` for search by image (hypothetical feature).

4.  **Name**: `Text` (Section Header)
    *   **Position & Size**: Below search bar.
    *   **Style**: `md.sys.typescale.titleMedium`, `FontWeight.Bold`.
    *   **Content**: "Browse all"

5.  **Name**: `LazyVerticalGrid` (Genre/Category Cards)
    *   **Position & Size**: Fills remaining space.
    *   **Layout**: `GridCells.Fixed(2)`, `verticalArrangement = Arrangement.spacedBy(16dp)`, `horizontalArrangement = Arrangement.spacedBy(16dp)`.
    *   **Content**: A grid of `Card` components.
        *   **Item**: `Card`
            *   Size: ~170dp x 100dp.
            *   Style: `CardDefaults.cardColors(containerColor = a dynamic color, e.g., md.sys.color.tertiaryContainer)`.
            *   Content: `Box` with a `Text` label ("Podcasts", "Pop", "Rock", etc.) at the top-left and a small cover art image rotated and positioned at the bottom-right.

6.  **Name**: `NavigationBar`
    *   **Position & Size**: Bottom of the `Scaffold`.
    *   **Content**: Same as `05_Home_Screen`, but with "Search" item selected.
        *   `NavigationBarItem` 2: `selected`: `true`, `icon`: `Icons.Filled.Search`.

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of `SearchBar` -> Transition to active search view (`06a_Search_Active_Screen`).
    *   On tap of a genre card -> Navigate to a screen showing content for that genre (e.g., `07_Playlist_Screen` filtered by genre).
    *   On tap of "Home" `NavigationBarItem` -> Navigate to `05_Home_Screen`.
    *   On tap of "Your Library" `NavigationBarItem` -> Navigate to `08_Library_Screen`.
*   **Animations**:
    *   **Screen Transition (Bottom Nav)**: `MaterialFadeThrough`.
    *   **Search Bar Transition**: The `SearchBar` seamlessly expands into the full-screen active search view.

---

### **Screen Name/ID**: 06a_Search_Active_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `LazyColumn` content.

#### III. Component Specifications
1.  **Name**: `SearchBar` (Active)
    *   **Position & Size**: Top of the screen. `modifier`: `fillMaxWidth()`.
    *   **Style**: Active state of the `SearchBar` component.
    *   **Content**:
        *   `leadingIcon`: `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   `placeholder`: Same as before.
        *   `trailingIcon`: `IconButton` with `Icons.Filled.Clear` if text is present. `contentDescription`: "Clear search".
        *   The keyboard is automatically focused and visible.

2.  **Name**: `LazyColumn` (Search Results)
    *   **Position & Size**: Fills the content area below the search bar.
    *   **Layout**: `Arrangement.spacedBy(8dp)`.
    *   **Content**: List of search results.
        *   **Item**: `ListItem`
            *   `leadingContent`: `Image` (64x64dp) for album/artist/song art.
            *   `headlineContent`: `Text` for the song/artist name (e.g., "Bohemian Rhapsody").
            *   `supportingContent`: `Text` for the subtitle (e.g., "Song • Queen").
            *   `trailingContent`: `IconButton` with `Icons.Filled.MoreVert`. `contentDescription`: "More options".

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of `ArrowBack` icon -> Navigate back to `06_Search_Screen`.
    *   As user types, search results populate the `LazyColumn` in real-time.
    *   On tap of a search result `ListItem` -> Navigate to the relevant screen (`07_Playlist_Screen` for an album, `09_Now_Playing_Screen` for a song).
    *   On tap of `Clear` icon -> Clears the text from the search query field.
*   **Animations**:
    *   The transition from the docked `SearchBar` to the active full-screen view is animated using Material Design's built-in `SearchBar` motion spec.

#### V. Critical Scenarios & States
*   **Empty State**:
    *   If a search yields no results, the `LazyColumn` is replaced with a centered `Column` containing:
        *   `Icon`: `Icons.Outlined.SearchOff`, size 64dp, color `md.sys.color.onSurfaceVariant`.
        *   `Text` (Headline): "Couldn't find anything." Style `md.sys.typescale.titleMedium`.
        *   `Text` (Body): "Try searching for something else." Style `md.sys.typescale.bodyMedium`.
*   **Loading State**:
    *   While waiting for search results after the user stops typing, a `LinearProgressIndicator` is displayed directly underneath the `SearchBar`.

---

### **Screen Name/ID**: 07_Playlist_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `LazyColumn`. A dynamic gradient based on the album art is drawn behind the `TopAppBar` and at the top of the content.

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**: Top of the `Scaffold`. Height 56dp.
    *   **Style**:
        *   Container Color: `Color.Transparent`.
        *   `scrollBehavior`: `TopAppBarDefaults.exitUntilCollapsedScrollBehavior()`. The title fades in as the user scrolls.
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   **Title**: `Text` with playlist name, initially transparent, fades to `md.sys.color.onSurface` on scroll.

2.  **Name**: `LazyColumn` (Playlist Content)
    *   **Position & Size**: Fills the `Scaffold` content area.
    *   **Content**:
        *   **Header Item**: `Column` with `padding(16dp)`.
            *   `Image`: 200x200dp, `Alignment.CenterHorizontally`, `shape = Shape.Corner.Medium`. Playlist/Album cover art.
            *   `Text` (Title): Playlist name, e.g., "Discover Weekly". Style `md.sys.typescale.headlineLarge`, `FontWeight.Bold`.
            *   `Text` (Description): Playlist description. Style `md.sys.typescale.bodyMedium`, color `md.sys.color.onSurfaceVariant`.
            *   `Row` (Actions): `Arrangement.spacedBy(16dp)`.
                *   `IconButton`: `Icons.Filled.FavoriteBorder`, `contentDescription`: "Like".
                *   `IconButton`: `Icons.Filled.DownloadForOffline`, `contentDescription`: "Download".
                *   `IconButton`: `Icons.Filled.MoreVert`, `contentDescription`: "More options".
        *   **Song Items**: List of `ListItem`s.
            *   `ListItem`:
                *   `leadingContent`: `Image` (56x56dp) for song's album art.
                *   `headlineContent`: `Text` for song title.
                *   `supportingContent`: `Text` for artist name.
                *   `trailingContent`: `IconButton` with `Icons.Filled.MoreVert`.

3.  **Name**: `FloatingActionButton` (Play)
    *   **Position & Size**: Anchored to the `LazyColumn` header, often overlapping the action `Row`. Size `56x56dp`.
    *   **Style**: `FloatingActionButtonDefaults.largeFAB()` with container color `md.sys.color.primary`.
    *   **Content**: `Icon` with `Icons.Filled.PlayArrow`, size 36dp. `contentDescription`: "Play playlist".

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of `ArrowBack` -> Navigate to the previous screen (e.g., `05_Home_Screen`).
    *   On tap of a song `ListItem` -> Navigate to `09_Now_Playing_Screen` and start playing that song.
    *   On tap of the `FloatingActionButton` -> Start playing the playlist from the first song and navigate to `09_Now_Playing_Screen`.
*   **Scroll Behavior**:
    *   As the user scrolls down, the header content (Image, Title) scrolls up. The `TopAppBar` title fades in, and its background color transitions from transparent to `md.sys.color.surface`. This is a collapsing toolbar effect.

---

### **Screen Name/ID**: 08_Library_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `LazyColumn`.

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**: Top of the `Scaffold`. Height 64dp.
    *   **Style**: `md.sys.color.surface`.
    *   **Content**:
        *   **Title**: `Row` with `Arrangement.spacedBy(8dp)`.
            *   `Avatar`: 32x32dp, `shape = CircleShape`. User's profile picture.
            *   `Text`: "Your Library". Style `md.sys.typescale.titleLarge`, `FontWeight.Bold`.
        *   **Actions**: `Row` with two `IconButton`s.
            *   `IconButton` 1: `Icons.Outlined.Search`, `contentDescription`: "Search in library".
            *   `IconButton` 2: `Icons.Filled.Add`, `contentDescription`: "Create playlist".

2.  **Name**: `LazyColumn` (Library Content)
    *   **Position & Size**: Fills the content area.
    *   **Content**: List of `ListItem`s representing playlists, albums, and artists.
        *   **Item**: `ListItem`
            *   `leadingContent`: `Image` (64x64dp) for playlist/album art. `shape = Shape.Corner.Small`.
            *   `headlineContent`: `Text` for the item name (e.g., "Liked Songs").
            *   `supportingContent`: `Text` for the subtitle (e.g., "Playlist • 123 songs").

3.  **Name**: `NavigationBar`
    *   **Position & Size**: Bottom of the `Scaffold`.
    *   **Content**: Same as `05_Home_Screen`, but with "Your Library" item selected.
        *   `NavigationBarItem` 3: `selected`: `true`, `icon`: `Icons.Filled.LibraryMusic`.

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of a `ListItem` -> Navigate to `07_Playlist_Screen`.
    *   On tap of "Home" `NavigationBarItem` -> Navigate to `05_Home_Screen`.
    *   On tap of "Search" `NavigationBarItem` -> Navigate to `06_Search_Screen`.
*   **Animations**:
    *   **Screen Transition (Bottom Nav)**: `MaterialFadeThrough`.

#### V. Critical Scenarios & States
*   **Empty State**:
    *   If the user has no saved items, the `LazyColumn` is replaced with a centered `Column`:
        *   `Text` (Headline): "Create your first playlist". Style `md.sys.typescale.titleLarge`.
        *   `Text` (Body): "It's easy, we'll help you." Style `md.sys.typescale.bodyMedium`.
        *   `FilledButton`: Content "Create playlist", `margin(top = 24dp)`.

---

### **Screen Name/ID**: 09_Now_Playing_Screen
*   **Dimensions**: 393x852dp
*   **Background**: Dynamic gradient extracted from the current song's album art.
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize()`, `padding(horizontal = 24dp, vertical = 16dp)`.

#### III. Component Specifications
1.  **Name**: `TopAppBar` (Simplified)
    *   **Position & Size**: Top of the screen.
    *   **Style**: `Color.Transparent`.
    *   **Content**:
        *   `leadingContent`: `IconButton` with `Icons.Filled.ExpandMore`. `contentDescription`: "Collapse player".
        *   `titleContent`: `Column` with `Alignment.CenterHorizontally`.
            *   `Text`: "PLAYING FROM ALBUM". Style `md.sys.typescale.labelSmall`.
            *   `Text`: Album Name. Style `md.sys.typescale.labelMedium`, `FontWeight.Bold`.
        *   `trailingContent`: `IconButton` with `Icons.Filled.MoreVert`. `contentDescription`: "More options".

2.  **Name**: `Image` (Album Art)
    *   **Position & Size**:
        *   `modifier`: `fillMaxWidth()`, `aspectRatio(1f)`, `padding(vertical = 32dp)`.
        *   `shape`: `Shape.Corner.Large`.
    *   **Content**: High-resolution album art for the currently playing song.

3.  **Name**: `Row` (Song Info & Like)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`.
    *   **Layout**: `Arrangement.SpaceBetween`, `Alignment.CenterVertically`.
    *   **Content**:
        *   `Column` (Song/Artist):
            *   `Text` (Title): Song Title. Style `md.sys.typescale.headlineSmall`, `FontWeight.Bold`.
            *   `Text` (Artist): Artist Name. Style `md.sys.typescale.bodyLarge`, color `md.sys.color.onSurfaceVariant`.
        *   `IconButton`: `Icons.Filled.Favorite` (if liked) or `Icons.Filled.FavoriteBorder` (if not). `contentDescription`: "Like".

4.  **Name**: `Slider` (Seek Bar)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`, `padding(vertical = 8dp)`.
    *   **Style**: `SliderDefaults.colors(thumbColor = md.sys.color.primary, activeTrackColor = md.sys.color.primary)`.
    *   **Content**: Represents song progress.

5.  **Name**: `Row` (Timestamps)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`.
    *   **Layout**: `Arrangement.SpaceBetween`.
    *   **Content**:
        *   `Text` (Current Time): e.g., "1:23". Style `md.sys.typescale.bodySmall`.
        *   `Text` (Total Time): e.g., "3:45". Style `md.sys.typescale.bodySmall`.

6.  **Name**: `Row` (Player Controls)
    *   **Position & Size**: `modifier`: `fillMaxWidth()`, `padding(vertical = 8dp)`.
    *   **Layout**: `Arrangement.SpaceAround`, `Alignment.CenterVertically`.
    *   **Content**:
        *   `IconButton`: `Icons.Filled.Shuffle`. `contentDescription`: "Shuffle".
        *   `IconButton`: `Icons.Filled.SkipPrevious`, size 48dp. `contentDescription`: "Previous song".
        *   `IconButton` (Play/Pause): `FilledIconButton` with large container.
            *   Size: 72x72dp.
            *   Icon: `Icons.Filled.Pause` or `Icons.Filled.PlayArrow`, size 48dp.
            *   `contentDescription`: "Play" or "Pause".
        *   `IconButton`: `Icons.Filled.SkipNext`, size 48dp. `contentDescription`: "Next song".
        *   `IconButton`: `Icons.Filled.Repeat`. `contentDescription`: "Repeat".

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of `ExpandMore` icon -> Collapse the screen into a mini-player anchored above the `NavigationBar` and navigate back to the previous screen.
    *   User can drag the `Slider` thumb to seek through the song.
    *   On tap of Play/Pause button -> Toggles playback state.
    *   On tap of Skip Next/Previous -> Changes the track.
*   **Animations**:
    *   The screen should slide up from the bottom when a song is played. It should slide down when collapsed. This is a `SharedElement` transition where the mini-player expands into the full screen.

---

### **Screen Name/ID**: 10_Settings_Screen
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with `LazyColumn`.

#### III. Component Specifications
1.  **Name**: `TopAppBar`
    *   **Position & Size**: Top of the `Scaffold`. Height 56dp.
    *   **Style**: `md.sys.color.surface`.
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icons.Filled.ArrowBack`. `contentDescription`: "Back".
        *   **Title**: `Text` with "Settings". Style `md.sys.typescale.titleLarge`.

2.  **Name**: `LazyColumn` (Settings List)
    *   **Position & Size**: Fills the content area.
    *   **Content**: A list of settings items, grouped by sections.

3.  **Name**: `ListItem` (Account)
    *   **Position & Size**: Item in `LazyColumn`.
    *   **Content**:
        *   `leadingContent`: `Avatar` (40x40dp) with user's profile picture.
        *   `headlineContent`: `Text` with user's name.
        *   `supportingContent`: `Text` with "View profile".
        *   `trailingContent`: `Icon` with `Icons.Filled.ChevronRight`.

4.  **Name**: `Text` (Section Header)
    *   **Position & Size**: Item in `LazyColumn`. `padding(horizontal = 16dp, vertical = 8dp)`.
    *   **Style**: `md.sys.typescale.titleSmall`, color `md.sys.color.primary`.
    *   **Content**: "Data Saver"

5.  **Name**: `ListItem` (Data Saver Toggle)
    *   **Position & Size**: Item in `LazyColumn`.
    *   **Content**:
        *   `headlineContent`: `Text` with "Data Saver".
        *   `supportingContent`: `Text` with "Sets your audio quality to low...".
        *   `trailingContent`: `Switch` component.

6.  **Name**: `ListItem` (Logout Button)
    *   **Position & Size**: Item in `LazyColumn`. `margin(top = 32dp)`.
    *   **Style**: `ListItemDefaults.colors(headlineColor = md.sys.color.error)`.
    *   **Content**:
        *   `headlineContent`: `Text` with "Log out", centered.

#### IV. Interaction & Behavior
*   **Interactions**:
    *   On tap of `ArrowBack` -> Navigate back to `05_Home_Screen`.
    *   On tap of Account `ListItem` -> Navigate to a Profile screen (not in tree).
    *   Toggling the `Switch` enables/disables the Data Saver feature.
    *   On tap of "Log out" -> A confirmation `AlertDialog` is shown.
        *   **AlertDialog**: Title "Log out?", Text "Are you sure you want to log out?", Confirm button "Log out", Dismiss button "Cancel".
        *   On confirm -> Log the user out and navigate to `02_Onboarding_Welcome_Screen`.
*   **Animations**:
    *   **Screen Transition (Enter/Exit)**: `MaterialSharedAxis(X)`.

```

---


============================================================
## APP 2: App_2
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

# Android Design Specification: SocialConnect App

## I. Global Specifications

*   **Platform**: Android Mobile App
*   **Design System**: Material Design 3
    *   **Dynamic Color**: Enabled (Material You). The specified colors serve as the baseline for devices without dynamic color support.
    *   **Modes**: Light and Dark themes are supported. All color roles are defined for both.
*   **Colors**:
    *   **Seed Color**: `#6750A4` (M3 Baseline Purple)
    *   **Key Color Roles (Light Theme)**:
        *   `md.sys.color.primary`: `#6750A4`
        *   `md.sys.color.onPrimary`: `#FFFFFF`
        *   `md.sys.color.primaryContainer`: `#EADDFF`
        *   `md.sys.color.onPrimaryContainer`: `#21005D`
        *   `md.sys.color.secondary`: `#625B71`
        *   `md.sys.color.onSecondary`: `#FFFFFF`
        *   `md.sys.color.secondaryContainer`: `#E8DEF8`
        *   `md.sys.color.onSecondaryContainer`: `#1D192B`
        *   `md.sys.color.tertiary`: `#7D5260`
        *   `md.sys.color.onTertiary`: `#FFFFFF`
        *   `md.sys.color.tertiaryContainer`: `#FFD8E4`
        *   `md.sys.color.onTertiaryContainer`: `#31111D`
        *   `md.sys.color.error`: `#B3261E`
        *   `md.sys.color.onError`: `#FFFFFF`
        *   `md.sys.color.errorContainer`: `#F9DEDC`
        *   `md.sys.color.onErrorContainer`: `#410E0B`
        *   `md.sys.color.background`: `#FFFBFE`
        *   `md.sys.color.onBackground`: `#1C1B1F`
        *   `md.sys.color.surface`: `#FFFBFE`
        *   `md.sys.color.onSurface`: `#1C1B1F`
        *   `md.sys.color.surfaceVariant`: `#E7E0EC`
        *   `md.sys.color.onSurfaceVariant`: `#49454F`
        *   `md.sys.color.outline`: `#79747E`
        *   `md.sys.color.inverseOnSurface`: `#F4EFF4`
        *   `md.sys.color.inverseSurface`: `#313033`
        *   `md.sys.color.inversePrimary`: `#D0BCFF`
        *   `md.sys.color.surfaceTint`: `#6750A4`
*   **Typography**:
    *   **Font Family**: Roboto
    *   **Type Scale**: Material 3 Type Scale
        *   `displayLarge`: Roboto, 57sp
        *   `displayMedium`: Roboto, 45sp
        *   `displaySmall`: Roboto, 36sp
        *   `headlineLarge`: Roboto, 32sp
        *   `headlineMedium`: Roboto, 28sp
        *   `headlineSmall`: Roboto, 24sp
        *   `titleLarge`: Roboto, 22sp
        *   `titleMedium`: Roboto, 16sp, Letter Spacing 0.15
        *   `titleSmall`: Roboto, 14sp, Letter Spacing 0.1
        *   `labelLarge`: Roboto, 14sp, Letter Spacing 0.1
        *   `labelMedium`: Roboto, 12sp, Letter Spacing 0.5
        *   `labelSmall`: Roboto, 11sp, Letter Spacing 0.5
        *   `bodyLarge`: Roboto, 16sp, Letter Spacing 0.5
        *   `bodyMedium`: Roboto, 14sp, Letter Spacing 0.25
        *   `bodySmall`: Roboto, 12sp, Letter Spacing 0.4
*   **Spacing**:
    *   **Base Grid Unit**: 8dp
    *   **Standard Padding**: 16dp
    *   **Standard Margins**: 16dp
*   **Accessibility**:
    *   **Target Standard**: WCAG 2.1 Level AA
    *   **Minimum Touch Target**: 48dp x 48dp for all interactive elements.
    *   **Content Descriptions**: All icons, images, and non-text controls must have descriptive content descriptions.

---

## II. Screen Specifications: 01_Splash_Screen

*   **Screen Name/ID**: `01_Splash_Screen`
*   **Dimensions**: 393x852dp (Typical mobile viewport)
*   **Background**: `md.sys.color.surface`
*   **Layout**: `Column`
    *   `verticalArrangement`: `Center`
    *   `horizontalAlignment`: `CenterHorizontally`
    *   `modifier`: `fillMaxSize`

### III. Component Specifications

1.  **Name**: `Icon` (App Logo)
    *   **Position & Size**:
        *   Size: 128dp x 128dp
        *   Alignment: Centered in the layout.
    *   **Style**:
        *   Icon: `Icons.Filled.Groups` (Placeholder)
        *   Tint: `md.sys.color.primary`
    *   **Content**: N/A

2.  **Name**: `Text` (App Name)
    *   **Position & Size**:
        *   Alignment: Centered horizontally.
        *   Margin (Top): 24dp from the App Logo.
    *   **Style**:
        *   Color: `md.sys.color.onSurface`
        *   Typography: `headlineMedium`
    *   **Content**: "SocialConnect"

### IV. Interaction & Behavior

*   **States**: This is a static screen. No interactive elements.
*   **Interactions**:
    *   On screen load, a timer is initiated.
    *   After a 2-second delay, the app automatically navigates to the next screen.
*   **Animations**:
    *   **Screen Transition (Exit)**: `MaterialFadeThrough` transition to `02_Login_Screen`.
*   **Scroll Behavior**: N/A (Content does not scroll).

### V. Critical Scenarios & States

*   **Loading State**: The entire screen serves as the initial loading state for the app.

---

## II. Screen Specifications: 02_Login_Screen

*   **Screen Name/ID**: `02_Login_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `verticalArrangement`: `Center`
    *   `horizontalAlignment`: `CenterHorizontally`
    *   `modifier`: `fillMaxSize`, `padding(horizontal = 24dp)`

### III. Component Specifications

1.  **Name**: `Icon` (App Logo)
    *   **Position & Size**:
        *   Size: 80dp x 80dp
        *   Margin (Bottom): 16dp
    *   **Style**:
        *   Icon: `Icons.Filled.Groups` (Placeholder)
        *   Tint: `md.sys.color.primary`
    *   **Content**: N/A

2.  **Name**: `Text` (Headline)
    *   **Position & Size**:
        *   Margin (Bottom): 8dp
    *   **Style**:
        *   Color: `md.sys.color.onBackground`
        *   Typography: `headlineLarge`
        *   Text Align: `Center`
    *   **Content**: "Welcome Back"

3.  **Name**: `Text` (Sub-headline)
    *   **Position & Size**:
        *   Margin (Bottom): 32dp
    *   **Style**:
        *   Color: `md.sys.color.onSurfaceVariant`
        *   Typography: `bodyLarge`
        *   Text Align: `Center`
    *   **Content**: "Sign in to your account"

4.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**:
        *   Size: `fillMaxWidth`
        *   Margin (Bottom): 16dp
    *   **Style**:
        *   Shape: `Shape.Corner.Medium`
        *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors()`
    *   **Content**:
        *   Label: `Text("Email")`
        *   Leading Icon: `Icon(Icons.Filled.Email)`
        *   Keyboard Type: `Email`
        *   Single Line: `true`

5.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**:
        *   Size: `fillMaxWidth`
        *   Margin (Bottom): 24dp
    *   **Style**:
        *   Shape: `Shape.Corner.Medium`
        *   Visual Transformation: `PasswordVisualTransformation` (by default)
    *   **Content**:
        *   Label: `Text("Password")`
        *   Leading Icon: `Icon(Icons.Filled.Lock)`
        *   Trailing Icon: `IconButton` with `Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff` to toggle password visibility.
        *   Keyboard Type: `Password`
        *   Single Line: `true`

6.  **Name**: `FilledButton` (Login)
    *   **Position & Size**:
        *   Size: `fillMaxWidth`, Height: 52dp
        *   Margin (Bottom): 16dp
    *   **Style**:
        *   Shape: `Shape.Corner.Full`
    *   **Content**:
        *   Text: `Text("Login", style = typography.labelLarge)`

7.  **Name**: `TextButton` (Sign Up)
    *   **Position & Size**:
        *   Alignment: `CenterHorizontally`
        *   Minimum Touch Target: 48x48dp
    *   **Style**: Standard `TextButton` style.
    *   **Content**:
        *   Text: `Text("Don't have an account? Sign Up")`

### IV. Interaction & Behavior

*   **States**:
    *   **TextFields**: Standard states for `focused`, `unfocused`, `error`.
    *   **Buttons**: Standard Material 3 state layers for `pressed`, `hovered`, `focused`. `Login` button is disabled if email/password fields are empty.
*   **Interactions**:
    *   **Email/Password Fields**: On focus, the label moves up.
    *   **Password Visibility Icon**: On tap, toggles the visibility of the password text.
    *   **Login Button**: On tap, performs authentication. On success, navigates to `03_Home_Screen`. On failure, shows an error state.
    *   **Sign Up TextButton**: On tap, navigates to `04_Registration_Screen`.
*   **Animations**:
    *   **Screen Transition (Entry)**: `MaterialSharedAxis(Z, forward = true)`
    *   **Screen Transition (Exit to Home)**: `MaterialSharedAxis(Z, forward = true)`
    *   **Screen Transition (Exit to Register)**: `MaterialSharedAxis(X, forward = true)`
*   **Scroll Behavior**: The layout is vertically scrollable on smaller screens to prevent UI elements from being obscured by the keyboard.

### V. Critical Scenarios & States

*   **Error State**:
    *   **Invalid Input**: `OutlinedTextField` border, label, and leading icon change to `md.sys.color.error`. A supporting text appears below the field with a message (e.g., "Invalid email format" or "Password cannot be empty").
    *   **Authentication Failure**: A `Snackbar` appears at the bottom of the screen with the message "Invalid email or password."
*   **Loading State**: On `Login` button tap, the button's text is replaced by a `CircularProgressIndicator` (size 24dp, color `md.sys.color.onPrimary`) and the button is disabled until the network request completes.

---

## II. Screen Specifications: 03_Home_Screen (Container)

*   **Screen Name/ID**: `03_Home_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold`
    *   This screen acts as the main container for the five primary tabs of the application. The content area of the scaffold will display the content of the currently selected tab (`03a` through `03e`).

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Position & Size**:
        *   Positioned at the top of the `Scaffold`.
        *   Size: `fillMaxWidth`, Height: 64dp
    *   **Style**:
        *   Type: `CenterAlignedTopAppBar`
        *   Colors: `md.sys.color.surface`
        *   Elevation: `Elevation.Level2` when content is scrolled beneath it.
    *   **Content**:
        *   **Title**: `Text` component. The content changes based on the active tab (e.g., "Feed", "Search").
        *   **Actions**: `IconButton`s on the right. For example, on the Feed tab, it might show an `IconButton` for `Icons.Filled.Chat`.

2.  **Name**: `NavigationBar` (Bottom Navigation)
    *   **Position & Size**:
        *   Positioned at the bottom of the `Scaffold`.
        *   Size: `fillMaxWidth`, Height: 80dp
    *   **Style**:
        *   Container Color: `md.sys.color.surfaceVariant`
        *   Indicator Color: `md.sys.color.secondaryContainer`
    *   **Content**: Contains five `NavigationBarItem` components.

3.  **Name**: `NavigationBarItem` (Feed)
    *   **Position & Size**: First item in the `NavigationBar`.
    *   **Style**:
        *   Selected Icon Color: `md.sys.color.onSecondaryContainer`
        *   Unselected Icon Color: `md.sys.color.onSurfaceVariant`
        *   Selected Text Color: `md.sys.color.onSurface`
        *   Unselected Text Color: `md.sys.color.onSurfaceVariant`
    *   **Content**:
        *   Icon: `Icons.Filled.Home` (selected), `Icons.Outlined.Home` (unselected)
        *   Label: `Text("Feed", style = typography.labelMedium)`

4.  **Name**: `NavigationBarItem` (Search)
    *   **Position & Size**: Second item in the `NavigationBar`.
    *   **Style**: Same as above.
    *   **Content**:
        *   Icon: `Icons.Filled.Search` (selected), `Icons.Outlined.Search` (unselected)
        *   Label: `Text("Search", style = typography.labelMedium)`

5.  **Name**: `NavigationBarItem` (Create Post)
    *   **Position & Size**: Third item in the `NavigationBar`.
    *   **Style**: Same as above.
    *   **Content**:
        *   Icon: `Icons.Filled.AddCircle` (selected), `Icons.Outlined.AddCircleOutline` (unselected)
        *   Label: `Text("Create", style = typography.labelMedium)`

6.  **Name**: `NavigationBarItem` (Notifications)
    *   **Position & Size**: Fourth item in the `NavigationBar`.
    *   **Style**: Same as above.
    *   **Content**:
        *   Icon: `Icons.Filled.Notifications` (selected), `Icons.Outlined.NotificationsNone` (unselected)
        *   Label: `Text("Alerts", style = typography.labelMedium)`

7.  **Name**: `NavigationBarItem` (Profile)
    *   **Position & Size**: Fifth item in the `NavigationBar`.
    *   **Style**: Same as above.
    *   **Content**:
        *   Icon: `Icons.Filled.Person` (selected), `Icons.Outlined.PersonOutline` (unselected)
        *   Label: `Text("Profile", style = typography.labelMedium)`

### IV. Interaction & Behavior

*   **Interactions**:
    *   Tapping a `NavigationBarItem` changes the content displayed in the `Scaffold`'s body to the corresponding screen (`03a` to `03e`) and updates the `TopAppBar` title.
*   **Animations**:
    *   **Tab Transition**: `MaterialFadeThrough` animation is used when switching between tabs.
*   **Scroll Behavior**:
    *   The `TopAppBar` uses a `TopAppBarDefaults.enterAlwaysScrollBehavior()`. It hides on scroll down and reappears on scroll up.

---

## II. Screen Specifications: 03a_Feed_Tab

*   **Screen Name/ID**: `03a_Feed_Tab`
*   **Dimensions**: Fills the content area of the `03_Home_Screen` `Scaffold`.
*   **Background**: `md.sys.color.background`
*   **Layout**: `LazyColumn`
    *   `modifier`: `fillMaxSize`
    *   `contentPadding`: `PaddingValues(bottom = 80dp)` to avoid overlap with the `NavigationBar`.

### III. Component Specifications (for a single item in the list)

1.  **Name**: `Card` (Post)
    *   **Position & Size**:
        *   Size: `fillMaxWidth`
        *   Margin: `16dp` horizontal, `8dp` vertical.
    *   **Style**:
        *   Type: `ElevatedCard`
        *   Colors: `md.sys.color.surface`
        *   Elevation: `Elevation.Level1`

2.  **Name**: `ListItem` (Post Header)
    *   **Position & Size**: Top of the `Card`.
    *   **Style**: Standard `ListItem` colors.
    *   **Content**:
        *   **Leading Content**: `AsyncImage` (User Avatar), 40x40dp, `CircleShape`.
        *   **Headline Content**: `Text("Username", style = typography.titleMedium)`
        *   **Supporting Content**: `Text("2 hours ago", style = typography.bodySmall, color = md.sys.color.onSurfaceVariant)`
        *   **Trailing Content**: `IconButton` with `Icons.Filled.MoreVert` for post options.

3.  **Name**: `Text` (Post Body)
    *   **Position & Size**: Below the header.
        *   Padding: `16dp` horizontal, `12dp` vertical.
    *   **Style**:
        *   Color: `md.sys.color.onSurface`
        *   Typography: `bodyLarge`
    *   **Content**: "This is the text content of the user's post. It can be multiple lines long."

4.  **Name**: `AsyncImage` (Post Image)
    *   **Position & Size**: Below the post text.
        *   Size: `fillMaxWidth`, Height: `220dp`
    *   **Style**:
        *   `contentScale`: `ContentScale.Crop`
    *   **Content**: The image associated with the post. This component is optional and only shown if an image exists.

5.  **Name**: `Row` (Action Bar)
    *   **Position & Size**: Bottom of the `Card`.
        *   Size: `fillMaxWidth`
        *   Padding: `horizontal = 8dp`
    *   **Layout**: `Arrangement.SpaceAround`
    *   **Content**: Contains three `TextButton`s with icons.
        *   **Like Button**: `Icon(Icons.Outlined.ThumbUp)` and `Text("1.2k")`
        *   **Comment Button**: `Icon(Icons.Outlined.Comment)` and `Text("98")`
        *   **Share Button**: `Icon(Icons.Outlined.Share)` and `Text("Share")`

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Post Card**: On tap, navigates to `05_Post_Detail_Screen` with the post ID.
    *   **Like Button**: On tap, toggles the like state. The icon changes to `Icons.Filled.ThumbUp` and the color to `md.sys.color.primary`.
    *   **Comment Button**: On tap, navigates to `05_Post_Detail_Screen` and focuses the comment input field.
*   **Scroll Behavior**: The `LazyColumn` scrolls vertically. The `TopAppBar` of the parent `Scaffold` reacts to this scroll.

### V. Critical Scenarios & States

*   **Empty State**: If the feed is empty, the `LazyColumn` is replaced with a `Column` centered on the screen containing:
    *   An `Icon(Icons.Outlined.DynamicFeed, size = 64dp, tint = md.sys.color.onSurfaceVariant)`
    *   A `Text("Nothing to see here", style = typography.headlineSmall)`
    *   A `Text("Follow people to see their posts in your feed.", style = typography.bodyMedium, textAlign = TextAlign.Center)`
*   **Loading State**: A full-screen `CircularProgressIndicator` is shown initially. For pull-to-refresh, a `SwipeRefreshIndicator` is shown at the top.

---

## II. Screen Specifications: 03b_Search_Tab

*   **Screen Name/ID**: `03b_Search_Tab`
*   **Dimensions**: Fills the content area of the `03_Home_Screen` `Scaffold`.
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize`

### III. Component Specifications

1.  **Name**: `SearchBar`
    *   **Position & Size**:
        *   Docked to the `TopAppBar` or placed at the top of the content area.
        *   Size: `fillMaxWidth`
        *   Margin: `16dp`
    *   **Style**:
        *   Type: `SearchBar` (M3 component)
    *   **Content**:
        *   Placeholder Text: "Search users or posts"
        *   Leading Icon: `Icon(Icons.Filled.Search)`
        *   Trailing Icon: `IconButton` with `Icon(Icons.Filled.Mic)` for voice search.

2.  **Name**: `LazyVerticalGrid` (Search Results/Suggestions)
    *   **Position & Size**: Below the `SearchBar`.
        *   `modifier`: `fillMaxSize`
    *   **Layout**:
        *   `columns`: `GridCells.Fixed(2)`
        *   `contentPadding`: `PaddingValues(horizontal = 12dp, vertical = 16dp)`
    *   **Content**: Initially shows trending topics or suggested users. After a search, it's populated with result items (e.g., user profiles or post thumbnails).

### IV. Interaction & Behavior

*   **Interactions**:
    *   **SearchBar**: On tap, it expands into a full-screen search view. As the user types, search results are populated in real-time in the `LazyVerticalGrid`.
*   **Animations**:
    *   The transition between the docked `SearchBar` and the full-screen search view is animated using `MaterialFade`.

### V. Critical Scenarios & States

*   **Empty State**: Before a search is performed, this screen can show "Trending Topics" or "Suggested Users".
*   **No Results State**: After a search yields no results, the grid is replaced with a centered `Column` containing:
    *   `Icon(Icons.Outlined.SearchOff, size = 64dp)`
    *   `Text("No results found", style = typography.headlineSmall)`
    *   `Text("Try searching for something else.", style = typography.bodyMedium)`
*   **Loading State**: A `LinearProgressIndicator` is displayed directly below the `SearchBar` while a search is in progress.

---

## II. Screen Specifications: 03c_Create_Post_Tab

*   **Screen Name/ID**: `03c_Create_Post_Tab`
*   **Dimensions**: Fills the content area of the `03_Home_Screen` `Scaffold`.
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize`, `padding(16dp)`

### III. Component Specifications

1.  **Name**: `TextField` (Post Content)
    *   **Position & Size**:
        *   Size: `fillMaxWidth`, `minHeight = 200dp`
    *   **Style**:
        *   Type: `TextField` (borderless)
        *   Colors: `TextFieldDefaults.textFieldColors(containerColor = Color.Transparent)`
    *   **Content**:
        *   Placeholder: `Text("What's on your mind?")`
        *   Typography: `bodyLarge`

2.  **Name**: `Row` (Attachment Actions)
    *   **Position & Size**: Below the text field.
        *   Size: `fillMaxWidth`
    *   **Layout**: `Arrangement.Start`
    *   **Content**:
        *   `IconButton` with `Icon(Icons.Filled.Image)` for adding photos.
        *   `IconButton` with `Icon(Icons.Filled.Videocam)` for adding videos.
        *   `IconButton` with `Icon(Icons.Filled.Poll)` for creating a poll.

3.  **Name**: `FilledButton` (Post)
    *   **Position & Size**:
        *   Alignment: `End` of the `Column`.
        *   Margin (Top): `32dp`
    *   **Style**: Standard `FilledButton`.
    *   **Content**: `Text("Post")`

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Attachment Icons**: On tap, opens the corresponding system picker (e.g., photo gallery).
    *   **Post Button**: On tap, submits the post content. The button is disabled if the text field is empty.
*   **Animations**: N/A

### V. Critical Scenarios & States

*   **Error State**: If posting fails, a `Snackbar` appears with an error message (e.g., "Couldn't create post. Please try again.").
*   **Loading State**: When the "Post" button is tapped, it becomes disabled and shows a `CircularProgressIndicator` until the post is successfully uploaded.

---

## II. Screen Specifications: 03d_Notifications_Tab

*   **Screen Name/ID**: `03d_Notifications_Tab`
*   **Dimensions**: Fills the content area of the `03_Home_Screen` `Scaffold`.
*   **Background**: `md.sys.color.background`
*   **Layout**: `LazyColumn`
    *   `modifier`: `fillMaxSize`

### III. Component Specifications (for a single notification item)

1.  **Name**: `ListItem` (Notification)
    *   **Position & Size**: `fillMaxWidth`
    *   **Style**:
        *   `colors`: A notification that is "unread" can have a slightly different background color, e.g., `md.sys.color.primaryContainer.copy(alpha = 0.1f)`.
    *   **Content**:
        *   **Leading Content**: `AsyncImage` (Avatar of the user who caused the notification), 40x40dp, `CircleShape`.
        *   **Headline Content**: `Text("Username liked your post.", style = typography.bodyLarge)`
        *   **Supporting Content**: `Text("5 minutes ago", style = typography.bodyMedium, color = md.sys.color.onSurfaceVariant)`
        *   **Trailing Content**: Optional `AsyncImage` (thumbnail of the post related to the notification), 56x56dp, `RoundedCornerShape(8.dp)`.

### IV. Interaction & Behavior

*   **Interactions**:
    *   Tapping a `ListItem` navigates to the relevant content (e.g., the post that was liked, the user profile that followed you).
*   **Scroll Behavior**: Standard vertical scroll.

### V. Critical Scenarios & States

*   **Empty State**: If there are no notifications, the `LazyColumn` is replaced with a centered `Column` containing:
    *   `Icon(Icons.Outlined.NotificationsOff, size = 64dp)`
    *   `Text("No Notifications Yet", style = typography.headlineSmall)`
    *   `Text("Your notifications will appear here.", style = typography.bodyMedium)`
*   **Loading State**: A `SwipeRefreshIndicator` is used for refreshing the notification list.

---

## II. Screen Specifications: 03e_Profile_Tab

*   **Screen Name/ID**: `03e_Profile_Tab`
*   **Dimensions**: Fills the content area of the `03_Home_Screen` `Scaffold`.
*   **Background**: `md.sys.color.background`
*   **Layout**: `LazyColumn`
    *   `modifier`: `fillMaxSize`

### III. Component Specifications

1.  **Name**: `Column` (Profile Header)
    *   **Position & Size**: Top of the `LazyColumn`.
        *   `modifier`: `fillMaxWidth`, `padding(16dp)`
    *   **Layout**: `horizontalAlignment`: `CenterHorizontally`
    *   **Content**:
        *   `AsyncImage` (User's Profile Picture), 96x96dp, `CircleShape`, with a `1dp` border of `md.sys.color.primary`.
        *   `Text` (Full Name), `style = typography.headlineSmall`, `margin(top = 16dp)`.
        *   `Text` (@username), `style = typography.bodyMedium`, `color = md.sys.color.onSurfaceVariant`.
        *   `Row` (Stats), `margin(top = 16dp)`, `horizontalArrangement = Arrangement.SpaceEvenly`, `fillMaxWidth`. Contains three `Column`s for "Posts", "Followers", "Following" with numbers and labels.
        *   `FilledButton` ("Edit Profile"), `margin(top = 16dp)`.

2.  **Name**: `TabRow` (User Content)
    *   **Position & Size**: Below the header.
        *   `modifier`: `fillMaxWidth`
    *   **Content**:
        *   `Tab` 1: `Icon(Icons.Filled.GridOn)`, Text("Posts")
        *   `Tab` 2: `Icon(Icons.Filled.Bookmark)`, Text("Saved")

3.  **Name**: `LazyVerticalGrid` (User's Posts)
    *   **Position & Size**: Below the `TabRow`.
    *   **Layout**: `GridCells.Fixed(3)`.
    *   **Content**: A grid of `AsyncImage` thumbnails of the user's posts.

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Edit Profile Button**: On tap, navigates to `07_Edit_Profile_Screen`.
    *   **Settings Icon (in TopAppBar)**: On tap, navigates to `06_Settings_Screen`.
    *   **Tab**: On tap, switches the content in the grid below.
*   **Scroll Behavior**: The entire profile scrolls, with the header and `TabRow` scrolling off-screen.

### V. Critical Scenarios & States

*   **Empty State**: If the user has no posts, the grid area shows a message like "No posts yet."

---

## II. Screen Specifications: 04_Registration_Screen

*   **Screen Name/ID**: `04_Registration_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`
    *   `modifier`: `fillMaxSize`, `padding(horizontal = 24dp)`, `verticalScroll(rememberScrollState())`

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Style**: `SmallTopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.ArrowBack)`
        *   **Title**: `Text("Create Account")`

2.  **Name**: `OutlinedTextField` (Full Name)
    *   **Position & Size**: `fillMaxWidth`, `margin(top = 16dp)`
    *   **Content**: Label: "Full Name", Leading Icon: `Icons.Filled.Person`

3.  **Name**: `OutlinedTextField` (Email)
    *   **Position & Size**: `fillMaxWidth`, `margin(top = 16dp)`
    *   **Content**: Label: "Email", Leading Icon: `Icons.Filled.Email`

4.  **Name**: `OutlinedTextField` (Password)
    *   **Position & Size**: `fillMaxWidth`, `margin(top = 16dp)`
    *   **Content**: Label: "Password", Leading Icon: `Icons.Filled.Lock`, Trailing Icon for visibility toggle.

5.  **Name**: `OutlinedTextField` (Confirm Password)
    *   **Position & Size**: `fillMaxWidth`, `margin(top = 16dp)`
    *   **Content**: Label: "Confirm Password", Leading Icon: `Icons.Filled.Lock`

6.  **Name**: `FilledButton` (Sign Up)
    *   **Position & Size**: `fillMaxWidth`, Height: 52dp, `margin(top = 32dp)`
    *   **Content**: `Text("Sign Up")`

7.  **Name**: `TextButton` (Login)
    *   **Position & Size**: `CenterHorizontally`, `margin(top = 16dp)`
    *   **Content**: `Text("Already have an account? Login")`

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Back Arrow**: On tap, navigates back to `02_Login_Screen`.
    *   **Sign Up Button**: On tap, validates fields and creates an account. On success, navigates to `03_Home_Screen`.
    *   **Login TextButton**: On tap, navigates to `02_Login_Screen`.
*   **Animations**:
    *   **Screen Transition (Entry)**: `MaterialSharedAxis(X, forward = true)`
    *   **Screen Transition (Exit)**: `MaterialSharedAxis(X, forward = false)`

### V. Critical Scenarios & States

*   **Error State**: Text fields show errors for invalid data (e.g., "Passwords do not match"). A `Snackbar` is used for registration API errors.
*   **Loading State**: The "Sign Up" button shows a `CircularProgressIndicator` during the registration process.

---

## II. Screen Specifications: 05_Post_Detail_Screen

*   **Screen Name/ID**: `05_Post_Detail_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Scaffold` with a `LazyColumn` in the body.

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.ArrowBack)`
        *   **Title**: `Text("Post")`

2.  **Name**: `LazyColumn`
    *   **Content**:
        *   **Item 1**: The full post content, identical in structure to the `Card` on the `03a_Feed_Tab` screen, but without card elevation (flat).
        *   **Item 2**: `Divider` component.
        *   **Subsequent Items**: A list of `ListItem` components, each representing a comment. Each comment `ListItem` includes an avatar, username, and the comment text.

3.  **Name**: `OutlinedTextField` (Add Comment)
    *   **Position & Size**: Docked to the bottom of the screen, outside the `LazyColumn`.
        *   `modifier`: `fillMaxWidth`, `padding(8dp)`
    *   **Content**:
        *   Placeholder: `Text("Add a comment...")`
        *   Trailing Icon: `IconButton` with `Icon(Icons.Filled.Send)` to post the comment.

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Back Arrow**: Navigates back to `03a_Feed_Tab`.
    *   **Send Icon**: Posts the comment and adds it to the list above.
*   **Scroll Behavior**: The `LazyColumn` scrolls through the post and all comments. The comment input field remains fixed at the bottom.

### V. Critical Scenarios & States

*   **Empty State**: If there are no comments, a `Text("No comments yet.")` is shown below the `Divider`.
*   **Loading State**: A `CircularProgressIndicator` is shown while comments are being loaded.

---

## II. Screen Specifications: 06_Settings_Screen

*   **Screen Name/ID**: `06_Settings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.ArrowBack)`
        *   **Title**: `Text("Settings")`

2.  **Name**: `ListItem` (Edit Profile)
    *   **Position & Size**: `fillMaxWidth`
    *   **Content**:
        *   **Leading Content**: `Icon(Icons.Filled.AccountCircle)`
        *   **Headline Content**: `Text("Edit Profile")`
        *   **Trailing Content**: `Icon(Icons.Filled.ChevronRight)`

3.  **Name**: `ListItem` (Account Settings)
    *   **Position & Size**: `fillMaxWidth`
    *   **Content**:
        *   **Leading Content**: `Icon(Icons.Filled.Tune)`
        *   **Headline Content**: `Text("Account Settings")`
        *   **Trailing Content**: `Icon(Icons.Filled.ChevronRight)`

4.  **Name**: `ListItem` (Privacy Settings)
    *   **Position & Size**: `fillMaxWidth`
    *   **Content**:
        *   **Leading Content**: `Icon(Icons.Filled.Security)`
        *   **Headline Content**: `Text("Privacy Settings")`
        *   **Trailing Content**: `Icon(Icons.Filled.ChevronRight)`

5.  **Name**: `TextButton` (Logout)
    *   **Position & Size**: `fillMaxWidth`, `padding(16dp)`
    *   **Style**: `colors = ButtonDefaults.textButtonColors(contentColor = md.sys.color.error)`
    *   **Content**: `Text("Logout")`

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Back Arrow**: Navigates back to `03e_Profile_Tab`.
    *   **Edit Profile**: Navigates to `07_Edit_Profile_Screen`.
    *   **Account Settings**: Navigates to `08_Account_Settings_Screen`.
    *   **Privacy Settings**: Navigates to `09_Privacy_Settings_Screen`.
    *   **Logout**: Shows a confirmation `AlertDialog` and then logs the user out, navigating to `02_Login_Screen`.

---

## II. Screen Specifications: 07_Edit_Profile_Screen

*   **Screen Name/ID**: `07_Edit_Profile_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column` with vertical scrolling.

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.Close)`
        *   **Title**: `Text("Edit Profile")`
        *   **Actions**: `TextButton` with `Text("Save")`

2.  **Name**: `AsyncImage` (Profile Picture)
    *   **Position & Size**: Centered, 96x96dp, `CircleShape`, `margin(top = 16dp)`.
    *   **Overlay**: A semi-transparent overlay with an `Icon(Icons.Filled.Edit)` to indicate it's tappable.

3.  **Name**: `OutlinedTextField` (Full Name)
    *   **Position & Size**: `fillMaxWidth`, `padding(horizontal = 16dp, vertical = 8dp)`
    *   **Content**: Label: "Full Name"

4.  **Name**: `OutlinedTextField` (Username)
    *   **Position & Size**: `fillMaxWidth`, `padding(horizontal = 16dp, vertical = 8dp)`
    *   **Content**: Label: "Username"

5.  **Name**: `OutlinedTextField` (Bio)
    *   **Position & Size**: `fillMaxWidth`, `minHeight = 120dp`, `padding(horizontal = 16dp, vertical = 8dp)`
    *   **Content**: Label: "Bio"

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Close Icon**: Navigates back to `06_Settings_Screen` without saving.
    *   **Save Button**: Saves changes and navigates back.
    *   **Profile Picture**: Opens an image picker.

---

## II. Screen Specifications: 08_Account_Settings_Screen

*   **Screen Name/ID**: `08_Account_Settings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.ArrowBack)`
        *   **Title**: `Text("Account Settings")`

2.  **Name**: `ListItem` (Change Email)
    *   **Content**: Headline: "Email", Supporting Text: "user@example.com"

3.  **Name**: `ListItem` (Change Password)
    *   **Content**: Headline: "Change Password"

4.  **Name**: `ListItem` (Deactivate Account)
    *   **Style**: `headlineColor = md.sys.color.error`
    *   **Content**: Headline: "Deactivate Account"

### IV. Interaction & Behavior

*   **Interactions**: Each `ListItem` opens a new screen or `AlertDialog` to perform the respective action.

---

## II. Screen Specifications: 09_Privacy_Settings_Screen

*   **Screen Name/ID**: `09_Privacy_Settings_Screen`
*   **Dimensions**: 393x852dp
*   **Background**: `md.sys.color.background`
*   **Layout**: `Column`

### III. Component Specifications

1.  **Name**: `TopAppBar`
    *   **Content**:
        *   **Navigation Icon**: `IconButton` with `Icon(Icons.Filled.ArrowBack)`
        *   **Title**: `Text("Privacy Settings")`

2.  **Name**: `ListItem` (Private Account)
    *   **Content**:
        *   **Headline Content**: `Text("Private Account")`
        *   **Supporting Content**: `Text("When your account is private, only people you approve can see your photos and videos.")`
        *   **Trailing Content**: `Switch` component.

3.  **Name**: `ListItem` (Blocked Accounts)
    *   **Content**:
        *   **Headline Content**: `Text("Blocked Accounts")`
        *   **Trailing Content**: `Icon(Icons.Filled.ChevronRight)`

### IV. Interaction & Behavior

*   **Interactions**:
    *   **Switch**: Toggles the account's privacy status.
    *   **Blocked Accounts**: Navigates to a screen listing all blocked users.

---


============================================================
## APP 3: App_3
============================================================

🚀 Generating detailed design specs... (output will stream below)
================================================================================

```markdown
# Android Design Specification: "Zenith" Fitness App

## I. Global Specifications

### Platform
*   **Platform:** Android Mobile App
*   **Target SDK:** 34+
*   **Minimum SDK:** 26

### Design System
*   **System:** Material Design 3
*   **Theming:** Supports Light and Dark modes. Implements dynamic color (Material You) where available, falling back to the defined brand theme.
*   **Density:** Default screen density.

### Colors
*   **Seed Color:** #4CAF50 (Green)
*   **Light Theme Color Roles:**
    *   `md.sys.color.primary`: #386A20
    *   `md.sys.color.onPrimary`: #FFFFFF
    *   `md.sys.color.primaryContainer`: #B7F397
    *   `md.sys.color.onPrimaryContainer`: #042100
    *   `md.sys.color.secondary`: #55624C
    *   `md.sys.color.onSecondary`: #FFFFFF
    *   `md.sys.color.secondaryContainer`: #D9E7CA
    *   `md.sys.color.onSecondaryContainer`: #131F0D
    *   `md.sys.color.tertiary`: #386666
    *   `md.sys.color.onTertiary`: #FFFFFF
    *   `md.sys.color.tertiaryContainer`: #BBEBEB
    *   `md.sys.color.onTertiaryContainer`: #002020
    *   `md.sys.color.error`: #BA1A1A
    *   `md.sys.color.onError`: #FFFFFF
    *   `md.sys.color.background`: #FCFDF7
    *   `md.sys.color.onBackground`: #1A1C18
    *   `md.sys.color.surface`: #FCFDF7
    *   `md.sys.color.onSurface`: #1A1C18
    *   `md.sys.color.surfaceVariant`: #DFE4D7
    *   `md.sys.color.onSurfaceVariant`: #43483F
    *   `md.sys.color.outline`: #73796E
*   **Dark Theme Color Roles:**
    *   `md.sys.color.primary`: #9CD67D
    *   `md.sys.color.onPrimary`: #0A3900
    *   `md.sys.color.primaryContainer`: #1F5207
    *   `md.sys.color.onPrimaryContainer`: #B7F397
    *   `md.sys.color.secondary`: #BDCBAF
    *   `md.sys.color.onSecondary`: #283420
    *   `md.sys.color.secondaryContainer`: #3E4A35
    *   `md.sys.color.onSecondaryContainer`: #D9E7CA
    *   `md.sys.color.tertiary`: #A0CFCF
    *   `md.sys.color.onTertiary`: #003737
    *   `md.sys.color.tertiaryContainer`: #1E4E4E
    *   `md.sys.color.onTertiaryContainer`: #BBEBEB
    *   `md.sys.color.error`: #FFB4AB
    *   `md.sys.color.onError`: #690005
    *   `md.sys.color.background`: #1A1C18
    *   `md.sys.color.onBackground`: #E2E3DC
    *   `md.sys.color.surface`: #1A1C18
    *   `md.sys.color.onSurface`: #E2E3DC
    *   `md.sys.color.surfaceVariant`: #43483F
    *   `md.sys.color.onSurfaceVariant`: #C3C8BC
    *   `md.sys.color.outline`: #8D9387

### Typography
*   **Font Family:** Roboto
*   **Type Scale (Material 3):**
    *   `md.sys.typography.displayLarge`
    *   `md.sys.typography.displayMedium`
    *   `md.sys.typography.displaySmall`
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

### Spacing
*   **Base Grid Unit:** 8dp
*   **Standard Margins:** 16dp
*   **Standard Padding:** 16dp
*   **Minimum Touch Target:** 48dp x 48dp

### Accessibility
*   **Target Standard:** WCAG 2.1 Level AA
*   **Requirements:** All interactive elements must have content descriptions. Color contrast ratios must meet or exceed WCAG AA standards. Font sizes should be scalable with system settings.

---

## II. Screen Specifications: 01_Splash_Screen

*   **Screen Name/ID:** `01_Splash_Screen`
*   **Dimensions:** 393x852dp (Typical mobile viewport)
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Column` layout, vertically and horizontally centered.

### III. Component Specifications

#### Component: App Logo
*   **Name:** `Image`
*   **Position & Size:**
    *   Alignment: Centered in the parent `Column`.
    *   Size: 120dp x 120dp.
*   **Style:**
    *   Iconography: A stylized green leaf intertwined with a dumbbell shape.
    *   Tint: `md.sys.color.primary`
*   **Content:** Vector asset for the "Zenith" app logo.

#### Component: App Name Text
*   **Name:** `Text`
*   **Position & Size:**
    *   Alignment: Centered horizontally.
    *   Margin: 16dp top margin from the App Logo.
*   **Style:**
    *   Typography: `md.sys.typography.displaySmall`
    *   Color: `md.sys.color.primary`
*   **Content:** "Zenith"

#### Component: Loading Indicator
*   **Name:** `CircularProgressIndicator`
*   **Position & Size:**
    *   Alignment: Centered horizontally.
    *   Margin: 48dp top margin from the App Name Text.
    *   Size: 48dp x 48dp.
*   **Style:**
    *   Color: `md.sys.color.primary`
    *   Stroke Width: 4dp.
*   **Content:** N/A

### IV. Interaction & Behavior

*   **States:** This screen is transient; no user interaction is possible.
*   **Interactions:** On screen load, a background process (e.g., checking authentication state, loading initial config) runs for 2-3 seconds.
    *   On completion (user not logged in) -> Navigate to `02_Onboarding_Welcome_Screen`.
    *   On completion (user already logged in) -> Navigate to `05_Home_Screen`.
*   **Animations:**
    *   Screen Transition (In): None (it's the first screen).
    *   Screen Transition (Out): Fade out (500ms).

---

## II. Screen Specifications: 02_Onboarding_Welcome_Screen

*   **Screen Name/ID:** `02_Onboarding_Welcome_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Column` layout with vertical arrangement space-between, filling the max size. Padding of 16dp on all sides.

### III. Component Specifications

#### Component: Welcome Image
*   **Name:** `Image`
*   **Position & Size:**
    *   Alignment: Top center of the screen.
    *   Size: `fillMaxWidth`, height 300dp.
    *   Margin: 24dp top margin.
*   **Style:**
    *   Content Scale: `Crop`.
    *   Shape: Rounded corners (16dp).
*   **Content:** A vibrant, high-quality stock photo of diverse people enjoying fitness activities outdoors.

#### Component: Headline Text
*   **Name:** `Text`
*   **Position & Size:**
    *   Alignment: Centered horizontally.
    *   Margin: 32dp top margin from the Welcome Image.
*   **Style:**
    *   Typography: `md.sys.typography.headlineLarge`
    *   Color: `md.sys.color.onSurface`
    *   Text Alignment: Center.
*   **Content:** "Welcome to Zenith"

#### Component: Body Text
*   **Name:** `Text`
*   **Position & Size:**
    *   Alignment: Centered horizontally.
    *   Margin: 16dp top margin from the Headline Text.
*   **Style:**
    *   Typography: `md.sys.typography.bodyLarge`
    *   Color: `md.sys.color.onSurfaceVariant`
    *   Text Alignment: Center.
*   **Content:** "Your personal journey to peak fitness starts now. Let's achieve your goals together."

#### Component: Get Started Button
*   **Name:** `FilledButton`
*   **Position & Size:**
    *   Alignment: Bottom center of the screen.
    *   Size: `fillMaxWidth`, height 56dp.
    *   Margin: 16dp bottom margin.
*   **Style:**
    *   Container Color: `md.sys.color.primary`
    *   Content Color: `md.sys.color.onPrimary`
    *   Typography: `md.sys.typography.labelLarge`
    *   Shape: `ShapeDefaults.Full` (Pill shape).
*   **Content:** "GET STARTED"

#### Component: Login Text Button
*   **Name:** `TextButton`
*   **Position & Size:**
    *   Alignment: Bottom center of the screen.
    *   Size: `wrapContentSize`, minimum touch target 48dp x 48dp.
    *   Margin: 8dp bottom margin from the Get Started Button.
*   **Style:**
    *   Content Color: `md.sys.color.primary`
    *   Typography: `md.sys.typography.labelLarge`
*   **Content:** "I ALREADY HAVE AN ACCOUNT"

### IV. Interaction & Behavior

*   **States:**
    *   `Get Started Button`: Default, Pressed (uses `md.sys.color.primary` with a `0.12` opacity `md.sys.color.onPrimary` state layer).
    *   `Login Text Button`: Default, Pressed (uses `md.sys.color.primary` with a `0.12` opacity `md.sys.color.primary` state layer).
*   **Interactions:**
    *   `Get Started Button` On tap -> Navigate to `03_Sign_Up_Screen`.
    *   `Login Text Button` On tap -> Navigate to `04_Login_Screen`.
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialSharedAxis` (Z-axis).

---

## II. Screen Specifications: 03_Sign_Up_Screen

*   **Screen Name/ID:** `03_Sign_Up_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Column` layout, scrollable. Padding of 16dp on left and right.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
    *   Elevation: 0dp (no shadow).
*   **Content:**
    *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        *   Tint: `md.sys.color.onSurface`
    *   **Title:** `Text` element.
        *   Typography: `md.sys.typography.titleLarge`
        *   Color: `md.sys.color.onSurface`
        *   Content: "Create Account"

#### Component: Email Address Field
*   **Name:** `OutlinedTextField`
*   **Position & Size:**
    *   Alignment: Top of the column, below the app bar.
    *   Size: `fillMaxWidth`, height `wrapContent`.
    *   Margin: 24dp top margin.
*   **Style:**
    *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors`.
    *   Typography: `md.sys.typography.bodyLarge`
    *   Shape: `ShapeDefaults.Medium`.
*   **Content:**
    *   `label`: "Email Address"
    *   `leadingIcon`: `Icons.Filled.Email`
    *   `keyboardOptions`: `KeyboardType.Email`

#### Component: Password Field
*   **Name:** `OutlinedTextField`
*   **Position & Size:**
    *   Alignment: Below Email field.
    *   Size: `fillMaxWidth`, height `wrapContent`.
    *   Margin: 16dp top margin.
*   **Style:**
    *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors`.
    *   Typography: `md.sys.typography.bodyLarge`
    *   Shape: `ShapeDefaults.Medium`.
    *   `visualTransformation`: `PasswordVisualTransformation`.
*   **Content:**
    *   `label`: "Password"
    *   `leadingIcon`: `Icons.Filled.Lock`
    *   `trailingIcon`: `IconButton` to toggle password visibility (`Icons.Filled.Visibility` / `Icons.Filled.VisibilityOff`).
    *   `keyboardOptions`: `KeyboardType.Password`.
    *   `supportingText`: "Must be at least 8 characters."

#### Component: Confirm Password Field
*   **Name:** `OutlinedTextField`
*   **Position & Size:**
    *   Alignment: Below Password field.
    *   Size: `fillMaxWidth`, height `wrapContent`.
    *   Margin: 16dp top margin.
*   **Style:**
    *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors`.
    *   Typography: `md.sys.typography.bodyLarge`
    *   Shape: `ShapeDefaults.Medium`.
    *   `visualTransformation`: `PasswordVisualTransformation`.
*   **Content:**
    *   `label`: "Confirm Password"
    *   `leadingIcon`: `Icons.Filled.Lock`
    *   `keyboardOptions`: `KeyboardType.Password`.

#### Component: Sign Up Button
*   **Name:** `FilledButton`
*   **Position & Size:**
    *   Alignment: Below Confirm Password field.
    *   Size: `fillMaxWidth`, height 56dp.
    *   Margin: 32dp top margin.
*   **Style:**
    *   Container Color: `md.sys.color.primary`
    *   Content Color: `md.sys.color.onPrimary`
    *   Typography: `md.sys.typography.labelLarge`
    *   Shape: `ShapeDefaults.Full`.
*   **Content:** "SIGN UP"

### IV. Interaction & Behavior

*   **States:**
    *   `TextFields`: Default, Focused (label moves up, border and label color change to `md.sys.color.primary`), Error (border and label color change to `md.sys.color.error`, supporting error text appears).
    *   `Sign Up Button`: Enabled (default), Disabled (container color `md.sys.color.onSurface` with `0.12` opacity, content color `md.sys.color.onSurface` with `0.38` opacity). Disabled until all fields are valid.
*   **Interactions:**
    *   `Navigation Icon` On tap -> Navigate back to `02_Onboarding_Welcome_Screen`.
    *   `Sign Up Button` On tap:
        1.  Validate fields (email format, password length, passwords match).
        2.  If invalid, show error states on relevant fields.
        3.  If valid, show a `CircularProgressIndicator` inside the button, disable it, and initiate sign-up API call.
        4.  On success -> Navigate to `05_Home_Screen`.
        5.  On failure -> Show an error `Snackbar`.
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialSharedAxis` (X-axis).

---

## II. Screen Specifications: 04_Login_Screen

*   **Screen Name/ID:** `04_Login_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.surface`
*   **Layout:** `Column` layout. Padding of 16dp on left and right.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
    *   Elevation: 0dp.
*   **Content:**
    *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
        *   Tint: `md.sys.color.onSurface`
    *   **Title:** `Text` element.
        *   Typography: `md.sys.typography.titleLarge`
        *   Color: `md.sys.color.onSurface`
        *   Content: "Welcome Back"

#### Component: Email Address Field
*   **Name:** `OutlinedTextField`
*   **Position & Size:**
    *   Alignment: Top of the column, below the app bar.
    *   Size: `fillMaxWidth`, height `wrapContent`.
    *   Margin: 24dp top margin.
*   **Style:**
    *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors`.
    *   Typography: `md.sys.typography.bodyLarge`
*   **Content:**
    *   `label`: "Email Address"
    *   `leadingIcon`: `Icons.Filled.Email`
    *   `keyboardOptions`: `KeyboardType.Email`

#### Component: Password Field
*   **Name:** `OutlinedTextField`
*   **Position & Size:**
    *   Alignment: Below Email field.
    *   Size: `fillMaxWidth`, height `wrapContent`.
    *   Margin: 16dp top margin.
*   **Style:**
    *   Colors: Standard `TextFieldDefaults.outlinedTextFieldColors`.
    *   Typography: `md.sys.typography.bodyLarge`
    *   `visualTransformation`: `PasswordVisualTransformation`.
*   **Content:**
    *   `label`: "Password"
    *   `leadingIcon`: `Icons.Filled.Lock`
    *   `trailingIcon`: `IconButton` to toggle password visibility.
    *   `keyboardOptions`: `KeyboardType.Password`.

#### Component: Login Button
*   **Name:** `FilledButton`
*   **Position & Size:**
    *   Alignment: Below Password field.
    *   Size: `fillMaxWidth`, height 56dp.
    *   Margin: 32dp top margin.
*   **Style:**
    *   Container Color: `md.sys.color.primary`
    *   Content Color: `md.sys.color.onPrimary`
    *   Typography: `md.sys.typography.labelLarge`
    *   Shape: `ShapeDefaults.Full`.
*   **Content:** "LOG IN"

### IV. Interaction & Behavior

*   **States:**
    *   `TextFields`: Default, Focused, Error.
    *   `Login Button`: Enabled (default), Disabled (if fields are empty).
*   **Interactions:**
    *   `Navigation Icon` On tap -> Navigate back to `02_Onboarding_Welcome_Screen`.
    *   `Login Button` On tap:
        1.  Validate fields are not empty.
        2.  If invalid, show error states.
        3.  If valid, show loading state and initiate login API call.
        4.  On success -> Navigate to `05_Home_Screen`.
        5.  On failure -> Show error `Snackbar` with message "Invalid email or password."
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialSharedAxis` (X-axis).

---

## II. Screen Specifications: 05_Home_Screen

*   **Screen Name/ID:** `05_Home_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar`, `LazyColumn` for content, and a `BottomAppBar`.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
    *   `scrollBehavior`: `TopAppBarDefaults.enterAlwaysScrollBehavior()` (collapses on scroll down, reappears on scroll up).
*   **Content:**
    *   **Title:** `Text` element.
        *   Typography: `md.sys.typography.titleLarge`
        *   Color: `md.sys.color.onSurface`
        *   Content: "Dashboard"
    *   **Actions:** `IconButton` with `Icons.Filled.Notifications`.
        *   Tint: `md.sys.color.onSurfaceVariant`

#### Component: Main Content Area
*   **Name:** `LazyColumn`
*   **Position & Size:**
    *   Fills the space between the `TopAppBar` and `BottomAppBar`.
    *   Padding: 16dp horizontal, 8dp vertical.
*   **Style:** N/A
*   **Content:** A list of cards representing different sections.
    *   **Item 1: "Today's Workout" Card:** `ElevatedCard` with a title, description, and a "Start Workout" button.
    *   **Item 2: "Progress Summary" Card:** `FilledCard` with charts or stats (e.g., "Calories Burned", "Active Minutes").
    *   **Item 3: "Challenges" Card:** `OutlinedCard` showing active community challenges.

#### Component: Bottom Navigation Bar
*   **Name:** `NavigationBar`
*   **Position & Size:**
    *   Alignment: Bottom of the screen.
    *   Size: `fillMaxWidth`, height 80dp.
*   **Style:**
    *   Container Color: `md.sys.color.surfaceVariant`
*   **Content:**
    *   **Item 1:** `NavigationBarItem`
        *   `icon`: `Icons.Filled.Home`
        *   `label`: "Home"
        *   `selected`: true
    *   **Item 2:** `NavigationBarItem`
        *   `icon`: `Icons.Outlined.List`
        *   `label`: "Workouts"
        *   `selected`: false
    *   **Item 3:** `NavigationBarItem`
        *   `icon`: `Icons.Outlined.BarChart`
        *   `label`: "Progress"
        *   `selected`: false
    *   **Item 4:** `NavigationBarItem`
        *   `icon`: `Icons.Outlined.AccountCircle`
        *   `label`: "Profile"
        *   `selected`: false

### IV. Interaction & Behavior

*   **States:**
    *   `NavigationBarItem`: Selected (icon becomes filled, colors change to `md.sys.color.onSecondaryContainer` and `md.sys.color.secondaryContainer`), Unselected (default).
*   **Interactions:**
    *   `Notifications Icon` On tap -> Navigate to `06_Notifications_Screen`.
    *   `"Start Workout" Button` On tap -> Navigate to `07_Workout_Detail_Screen`.
    *   `"Workouts" Nav Item` On tap -> Navigate to `08_Workout_List_Screen`.
    *   `"Profile" Nav Item` On tap -> Navigate to `09_Profile_Screen`.
*   **Animations:**
    *   Screen transitions via Bottom Nav: `Fade` through transition.
*   **Scroll Behavior:** The `TopAppBar` collapses as the user scrolls the `LazyColumn` down.

---

## II. Screen Specifications: 06_Notifications_Screen

*   **Screen Name/ID:** `06_Notifications_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar` and a `LazyColumn`.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
*   **Content:**
    *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Title:** `Text` with content "Notifications".

#### Component: Notification List
*   **Name:** `LazyColumn`
*   **Position & Size:**
    *   Fills the remaining screen space.
*   **Style:** N/A
*   **Content:** A list of `ListItem` components.
    *   **Each `ListItem`:**
        *   `leadingContent`: `Icon` (e.g., `Icons.Filled.CheckCircle` for completed goals, `Icons.Filled.Campaign` for announcements).
        *   `headlineText`: `Text` with the notification title (e.g., "Goal Achieved!").
        *   `supportingText`: `Text` with the notification body (e.g., "You completed your 10,000 steps goal.").
        *   `trailingContent`: `Text` with the timestamp (e.g., "2h ago").
        *   `modifier`: `clickable`.

### IV. Interaction & Behavior

*   **States:**
    *   `ListItem`: Default, Pressed (ripple effect).
*   **Interactions:**
    *   `Navigation Icon` On tap -> Navigate back to `05_Home_Screen`.
    *   `ListItem` On tap -> Navigate to a relevant screen (e.g., a challenge screen, a workout summary).
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialSharedAxis` (X-axis).

### V. Critical Scenarios & States

*   **Empty State:** If there are no notifications, the `LazyColumn` is replaced with a `Column` containing:
    *   An `Icon` (`Icons.Outlined.NotificationsOff`), size 96dp, color `md.sys.color.surfaceVariant`.
    *   A `Text` element ("No notifications yet"), typography `md.sys.typography.titleMedium`, color `md.sys.color.onSurfaceVariant`.
    *   A `Text` element ("We'll let you know when something important happens."), typography `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.

---

## II. Screen Specifications: 07_Workout_Detail_Screen

*   **Screen Name/ID:** `07_Workout_Detail_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a collapsing `TopAppBar` and a `LazyColumn`.

### III. Component Specifications

#### Component: Collapsing Top App Bar
*   **Name:** `LargeTopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, expanded height ~256dp, collapsed height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
    *   `scrollBehavior`: `TopAppBarDefaults.exitUntilCollapsedScrollBehavior()`.
    *   The background of the app bar is a high-quality image of the workout.
*   **Content:**
    *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Title (Collapsed):** `Text` with content "Full Body Burn".
    *   **Title (Expanded):** `Text` with content "Full Body Burn", placed at the bottom of the expanded app bar. Typography `md.sys.typography.headlineMedium`.

#### Component: Workout Details List
*   **Name:** `LazyColumn`
*   **Position & Size:**
    *   Fills the remaining screen space.
    *   Padding: 16dp horizontal.
*   **Content:**
    *   **Item 1: Stats Row:** A `Row` with `Icon` and `Text` for Duration (e.g., "35 min"), Difficulty ("Intermediate"), and Equipment ("Dumbbells").
    *   **Item 2: Description:** A `Text` element with a detailed description of the workout.
    *   **Item 3: Exercises Header:** A `Text` element with content "Exercises".
    *   **Item 4...N: Exercise `ListItem`s:** A list of exercises, each with a thumbnail, name, and rep/time count (e.g., "Push-ups: 3 sets of 12").

#### Component: Start Workout FAB
*   **Name:** `ExtendedFloatingActionButton`
*   **Position & Size:**
    *   Alignment: `BottomEnd` of the `Scaffold`.
    *   Margin: 16dp.
*   **Style:**
    *   Container Color: `md.sys.color.primary`
    *   Content Color: `md.sys.color.onPrimary`
*   **Content:**
    *   `icon`: `Icons.Filled.PlayArrow`
    *   `text`: "START"

### IV. Interaction & Behavior

*   **Interactions:**
    *   `Navigation Icon` On tap -> Navigate back to `05_Home_Screen`.
    *   `Start Workout FAB` On tap -> Navigate to the active workout player screen (not specified in flow).
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialContainerTransform`.
*   **Scroll Behavior:** The `LargeTopAppBar` collapses into a standard `TopAppBar` as the user scrolls down. The `ExtendedFloatingActionButton` shrinks to a regular `FloatingActionButton` on scroll.

---

## II. Screen Specifications: 08_Workout_List_Screen

*   **Screen Name/ID:** `08_Workout_List_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar`, `LazyColumn`, and `BottomAppBar`.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
*   **Content:**
    *   **Title:** `Text` with content "Workouts".
    *   **Actions:** `IconButton` with `Icons.Filled.FilterList`.

#### Component: Workout List
*   **Name:** `LazyColumn`
*   **Position & Size:**
    *   Fills the space between app bars.
    *   Padding: 16dp horizontal.
*   **Content:** A list of `Card` components.
    *   **Each `Card`:**
        *   Contains an `Image` (workout thumbnail).
        *   A `Column` with a `Text` title ("Morning Yoga"), and a `Text` subtitle ("15 min | Beginner").
        *   `modifier`: `clickable`.

#### Component: Bottom Navigation Bar
*   **Name:** `NavigationBar`
*   **Position & Size:**
    *   Alignment: Bottom of the screen.
    *   Size: `fillMaxWidth`, height 80dp.
*   **Style:**
    *   Container Color: `md.sys.color.surfaceVariant`
*   **Content:**
    *   `NavigationBarItem` for "Home" (selected: false).
    *   `NavigationBarItem` for "Workouts" (selected: true).
    *   `NavigationBarItem` for "Progress" (selected: false).
    *   `NavigationBarItem` for "Profile" (selected: false).

### IV. Interaction & Behavior

*   **Interactions:**
    *   `FilterList Icon` On tap -> Opens a `ModalBottomSheet` with filter options (e.g., by duration, difficulty).
    *   `Workout Card` On tap -> Navigate to `07_Workout_Detail_Screen` for the selected workout.
    *   `Bottom Nav Items` -> Navigate to their respective screens.
*   **Animations:**
    *   Screen transitions via Bottom Nav: `Fade` through transition.

---

## II. Screen Specifications: 09_Profile_Screen

*   **Screen Name/ID:** `09_Profile_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar`, `LazyColumn`, and `BottomAppBar`.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
*   **Content:**
    *   **Title:** `Text` with content "Profile".
    *   **Actions:** `IconButton` with `Icons.Filled.Settings`.

#### Component: Profile Header
*   **Name:** `Column`
*   **Position & Size:**
    *   Top of the `LazyColumn`.
    *   Padding: 32dp vertical.
*   **Content:**
    *   `Image` (Profile Picture): 96dp x 96dp, `CircleShape`.
    *   `Text` (User Name): "Alex Doe", typography `md.sys.typography.headlineSmall`.
    *   `Text` (Join Date): "Joined Jan 2024", typography `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.

#### Component: Settings List
*   **Name:** `LazyColumn` (content starts after the header)
*   **Position & Size:** Fills the screen.
*   **Content:**
    *   `ListItem` with `leadingContent`=`Icons.Filled.AccountCircle`, `headlineText`="Account Details".
    *   `ListItem` with `leadingContent`=`Icons.Filled.Shield`, `headlineText`="Privacy & Security".
    *   `ListItem` with `leadingContent`=`Icons.Filled.HelpOutline`, `headlineText`="Help & Support".
    *   `Divider` component.
    *   `ListItem` with `headlineText`="Log Out", `headlineColor`=`md.sys.color.error`.

#### Component: Bottom Navigation Bar
*   **Name:** `NavigationBar`
*   **Position & Size:**
    *   Alignment: Bottom of the screen.
    *   Size: `fillMaxWidth`, height 80dp.
*   **Content:**
    *   `NavigationBarItem` for "Home" (selected: false).
    *   `NavigationBarItem` for "Workouts" (selected: false).
    *   `NavigationBarItem` for "Progress" (selected: false).
    *   `NavigationBarItem` for "Profile" (selected: true).

### IV. Interaction & Behavior

*   **Interactions:**
    *   `Settings Icon` On tap -> Navigate to `10_Settings_Screen`.
    *   `"Account Details" ListItem` On tap -> Navigate to a dedicated account details screen.
    *   `"Log Out" ListItem` On tap -> Show a confirmation `AlertDialog`. On confirm, log the user out and navigate to `02_Onboarding_Welcome_Screen`.
    *   `Bottom Nav Items` -> Navigate to their respective screens.
*   **Animations:**
    *   Screen transitions via Bottom Nav: `Fade` through transition.

---

## II. Screen Specifications: 10_Settings_Screen

*   **Screen Name/ID:** `10_Settings_Screen`
*   **Dimensions:** 393x852dp
*   **Background:** `md.sys.color.background`
*   **Layout:** `Scaffold` with a `TopAppBar` and `LazyColumn`.

### III. Component Specifications

#### Component: Top App Bar
*   **Name:** `TopAppBar`
*   **Position & Size:**
    *   Alignment: Top of the screen.
    *   Size: `fillMaxWidth`, height 64dp.
*   **Style:**
    *   Container Color: `md.sys.color.surface`
*   **Content:**
    *   **Navigation Icon:** `IconButton` with `Icons.Filled.ArrowBack`.
    *   **Title:** `Text` with content "Settings".

#### Component: Settings List
*   **Name:** `LazyColumn`
*   **Position & Size:** Fills the screen.
*   **Content:**
    *   **Category 1: "Theme"**
        *   `ListItem` with `headlineText`="Dark Mode", `trailingContent`= a `Switch` component.
    *   **Category 2: "Notifications"**
        *   `ListItem` with `headlineText`="Push Notifications", `supportingText`="Workout reminders, goal updates", `trailingContent`= a `Switch`.
        *   `ListItem` with `headlineText`="Email Notifications", `trailingContent`= a `Switch`.
    *   **Category 3: "About"**
        *   `ListItem` with `headlineText`="Version", `supportingText`="1.0.0".
        *   `ListItem` with `headlineText`="Terms of Service".
        *   `ListItem` with `headlineText`="Privacy Policy".

### IV. Interaction & Behavior

*   **Interactions:**
    *   `Navigation Icon` On tap -> Navigate back to `09_Profile_Screen`.
    *   `Switch` components On toggle -> Update the corresponding app setting. The Dark Mode switch should immediately change the app's theme.
    *   `"Terms of Service"` On tap -> Open a web view or browser with the ToS URL.
*   **Animations:**
    *   Screen Transition (In/Out): `MaterialSharedAxis` (X-axis).

---

## V. Critical Scenarios & States (Global)

### Error States
*   **No Internet Connection:**
    *   **UI:** A `Snackbar` appears at the bottom of the screen.
    *   **Style:** Container color `md.sys.color.errorContainer`, content color `md.sys.color.onErrorContainer`.
    *   **Content:** "No internet connection. Please check your network."
    *   **Action:** Optional "Retry" button.
*   **API/Server Error:**
    *   **UI:** A `Snackbar` appears.
    *   **Content:** "Something went wrong. Please try again later."

### Empty States
*   **Generic Empty State:** Used on list screens (e.g., Workouts, Notifications) when no data is available.
    *   **Layout:** Centered `Column`.
    *   **Components:**
        *   `Icon`: A relevant outlined icon (e.g., `Icons.Outlined.ListAlt`), size 96dp, color `md.sys.color.surfaceVariant`.
        *   `Text` (Title): e.g., "No Workouts Found", typography `md.sys.typography.titleMedium`, color `md.sys.color.onSurfaceVariant`.
        *   `Text` (Body): e.g., "Try adjusting your filters or check back later.", typography `md.sys.typography.bodyMedium`, color `md.sys.color.onSurfaceVariant`.
        *   `Button` (Optional CTA): e.g., "Clear Filters".

### Loading States
*   **Initial Screen Load:**
    *   **UI:** A centered `CircularProgressIndicator` is displayed over the screen content area.
*   **Pull-to-Refresh:**
    *   **UI:** Standard `pullRefresh` indicator at the top of a scrollable list.
*   **Button Loading:**
    *   **UI:** The button becomes disabled, and its text label is replaced by a `CircularProgressIndicator` (size 24dp). The button's width is maintained.
```

---
