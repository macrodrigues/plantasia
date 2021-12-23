#%% IMPORTS
import pandas as pd
import os

#%% DIRECTORIES
PATH = os.path.dirname(os.path.dirname(__file__))
PATH_DATA = f"{PATH}/data/info.json"
PATH_IMG = f"{PATH}/images/"
PATH_UTILS = f"{PATH}/utils/"
df = pd.read_json(PATH_DATA)
labels = df.columns.tolist()
str_no_species = ''
#%% OBTAIN ARRAYS

def get_species_array(df):
    if df.empty:
        return [str_no_species]
    res = df[labels[0]].values.tolist()
    res.sort()
    return res

def get_families_array(df):
    if df.empty:
        return [str_no_species]
    res = list(set(df[labels[1]].values))
    res.sort()
    return res

def get_descriptions_array(df):
    if df.empty:
        return [str_no_species]
    res = list(df[labels[2]].values)
    res.sort()
    return res

def get_properties_array(df):
    if df.empty:
        return [str_no_species]
    res = df[labels[3]].values.tolist()
    res = list(set(item for sublist in res for item in sublist))
    res.sort()
    return res

def get_side_effects_array(df):
    if df.empty:
        side_effects = [str_no_species]
        return side_effects
    res = df[labels[4]].values.tolist()
    res.sort()
    res = list(set(item for sublist in res for item in sublist))
    return res

#%% TOOLS

def convert_list(properties):
    res = []
    for p in properties:
        p_to_string = '\n\n - ' + p
        res.append(p_to_string)

    return ''.join(res)

def get_species_by_family(df, family):
    df_family = df.loc[df['family'] == family]
    return df_family['specie'].values.tolist()

def get_species_by_properties(df, property):
    species = []
    for i, item in df.iterrows():
        if property in item.properties:
            species.append(item.specie)
    return species


#%% RESULTS
species = get_species_array(df)
descriptions = get_descriptions_array(df)
properties = get_properties_array(df)
families = get_families_array(df)
side_effects = get_side_effects_array(df)
options_labels = ['Species', 'Families', 'Properties']
set_file = 0
