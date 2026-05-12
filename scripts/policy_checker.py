#!/usr/bin/env python3
import re

def check_password_strength(password):
    score = 0
    issues = []

    if len(password) >= 12:
        score += 1
    else:
        issues.append("Too short (min 12 chars)")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        issues.append("No uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        issues.append("No lowercase letter")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        issues.append("No number")

    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        issues.append("No special character")

    common = ["password", "123456", "qwerty", "letmein", "welcome", "monkey"]

    if any(c in password.lower() for c in common):
        issues.append("Contains common pattern")
        score -= 1

    if score <= 1:
        strength = "CRITICAL"
    elif score == 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return strength, issues

passwords = {
    "alice": "password123",
    "bob": "123456",
    "charlie": "welcome1",
    "diana": "qwerty",
    "eve": "letmein",
    "frank": "monkey123",
    "grace": "password1",
    "henry": "abc123",
    "ivan": "Summer2024",
    "julia": "Dragon@99",
    "kevin": "Laptop#01",
    "laura": "March2024!",
    "mike": "X#9kL@mP2!qR",
    "nina": "Tr0ub4dor&3",
    "oscar": "correct-horse-battery",
    "paula": "G7$mK#nQ2@pL9"
}

print("=" * 60)
print("PASSWORD POLICY COMPLIANCE CHECK")
print("=" * 60)

for user, pwd in passwords.items():
    strength, issues = check_password_strength(pwd)

    print(f"\n{user}: {strength}")

    if issues:
        for issue in issues:
            print(f"  - {issue}")
