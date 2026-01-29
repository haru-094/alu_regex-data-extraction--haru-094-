import re


# Define the Regular expression pattern that will used with sample
regex_email_pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}"
regex_credit_pattern = r"\b[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?\b"
regex_phone_pattern = r"(?:\+\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"
regex_URL_pattern = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)"
                    

# using try/except to open the file sample
try:
    with open("sample.txt", "r") as regex_sample:
        sample = regex_sample.read()
except FileNotFoundError:
    print("There is error: sample.txt file not found")



