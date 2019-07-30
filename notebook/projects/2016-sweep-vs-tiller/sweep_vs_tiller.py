"""Temporary workspace for analyzing spreadsheet"""
from typing import Tuple, Mapping, List, Dict, Iterable

import pandas
from pandas import DataFrame, Series

from helper import get_sheets, normalize_str, alphanumeric_lower

HEAD_COUNTS: str = 'Head Counts'
SHEET2: str = 'Sheet2'

sheet_names: Tuple[str, str] = (HEAD_COUNTS, SHEET2,)
filename: str = '../../data/2016-sweep-vs-tiller/2016 combination.xlsx'

sheets_to_compare: Mapping[str, DataFrame] = get_sheets(
    filename,
    sheet_names,
)

sheet2: DataFrame = sheets_to_compare[SHEET2]
if sheet2.columns.size > 0:
    sheet2.columns = sheet2.columns.str.strip().str.lower()

head_counts: DataFrame = sheets_to_compare[HEAD_COUNTS]
head_counts['date'] = pandas.to_datetime(
    head_counts['date'],
    format='%d/%m/%Y',
)

sheet2.drop(columns='date', inplace=True)
sheet2.rename(
    columns={'collection_date': 'date'},
    inplace=True,
)
sheet2['date'] = pandas.to_datetime(
    sheet2['date'],
    format='%d_%m_%Y',
)

non_organism_column_names: Tuple[str, ...] = (
    'date',  # time
    'julian_date',  # redundant date coding
    'date_by_week',  # redundant date coding
    'crop',  # location
    'distance(m)',  # location
    'field',  # location
    'field_name',  # location
    'province',  # location
    'site',  # location
    'id',  # not relevant for this analysis
    'number of samples',  # used for sums, which are redundant
    'zadoks_stage',  # not relevant for this analysis
)
non_organism_column_names_series: Series = pandas.Series(data=non_organism_column_names)

for frame in (head_counts, sheet2):
    frame.rename(
        columns={'field_name': 'field'},
        inplace=True,
    )

hc_indexed: DataFrame = head_counts.set_index('date')
s2_indexed: DataFrame = sheet2.set_index('date')

for frame in (head_counts, sheet2):
    frame.crop = frame.crop.apply(normalize_str)

