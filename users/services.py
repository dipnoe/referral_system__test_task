import random
import string
import time

from config.settings import AUTH_CODE_LENGTH


def send_auth_code() -> str:
    """
    Generates a random 4-character invite code consisting of digits.
    """
    auth_code = ''.join(random.choice(string.digits) for _ in range(AUTH_CODE_LENGTH))
    time.sleep(2)
    return auth_code


def create_invite_code() -> str:
    """
    Generates a random 6-character invite code consisting of letters and digits.
    """
    invite_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return invite_code
