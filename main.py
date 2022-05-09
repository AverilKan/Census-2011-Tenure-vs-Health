import itertools

import pandas as pd
import math
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import umap
import time

"""
nssec_eth_sex_age = pd.read_csv('./nssec_eth_sex_age_4.csv', delimiter=None, header=None)
# print(nssec_eth_sex_age)

tables = []

# population = []
# units = []
sex = []
age = []
NS_SeC = []

lines_per_table = 373
col_names = nssec_eth_sex_age.loc[9]
num_of_tables = len(nssec_eth_sex_age) // 373 + 1

for table_id in range(num_of_tables):
    start_id = lines_per_table * table_id
    end_id = (lines_per_table * (table_id + 1)) - 1

    tmp_table = nssec_eth_sex_age.loc[start_id: end_id]

    # record table attribute
    sex.append(nssec_eth_sex_age.iloc[5 + start_id].values[1])  # sex
    age.append(nssec_eth_sex_age.iloc[6 + start_id].values[1])  # age
    NS_SeC.append(nssec_eth_sex_age.iloc[7 + start_id].values[1])  # NS_SeC

    # extract true table
    true_table = tmp_table.loc[11 + start_id:end_id - 14]

    # modify header
    true_table = true_table.rename(columns=col_names)

    # remove rows with nan
    true_table = true_table.dropna()
    tables.append(true_table)

# print(tables[1])

def trans_to_percentage_col_opp(input_table):
    need_trans_col_name = list(col_names[2:])
    for col_name in need_trans_col_name:
        # change object to numeric
        input_table[col_name] = pd.to_numeric(input_table[col_name])
        input_table["All categories: Ethnic group"] = pd.to_numeric(input_table["All categories: Ethnic group"])
        input_table[col_name] = input_table[col_name] / input_table["All categories: Ethnic group"]
    return input_table

# trans = trans_to_percentage_col_opp(tables[1])
# print(trans)

# def trans_to_percentage_row_opp(input_table):
#     for row in range(len(input_table)):
#         input_table.iloc[:,1] = pd.to_numeric(input_table.iloc[:,1])
#         input_table.iloc[row, 1] = input_table.iloc[row, 1] / input_table.iloc[0, 1]
#
#     return input_table
#
# # trans = trans_to_percentage_row_opp(trans_to_percentage_col_opp(tables[1]))
# # print(trans)

# find unique tags for id process
sex_tags = list(set(sex))
age_tags = list(set(age))

NS_SeC_tags = list(set(NS_SeC))
combinations = list(itertools.product(sex_tags, age_tags))


# function to get table ids
def get_ids(NS_SeC_tag, sex_tag, age_tag):
    ids = []
    for id in range(len(NS_SeC_tag)):
        if NS_SeC_tag[id] in NS_SeC_tag and sex[id] in sex_tag and age[id] in age_tag:
            ids.append(id)
    return ids


# create df for tags: All persons, All ages to compare  NS-sec

NS_SeC_compare_ids = get_ids(NS_SeC_tags, 'All persons', 'All categories: Age 16 and over')
occupation_vs_area = pd.DataFrame()
cols = []

for id in NS_SeC_compare_ids:
    tmp_lst = list(tables[id].iloc[:, 1])
    cols.append(NS_SeC[id])
    occupation_vs_area[id] = tmp_lst

occupation_vs_area.columns = cols
# cols = cols[1:]

for col_name in cols[1:]:
    occupation_vs_area[col_name] = pd.to_numeric(occupation_vs_area[col_name])
    occupation_vs_area['All categories: NS-SeC'] = pd.to_numeric(occupation_vs_area['All categories: NS-SeC'])
    occupation_vs_area[col_name] = occupation_vs_area[col_name] / occupation_vs_area['All categories: NS-SeC']

occupation_vs_area['All categories: NS-SeC'] = 1
# occupation_vs_area = occupation_vs_area.drop(columns='All categories: NS-SeC')


# combined tables for 1 output table
final_table = pd.DataFrame()

for comb_id, comb in enumerate(combinations):
    ids = get_ids(NS_SeC_tags, comb[0], comb[1])
    for id in ids:
        tmp_table = trans_to_percentage_col_opp(tables[id])
        tmp_table.reset_index(inplace=True)
        tmp_table['% of occupation in area'] = occupation_vs_area[NS_SeC[id]]

        # tmp_table = trans_to_percentage_row_opp(trans_to_percentage_col_opp(tables[id]))
        tmp_table = tmp_table.melt(id_vars=['local authority: district / unitary (prior to April 2015)', '% of occupation in area'], value_vars=list(col_names[2:]))

        tmp_table.rename(columns={'value': 'percentage of people in ethnic group', 'variable': 'ethnic group'}, inplace=True)
        tmp_table['NS_SeC'] = NS_SeC[id]
        tmp_table['sex'] = sex[id]
        tmp_table['age'] = age[id]

        final_table = pd.concat([final_table,  tmp_table])

final_table.reset_index(inplace=True)
final_table.drop(columns='index', inplace=True)
# print(final_table)

final_table.to_csv('./complete.csv')

"""


