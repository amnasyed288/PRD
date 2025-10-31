Budgetly's "Flow Capture" aims to be the effortless entry point for all user spending data, ensuring accuracy and minimal user intervention. It combines diverse automatic capture methods with flexible manual inputs, centralizing and cleaning transaction data for downstream financial analysis tools (Flow Map, Flow Lens). The core value is to free users from manual data entry burden while providing a reliable and trusted financial ledger.

---

### 1. Core Product Vision

*   **Problem Solved:** Users struggle with the effort and time required to manually track and categorize their spending across various sources (bank, cash, receipts, online purchases). This leads to incomplete or inaccurate financial overviews.
*   **Target Users:** Mobile application users who want to effortlessly log all their financial transactions and need clean, de-duplicated, and categorized data for personal finance management.
*   **Unique Value Proposition:**
    *   **Effortless Ingestion:** Automatically captures spending from diverse sources (SMS, email, bank, gallery, chat) and offers intuitive manual inputs (form, voice, file uploads, widget, QR).
    *   **Data Integrity:** Guarantees clean, de-duplicated, and accurately categorized transactions.
    *   **Trustworthy Data:** Provides a reliable foundation for deeper financial analysis and visualization tools (Flow Map, Flow Lens).
    *   **Privacy-First:** Prioritizes on-device parsing and granular user consent for data sources.

---

### 2. Key Features & Functionality

This section lists all in-scope features, highlighting those critical for the MVP and design.

**A. Manual Capture (User-Initiated)**
*   **A1. Classic Form Entry (Legacy):**
    *   **Functionality:** Structured form to add expense (Description/Merchant, Amount, Category, Source, Date/Time, Notes, Attachments).
    *   **Requirements:**
        *   Defaults to current date/time, last used source, and last used category for the merchant.
        *   "Save" button disabled until required fields are filled (e.g., Amount).
        *   Optimistic UI updates immediately upon submission.
        *   Confirms submission with a toast/snackbar showing "₹1,250 • Groceries logged" and an "Undo" action.
    *   **Entry Points:** "+ Add" Floating Action Button (FAB), Home screen widget, "Add Manually" option within Review Inbox.
*   **A2. Voice / Natural-Language (NL) Entry:**
    *   **Functionality:** Allows speaking or typing free text (e.g., "Spent ₹500 on petrol yesterday 8pm") for parsing.
    *   **Requirements:**
        *   System reads back interpretation.
        *   Provides "Edit" and "Confirm" options.
        *   Low confidence parsing (<85) displays a "yellow state" and "Edit details" button.
        *   "Edit" opens a mini-form pre-filled with parsed values.
        *   "Confirm" creates transaction with "Undo" available.
    *   **Entry Points:** Tap microphone icon or type in a "Quick Add" input.
*   **A3. Attach & Parse (Manual Receipt Photo/PDF/CSV):**
    *   **Functionality:** Manually selects a file/photo for local OCR/CSV parsing.
    *   **Requirements:**
        *   Displays a field-mapped preview (for images/PDFs) or a table preview with checkboxes (for CSV/PDF statements).
        *   Allows confirmation or fixing of parsed data.
        *   Dedup fingerprints generated per row; obvious duplicates are pre-unchecked.
        *   "Possible duplicate" flag for matched rows.
        *   Supports creating multiple transactions from one file (e.g., CSV rows).
        *   **Privacy note:** Explicit file/photo selection, no broad gallery permission needed for this flow.
    *   **Entry Points:** "Attach & Parse" button/option.
*   **A4. Home-Screen Widget Quick Add:**
    *   **Functionality:** Quick expense entry directly from the device home screen.
    *   **Requirements:**
        *   Minimal UI: Primarily Amount and Category input (≤3 taps to log).
        *   Logs with current time and location (if enabled).
        *   Suggests merchant from inferred location context.
        *   Gracefully handles denied location permission (logs without inference).
*   **A5. QR/Barcode Scan:**
    *   **Functionality:** Scans merchant QR or receipt barcode to auto-fill transaction details.
    *   **Requirements:**
        *   Opens camera for scanning.
        *   If supported, pre-fills merchant and amount; otherwise, falls back to OCR/manual entry.
        *   Shows a preview before confirmation.

