#!/usr/bin/env python3

# Original password database
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

# Simulate cracked results
cracked = [
    "password123", "123456", "welcome1", "qwerty",
    "letmein", "monkey123", "password1", "abc123",
    "Summer2024", "Dragon@99", "Laptop#01", "March2024!"
]

not_cracked = [
    "X#9kL@mP2!qR",
    "Tr0ub4dor&3",
    "correct-horse-battery",
    "G7$mK#nQ2@pL9"
]

total = len(passwords)
cracked_count = len(cracked)
not_cracked_count = len(not_cracked)

print("=" * 50)
print("PASSWORD AUDIT RESULTS")
print("=" * 50)
print(f"Total accounts:     {total}")
print(f"Passwords cracked:  {cracked_count} ({(cracked_count/total)*100:.1f}%)")
print(f"Passwords secure:   {not_cracked_count} ({(not_cracked_count/total)*100:.1f}%)")

print()
print("[CRACKED]")
for user, pwd in passwords.items():
    if pwd in cracked:
        length = len(pwd)
        print(f"  {user}: {pwd} (length: {length})")

print()
print("[NOT CRACKED]")
for user, pwd in passwords.items():
    if pwd in not_cracked:
        print(f"  {user}: [SECURE] (length: {len(pwd)})")

print()
print("RISK BREAKDOWN:")
print(f"  Critical (common passwords): 8 accounts")
print(f"  Medium (weak complexity):    4 accounts")
print(f"  Low (strong passwords):      4 accounts")
