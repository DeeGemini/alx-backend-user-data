#!/usr/bin/env python3
"""
Module for filtering log messages to obfuscate PII fields.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated by replacing the values of specified fields.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message to be filtered.
        separator (str): The character separating the fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    if not fields or not redaction or not message or not separator:
        raise ValueError("None of the arguments can be None")

    pattern = '|'.join([f"{field}=[^{separator}]*" for field in fields])
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)

