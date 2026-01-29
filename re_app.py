import re


# Define the Regular expression pattern that will used with sample
regex_email_pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}"
regex_credit_pattern = r"\b[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?[0-9]{4}[-\s]?\b"
regex_phone_pattern = r"(?:\+\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"
regex_url_pattern = r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)"
regex_security_pattern = r"<script.*?>.*?</script>|javascript:"


# Using try/except to open the file sample
try:
    with open("sample.txt", "r") as regex_sample:
        sample = regex_sample.read()
except FileNotFoundError:
    print("There is error: sample.txt file not found")

# Security check of harm input
if sample:
    security_harm = []
    if re.search(regex_security_pattern, sample, re.IGNORECASE):
        security_harm.append("security warnings, detected harm input")


# encrypt the credit card number to [xxxx] & email
def encrypt_card(credit_num):
    try:
        number = re.sub(r"[-\s]", "", credit_num)
        if len(number) >= 4:
            return f"XXXX-XXXX-XXXX-{number[-4:]}"
        else:
            return f"XXXX-XXXX-XXXX-XXXX"
    except ValueError:
        return f"XXXX-XXXX-XXXX-XXXX"


def encrypt_email(email_input):
    try:
        user, domain = email_input.split("@")
        if len(user) > 1:
            user_encrypted = user[0] + "*" * (len(user) - 1)
        else:
            user_encrypted = "*"

        return f"{user_encrypted}@{domain}"
    except ValueError:
        return email_input


# Using re library to check the sample with pattern
phone_checker = re.findall(regex_phone_pattern, sample)
url_checker = re.findall(regex_url_pattern, sample)

email_checker = re.findall(regex_email_pattern, sample)
new_email = [encrypt_email(e) for e in email_checker]
print(new_email)
credit_checker = re.findall(regex_credit_pattern, sample)
new_credit = [encrypt_card(c) for c in credit_checker]
print(new_credit)

# Add the output to file
# with open("sample_output.txt", "w") as regex_output:
#     if not email_checker:
#         regex_output.write("email not found in the sample")
#     else:
#         regex_output.write(str(email_checker))

#     if not phone_checker:
#         regex_output.write("phone not found in the sample")
#     else:
#         regex_output.write(str(phone_checker))

#     if not credit_checker:
#         regex_output.write("credit not found in the sample")
#     else:
#         regex_output.write(str(credit_checker))

#     if not url_checker:
#         regex_output.write("url not found in the sample")
#     else:
#         regex_output.write(str(url_checker))
