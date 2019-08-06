"""Functions used by scripts analysing Excel spreadsheet data."""
import re
from typing import Iterable

import pandas

nan = pandas.np.nan


def get_sheets(filename: str, names: Iterable):
    """
    Return a mapping of `names` and corresponding DataFrames made from sheets
    in the spreadsheet specified by `filename`.
    """
    data_file = pandas.ExcelFile(filename)
    return {name: data_file.parse(name)
            for name in names}


def normalize_str(value: str, separator: str = ' ') -> str:
    """Transform string from camel-case to lowercase alphanumeric."""
    return convert_from_plural(
        re.compile(r'[^a-zA-Z0-9]').sub(
            separator, convert_from_camel_case(
                separator, str(value), ).lower()))


def convert_from_plural(string: str) -> str:
    """
    Singularize nouns in label string
    """
    # @todo: replace with regex
    if string.endswith('oats'):
        string: str = string[:-1]
    return string


def convert_from_camel_case(separator: str, string: str) -> str:
    """
    Convert all words from camel-case to lowercase.
    """
    if not (string.islower() or
            string.isupper() or
            string.lower() == string.upper()):
        indices = [index for index, char in enumerate(string)
                   if char.isupper()]
        indices.append(len(string))
        word_index = indices
        if word_index:
            string = separator.join(
                [string[word_index[i]:word_index[i + 1]].strip()
                 for i in range(len(word_index) - 1)])
    return string


def alphanumeric_lower(value: str) -> str:
    """Chained functions `str.lower()` and `alphanumeric()`."""
    return alphanumeric(str(value).lower())


def alphanumeric(string: str) -> str:
    """Remove all non-alphanumeric characters."""
    return re.compile(r"[^a-zA-Z0-9]").sub('', string)


