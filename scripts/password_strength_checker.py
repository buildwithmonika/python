import re

def password_checker(password):
    errors = []
    password_type = ''

    if not password:
        return False, ["Password is empty."], "Invalid"
    if not re.search(r'[a-z]', password):
        errors.append("Missing one lowercase character.")
    if not re.search(r'[A-Z]', password):
        errors.append("Missing one uppercase character.")
    if not re.search(r'\d', password):
        errors.append("Missing one digit.")
    if not re.search(r'[!@#$%^&*()_+\-]', password):  
        errors.append("Missing one special character.")
    if len(password) < 8: 
        errors.append("Password should be at least 8 characters.")

    # Determine password strength
    if len(errors) == 0:
        password_type = "Strong password."
    elif len(errors) <= 2:
        password_type = "Medium password."
    else:
        password_type = "Weak password."

    return len(errors) == 0, errors, password_type

# Main execution
password = input("Please enter password: ")
is_valid, errors, password_type = password_checker(password)

print("Password strength:", password_type)

if errors:
    print("Issues found:")
    for err in errors:
        print("-", err)
else:
    print("Your password meets all requirements!")
