"""Temporary workspace for analyzing spreadsheet
(PyCharm scientific mode)"""

# %%

from os import getcwd
from typing import Dict

import pandas

import helper

# %%

"""Load spreadsheet into DataFrames"""

filename: str = '../../data/2016-sweep-vs-tiller/2016 combination.xlsx'
# filename: str = 'data/2016-sweep-vs-tiller/2016 combination.xlsx'
HEAD_COUNTS: str = 'Head Counts'
SHEET2: str = 'Sheet2'
sheet_names = (HEAD_COUNTS, SHEET2)
print(getcwd())
frames_dict: dict = helper.get_sheets(filename, sheet_names, )
# @todo: refactor out frames_dict
data = pandas.concat(
    frames_dict,
    axis='columns',
    names=sheet_names,
)

# %%

"""
* drop columns
* rename columns
"""

desired_columns: Dict[str, Dict[str, str]] = {
    HEAD_COUNTS: {
        'Site':           'site',
        'Crop':           'crop',
        'Date':           'date',
        'Field':          'field',
        'EGA_head':       'ega head',
        'EGA_leaf':       'ega leaf',
        'BCO_head':       'bco head',
        'BCO_leaf':       'bco leaf',
        'EGA_grn':        'ega green',
        'EGA_alate':      'ega alate',
        'EGA_apt':        'ega apt',
        'EGA_total':      'ega total',
        'BCO_apt':        'bco apt',
        'BCO_total':      'bco total',
        'greenbug_alate': 'greenbug alate',
        'greenbug_apt':   'greenbug apt',
        'aphids_total':   'aphid total',
    },
    SHEET2:      {
        'Collection_Date':                      'date',
        'Site':                                 'site',
        'Field_name':                           'field',
        'Crop':                                 'crop',
        'Distance(m)':                          'distance',
        'Sitobion_avenae_EGA_green (wingless)': 'ega green apt',
        'Sitobion_avenae_EGA_red':              'ega red',
        'EGA alate':                            'ega alate',
        'Bird_Cherry_Oat_Aphid':                'bco',
        'greenbug_aphid':                       'greenbug',
        'pea aphids':                           'pea',
        'Total_apterous_aphids':                'total apt',
        'Total_alate_aphids':                   'total alate',
        '4th_Instar_Pre-alate':                 'ega instar_4 pre-alate',
        '3rd_Instar_EGA':                       'ega instar_3',
        '3rd_Instar_EGA_Pre-alate':             'ega instar_3 pre-alate',
        '2nd_Instar_EGA':                       'ega instar_2',
        '1st_Instar_EGA':                       'ega instar_1',
    },
}

desired_columns_list = [
    (sheet_name, key)
    for sheet_name in sheet_names
    for key in desired_columns[sheet_name].keys()
]
desired_columns_rename_mapper = {
    (sheet_name, key): (sheet_name, value)
    for sheet_name in desired_columns
    for key, value in desired_columns[sheet_name].items()
}
data = data.reindex(
    columns=desired_columns_list, )
data = data.rename(
    columns=desired_columns_rename_mapper,
    level=1,
)

# %%

"""parse dates"""

# head_counts = frames_dict[HEAD_COUNTS]
head_counts = data.loc[:, HEAD_COUNTS]
head_counts['date'] = pandas.to_datetime(
    head_counts['date'],
    format="%d/%m/%Y", )

# sheet2_ = frames_dict[SHEET2]
data.loc[:, SHEET2]['date'] = pandas.to_datetime(
    data.loc[:, SHEET2]['date'],
    format="%d_%m_%Y")

# %%

"""normalize text values"""

"""crop"""
for frame in frames_dict.values():
    frame.crop = frame.crop.apply(helper.normalize_str)

"""site"""
frames_site = (frame[['site']] for frame in frames_dict.values())
frames_dict['site'] = pandas.concat(
    frames_site,
    keys=sheet_names,
    names=['Sheet Name', 'index', ],
).drop_duplicates().sort_values('site')
for frame in (*frames_dict.values(),):
    frame['site_index'] = frame.site.apply(helper.alphanumeric_lower)
frame.set_index('site_index', append=True, inplace=True)
del frames_dict['site']
standard_site_names = ['Alvena', 'Clavet', 'Indian Head', 'Kernan',
                       'Llewellyn', 'Meadow Lake', 'Melfort', 'Outlook',
                       'SEF', 'Wakaw', 'Yellow Creek', ]
standard_site_names_index_values = {
    helper.alphanumeric_lower(item): item
    for item in standard_site_names}
preferred_site_id = pandas.Series(name='site',
                                  data=standard_site_names_index_values, )
preferred_site_id.index.set_names(['site_index'], inplace=True)
for frame in frames_dict.values():
    frame.loc[:, 'site'] = preferred_site_id.to_frame().combine_first(
        frame).loc[:, 'site']
frame.reset_index(level='site_index', drop=True, inplace=True, )
frame.field = frame.field.str.extract(
    pat=r'(?P<text>\D*)(?P<number>\d*)',
).loc[:, 'number'].apply(pandas.to_numeric)

# %%

for name in sheet_names:
    frames_dict[name] = frames_dict[name].set_index(
        ['date', 'site', 'crop', 'field', ],
        drop=True,
        append=True,
        inplace=False,
    )

# %%

### @todo: 'distance'

# %%

### @todo: split column names, build `MultiIndex`

# %%

### @todo: convert to categorical indices where applicable

# %%

### @todo: corr frames
