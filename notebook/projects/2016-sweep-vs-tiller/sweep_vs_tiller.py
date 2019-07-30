import pandas

from helper import get_sheets, normalize_str, alphanumeric_lower

sheet_names = ('Head Counts', 'Sheet2',)
filename = '../../data/2016-sweep-vs-tiller/2016 combination.xlsx'
sheets_to_compare = get_sheets(
    filename,
    sheet_names,
)

for sheet2 in sheets_to_compare.values():
    if sheet2.columns.size > 0:
        sheet2.columns = sheet2.columns.str.strip().str.lower()

head_counts = sheets_to_compare['Head Counts']
head_counts['date'] = pandas.to_datetime(
    head_counts['date'],
    format='%d/%m/%Y',
)

sheet2 = sheets_to_compare['Sheet2']
sheet2.drop(columns='date', inplace=True)
sheet2.rename(
    columns={'collection_date': 'date'},
    inplace=True,
)
sheet2['date'] = pandas.to_datetime(
    sheet2['date'],
    format='%d_%m_%Y',
)

# compare_columns(sheets_to_compare)

# ssc.columns.symmetric_difference(s2.columns).tolist()


# pandas.DataFrame(
#     {
#         name: frame.date
#         for name, frame in sheets_to_compare.items()
#     }
# ).apply(
#     [
#         pandas.Series.max,
#         pandas.Series.min,
#         len_unique,
#     ]
# )

# ssc.date.isin(s2.date).all()

# s2.date.isin(ssc.date).all()

# (
#     s2.date.loc[~s2.date.isin(ssc.date)]
#     .drop_duplicates()
# )

# sheets_to_compare = {
#     name: sheets[name]
#     for name in (
#         'Sweep Samples Cereals Edited',
#         'Sheet2',
#     )
# }
# ssce, s2 = sheets_to_compare.values()
# sheet_names = sheets_to_compare.keys()

# pandas.options.display.max_rows = 140
#
# compare_columns(sheets_to_compare)


# pandas.DataFrame(
#     {
#         name: frame.date
#         for name, frame in sheets_to_compare.items()
#     }
# ).apply([
#     pandas.Series.max,
#     pandas.Series.min,
#     len_unique,
#     len,
# ])

# ssce.date.isin(s2.date).all()

# sheets_to_compare = {
#     name: sheets[name]
#     for name in (
#         'leafhoppers 2016 cereal sweeps',
#         'Sheet2',
#     )
# }
# lh2016, s2 = sheets_to_compare.values()
# sheet_names = sheets_to_compare.keys()

# compare_columns(sheets_to_compare)

# sheets_to_compare = {
#     name: sheets[name]
#     for name in (
#         'Head Counts',
#         'Head Counts Edited',
#     )
# }
# hc, hce = sheets_to_compare.values()
# sheet_names = sheets_to_compare.keys()

# compare_columns(sheets_to_compare)

# pandas.DataFrame(
#     {
#         name: frame.date
#         for name, frame in sheets_to_compare.items()
#     }
# ).apply([
#     pandas.Series.max,
#     pandas.Series.min,
#     len_unique,
#     len,
# ])

# hc.date.index.isin(hce.date.index).all()

# sheets_to_compare = {
#     'Head Counts': hc,
#     'Sheet2': s2,
# }
# sheet_names = sheets_to_compare.keys()

# pandas.concat(
#     (
#         pandas.DataFrame(
#             data={
#                 'Sheet2': s2.columns.difference(hc.columns),
#             }
#         ),
#         pandas.DataFrame(
#             data={
#                 'Head Counts': hc.columns.difference(s2.columns),
#             }
#         ),
#         pandas.DataFrame(
#             data={
#                 'common': s2.columns.intersection(hc.columns),
#             }
#         ),
#     ),
#     sort=False,
#     axis='columns',
# ).fillna('--')

non_organism_column_names = pandas.Series(data=(
    'crop',  # location
    'date',  # time
    'date_by_week',  # redundant date coding
    'distance(m)',  # location
    'field',  # location
    'field_name',  # location
    'id',  # not relevant for this analysis
    'julian_date',  # redundant date coding
    'number of samples',  # used for sums, which are redundant
    'province',  # location
    'site',  # location
    'zadoks_stage',  # not relevant for this analysis
))

