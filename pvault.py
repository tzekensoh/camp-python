import json
import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

VAULT_FILE = "vault.json"
SALT_FILE = "salt.bin"
CHECK_VALUE = "vault-unlocked"


def load_or_create_salt():
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            return f.read()
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
        f.write(salt)
    return salt


def derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "r") as f:
        return json.load(f)


def save_vault(vault):
    with open(VAULT_FILE, "w") as f:
        json.dump(vault, f, indent=2)


def verify_or_initialize_vault(vault, fernet):
    if "_check" not in vault:
        # First-time initialization
        vault["_check"] = fernet.encrypt(CHECK_VALUE.encode()).decode()
        save_vault(vault)
        print("Vault initialized.")
        return True

    try:
        decrypted = fernet.decrypt(vault["_check"].encode()).decode()
        return decrypted == CHECK_VALUE
    except InvalidToken:
        return False


def add_password(vault, fernet):
    service = input("Service name: ")
    password = input("Password: ")

    encrypted = fernet.encrypt(password.encode()).decode()
    vault[service] = encrypted
    save_vault(vault)
    print("Password saved.")


def get_password(vault, fernet):
    service = input("Service name: ")

    if service not in vault:
        print("No such service.")
        return

    decrypted = fernet.decrypt(vault[service].encode()).decode()
    print("Password:", decrypted)


def main():
    master_password = input("Enter master password: ")

    salt = load_or_create_salt()
    key = derive_key(master_password, salt)
    fernet = Fernet(key)

    vault = load_vault()

    if not verify_or_initialize_vault(vault, fernet):
        print("❌ Incorrect master password.")
        return

    while True:
        print("\n1) Add password")
        print("2) Get password")
        print("3) Exit")

        choice = input("> ")

        if choice == "1":
            add_password(vault, fernet)
        elif choice == "2":
            get_password(vault, fernet)
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
