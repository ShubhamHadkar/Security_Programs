import re
import math


# Common weak passwords
COMMON_PASSWORDS = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "welcome",
    "password123"
]


# Function to calculate entropy
def calculate_entropy(password):

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"[0-9]", password):
        charset_size += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32

    entropy = len(password) * math.log2(charset_size) if charset_size else 0

    return round(entropy, 2)


# Function to check password strength
def check_password_strength(password):

    feedback = []

    # Length Check
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Check
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if not re.search(r"[0-9]", password):
        feedback.append("Add at least one number.")

    # Special Character Check
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Add at least one special character.")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is very common and insecure.")

    # Repeated Character Check
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeated characters like aaa or 111.")

    # Entropy Calculation
    entropy = calculate_entropy(password)

    # Strength Classification
    if entropy < 40:
        strength = "Weak"

    elif entropy < 70:
        strength = "Moderate"

    else:
        strength = "Strong"

    return strength, entropy, feedback


# Main Program
print("======================================")
print("   INDUSTRY LEVEL PASSWORD CHECKER")
print("======================================")

password = input("Enter your password: ")

strength, entropy, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

print("Password Entropy:", entropy)

if feedback:

    print("\nSecurity Suggestions:")

    for suggestion in feedback:
        print("-", suggestion)

else:
    print("\nExcellent! Your password is highly secure.")
