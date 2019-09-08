import load_table_functions as load
import pandas as pd
import pickle

###  File 0226 (25501-0226) - Medical Conditions  ###
###  File 0226 (25502-0227) - Medical Conditions  ###
###  File 0226 (25503-0227) - Medical Conditions  ###
###  File 0226 (25504-0227) - Medical Conditions  ###

### 25504

## Column Mappings ##
cols_0226 = {'SEQN':['subject_id','Respondent sequence number'],
             'MCQ160B':['subject_heart_fail','Ever told had congestive heart failure'],
             'MCQ160C':['subject_heart_disease','Ever told you had coronary heart disease'],
             'MCQ160E':['subject_heart_attack','Ever told you had heart attack'],
             'MCQ180B':['subject_heart_fail_age','Age when told you had heart failure'],
             'MCQ180C':['subject_heart_disease_age','Age when told had coronary heart disease'],
             'MCQ180E':['subject_heart_attack_age','Age when told you had heart attack']
             }


## Create Table ##
tables = ['0226','0227','0227','0227']
studies = [25501,25502,25503,25504]
col_dict = cols_0226
df_0226 = load.create_tables_multiyear(tables,col_dict,studies)



## Fix Data ##
mappings = {i:' ' for i in df_0226.columns} # format will look like {'col1':' ','col2':' '....}
df_0226 = df_0226.replace(mappings, 0).astype(int)
df_0226['subject_heart_fail'] = (df_0226['subject_heart_fail'] == 1) * 1
df_0226['subject_heart_disease'] = (df_0226['subject_heart_disease'] == 1) * 1
df_0226['subject_heart_attack'] = (df_0226['subject_heart_attack'] == 1) * 1
df_0226 = df_0226.replace([77777,99999], 0)

## Pickle Data ##
with open('../pickle_data/ds0226.pkl', 'wb') as picklefile:
    pickle.dump(df_0226, picklefile)