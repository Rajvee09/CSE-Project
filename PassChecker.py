import re
import string
import getpass  # Library to hide password input

def password_strength(password):
    score = 0
    feedback = []
    
    # 0. Preliminary Check: Common Weak Passwords
    common_passwords = ["password", "123456", "qwerty", "admin", "welcome"]
    if password.lower() in common_passwords:
        return "Very Weak", ["This is a very common password. Please choose something unique."]

    # 1. Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    # 2. Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # 3. Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # 4. Number
    if re.search(r"\d", password): # \d is a regex shortcut for [0-9]
        score += 1
    else:
        feedback.append("Add at least one number.")

    # 5. Special character
    # Using string.punctuation covers all standard symbols (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character (e.g., !, @, #, $).")

    # Final rating logic
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

# --- Main Execution ---

print("--- Password Strength Checker ---")

# Try to use getpass to hide input, fallback to input() if running in an IDE that doesn't support it
try:
    user_password = getpass.getpass("Enter password to check (hidden): ").strip()
except:
    user_password = input("Enter password to check: ").strip()

if not user_password:
    print("Error: You did not enter a password.")
else:
    strength, feedback = password_strength(user_password)
    
    print(f"\nPassword Strength: {strength}")
    
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")
    else:
        print(" Your password looks good!")