#!/usr/bin/env python3
"""filtering and obfuscating logs.
"""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    :fields: A list of strings representing the fields to obfuscate.
    :redaction: the value by which the field will be obfuscated.
    :message: A string representing the log line that needs to be processed.
    :separator: character used to separate all fields in the log line.
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
