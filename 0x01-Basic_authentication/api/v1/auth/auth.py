#!/usr/bin/env python3
"""authentication
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """manage api authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if path requires authentication
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """returns value in auth header
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user
        """
        return None