# emojify_boolean(pandas.DataFrame(
#     {
#         name: dict(zip(non_organism_column_names,
#                        non_organism_column_names.isin(frame.columns)))
#         for name, frame
#         in zip(sheet_names, (hc, s2))
#     }
# ))
for frame in (head_counts, sheet2):
    frame.rename(
        columns={'field_name': 'field'},
        inplace=True,
    )

hhc = head_counts.set_index('date')
ss2 = sheet2.set_index('date')


# pandas.concat(
#     (
#         pandas.concat(  # convenient way to add sheet name to column hierarchy
#             {name: sheet},
#             axis='columns',
#         ).reorder_levels([1, 0], axis='columns')
#         # Sheet names paired with date-indexed frames.
#         for name, sheet in zip(sheet_names, (hhc, ss2))
#     ),
#     axis='rows',
# ).loc[
#     # Overlapping dates in date-index frames:
#     hhc.index.intersection(ss2.index),
#     # Non-date indices:
#     (
#         [
#             'site',
#             'field',
#             'field_name',
#             'crop',
#         ],
#     )
# ]


# show_spaces(
#     pandas.Series(
#         [
#             ' hello, friend ',
#             'I love    space    !',
#         ]
#     )
# )

crops = pandas.concat(
    (
        frame.crop.apply(str)
        for frame in sheets_to_compare.values()
    ),
    keys=sheet_names,
    sort=True,
).drop_duplicates().reset_index(drop=True).sort_values()


# show_spaces(crops)


# pandas.concat(
#     (
#         crops,
#         crops.apply(normalize_str),
#     ),
#     keys=("Before", "After"),
#     axis='columns',
# ).sort_values('After').apply(show_spaces)

for frame in (head_counts, sheet2):
    frame.crop = frame.crop.apply(normalize_str)

site_values = (
    pandas.concat(
        (frame[['site']] for frame in (head_counts, sheet2)),
        keys=sheet_names,
        names=['Sheet Name', 'index', ],
    ).drop_duplicates().sort_values('site')
)


# show_spaces(site_values.site)


# (
#     site_values
#     .reset_index(level='index', drop=True)
#     .loc[:, ['site']]
#     .apply(show_spaces)
# )

preferred_site_id = pandas.Series(
    name='site',
    data={
        alphanumeric_lower(item): item
        for item in [
            'Alvena',
            'Clavet',
            'Indian Head',
            'Kernan',
            'Llewellyn',
            'Meadow Lake',
            'Melfort',
            'Outlook',
            'SEF',
            'Wakaw',
            'Yellow Creek',
        ]
    },
)
preferred_site_id.index.set_names(['site_index'], inplace=True)
# preferred_site_id.to_frame()

for frame in (head_counts, sheet2) + (site_values,):
    frame['site_index'] = frame.site.apply(alphanumeric_lower)
    frame.set_index('site_index', append=True, inplace=True)

# site_values[
#     ~ (  # ~ is the 'not' operator
#         site_values.index.get_level_values('site_index')
#         .isin(preferred_site_id.index)
#     )
# ].reset_index('index', drop=True)

# (
#     pandas.concat(
#         (
#             site_values,
#             preferred_site_id.to_frame().combine_first(site_values),
#         ),
#         keys=['Before', 'After'],
#         axis='columns',
#     )
#     .reorder_levels([1, 0], axis='columns')
#     .reset_index(['site_index', 'index'], drop=True)
#     .apply(show_spaces)
# )

for frame in (head_counts, sheet2):
    frame.loc[:, 'site'] = (
        preferred_site_id.to_frame().combine_first(frame).loc[:, 'site']
    )
    frame.reset_index(
        level='site_index',
        drop=True,
        inplace=True,
    )

# show_spaces(
#     pandas.concat(
#         (frame[['site']] for frame in (hc, s2)),
#     )
#     .loc[:, 'site']
#     .reset_index(drop=True)
#     .sort_values()
#     .drop_duplicates()
# )

pandas.options.display.max_rows = 20

