import load_table_functions as load
import pickle

###  File 0210 - Diabetes  ###

## Column Mappings ##
cols_0210 = {'SEQN':['subject_id','Respondent sequence number'],
             'DIQ010':['subject_diab','Doctor told you have diabetes'] # 1=Yes
            }

## Value Mappings for Columns ##
map_subject_diab = {'1':1, '2':0, '3':0, '7':0, '9':0, ' ':0, 1:1, 2:0, 3:0, 7:0, 9:0}

## Create Table ##
tables = ['0210','0211','0210','0217']
studies = [25501,25502,25503,25504]
col_dict = cols_0210
df_0210 = load.create_tables_multiyear(tables,col_dict,studies)

## Fix Data ##
df_0210['subject_diab'].replace(map_subject_diab,inplace=True)

## Pickle Data ##
with open('../pickle_data/ds0210.pkl', 'wb') as picklefile:
    pickle.dump(df_0210, picklefile)