**B. Automatic Capture (System-Initiated)**
*   **B1. Bank Sync (Open Banking / Aggregator):**
    *   **Functionality:** Connects to bank accounts for automatic, scheduled transaction import.
    *   **Requirements:**
        *   One-time OAuth connect flow.
        *   New transactions appear within the next cycle (≤4 hours).
        *   Handles pending → posted reconciliation.
        *   Deduplication engine collapses transactions from multiple sources (e.g., SMS & bank sync).
    *   **UX Consideration:** Clear "Connect Bank" UI and OAuth integration.
*   **B2. SMS Parser:**
    *   **Functionality:** On-device listener parses bank/card SMS for transaction details.
    *   **Requirements:**
        *   Requests SMS permission with clear scope explanation.
        *   Logs high-confidence transactions immediately (<3s).
        *   Low-confidence items go to Review Inbox.
        *   Ignores non-transactional SMS (OTP, marketing).
*   **B3. Email Ingest (Receipts & Statements):**
    *   **Functionality:** Connects to Gmail/IMAP to parse e-receipts and monthly statements.
    *   **Requirements:**
        *   "Connect Email" UI.
        *   First-time senders/statements require a "Preview import" screen for field mapping confirmation.
        *   Subsequent runs can auto-apply learned mappings.
        *   Deduplication flags/skips duplicate rows against existing ledger.
*   **B4. Gallery OCR (Auto):**
    *   **Functionality:** Scans device's /Screenshots and /Camera folders for new receipt images.
    *   **Requirements:**
        *   Requires explicit Gallery scan permission toggle.
        *   Scans occur nightly (on charge + Wi-Fi).
        *   Auto-posts transactions if confidence ≥85.
        *   Low-confidence (<85) items go to Review Inbox.
        *   New merchants require one-time confirmation.
*   **B5. Chat Share Hook (WhatsApp/Telegram):**
    *   **Functionality:** Integrates with OS share sheet to allow sharing messages/screenshots from chat apps to Budgetly for parsing.
    *   **Requirements:**
        *   Extracts amount/merchant.
        *   Flags potential IOUs (e.g., based on keywords like "you owe").
        *   Creates a candidate expense for user confirmation.
*   **B6. Smart Templates (Auto-suggest):**
    *   **Functionality:** Learns from repeated manual input phrases to offer one-tap suggestion chips.
    *   **Requirements:**
        *   Suggestion chips appear contextually (same time/location) after 3+ occurrences.
        *   Chips decay and stop showing if ignored 3 times.

**C. Quality, Safety, and Recovery (Cross-Cutting)**
*   **C1. Deduplication Engine:**
    *   **Functionality:** Ensures only one transaction is logged when the same spend is captured via multiple channels (e.g., SMS and Bank Sync).
    *   **Requirements:** Merges sources and attachments, keeps earliest `occurred_at`.
*   **C2. Review Inbox:**
    *   **Functionality:** A dedicated queue for low-confidence (<85) or ambiguous items.
    *   **Requirements:**
        *   "Inbox badge" displays count of pending items.
        *   Card-list UI: swipe Left to Fix (edit), swipe Right to Confirm, tap for details, long-press to Delete.
        *   "Inbox Zero" state/reward upon completion.
*   **C3. Undo & Edit Everywhere:**
    *   **Functionality:** Provides immediate reversal and later modification of transactions.
    *   **Requirements:**
        *   "Undo" action available within a 5-second window after *any* transaction creation (manual or auto).
        *   "Undo" triggers a soft-delete or "void" flag.
        *   "Edit" option available from transaction detail screen, with changes propagating to Flow Map/Lens.
*   **C4. Offline & Error Handling:**
    *   **Functionality:** Allows manual entries/shares to work offline, queuing data for later sync.
    *   **Requirements:**
        *   Displays "Pending sync" status for queued items.
        *   Informs user when connectivity returns and syncs.
        *   Parse failures offer a "Fix manually" path, preventing data loss.
        *   Never loses user-entered data.