index_column_names = ['crop', 'site', 'date', 'field', ]
# (
#     pandas.concat(
#         (
#             hc[index_column_names],
#             s2[index_column_names],
#         ),
#         keys=sheet_names,
#         names=['worksheet', 'index',],
#     )
#     .sort_values(
#         by=index_column_names,
#     )
#     .set_index(
#         keys=['crop', 'site'],
#     )
#     .drop_duplicates()
#     .apply(
#         {
#             'field': show_spaces,
#             'date': lambda x: x,
#         }
#     )
# )
# pandas.options.display.max_rows = 40

# (
#     _  # Previous cell output.
#     .reset_index()
#     .apply(
#         dict(
#             tuple(
#                 dict.fromkeys(
#                     (
#                         'date',
#                         'site',
#                         'crop',
#                     ),
#                     lambda x: x,
#                 ).items()
#             ) + tuple(
#                 {
#                     'field': lambda x: x.str.extract(
#                         pat=r'(?P<text>\D*)(?P<number>\d*)',
#                     ),
#                 }.items(),
#             ),
#         )
#     )
#     .drop_duplicates(
#         subset=[
#             ('date', 'date'),
#             ('field', 'number'),
#         ],
#     )
#     .dropna(
#         subset=[
#             ('date', 'date'),
#             ('field', 'number'),  # @todo: needed?
#         ],
#     )
# )

for sheet in (head_counts, sheet2):
    sheet.field = (
        sheet.field.str.extract(
            pat=r'(?P<text>\D*)(?P<number>\d*)').loc[:, 'number'].apply(
            pandas.to_numeric, downcast='integer'))

# s2['number of samples'].value_counts(dropna=False)

# s2[
#     ['distance(m)', 'number of samples']
# ].dropna(how='all').drop_duplicates()

aphid_column_names = {
    'ega': (
        '1st_instar_ega',
        '2nd_instar_ega',
        '3rd_instar_ega',
        '3rd_instar_ega_pre-alate',
        'ega alate',
        'ega_alate',
        'ega_apt',
        'ega_grn',
        'ega_head',
        'ega_leaf',
        'ega_red',
        'sitobion_avenae_ega_green (wingless)',
        'sitobion_avenae_ega_red',
        '4th_instar_pre-alate',
    ),
    'bco': (
        'bco_alate',
        'bco_apt',
        'bco_head',
        'bco_leaf',
        'bird_cherry_oat_aphid',
    ),
    'greenbug': (
        'greenbug_alate',
        'greenbug_apt',
        'greenbug_aphid',
    ),
    'pea': (
        'pea aphids',
    ),
}
aphid_column_names_level_names = ['aphid_type', 'column_name']

# emojify_boolean(
#     pandas.DataFrame(
#         data={
#             name: sheet.columns[
#                 sheet.columns.isin(
#                     sum(
#                         aphid_column_names.values(),
#                         ()
#                     )
#                 )
#             ].to_series(name=name)
#             for name, sheet in sheets_to_compare.items()
#         },
#     ).notna()
# )


# index_columns = ['date', 'site', 'crop', 'field']
# pandas.concat(
#     (frame.set_index(index_columns).loc[hhc.index.intersection(ss2.index)]
#      for frame in sheets_to_compare.values()),
#     sort=False,
# ).reindex(
#     columns=pandas.MultiIndex.from_tuples(
#         tuple(((aphid_type, column_name)
#                for aphid_type, column_names in aphid_column_names.items()
#                for column_name in column_names)),
#         names=aphid_column_names_level_names,
#     ),
#     level=1,
# )
#

# pandas.concat(
#     (
#         pandas.concat(  # Convenient way to add sheet name to column hierarchy.
#             {
#                 name: sheet.loc[
#                     hhc.index.intersection(ss2.index),  # only dates in common
#                 ].reindex(
#                     columns=pandas.MultiIndex.from_tuples(
#                         (
#                             (aphid_type, aphid_categorization, column_name)
#                             for aphid_type, inner_hierarchy in aphid_column_names.items()
#                             for aphid_categorization, column_names in inner_hierarchy.items()
#                             for column_name in column_names
#                         ),
#                         names=aphid_column_names_level_names
#                     ),
#                     level=2,
#                 )
#             },
#             axis='columns',
#         ).reorder_levels([1, 2, 3, 0, ], axis='columns')  # So sheet names don't ruin alignment.
#         for name, sheet in sheets_to_compare.items()
#     ),
#     axis='rows',
# )

