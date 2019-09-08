import load_table_functions as load
import pickle

###  File 0016 - Body Measures  ###

## Column Mappings ##
cols_0016 = {'SEQN':['subject_id','Respondent sequence number'],
             'BMXWT':['subject_body_weight_kg','Weight (kg)'],
             'BMXHT':['subject_body_hight_cm','Standing Height (cm)'],
             'BMXBMI':['subject_body_bmi','Body Mass Index (kg/m**2)']
            }

## Create Table ##
tables = ['0016','0015','0016','0013']
studies = [25501,25502,25503,25504]
col_dict = cols_0016
df_0016 = load.create_tables_multiyear(tables,col_dict,studies)

## Fix Data ##
df_0016 = df_0016.replace({'subject_body_weight_kg':' ', 'subject_body_hight_cm':' ', 'subject_body_bmi':' '}, 0).astype(float)
df_0016 = df_0016.astype({'subject_body_weight_kg':float, 'subject_body_hight_cm':float, 'subject_body_bmi':float})

## Pickle Data ##
with open('../pickle_data/ds0016.pkl', 'wb') as picklefile:
    pickle.dump(df_0016, picklefile)
