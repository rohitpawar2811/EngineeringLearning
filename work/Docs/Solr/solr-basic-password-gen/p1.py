import base64

encoded_text = "DhlMCx0Th-XYICEDJIwczb2ShLmwIUXsNV5IhxGicwvCXdSQwOigq9NZurWOvGIpZ_vkOQ6kkuWyMK3fsXjE8sHKtz30A9PhEm8rWw-UB4-MmykBZt4OFP5oKcQtcO_5W9tfUuB6U2QJ1xCLnCEYFQJtI3RTo5ykJRha1B7nWGw"

# Decoding from Base64
decoded_text = base64.b64decode(encoded_text).decode('utf-8')

print(decoded_text)
