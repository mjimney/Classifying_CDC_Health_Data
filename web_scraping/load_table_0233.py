import load_table_functions as load
import pickle

###  File 0233 - Physical Activity (Subject Summary)  ###

## Column Mappings ##
cols_0233 = {'SEQN':['subject_id','Respondent sequence number'],
             'PAD020':['subject_act_wb','Walked or bicycled over past 30 days'],
             'PAD080':['subject_act_wb_l','Walked or bicycled - How long per day (minutes)'],
             'PAQ100':['subject_act_hw','Tasks around home/yard past 30 days'],
             'PAQ180':['subject_act_avg','Avg level of physical activity each day'],
             'PAD200':['subject_act_vig','Vigorous activity over past 30 days'],
             'PAD320': ['subject_act_mod', 'Moderate activity over past 30 days'],
             'PAD440': ['subject_act_lift', 'Muscle strengthening activities'],
             'PAD460': ['subject_act_lift_fq', 'Number of times past 30 days'],
            }

## Value Mappings for Columns ##
map_subject_act_avg = {7:0, 9:0}
map_subject_act_tv = {6:0, 77:0, 99:0}

## Create Table ##
tables = ['0233','0233','0233','0231']
studies = [25501,25502,25503,25504]
col_dict = cols_0233
df_0233 = load.create_tables_multiyear(tables,col_dict,studies)

## Fix Data ##
mappings = {i:' ' for i in df_0233.columns} # format will look like {'col1':' ','col2':' '....}
df_0233 = df_0233.replace(mappings, 0).astype(int)
df_0233['subject_act_wb'] = (df_0233['subject_act_wb'] == 1) * 1
df_0233['subject_act_hw'] = (df_0233['subject_act_hw'] == 1) * 1
df_0233['subject_act_comb'] = (df_0233['subject_act_wb'] + df_0233['subject_act_hw']).replace(2,1)
df_0233['subject_act_avg'].replace(map_subject_act_avg,inplace=True)
df_0233['subject_act_vig'] = (df_0233['subject_act_vig'] == 1) * 1
df_0233['subject_act_mod'] = (df_0233['subject_act_mod'] == 1) * 1
df_0233['subject_act_lift'] = (df_0233['subject_act_lift'] == 1) * 1

## Drop Columns ##
df_0233.drop(columns=['subject_act_wb','subject_act_wb_l',
                      'subject_act_hw','subject_act_avg',
                      'subject_act_lift_fq'],inplace=True)

## Pickle Data ##
with open('../pickle_data/ds0233.pkl', 'wb') as picklefile:
    pickle.dump(df_0233, picklefile)

