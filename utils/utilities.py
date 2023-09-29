"""Contains the utility functions for the application"""
from fastapi.encoders import jsonable_encoder


def encode_input(data) -> dict:
    """The function that encodes the input data

    Args:
        data (UpdateBook): The data to be updated

    Returns:
        dict: The encoded data
    """
    data = jsonable_encoder(data)
    data = {k: v for k, v in data.items() if v is not None}
    return data
