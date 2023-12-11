#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City class"""

    state_id = ""
    name = ""


if __name__ == "__main__":
    City()
