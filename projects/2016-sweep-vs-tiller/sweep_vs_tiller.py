"""Temporary workspace for analyzing spreadsheet
(PyCharm scientific mode)"""

# %%

from os import getcwd
from typing import Dict

from pandas import to_datetime, concat, Series, to_numeric

import helper

# %%

"""Load spreadsheet into DataFrames"""

filename: str = '../../data/2016-sweep-vs-tiller/2016 combination.xlsx'
HEAD_COUNTS: str = 'Head Counts'
SHEET2: str = 'Sheet2'
sheet_names = (HEAD_COUNTS, SHEET2)
print(getcwd())
frames: dict = helper.get_sheets(filename, sheet_names, )

# %%

"""
* drop columns
* rename columns
"""

columns: Dict[str, Dict[str, str]] = {
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

for sheet_name in sheet_names:
    frames[sheet_name] = helper.drop_except(
        frames[sheet_name], [*columns[sheet_name].keys()]
    ).rename(columns=columns[sheet_name], )

# %%

"""parse dates"""

frames[HEAD_COUNTS]['date'] = to_datetime(frames[HEAD_COUNTS]['date'],
                                          format="%d/%m/%Y", )
frames[SHEET2]['date'] = to_datetime(frames[SHEET2]['date'],
                                     format="%d_%m_%Y")

# %%

"""normalize text values"""

"""crop"""
for frame in frames.values():
    frame.crop = frame.crop.apply(helper.normalize_str)

"""site"""
frames_site = (frame[['site']] for frame in frames.values())
frames['site'] = concat(
    frames_site,
    keys=sheet_names,
    names=['Sheet Name', 'index', ],
).drop_duplicates().sort_values('site')
for frame in (*frames.values(),):
    frame['site_index'] = frame.site.apply(helper.alphanumeric_lower)
    frame.set_index('site_index', append=True, inplace=True)
del frames['site']
standard_site_names = ['Alvena', 'Clavet', 'Indian Head', 'Kernan',
                       'Llewellyn', 'Meadow Lake', 'Melfort', 'Outlook',
                       'SEF', 'Wakaw', 'Yellow Creek', ]
standard_site_names_index_values = {helper.alphanumeric_lower(item): item
                                    for item in standard_site_names}
preferred_site_id = Series(name='site',
                           data=standard_site_names_index_values, )
preferred_site_id.index.set_names(['site_index'], inplace=True)
for frame in frames.values():
    frame.loc[:, 'site'] = preferred_site_id.to_frame().combine_first(
        frame).loc[:, 'site']
    frame.reset_index(level='site_index', drop=True, inplace=True, )
    frame.field = frame.field.str.extract(
        pat=r'(?P<text>\D*)(?P<number>\d*)',
    ).loc[:, 'number'].apply(to_numeric)

# %%

for name in sheet_names:
    frames[name] = frames[name].set_index(
        ['date', 'site', 'crop', 'field', ],
        drop=True,
        append=True,
        inplace=False,
    )

# %%

# @todo: 'distance'
