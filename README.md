# ALU Regex Data Extraction

## Project Overview

This project is a Python-based tool designed to extract, validate, and secure structured data from raw, messy text inputs. It simulates a real-world scenario where a Junior Frontend Developer must process large volumes of unstructured data (such as server logs or raw API responses).

The program identifies specific data entities (Emails, Phone Numbers, Credit Cards, and URLs) while implementing strict security measures to protect sensitive Personally Identifiable Information (PII) and detect potentially malicious input.

## Features

- **Robust Pattern Matching:** Accurately extracts data even with realistic variations (e.g., different phone number formats, subdomains, sub-paths).
- **Security & Privacy:**
  - **PII Masking:** Automatically masks sensitive parts of Credit Card numbers (`XXXX-XXXX-XXXX-1234`) and Emails (`j***@example.com`) before outputting them.
  - **Hostile Input Detection:** Scans for and flags potential injection attacks (e.g., `<script>` tags).
- **Error Handling:** Gracefully handles missing input files without crashing.
- **Formatted Output:** Generates a clean, readable text report distinguishing between found data and security alerts.

## Getting Started

### Prerequisites

- Python 3.x installed.
- A text file named `sample.txt` containing the raw input data.

### Installation & Usage

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YourUsername/alu_regex-data-extraction.git](https://github.com/YourUsername/alu_regex-data-extraction.git)
    cd alu_regex-data-extraction
    ```

2.  **Prepare Input Data:**
    Ensure `sample.txt` exists in the root directory. You can add your own raw text or use the provided sample.

3.  **Run the Script:**

    ```bash
    python main.py
    ```

4.  **View Results:**
    The script will generate a report in `sample_output.txt`.

## Regular Expression Logic

The core of this project relies on four robust Regex patterns:

### 1. Email Addresses

`r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}"`

- **Logic:** Matches standard usernames (allowing dots/underscores), followed by `@`, a domain name, and a valid extension of at least 2 letters (e.g., `.com`, `.io`).

### 2. Phone Numbers

`r"(?:\+\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"`

- **Logic:** Handles complex real-world formats including:
  - Optional Country Codes: `+1`, `+254`
  - Parentheses: `(555)`
  - Separators: Dots `.` or Dashes `-`

### 3. Credit Card Numbers

`r"\b[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}\b"`

- **Logic:** Identifies 16-digit numbers grouped in fours. It accepts both space-separated (`1234 5678...`) and dash-separated (`1234-5678...`) formats.

### 4. URLs

`r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)"`

- **Logic:** Captures `http` or `https` links. It is designed to be flexible enough to catch subdomains (`api.google.com`) and file paths (`/images/logo.png`).

## Security Measures

### PII Protection (Masking)

To comply with data privacy standards, raw sensitive data is never written to the logs.

- **Credit Cards:** Converted to `XXXX-XXXX-XXXX-1234`.
- **Emails:** Converted to `u***@domain.com`.

### Threat Detection

The system scans for common injection patterns using:
`r"<script.*?>.*?</script>|javascript:"`
If found, a **SECURITY ALERT** is logged in the output file, warning administrators of potential XSS (Cross-Site Scripting) attempts in the input data.
