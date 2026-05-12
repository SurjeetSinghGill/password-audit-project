#!/usr/bin/env python3
import hashlib
import os

# Simulated employee passwords
passwords = {
    # Weak passwords
    "alice": "password123",
    "bob": "123456",
    "charlie": "welcome1",
    "diana": "qwerty",
    "eve": "letmein",
    "frank": "monkey123",
    "grace": "password1",
    "henry": "abc123",

    # Medium passwords
    "ivan": "Summer2024",
    "julia": "Dragon@99",
    "kevin": "Laptop#01",
    "laura": "March2024!",

    # Strong passwords
    "mike": "X#9kL@mP2!qR",
    "nina": "Tr0ub4dor&3",
    "oscar": "correct-horse-battery",
    "paula": "G7$mK#nQ2@pL9"
}

output_dir = "../hashes"
os.makedirs(output_dir, exist_ok=True)

md5_file = open(f"{output_dir}/md5_hashes.txt", "w")
sha1_file = open(f"{output_dir}/sha1_hashes.txt", "w")
sha256_file = open(f"{output_dir}/sha256_hashes.txt", "w")
ntlm_file = open(f"{output_dir}/ntlm_hashes.txt", "w")

for username, password in passwords.items():
    pwd_bytes = password.encode('utf-8')

    md5 = hashlib.md5(pwd_bytes).hexdigest()
    sha1 = hashlib.sha1(pwd_bytes).hexdigest()
    sha256 = hashlib.sha256(pwd_bytes).hexdigest()

    # NTLM = MD4 of UTF-16LE password
    ntlm = hashlib.new('md4', password.encode('utf-16-le')).hexdigest()

    md5_file.write(f"{username}:{md5}\n")
    sha1_file.write(f"{username}:{sha1}\n")
    sha256_file.write(f"{username}:{sha256}\n")
    ntlm_file.write(f"{username}:{ntlm}\n")

    print(f"[+] Generated hashes for {username}:{password}")

md5_file.close()
sha1_file.close()
sha256_file.close()
ntlm_file.close()

print("\n[+] All hashes saved inside /hashes/")