gh_ten_age = pd.read_csv('./gh_ten_age.csv', delimiter=None, header=None)
# print(gh_ten_age)

tables = []

# population = []
# units = []
# sex = []
age = []
general_health = []

lines_per_table = 372
col_names = gh_ten_age.loc[8]
num_of_tables = len(gh_ten_age) // 372 + 1

for table_id in range(num_of_tables):
    start_id = lines_per_table * table_id
    end_id = (lines_per_table * (table_id + 1)) - 1

    tmp_table = gh_ten_age.loc[start_id: end_id]

    # record table attribute
    # sex.append(gh_ten_age.iloc[5 + start_id].values[1])  # sex
    age.append(gh_ten_age.iloc[5 + start_id].values[1])  # age
    # disability.append(gh_eth_sex_age.iloc[7 + start_id].values[1])  # economic_activity
    general_health.append(gh_ten_age.iloc[6 + start_id].values[1])

    # extract true table
    true_table = tmp_table.loc[10 + start_id:end_id - 14]

    # modify header
    true_table = true_table.rename(columns=col_names)

    # remove rows with nan
    true_table = true_table.dropna()
    tables.append(true_table)


# print(tables[1])

def trans_to_percentage_col_opp(input_table):
    need_trans_col_name = list(col_names[2:])
    for col_name in need_trans_col_name:
        # change object to numeric
        input_table[col_name] = pd.to_numeric(input_table[col_name])
        input_table["All categories: Tenure"] = pd.to_numeric(input_table["All categories: Tenure"])
        input_table[col_name] = input_table[col_name] / input_table["All categories: Tenure"]
    return input_table

# trans = trans_to_percentage_col_opp(tables[1])
# print(trans)

# find unique tags for id process
age_tags = list(set(age))
general_health_tags = ['Bad or very bad health', 'Very good or good health', 'Fair health']

# function to get table ids
def get_ids(general_health_tag, age_tag):
    ids = []
    for id in range(len(tables)):
        # if general_health[id] in general_health_tag and sex[id] in sex_tag and age[id] in age_tag:
        if general_health[id] in general_health_tag and age[id] in age_tag:
            ids.append(id)
    return ids

# function to get table ids
# def get_ids(NS_SeC_tag, sex_tag, age_tag):
#     ids = []
#     for id in range(len(NS_SeC_tag)):
#         if NS_SeC_tag[id] in NS_SeC_tag and sex[id] in sex_tag and age[id] in age_tag:
#             ids.append(id)
#     return ids


# combined tables for 1 output table
# final_table = pd.DataFrame()
#
# for comb_id, comb in enumerate(age_tags):
#     ids = get_ids(general_health_tags, comb)
#     total_id_health = get_ids('All categories: General health', comb)
#
#     for id in ids:
#         tabs = pd.to_numeric(tables[id].iloc[:, 1])
#         tot = pd.to_numeric(tables[total_id_health[0]].iloc[:, 1])
#
#         tmp_table = trans_to_percentage_col_opp(tables[id])
#
#         tmp_table['health rate'] = tabs.values / tot.values
#
#         # tmp_table.reset_index(inplace=True, drop=True)
#         tmp_table = tmp_table.melt(id_vars=['local authority: district / unitary (prior to April 2015)', 'health rate'], value_vars=list(col_names[2:]))
#
#         tmp_table.rename(columns={'value': 'Percentage of people in Tenure group', 'variable': 'Tenure group'}, inplace=True)
#         tmp_table['general_health'] = general_health[id]
#         tmp_table['age'] = age[id]
#
#         final_table = pd.concat([final_table,  tmp_table])
#
# final_table.reset_index(inplace=True)
# final_table.drop(columns='index', inplace=True)
# #final_table[]
# # print(final_table)