site_values: DataFrame = (
    pandas.concat(
        (frame[['site']] for frame in (head_counts, sheet2)),
        keys=sheet_names,
        names=['Sheet Name', 'index', ],
    ).drop_duplicates().sort_values('site')
)
preferred_site_id: Series = pandas.Series(
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

for frame in (head_counts, sheet2) + (site_values,):
    frame['site_index'] = frame.site.apply(alphanumeric_lower)
    frame.set_index('site_index', append=True, inplace=True)

for frame in (head_counts, sheet2):
    frame.loc[:, 'site'] = (
        preferred_site_id.to_frame().combine_first(frame).loc[:, 'site']
    )
    frame.reset_index(
        level='site_index',
        drop=True,
        inplace=True,
    )
# pandas.options.display.max_rows = 20

index_column_names: List[str] = ['crop', 'site', 'date', 'field', ]
for sheet in (head_counts, sheet2):
    sheet.field = (
        sheet.field.str.extract(
            pat=r'(?P<text>\D*)(?P<number>\d*)').loc[:, 'number'].apply(
            pandas.to_numeric, downcast='integer'))

aphid_column_names: Dict[str, tuple] = {
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
aphid_column_names_level_names: List[str] = [
    'aphid_type', 'column_name']

aphid_column_names_deep: Dict[str, Dict[str, tuple]] = {
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
aphid_column_names_deep_level_names: List[str] = [
    'aphid_type', 'category', 'column_name']

s2_labels: Mapping[str, Iterable[str]] = {
    'id': (
        'index', 'unique',),
    'province': (
        'index', 'place',),
    'date': (
        'index', 'time',),
    'sample_by_week': (
        'not applicable',),
    'date_by_week': (
        'not applicable',),
    'julian_date': (
        'not applicable',),
    'site': (
        'index', 'place',),
    'field': (
        'index', 'place',),
    'crop': (
        'observation', 'crop', 'type',),
    'distance(m)': (
        'index', 'place',),
    'number of samples': (
        'not applicable',),
    'sitobion_avenae_ega_green (wingless)': (
        'observation', 'aphid', 'count', 'ega', 'apterous',),
    'sitobion_avenae_ega_red': (
        'observation', 'aphid', 'count', 'ega', 'uncategorized',),
    'ega alate': (
        'observation', 'aphid', 'count', 'ega', 'alate',),
    'bird_cherry_oat_aphid': (
        'observation', 'aphid', 'count', 'bco', 'uncategorized',),
    'greenbug_aphid': (
        'observation', 'aphid', 'count', 'greenbug', 'uncategorized',),
    'pea aphids': (
        'observation', 'aphid', 'count', 'pea', 'uncategorized',),
    'total_apterous_aphids': (
        'observation', 'aphid', 'count', 'uncategorized', 'apterous',),
    'total_alate_aphids': (
        'observation', 'aphid', 'count', 'uncategorized', 'apterous',),
    '4th_instar_pre-alate': (
        'observation', 'aphid', 'count', 'uncategorized', 'pre-alate',),
    '3rd_instar_ega': (
        'observation', 'aphid', 'count', 'ega', 'uncategorized',),
    '3rd_instar_ega_pre-alate': (
        'observation', 'aphid', 'count', 'ega', 'pre-alate',),
    '2nd_instar_ega': (
        'observation', 'aphid', 'count', 'ega', 'uncategorized',),
    '1st_instar_ega': (
        'observation', 'aphid', 'count', 'ega', 'uncategorized',),
    'aphid_mummies_aphelinus_black': (
        'not applicable',),
    'aphid_mummies_aphidius_brown': (
        'not applicable',),
    'aphid_mummies': (
        'not applicable',),
    'female_macrosteles_quadrilineatus': (
        'not applicable',),
    'male_macrosteles_quadrilineatus': (
        'not applicable',),
    'macrosteles_quadrilineatus nymphs': (
        'not applicable',),
    '1st_instar_macrosteles': (
        'not applicable',),
    '2nd_instar_macrosteles': (
        'not applicable',),
    '3rd_instar_macrosteles': (
        'not applicable',),
    '4th_instar_macrosteles': (
        'not applicable',),
    'athysanus_argentarius': (
        'not applicable',),
    'doratura_sp.': (
        'not applicable',),
    'errastunus_ocellaris_lh': (
        'not applicable',),
    'other_leafhoppers': (
        'not applicable',),
    'other coccinellid_adults': (
        'not applicable',),
    'hippodamia_tredecimpunctata_c13': (
        'not applicable',),
    'coccinella_septempunctata_c7': (
        'not applicable',),
    'ladybugs- larvae': (
        'not applicable',),
    'chrysopidae_adults': (
        'not applicable',),
    'chrysoperla_carnea_adult': (
        'not applicable',),
    'chrysopa_oculata_adult': (
        'not applicable',),
    'chrysoperla_carnea_larva': (
        'not applicable',),
    'chrysopa_oculata_larvae': (
        'not applicable',),
    'g_lacewing_larvae': (
        'not applicable',),
    'orius_tristicolor': (
        'not applicable',),
    'anthocoridae': (
        'not applicable',),
    '( damsel bug)nabis_americoferus_adult': (
        'not applicable',),
    'nabis_americoferus_nymph': (
        'not applicable',),
    'nabicula': (
        'not applicable',),
    'nabis_alternatus': (
        'not applicable',),
    'chalcid_wasps': (
        'not applicable',),
    'aphelinus_varipes': (
        'not applicable',),
    'aphelinus_asychis': (
        'not applicable',),
    'aphelinus_albipodus': (
        'not applicable',),
    'braconid_wasps': (
        'not applicable',),
    'aphidiius_sp.': (
        'not applicable',),
    'any parasitoid_adults': (
        'not applicable',),
    'hyperparasitoids ???': (
        'not applicable',),
    'aphidencyrtus_sp': (
        'not applicable',),
    'asaphes_suspensus': (
        'not applicable',),
    'flies': (
        'not applicable',),
    'lauxaniidae': (
        'not applicable',),
    'dolichopodidae': (
        'not applicable',),
    'syrphid_flies': (
        'not applicable',),
    'hoverflies': (
        'not applicable',),
    'female_delia_sp_1': (
        'not applicable',),
    'male_delia_sp_1': (
        'not applicable',),
    'female_delia_sp_2': (
        'not applicable',),
    'male_delia_sp_2': (
        'not applicable',),
    'anthomyiidae-delia': (
        'not applicable',),
    'midge': (
        'not applicable',),
    'lygus_punctatus': (
        'not applicable',),
    'lygus_elisus': (
        'not applicable',),
    'miridae_lygus lineolaris': (
        'not applicable',),
    'lygus_nymph': (
        'not applicable',),
    'green_grass_bugs_trigonotylus_coelestialium miridae': (
        'not applicable',),
    'green_grass nymphs': (
        'not applicable',),
    'capsus_simulans': (
        'not applicable',),
    'katydids': (
        'not applicable',),
    'thrips': (
        'not applicable',),
    'grasshoppers': (
        'not applicable',),
    'spiders': (
        'not applicable',),
    'spider_tetragnathidae': (
        'not applicable',),
    'mosquitoes': (
        'not applicable',),
    'dragonflies+damsel fly': (
        'not applicable',),
    'flea_beetles hop': (
        'not applicable',),
    'flea_beetles striped': (
        'not applicable',),
    'flea_beetles crucifer': (
        'not applicable',),
    'cicindela': (
        'not applicable',),
    'tychius_picirostris (weevil)': (
        'not applicable',),
    'bertha_armyworms': (
        'not applicable',),
    'shield_bugs': (
        'not applicable',),
    'worms': (
        'not applicable',),
    'beetles': (
        'not applicable',),
    'maggots': (
        'not applicable',),
    'stink_bugs (adult and nymph)': (
        'not applicable',),
    'red_mite': (
        'not applicable',),
    'moths': (
        'not applicable',),
    'plant_bugs': (
        'not applicable',),
    'pirate_bugs': (
        'not applicable',),
    'assassin_bug (reduviid bugs)': (
        'not applicable',),
    'bees': (
        'not applicable',),
    'harvestman': (
        'not applicable',),
    'treehoppers': (
        'not applicable',),
    'cabbage_butterfly': (
        'not applicable',),
    'caterpillar': (
        'not applicable',),
    'legume_bug': (
        'not applicable',),
    'chinch_bug': (
        'not applicable',),
    'ambush_bugs': (
        'not applicable',),
    'ichneumonidae': (
        'not applicable',),
    'pumace_flies (drosophilidae)': (
        'not applicable',),
    'scorpion_flies': (
        'not applicable',),
    'seed bugs (lygaeidea)': (
        'not applicable',),
    'seed_corn_beetles': (
        'not applicable',),
    'ufi_bugs': (
        'not applicable',),
    'wasps_other': (
        'not applicable',),
    'eulophid_wasp': (
        'not applicable',),
    'oribatid': (
        'not applicable',),
    'spider_mites': (
        'not applicable',),
    'springtails': (
        'not applicable',),
    'mollusks': (
        'not applicable',),
    'formicidae': (
        'not applicable',),
    'weevil': (
        'not applicable',),
    'lepidopteran_pupa': (
        'not applicable',),
    'unnamed: 129': (
        'not applicable',),
    'hymenoptera_proctotrupidae': (
        'not applicable',),
    'hymenoptera_pteromalidae': (
        'not applicable',),
    'hymenoptera_apidae': (
        'not applicable',),
    'hymenoptera_diplazontinae': (
        'not applicable',),
    'hymenoptera_figitidae': (
        'not applicable',),
    'hymenoptera_aphelinidae': (
        'not applicable',),
    'hymenoptera_perilampidae': (
        'not applicable',),
    'hymenoptera_chalcidoidea': (
        'not applicable',),
    'hymenoptera_ichneumondoidea': (
        'not applicable',),
    'hymenoptera_proctotrupoidea': (
        'not applicable',),
}

indexed_frames: Tuple[DataFrame, DataFrame] = (
    hc_indexed, s2_indexed)
sheets_to_compare_: Dict[str, DataFrame] = dict(
    zip(sheet_names, indexed_frames))

hc_ega_sums: DataFrame = pandas.concat(
    {
        'head + leaf':
            (head_counts['ega_head'] + head_counts['ega_leaf']),
        'apt + alate':
            (head_counts['ega_apt'] + head_counts['ega_alate']),
        'reg + grn':
            (head_counts['ega_red'] + head_counts['ega_grn']),
    },
    axis='columns',
)

index_columns: List[str] = ['date', 'site', 'crop', 'field']

hc_column_names: pandas.Index = head_counts.columns
