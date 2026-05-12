Professional GitHub README
Password Audit & Hash Cracking Project
Overview

This project simulates a post-breach password security audit in which leaked password hashes are analyzed and cracked using offensive security tools and custom Python scripts.

The objective was to demonstrate:

Password hash generation
Dictionary-based password cracking
Rule-based password attacks
NTLM credential auditing
Password policy analysis
Security reporting and remediation recommendations
Technologies & Tools Used
Kali Linux
Python 3
Hashcat
John the Ripper
Git & GitHub
RockYou Wordlist
Custom Password Wordlists
Hash Types Audited
MD5
SHA1
SHA256
NTLM
Project Structure
password-audit-project/
├── README.md
├── hashes/
├── results/
├── scripts/
├── report/
├── screenshots/
└── wordlists/
Features
Simulated Breach Environment

Generated realistic employee password datasets and converted them into:

MD5 hashes
SHA1 hashes
SHA256 hashes
NTLM hashes
Password Cracking Attacks

Performed:

Dictionary attacks
Custom wordlist attacks
Rule-based attacks
NTLM cracking
John the Ripper password recovery
Password Policy Auditing

Developed Python scripts to:

Analyze cracked password statistics
Identify weak password patterns
Check password policy compliance
Professional Security Reporting

Produced a full password audit report including:

Risk analysis
Findings
Attack methodology
Security recommendations
Key Findings
75% of passwords were cracked successfully
Weak passwords were recovered within seconds
Seasonal password patterns were vulnerable to rule-based attacks
NTLM hashes were susceptible to dictionary attacks
Strong passwords resisted cracking attempts
Security Recommendations
Replace MD5/SHA1 with bcrypt or Argon2
Enforce minimum 12-character passwords
Require MFA
Block common passwords
Implement password rotation policies
Conduct periodic password audits
Screenshots Included
Hash generation
Hashcat cracking sessions
NTLM attacks
Rule-based attacks
John the Ripper output
Analysis scripts
Final security report
Educational Purpose

This project was created strictly for:

cybersecurity learning
password auditing practice
penetration testing education
defensive security awareness

No real credentials or systems were targeted.

Author

Surjeet Singh Gill
