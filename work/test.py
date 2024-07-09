import base64
import json
from itsdangerous import URLSafeTimedSerializer

# Define your secret key
SECRET_KEY = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"

# Encoded session value
encoded_session_value = "eJwljt1KxDAQRt8l17L5n2T6KiJlMsmYQrFLm0UX8d2NeHn4Pg7nW61ytqurZZyP9qLWrapFQaJgghTO1NCjKdZWEbGWOWcIQN4WNjk4TBEZvLgMsaBPwGxq5uykWDE5YsyFOKQgUAjBJbEOXA0pBkIsdW4tUUTwLlJyZCvW2ljNkMfVzv8aO3E_mPY2oX1MutN7W_t2jeN8quVV9THui9aDRn_SrR_jk75u26H_HJfe51Grt59fnVJHbA.ZjI0iA.tuubSjKT_HnNEV0Ji5IWVupHk_A"

# Decode the session value from Base64
decoded_session_value = base64.urlsafe_b64decode(encoded_session_value)

# Split the decoded value into payload and signature
separator_index = decoded_session_value.rfind(b'.')
payload = decoded_session_value[:separator_index]
signature = decoded_session_value[separator_index + 1:]

# Verify the signature
serializer = URLSafeTimedSerializer(SECRET_KEY)
try:
    actual_data = serializer.loads(payload)
    print("Decoded session data:", actual_data)
except Exception as e:
    print("Error decoding session data:", e)
