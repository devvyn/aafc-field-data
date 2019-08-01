import re
from typing import Dict, Mapping, Iterable, Any

from pandas import ExcelFile, DataFrame
from pandas import np

NaN = np.nan

mapping_str_any_ = Mapping[str, Any]

sheet_dict = Mapping[str, mapping_str_any_]


def get_sheets(filename: str, names: Iterable[str] = None) -> (
        sheet_dict):
    """
    Return a mapping of `names` and corresponding DataFrames made from sheets
    in the spreadsheet specified by `filename`.
    """
    data_file = ExcelFile(filename)
    sheet_names = names or data_file.sheet_names
    return {
        sheet_name: data_file.parse(sheet_name)
        for sheet_name in sheet_names
    }


def emojify_boolean(frame: DataFrame) -> DataFrame:
    return (frame.replace({
        True: '✅', False: '✖️',
    }))


def compare_columns(frames: Dict[str, DataFrame]) -> DataFrame:
    return emojify_boolean(DataFrame(data={name: sheet.columns.to_series(
        name=name) for name, sheet in frames.items()}).notna())


def len_unique(pandas_object):
    return len(pandas_object.unique())


def show_spaces(x):
    return x.str.replace(' ', '⬜️')


def normalize_str(value, separator: str = ' ') -> str:
    if value == NaN:
        return value
    return convert_from_plural(replace_non_alphanumeric(separator,
        convert_from_camel_case(separator, str(value))))


def convert_from_plural(transformed: str) -> str:
    # @todo: replace with regex
    if transformed.endswith('oats'):
        transformed = transformed[:-1]
    return transformed


def replace_non_alphanumeric(separator: str, str_value: str) -> str:
    transformed: str = re.compile(r'[^a-zA-Z0-9]').sub(separator,
        str_value.lower())
    return transformed


def convert_from_camel_case(separator: str, string: str) -> str:
    """
    Convert all words from camel-case to lowercase.
    """
    is_mixed_case: bool = (
        not (str_value.islower() or str_value.isupper()) and (
            str_value.upper() != str_value.lower()))
    if is_mixed_case:
        # noinspection PyTypeChecker
        word_index = [
                         # Remember starting positions of all uppercase
                         # characters.
                         index for index, char in enumerate(string)
                         if char.isupper()
                     ] + [
                         None,
                     ]  # Final null for easier string slicing with [
        # …:word_index[i + 1]].
        if word_index:
            words = [  # Strip leading and trailing whitespace from each word.
                string[word_index[i]:word_index[i + 1]].strip() for i in
                range(len(word_index) - 1)]
            string = separator.join(words)  # Rejoin words.
    return string


def alphanumeric_lower(value):
    return re.compile(r"[^a-z0-9]").sub('', str(value).lower())


def drop_except(frame: DataFrame, columns: list) -> DataFrame:
    """
    Drop all columns from `frame` not named in `columns`.
    """
    return frame.drop(columns=(
        frame.columns[~ frame.columns.isin(columns)]
    ))
