import re
import string


def password_strength(password):
    score = 0
    feedback = []
    
    # Commonly used password
    common_passwords = ["password", "123456", "qwerty", "admin", "welcome"]
    if password.lower() in common_passwords:
        return "Very Weak", ["This is a very common password. Please choose something unique."]

    # length of password
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
    if re.search(r"\d", password): 
        score += 1
    else:
        feedback.append("Add at least one number.")


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


try:
    user_password = input("Enter password to check : ").strip()
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