aphid_column_names_deep = {
    'ega': {
        'alate': (
            'ega alate',
            'ega_alate',
        ),
        'apterous': (
            'ega_apt',
            'sitobion_avenae_ega_green (wingless)',
        ),
        'pre-alate': (
            '3rd_instar_ega_pre-alate',
            '4th_instar_pre-alate',
        ),
        'red': (
            'ega_red',
            'sitobion_avenae_ega_red',
        ),
        'green': (
            'ega_grn',
            'sitobion_avenae_ega_green (wingless)',
        ),
        'head': (
            'ega_head',
        ),
        'leaf': (
            'ega_leaf',
        ),
        'uncategorized': (
            '1st_instar_ega',
            '2nd_instar_ega',
            '3rd_instar_ega',
        )
    },
    'bco': {
        'alate': (
            'bco_alate',
        ),
        'apterous': (
            'bco_apt',
        ),
        'head': (
            'bco_head',
        ),
        'leaf': (
            'bco_leaf',
        ),
        'uncategorized': (
            'bird_cherry_oat_aphid',
        ),
    },
    'greenbug': {
        'alate': (
            'greenbug_alate',
        ),
        'apterous': (
            'greenbug_apt',
        ),
        'uncategorized': (
            'greenbug_aphid',
        ),
    },
    'pea': {
        'uncategorized': (
            'pea aphids',
        ),
    },
}
aphid_column_names_deep_level_names = ['aphid_type', 'category', 'column_name']

# pandas.options.display.max_columns = 100
#
# indices = [
#     'date',
#     'site',
#     'crop',
#     'field',
# ]
# hhc, ss2 = (frame.set_index(indices) for frame in (hc, s2))
# ss2 = ss2.set_index(['distance(m)', 'id'], append=True).sum(level=[0, 1, 2, 3,])
# ss2

# hc.columns.to_list()

