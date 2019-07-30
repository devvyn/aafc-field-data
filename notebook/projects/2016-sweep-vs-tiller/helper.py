import re
from typing import Iterable, Dict

import pandas


def get_sheets(filename: str, names: Iterable = None) -> dict:
    data_file = pandas.ExcelFile(filename)
    sheet_names = names or data_file.sheet_names
    return {
        sheet_name: data_file.parse(sheet_name)
        for sheet_name in sheet_names
    }


def emojify_boolean(frame: pandas.DataFrame) -> pandas.DataFrame:
    return (
        frame.replace({
            True: '✅',
            False: '✖️',
        })
    )


def compare_columns(frames: Dict[str, pandas.DataFrame]) -> pandas.DataFrame:
    return emojify_boolean(
        pandas.DataFrame(
            data={
                name: sheet.columns.to_series(name=name)
                for name, sheet in frames.items()
            }
        ).notna()
    )


def len_unique(pandas_object):
    return len(pandas_object.unique())


def show_spaces(x):
    return x.str.replace(
        ' ', '⬜️'
    )


def normalize_str(value: (str, float), separator: str = ' ') -> (str, float):
    if value == pandas.np.nan:
        return value
    str_value = str(value)

    # Convert camel case strings. E.g.: "WinterWheat" -> "winter wheat"
    is_mixed_case = (
            not (str_value.islower() or str_value.isupper())
            and (str_value.upper() != str_value.lower())
    )
    if is_mixed_case:
        word_index = [
                         # Remember starting positions of all uppercase characters.
                         index for index, char in enumerate(str_value)
                         if char.isupper()
                     ] + [
                         None,
                     ]  # Final null for easier string slicing with […:word_index[i + 1]].
        if word_index:
            words = [
                # Strip leading and trailing whitespace from each word.
                str_value[word_index[i]:word_index[i + 1]].strip()
                for i in range(len(word_index) - 1)
            ]
            str_value = separator.join(words)  # Rejoin words.

    # Replace non-alphanumeric characters with separator (default: space).
    transformed = re.compile(r'[^a-zA-Z0-9]').sub(separator, str_value.lower())

    # De-pluralize special case.
    if transformed.endswith('oats'):
        transformed = transformed[:-1]

    return transformed


def alphanumeric_lower(value):
    return re.compile(r"[^a-z0-9]").sub('', str(value).lower())
