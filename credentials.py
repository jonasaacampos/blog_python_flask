from dotenv import load_dotenv
import os


def get_secret(secret):
    load_dotenv()
    secret_revel = os.getenv(secret)
    return secret_revel

# gerar o token e armazenar em local seguro:
# import secrets
# secrets.token_hex()
