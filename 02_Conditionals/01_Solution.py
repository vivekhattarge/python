password = "VivekP@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weakk"
elif len(password) <= 10:
    strength = "Mediumm"
else:
    strength = "Strongg"

print("Password strength is: ", strength)