#!/usr/bin/python3
"""Defines the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""


if __name__ == "__main__":
    User()
