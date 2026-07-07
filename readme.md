# Vrit Technologies QA Automation Task

## Overview

This project is an end-to-end Selenium automation framework developed as part of the Vrit Technologies QA Internship Task.

The automation covers the complete registration workflow of the Authorized Partner Portal, including:

- Home Page
- Terms & Conditions
- Account Registration
- Agency Details
- Professional Experience
- Verification & Preferences
- Document Upload

Since the application uses email-based OTP verification, the OTP step is completed manually. Once the OTP is verified, the automation resumes automatically.

---

## Tech Stack

- Python 3.14
- Selenium WebDriver
- Pytest
- webdriver-manager
- Google Chrome
- ChromeDriver

---

## Project Structure

```
vrit-qa-intern-task/
│
├── main.py
├── signup.py
├── agency.py
├── experience.py
├── verification.py
├── conftest.py
├── test_data.py
├── requirements.txt
├── README.md
└── sample.pdf
```

---

## Features

### Automated

- Launch Chrome Browser
- Navigate to Website
- Click Get Started
- Accept Terms & Conditions
- Fill Registration Form
- Fill Agency Details
- Fill Professional Experience
- Fill Verification & Preferences
- Upload Required Documents
- Submit Registration

### Manual

- Email OTP Verification

Automation pauses until the user enters the OTP and clicks **Verify Code**, after which execution continues automatically.

---

## Test Flow

```
Open Website
        │
        ▼
Get Started
        │
        ▼
Accept Terms
        │
        ▼
Fill Account Details
        │
        ▼
Click Next
        │
        ▼
Manual OTP Verification
        │
        ▼
Agency Details
        │
        ▼
Professional Experience
        │
        ▼
Verification & Preferences
        │
        ▼
Upload Documents
        │
        ▼
Submit Registration
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/vrit-qa-intern-task.git
```

Go to the project

```bash
cd vrit-qa-intern-task
```

Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate virtual environment

PowerShell

```bash
.venv\Scripts\Activate.ps1
```

Command Prompt

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

```
selenium
pytest
webdriver-manager
```

or simply

```bash
pip install -r requirements.txt
```

---

## Configuration

Update **test_data.py**

Example

```python
FIRST_NAME = "John"
LAST_NAME = "Doe"

EMAIL = "example@gmail.com"

PHONE = "9812345678"

PASSWORD = "Password@123"

AGENCY_NAME = "ABC Consultancy"

ROLE = "Director"

AGENCY_EMAIL = "agency@gmail.com"

WEBSITE = "https://abc.com"

ADDRESS = "Kathmandu"

REGION = "Nepal"

YEARS = "2 Years"

STUDENTS = "250"

FOCUS_AREA = "Canada"

SUCCESS_RATE = "95%"

REGISTRATION_NUMBER = "123456"

PREFERRED_COUNTRIES = [
    "Australia",
    "Canada"
]

INSTITUTION_TYPES = [
    "Universities",
    "Colleges"
]

CERTIFICATION = "ICEF Certified"

DOCUMENT = r"D:\Documents\sample.pdf"
```

---

## Running the Test

Run using pytest

```bash
pytest main.py -v -s
```

or

```bash
pytest -v -s
```

---

## Assertions

The automation validates that the registration flow progresses through each page successfully.

Additional assertions can be added based on application success messages or page redirects.

---

## Framework Design

The framework follows a modular Page-Based approach.

### signup.py

Handles

- Home page
- Terms
- Registration Form
- OTP Wait

---

### agency.py

Handles

- Agency Information
- Region Selection

---

### experience.py

Handles

- Professional Experience
- Services Offered

---

### verification.py

Handles

- Registration Number
- Preferred Countries
- Institution Types
- Certification Details
- Document Upload
- Final Submission

---

### test_data.py

Stores all configurable test data separately from the automation logic.

---

### conftest.py

Contains the reusable WebDriver fixture used across the project.

---

## Known Limitation

The application requires email-based OTP verification.

Since the OTP is dynamically generated and sent to the registered email address, this step cannot be fully automated without backend/API access.

The automation pauses for manual OTP entry and resumes automatically after verification.

---

## Future Improvements

- Page Object Model (POM)
- Logging
- HTML Reports
- Screenshots on Failure
- Cross-browser Testing
- Parallel Test Execution
- CI/CD Integration (GitHub Actions)
- Data-driven Testing

---

## Author

**Aaditya Bhandari**

QA Automation Internship Task

Vrit Technologies