# final_table.to_csv('./complete_gh_ten.csv')


# =========================================== health embedding ==================================================
#
# apply pca
final_table = pd.DataFrame()

for comb_id, comb in enumerate(age_tags):
    ids = get_ids(general_health_tags, comb)
    total_id = get_ids('All categories: General health', comb)

    for id in ids:
        tabs = pd.to_numeric(tables[id].iloc[:, 1])
        tot = pd.to_numeric(tables[total_id[0]].iloc[:, 1])

        tmp_table = trans_to_percentage_col_opp(tables[id])

        tmp_table['% of health class x in area'] = tabs.values / tot.values
        # tmp_table.reset_index(inplace=True, drop=True)
        # tmp_table = tmp_table.melt(id_vars=['local authority: district / unitary (prior to April 2015)', '% of health class x in area'], value_vars=list(col_names[2:]))

        tmp_table.rename(columns={'value': 'Percentage of people in Tenure group', 'variable': 'Tenure group'}, inplace=True)
        tmp_table['general_health'] = general_health[id]
        tmp_table['age'] = age[id]

        final_table = pd.concat([final_table,  tmp_table])

final_table.reset_index(inplace=True)
final_table.drop(columns='index', inplace=True)

map_table = final_table.drop(columns=['local authority: district / unitary (prior to April 2015)',
                                 'general_health',
                                 'age',
                                 'All categories: Tenure'])

time_start = time.time()
model = umap.UMAP(n_components=2, n_neighbors=50, min_dist=0.25)
health_score = model.fit_transform(map_table)
print('UMAP done! Time elapsed: {} seconds'.format(time.time()-time_start))

time_start = time.time()
model = PCA(n_components=2)
health_score = model.fit_transform(map_table)
print('PCA done! Time elapsed: {} seconds'.format(time.time()-time_start))

health_score = pd.DataFrame(health_score, columns = ['Age embedding 1','Age embedding 2'])

final_table = final_table.drop(columns = ['Owned: Owned outright',
                               'Owned: Owned with a mortgage or loan or shared ownership',
                               'Rented: Social rented',
                               'Rented: Private rented or living rent free',
                               '% of health class x in area'])

final_table = final_table.join(health_score)
# print(final_table)
# final_table.to_csv('./umap age.csv')


# =========================================== health rate ==================================================
#
# final_table = pd.DataFrame()
#
# for comb_id, comb in enumerate(general_health_tags):
#     ids = get_ids(comb, age_tags)
#     total_id = get_ids(comb, 'All categories: Ages')
#
#     for id in ids:
#         tabs = pd.to_numeric(tables[id].iloc[:, 1])
#         tot = pd.to_numeric(tables[total_id[0]].iloc[:, 1])
#
#         tmp_table = trans_to_percentage_col_opp(tables[id])
#
#         tmp_table['health rate'] = tabs.values / tot.values
#
#         # tmp_table.reset_index(inplace=True, drop=True)
#         tmp_table = tmp_table.melt(id_vars=['local authority: district / unitary (prior to April 2015)', 'health rate'], value_vars=list(col_names[2:]))
#
#         tmp_table.rename(columns={'value': 'Percentage of people in Tenure group', 'variable': 'Tenure group'}, inplace=True)
#         tmp_table['general_health'] = general_health[id]
#         tmp_table['age'] = age[id]
#
#         final_table = pd.concat([final_table,  tmp_table])
#
# final_table.reset_index(inplace=True)
# final_table.drop(columns='index', inplace=True)
# #final_table[]
# # print(final_table)
# final_table.to_csv('./complete_gh_ten_hr.csv')
