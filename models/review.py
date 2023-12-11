#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review class"""

    place_id = ""
    user_id = ""
    text = ""


if __name__ == "__main__":
    Review()