s2_labels = {
    'id': ('index', 'unique',),
    'province': ('index', 'place',),
    'date': ('index', 'time',),
    'sample_by_week': ('not applicable',),
    'date_by_week': ('not applicable',),
    'julian_date': ('not applicable',),
    'site': ('index', 'place',),
    'field': ('index', 'place',),
    'crop': ('observation', 'crop', 'type',),
    'distance(m)': ('index', 'place',),
    'number of samples': ('not applicable',),
    'sitobion_avenae_ega_green (wingless)': ('observation', 'aphid', 'count', 'ega', 'apterous',),
    'sitobion_avenae_ega_red': ('observation', 'aphid', 'count', 'ega', 'uncategorized',),
    'ega alate': ('observation', 'aphid', 'count', 'ega', 'alate',),
    'bird_cherry_oat_aphid': ('observation', 'aphid', 'count', 'bco', 'uncategorized',),
    'greenbug_aphid': ('observation', 'aphid', 'count', 'greenbug', 'uncategorized',),
    'pea aphids': ('observation', 'aphid', 'count', 'pea', 'uncategorized',),
    'total_apterous_aphids': ('observation', 'aphid', 'count', 'uncategorized', 'apterous',),
    'total_alate_aphids': ('observation', 'aphid', 'count', 'uncategorized', 'apterous',),
    '4th_instar_pre-alate': ('observation', 'aphid', 'count', 'uncategorized', 'pre-alate',),
    '3rd_instar_ega': ('observation', 'aphid', 'count', 'ega', 'uncategorized',),
    '3rd_instar_ega_pre-alate': ('observation', 'aphid', 'count', 'ega', 'pre-alate',),
    '2nd_instar_ega': ('observation', 'aphid', 'count', 'ega', 'uncategorized',),
    '1st_instar_ega': ('observation', 'aphid', 'count', 'ega', 'uncategorized',),
    'aphid_mummies_aphelinus_black': ('not applicable',),
    'aphid_mummies_aphidius_brown': ('not applicable',),
    'aphid_mummies': ('not applicable',),
    'female_macrosteles_quadrilineatus': ('not applicable',),
    'male_macrosteles_quadrilineatus': ('not applicable',),
    'macrosteles_quadrilineatus nymphs': ('not applicable',),
    '1st_instar_macrosteles': ('not applicable',),
    '2nd_instar_macrosteles': ('not applicable',),
    '3rd_instar_macrosteles': ('not applicable',),
    '4th_instar_macrosteles': ('not applicable',),
    'athysanus_argentarius': ('not applicable',),
    'doratura_sp.': ('not applicable',),
    'errastunus_ocellaris_lh': ('not applicable',),
    'other_leafhoppers': ('not applicable',),
    'other coccinellid_adults': ('not applicable',),
    'hippodamia_tredecimpunctata_c13': ('not applicable',),
    'coccinella_septempunctata_c7': ('not applicable',),
    'ladybugs- larvae': ('not applicable',),
    'chrysopidae_adults': ('not applicable',),
    'chrysoperla_carnea_adult': ('not applicable',),
    'chrysopa_oculata_adult': ('not applicable',),
    'chrysoperla_carnea_larva': ('not applicable',),
    'chrysopa_oculata_larvae': ('not applicable',),
    'g_lacewing_larvae': ('not applicable',),
    'orius_tristicolor': ('not applicable',),
    'anthocoridae': ('not applicable',),
    '( damsel bug)nabis_americoferus_adult': ('not applicable',),
    'nabis_americoferus_nymph': ('not applicable',),
    'nabicula': ('not applicable',),
    'nabis_alternatus': ('not applicable',),
    'chalcid_wasps': ('not applicable',),
    'aphelinus_varipes': ('not applicable',),
    'aphelinus_asychis': ('not applicable',),
    'aphelinus_albipodus': ('not applicable',),
    'braconid_wasps': ('not applicable',),
    'aphidiius_sp.': ('not applicable',),
    'any parasitoid_adults': ('not applicable',),
    'hyperparasitoids ???': ('not applicable',),
    'aphidencyrtus_sp': ('not applicable',),
    'asaphes_suspensus': ('not applicable',),
    'flies': ('not applicable',),
    'lauxaniidae': ('not applicable',),
    'dolichopodidae': ('not applicable',),
    'syrphid_flies': ('not applicable',),
    'hoverflies': ('not applicable',),
    'female_delia_sp_1': ('not applicable',),
    'male_delia_sp_1': ('not applicable',),
    'female_delia_sp_2': ('not applicable',),
    'male_delia_sp_2': ('not applicable',),
    'anthomyiidae-delia': ('not applicable',),
    'midge': ('not applicable',),
    'lygus_punctatus': ('not applicable',),
    'lygus_elisus': ('not applicable',),
    'miridae_lygus lineolaris': ('not applicable',),
    'lygus_nymph': ('not applicable',),
    'green_grass_bugs_trigonotylus_coelestialium miridae': ('not applicable',),
    'green_grass nymphs': ('not applicable',),
    'capsus_simulans': ('not applicable',),
    'katydids': ('not applicable',),
    'thrips': ('not applicable',),
    'grasshoppers': ('not applicable',),
    'spiders': ('not applicable',),
    'spider_tetragnathidae': ('not applicable',),
    'mosquitoes': ('not applicable',),
    'dragonflies+damsel fly': ('not applicable',),
    'flea_beetles hop': ('not applicable',),
    'flea_beetles striped': ('not applicable',),
    'flea_beetles crucifer': ('not applicable',),
    'cicindela': ('not applicable',),
    'tychius_picirostris (weevil)': ('not applicable',),
    'bertha_armyworms': ('not applicable',),
    'shield_bugs': ('not applicable',),
    'worms': ('not applicable',),
    'beetles': ('not applicable',),
    'maggots': ('not applicable',),
    'stink_bugs (adult and nymph)': ('not applicable',),
    'red_mite': ('not applicable',),
    'moths': ('not applicable',),
    'plant_bugs': ('not applicable',),
    'pirate_bugs': ('not applicable',),
    'assassin_bug (reduviid bugs)': ('not applicable',),
    'bees': ('not applicable',),
    'harvestman': ('not applicable',),
    'treehoppers': ('not applicable',),
    'cabbage_butterfly': ('not applicable',),
    'caterpillar': ('not applicable',),
    'legume_bug': ('not applicable',),
    'chinch_bug': ('not applicable',),
    'ambush_bugs': ('not applicable',),
    'ichneumonidae': ('not applicable',),
    'pumace_flies (drosophilidae)': ('not applicable',),
    'scorpion_flies': ('not applicable',),
    'seed bugs (lygaeidea)': ('not applicable',),
    'seed_corn_beetles': ('not applicable',),
    'ufi_bugs': ('not applicable',),
    'wasps_other': ('not applicable',),
    'eulophid_wasp': ('not applicable',),
    'oribatid': ('not applicable',),
    'spider_mites': ('not applicable',),
    'springtails': ('not applicable',),
    'mollusks': ('not applicable',),
    'formicidae': ('not applicable',),
    'weevil': ('not applicable',),
    'lepidopteran_pupa': ('not applicable',),
    'unnamed: 129': ('not applicable',),
    'hymenoptera_proctotrupidae': ('not applicable',),
    'hymenoptera_pteromalidae': ('not applicable',),
    'hymenoptera_apidae': ('not applicable',),
    'hymenoptera_diplazontinae': ('not applicable',),
    'hymenoptera_figitidae': ('not applicable',),
    'hymenoptera_aphelinidae': ('not applicable',),
    'hymenoptera_perilampidae': ('not applicable',),
    'hymenoptera_chalcidoidea': ('not applicable',),
    'hymenoptera_ichneumondoidea': ('not applicable',),
    'hymenoptera_proctotrupoidea': ('not applicable',),
}