**Priority/Critical Features for MVP (implicitly high priority based on purpose & KPIs):**
*   All manual capture methods (A1-A5)
*   Bank Sync (B1) & SMS Parser (B2)
*   Review Inbox (C2)
*   Deduplication Engine (C1)
*   Undo & Edit (C3)
*   Offline & Error Handling (C4)
*   Permissions UX (implied by granular controls and consent requirements)

---

### 3. User Flows & Journeys

**Primary User Tasks & Goals:**
*   Log expenses with minimal effort.
*   Ensure all spending is captured accurately.
*   Correct or confirm low-confidence transactions quickly.
*   Maintain control over personal data and permissions.
*   Have a clean, de-duplicated financial ledger.

**Key User Scenarios:**

*   **Manual Form Entry:**
    1.  User taps FAB or widget "+ Add".
    2.  User fills out form fields (Amount, Category, Merchant, etc.).
    3.  User taps "Save" (disabled if required fields are missing).
    4.  Transaction appears in ledger; "Undo" snackbar shows for 5s.
    5.  (Offline scenario) User adds offline, sees "Will sync when online" message.
*   **Voice/NL Entry:**
    1.  User taps microphone/types into Quick Add.
    2.  User speaks/types natural language (e.g., "Spent 2000 groceries at Naheed").
    3.  System proposes parsed transaction details (amount, category, merchant) on a confirmation card.
    4.  User can "Confirm" or "Edit details" (opens mini-form).
    5.  On confirm, transaction is created; "Undo" is available.
*   **Attach & Parse (Receipt Photo):**
    1.  User taps "Add" → "Attach & Parse" and selects a receipt photo.
    2.  App processes (OCR) and shows a candidate expense with merchant/date/amount.
    3.  User confirms or edits the parsed details.
*   **Bank Sync:**
    1.  User initiates "Connect Bank" flow.
    2.  User completes OAuth process.
    3.  New bank transactions automatically appear in the ledger (and potentially Review Inbox if low confidence).
*   **SMS Auto-Capture:**
    1.  User grants SMS permission.
    2.  Bank/card payment SMS arrives.
    3.  Transaction is automatically logged (or sent to Review Inbox if ambiguous).
*   **Review Inbox Resolution:**
    1.  User notices Inbox badge with pending count.
    2.  User taps Inbox.
    3.  User sees a list of low-confidence items (cards).
    4.  User swipes card Left to "Fix" (edit form) or Right to "Confirm."
    5.  Upon resolving all, "Inbox Zero" state is displayed.
*   **Undo Action:**
    1.  After any transaction creation, an "Undo" snackbar/toast appears for 5 seconds.
    2.  User taps "Undo" within the window.
    3.  The transaction is soft-deleted/voided and disappears.

**Expected User Interactions:**
*   Form input, dropdowns, date pickers.
*   Voice input activation and visual feedback for speech-to-text.
*   Confirmation cards with clear "Confirm" and "Edit" actions.
*   File/photo picker interaction.
*   Camera activation for QR/barcode scanning.
*   System permissions prompts (SMS, Gallery, Location).
*   OAuth flows for bank/email connection.
*   Swipe gestures for Review Inbox.
*   Snackbars/toasts for confirmations and "Undo."
*   Badge notifications for pending items (e.g., Review Inbox).
*   Suggestion chips for quick entry.

---

### 4. Technical Requirements (Relevant to UX)

*   **Platform Specifications:** Mobile application (iOS and Android implied by "home-screen widget," "OS share sheet," "gallery/camera folders"). No specific OS versions mentioned.
*   **Integration Requirements:**
    *   **Bank Sync:** OAuth integration (Open Banking / Aggregators).
    *   **Email:** Gmail/IMAP connect.
    *   **Chat Share:** OS-level share sheet integration.
    *   **APIs:**
        *   `/transactions.create`: For manual and parsed submissions.
        *   `/transactions.quickCreate`: For widget submissions.
        *   `/nlp/parse`: For Voice/NL processing.
        *   `/attachments.parse`: For manual receipt/file parsing.
        *   `/review/confirm`, `/review/fix`: For Review Inbox actions.
        *   Webhooks/connectors for automatic bank/email/SMS inputs.
