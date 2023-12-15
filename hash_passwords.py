
import bcrypt
# Run this in a separate Python script, not in your Streamlit app
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')

hashed_password1 = hash_password("password1")
hashed_password2 = hash_password("password2")

print("Hashed Password 1:", hashed_password1)
print("Hashed Password 2:", hashed_password2)

def hash_password(password):
    # Hash a password for the first time, with a randomly-generated salt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
