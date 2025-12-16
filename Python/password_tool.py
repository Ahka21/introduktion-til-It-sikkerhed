import argparse
import hashlib
import os
import re
from datetime import datetime

def check_password(pw: str) -> list[str]:
    errors = []
    if len(pw) < 12:
        errors.append("Password skal være mindst 12 tegn.")
    if not re.search(r"[A-Z]", pw):
        errors.append("Password mangler stort bogstav.")
    if not re.search(r"[0-9]", pw):
        errors.append("Password mangler tal.")
    if not re.search(r"[^A-Za-z0-9]", pw):
        errors.append("Password mangler specialtegn.")
    return errors

def hash_password(pw: str, salt: bytes) -> str:
    return hashlib.sha256(salt + pw.encode("utf-8")).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--password", required=True)
    parser.add_argument("--logfile", default="password_tool.log")
    args = parser.parse_args()

    errors = check_password(args.password)
    with open(args.logfile, "a", encoding="utf-8") as f:
        if errors:
            f.write(f"{datetime.now()} FAIL: {errors}\n")
            print("FEJL:")
            for e in errors:
                print("-", e)
            return

        salt = os.urandom(16)
        hashed = hash_password(args.password, salt)
        f.write(f"{datetime.now()} OK: sha256={hashed}\n")
        print("OK – password opfylder krav.")
        print("Hash:", hashed)

if __name__ == "__main__":
    main()