*   **Performance Requirements (Latency):**
    *   Manual form to ledger visibility: ≤ 1 second (optimistic UI).
    *   SMS parse to ledger visibility: ≤ 3 seconds.
    *   Voice/NL parse to proposal display: ≤ 2 seconds.
    *   Single image OCR to candidate expense: ≤ 8 seconds.
    *   Email e-receipt parse to transaction: ≤ 60 seconds.
    *   General auto-capture ingest to ledger visibility: ≤ 3 seconds.
    *   Manual entry with OCR ingest to ledger visibility: ≤ 10 seconds.
*   **Security & Privacy:**
    *   TLS 1.3 for data in transit; AES-256 at rest.
    *   **User Control:** Granular and reversible toggles for all automatic capture sources (SMS, Email, Gallery, Bank, Location).
    *   **Data Handling:** On-device parsing preferred. Only structured fields synced; raw artifacts pruned after 30 days unless "pinned" (implies a UI to pin attachments).
    *   No capture without explicit consent.

---

### 5. Design Requirements

*   **Branding Guidelines/Constraints:**
    *   No specific brand guidelines provided, but the product name "Budgetly" implies a focus on personal finance management.
    *   Confirmation toast messages use "₹1,250 • Groceries logged" format.
*   **Accessibility Requirements:** Not explicitly detailed beyond standard application practices, but clear navigation, visible states, and intuitive interactions are implied by the focus on "minimum effort."
*   **Specific UI/UX Patterns Mentioned:**
    *   **Form Design:** Structured forms with sensible default values, clear validation (e.g., "Save" disabled).
    *   **Confirmation UI:** Toast/snackbar messages with an "Undo" action (5-second window).
    *   **Voice/NL Input:** Dedicated microphone icon, visual display of parsed interpretation, "Confirm"/"Edit" action buttons. "Yellow state" for low confidence.
    *   **Preview Screens:** Field-mapped preview for image/PDF parsing; table with checkboxes for CSV/PDF statements; candidate expense for chat share.
    *   **Widget Design:** Minimalist home-screen widget for quick entry (Amount, Category).
    *   **Camera UI:** Full-screen camera view for QR/barcode scanning with clear instructions/feedback.
    *   **Permissions UX:** Progressive, granular, and reversible prompts with benefit explainers.
    *   **Review Inbox:** Card-list UI with prominent "Fix"/"Confirm" actions (swipe gestures). Inbox badge with count. "Inbox Zero" state.
    *   **Suggestion Chips:** Contextual, one-tap chips for Smart Templates.
    *   **Error States:** Clear messaging for offline status ("Pending sync") and parse failures ("Fix manually").
    *   **Transaction Display:** Needs to clearly show fields like `amount`, `currency`, `occurred_at`, `merchant_name`, `category`, `source_channel` (potentially via icon), `notes`, `attachments`, `confidence` (visual cue if low), and `status` (CONFIRMED|REVIEW|VOID).

---

### 6. Business Rules & Logic

*   **Transaction Confidence Thresholds:**
    *   Confidence ≥ 85: Auto-posts to ledger.
    *   Confidence 70-84: Requires Review (sent to Review Inbox).
    *   Confidence < 70: Requires confirmation UI (explicit user action).
    *   Ambiguity or missing fields also send to Review Inbox.
*   **Deduplication Logic:**
    *   Fingerprint: SHA-1 of (rounded_timestamp ± 2h, abs_amount, normalized_merchant) + channel hints.
    *   If match found within ±48h and amount delta within tolerance, merge sources, keep earliest `occurred_at`.
    *   Identifies "possible duplicate" for user review (e.g., during CSV import).
*   **Undo Logic:**
    *   Available for 5 seconds after any creation event.
    *   Triggers soft-delete (or "void" flag if source immutable).
*   **Offline Handling:** Manual entries are queued and synced once connectivity returns, preserving timestamps.
*   **Permissions & Consent:**
    *   Granular toggles for SMS, Email, Gallery, Bank, Location.
    *   All permissions are reversible.
    *   No automatic capture runs without explicit user consent.
*