import hashlib
import base64

def generate_sha256_hash(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).digest()
    # Base64 encode the hashed password
    hashed_password_base64 = base64.b64encode(hashed_password).decode('utf-8')
    return hashed_password_base64

# Example password
password = "SolrRocks"

# Generate the SHA-256 hash and Base64 encode
hashed_password_base64 = generate_sha256_hash(password)

print(f"Password: {password}")
print(f"SHA-256 Hash (Base64): {hashed_password_base64}")
