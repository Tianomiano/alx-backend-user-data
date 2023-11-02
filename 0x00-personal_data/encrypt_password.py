#!/usr/bin/env python3
"""use bcrypt to encrypt passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password randomly
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
