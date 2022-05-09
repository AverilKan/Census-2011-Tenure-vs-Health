import itertools

import pandas as pd
import math
import numpy as np

gh_eth_sex_age = pd.read_csv('./gh_eth_sex_age.csv', delimiter=None, header=None)
print(gh_eth_sex_age)

tables = []

# population = []
# units = []
sex = []
age = []
NS_SeC = []

lines_per_table = 373
col_names = nssec_eth_sex_age.loc[9]
num_of_tables = len(nssec_eth_sex_age) // 373 + 1
#
# for table_id in range(num_of_tables):
#     start_id = lines_per_table * table_id
#     end_id = (lines_per_table * (table_id + 1)) - 1
#
#     tmp_table = nssec_eth_sex_age.loc[start_id: end_id]
#
#     # record table attribute
#     sex.append(nssec_eth_sex_age.iloc[5 + start_id].values[1])  # sex
#     age.append(nssec_eth_sex_age.iloc[6 + start_id].values[1])  # age
#     NS_SeC.append(nssec_eth_sex_age.iloc[7 + start_id].values[1])  # NS_SeC
#
#     # extract true table
#     true_table = tmp_table.loc[11 + start_id:end_id - 14]
#
#     # modify header
#     true_table = true_table.rename(columns=col_names)
#
#     # remove rows with nan
#     true_table = true_table.dropna()
#     tables.append(true_table)
#
# # print(tables[1])
#
# def trans_to_percentage_col_opp(input_table):
#     need_trans_col_name = list(col_names[2:])
#     for col_name in need_trans_col_name:
#         # change object to numeric
#         input_table[col_name] = pd.to_numeric(input_table[col_name])
#         input_table["All categories: Ethnic group"] = pd.to_numeric(input_table["All categories: Ethnic group"])
#         input_table[col_name] = input_table[col_name] / input_table["All categories: Ethnic group"]
#     return input_table
#
# # trans = trans_to_percentage_col_opp(tables[1])
# # print(trans)
#
# # def trans_to_percentage_row_opp(input_table):
# #     for row in range(len(input_table)):
# #         input_table.iloc[:,1] = pd.to_numeric(input_table.iloc[:,1])
# #         input_table.iloc[row, 1] = input_table.iloc[row, 1] / input_table.iloc[0, 1]
# #
# #     return input_table
# #
# # # trans = trans_to_percentage_row_opp(trans_to_percentage_col_opp(tables[1]))
# # # print(trans)
#
# # find unique tags for id process
# sex_tags = list(set(sex))
# age_tags = list(set(age))
#
# NS_SeC_tags = list(set(NS_SeC))
# combinations = list(itertools.product(sex_tags, age_tags))
#
#
# # function to get table ids
# def get_ids(NS_SeC_tag, sex_tag, age_tag):
#     ids = []
#     for id in range(len(NS_SeC_tag)):
#         if NS_SeC_tag[id] in NS_SeC_tag and sex[id] in sex_tag and age[id] in age_tag:
#             ids.append(id)
#     return ids
#
#
# # create df for tags: All persons, All ages to compare  NS-sec
#
# NS_SeC_compare_ids = get_ids(NS_SeC_tags, 'All persons', 'All categories: Age 16 and over')
# occupation_vs_area = pd.DataFrame()
# cols = []
#
# for id in NS_SeC_compare_ids:
#     tmp_lst = list(tables[id].iloc[:, 1])
#     cols.append(NS_SeC[id])
#     occupation_vs_area[id] = tmp_lst
#
# occupation_vs_area.columns = cols
# # cols = cols[1:]
#
# for col_name in cols[1:]:
#     occupation_vs_area[col_name] = pd.to_numeric(occupation_vs_area[col_name])
#     occupation_vs_area['All categories: NS-SeC'] = pd.to_numeric(occupation_vs_area['All categories: NS-SeC'])
#     occupation_vs_area[col_name] = occupation_vs_area[col_name] / occupation_vs_area['All categories: NS-SeC']
#
# occupation_vs_area['All categories: NS-SeC'] = 1
# # occupation_vs_area = occupation_vs_area.drop(columns='All categories: NS-SeC')
#
#
# # combined tables for 1 output table
# final_table = pd.DataFrame()
#
# for comb_id, comb in enumerate(combinations):
#     ids = get_ids(NS_SeC_tags, comb[0], comb[1])
#     for id in ids:
#         tmp_table = trans_to_percentage_col_opp(tables[id])
#         tmp_table.reset_index(inplace=True)
#         tmp_table['% of occupation in area'] = occupation_vs_area[NS_SeC[id]]
#
#         # tmp_table = trans_to_percentage_row_opp(trans_to_percentage_col_opp(tables[id]))
#         tmp_table = tmp_table.melt(id_vars=['local authority: district / unitary (prior to April 2015)', '% of occupation in area'], value_vars=list(col_names[2:]))
#
#         tmp_table.rename(columns={'value': 'percentage of people in ethnic group', 'variable': 'ethnic group'}, inplace=True)
#         tmp_table['NS_SeC'] = NS_SeC[id]
#         tmp_table['sex'] = sex[id]
#         tmp_table['age'] = age[id]
#
#         final_table = pd.concat([final_table,  tmp_table])
#
# final_table.reset_index(inplace=True)
# final_table.drop(columns='index', inplace=True)
# # print(final_table)
#
# final_table.to_csv('./complete.csv')




