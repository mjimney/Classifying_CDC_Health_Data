import load_table_functions as load
import pickle

###  File 0001 - Demographics  ###

## Column Mappings ##
cols_0001 = {'SEQN':['subject_id','Respondent sequence number'],
             'RIDSTATR':['subject_int_status','Interview/Examination Status'], #Make sure only looking at "both Interviewed and MEC examined"
             'RIAGENDR':['subject_gender','Gender'],
             'RIDAGEYR':['subject_age','Age'],            
             'RIDRETH1':['subject_eth','Race/Ethnicity'],
             'DMDCITZN':['subject_cit','Citizenship Status'],
             'DMDEDUC3':['subject_edu_y','Education level - Children/Youth 6-19'],
             'DMDEDUC2':['subject_edu_a','Education level - Adults 20+'],
             'DMDSCHOL':['subject_edu_s','Now attending school?'],
             'DMDHHSIZ':['subject_house_size','Total number of people in the Household'],
             'INDFMINC':['subject_income_f','Annual Family Income'],
             'RIDEXPRG':['subject_preg','Pregnancy Status at Exam']
            }

## Value Mappings for Columns ##
map_subject_income_f = {'1':3, '2':7, '3':13, '4':17, '5':23, '6':30, '7':40,
                        '8':50,'9':60, '10':70, '11':100, '12':50, '13':3, '77':0, '99':0, ' ':0}
map_subject_cit = {'1':0, '2':1, '7':1, '9':1, ' ':1, 1:0, 2:1, 7:1, 9:1}
map_subject_preg = {'1':1, '2':0, '3':0, ' ':0}


## Create Table ##
tables = ['0001','0001','0001','0001']
studies = [25501,25502,25503,25504]
col_dict = cols_0001
df_0001 = load.create_tables_multiyear(tables,col_dict,studies,add_study=True)


## Fix Data ##
df_0001 = df_0001[df_0001['subject_int_status'] == 2]  # Filtering out ppl who did not take the survey
df_0001['subject_gender'].replace(2,0,inplace=True) # F=0,M=1
# df_0001 = df_0001[df_0001['subject_age'] >= 18]  # Moved to modeling sheet
df_0001['subject_cit'].replace(map_subject_cit,inplace=True) # 0=citizen,1=not citz
df_0001['subject_income_f'].replace(map_subject_income_f,inplace=True) # interum step
df_0001['subject_preg'].replace(map_subject_preg,inplace=True) # interum step
df_0001 = df_0001[df_0001['subject_preg'] == 0]  # Filtering out ppl who did not take the survey

## Drop Columns ##
df_0001.drop(columns=['subject_edu_y','subject_edu_a','subject_edu_s','subject_preg','subject_int_status']
             ,inplace=True) # dropping EDU columns for now

## Pickle Data ##
with open('../pickle_data/ds0001.pkl', 'wb') as picklefile:
    pickle.dump(df_0001, picklefile)