# [(key, *values) for key, values in s2_labels.items()]

# pandas.MultiIndex.from_tuples((key, *values) for key, values in s2_labels.items()).to_frame().T

sheets_to_compare = dict(zip(sheet_names, (hhc, ss2)))  # Sheet name paired with date-indexed frame.
# pandas.concat(
#     (
#         pandas.concat(  # Convenient way to add sheet name to column hierarchy.
#             {
#                 name: sheet.loc[
#                     hhc.index.intersection(ss2.index),  # only dates in common
#                 ].reindex(
#                     columns=pandas.MultiIndex.from_tuples(
#                         (
#                             (aphid_type, aphid_categorization, column_name)
#                             for aphid_type, inner_hierarchy in aphid_column_names.items()
#                             for aphid_categorization, column_names in inner_hierarchy.items()
#                             for column_name in column_names
#                         ),
#                         names=aphid_column_names_level_names
#                     ),
#                     level=2,
#                 )
#             },
#             axis='columns',
#         ).reorder_levels([1, 2, 3, 0, ], axis='columns')  # So sheet names don't ruin alignment.
#         for name, sheet in sheets_to_compare.items()
#     ),
#     axis='rows',
# )

hc_ega_sums = pandas.concat(
    {
        'head + leaf': (head_counts['ega_head'] + head_counts['ega_leaf']),
        'apt + alate': (head_counts['ega_apt'] + head_counts['ega_alate']),
        'reg + grn': (head_counts['ega_red'] + head_counts['ega_grn']),
    },
    axis='columns',
)

# pandas.options.display.max_rows = 25
# pandas.concat(
#     (
#         hc_ega_sums,
#         pandas.Series(
#             data=hc_ega_sums.std(axis='columns'),
#             name='std',
#         ),
#     ),
#     axis='columns',
# ).sort_values(
#     by='std',
#     ascending=False
# ).head(25)

# _.loc[[34, 80, 33, 81]]

# __.loc[[14, 75, 155]]

index_columns = ['date', 'site', 'crop', 'field']
# pandas.concat(
#     (frame.set_index(index_columns).loc[hhc.index.intersection(ss2.index)]
#      for frame in sheets_to_compare.values()),
#     sort=False,
# ).reindex(
#     columns=pandas.MultiIndex.from_tuples(
#         tuple(((aphid_type, column_name)
#                for aphid_type, column_names in aphid_column_names.items()
#                for column_name in column_names)),
#         names=aphid_column_names_level_names,
#     ),
#     level=1,
# )
hc_column_names = head_counts.columns
