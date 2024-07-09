import hashlib
import base64

def generate_sha256_hash(password, salt):
    # Combine password and salt and then hash
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).digest()
    return base64.b64encode(hashed_password).decode('utf-8')

# Example password and salt
password = "Ht5@nadm!n"
salt = "mysalt"  # Replace with a unique and secure salt in a real-world scenario

# Generate the SHA-256 hash and Base64 encode
hashed_password_base64 = generate_sha256_hash(password, salt)

print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"SHA-256 Hash (Base64): {hashed_password_base64}")

