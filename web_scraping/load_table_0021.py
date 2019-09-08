import load_table_functions as load
import pandas as pd
import pickle

###  File 0021 (25501-0021) - Diet (Individual Foods)  ###
###  File 0021 (25502-0021) - Diet (Individual Foods)  ###
###  File 0021 (25503-0022) - Diet (Individual Foods - Day 1)  ###
###  File 0021 (25504-0015) - Diet (Individual Foods - Day 1)  ###

## Column Mappings ##
cols_0021_01 = {'SEQN':['subject_id','Respondent sequence number'],
                'DRXILINE':['fd_entry','Food component number'],
                'DRXCCMNM':['fd_combo_num','Combination food number'],
                'DRDCCMTY':['fd_type','Combination food type'],
                'DRD020':['fd_time','Time of eating occasion (HH:MM)'],  # mostly blank in 01
                'DRD030':['fd_meal','Meal name'],
                'DRD040':['fd_home','Meal place'],
                'DRDIFDCD':['fd_usda_code','USDA food code'],
                'DRXIGRMS':['fd_g','Grams'],
                'DRXIKCAL':['fd_cal','Energy (kcal)'],
                'DRXIPROT':['fd_p','Protein (gm)'],
                'DRXICARB':['fd_carb','Carbohydrate (gm)'],
                'DRXITFAT':['fd_f','Total fat (gm)'],
                'DRXICHOL':['fd_chol', 'Cholesterol (mg)'],
                'DRXIFIBE':['fd_df', 'Dietary fiber (gm)'],
                'DRDISODI':['fd_sod', 'Sodium (mg)'],
                'DRXICAFF':['fd_caf', 'Caffeine (mg)'],
                'DRXIALCO':['fd_alc', 'Alcohol (gm)']
                }

cols_0021_02 = {'SEQN':['subject_id','Respondent sequence number'],
                'DRXILINE':['fd_entry','Food component number'],
                'DRXCCMNM':['fd_combo_num','Combination food number'],
                'DRDCCMTZ':['fd_type','Combination food type'],
                'DRD020':['fd_time','Time of eating occasion (HH:MM)'],  # mostly blank in 01
                'DRD030Z':['fd_meal','Meal name'],
                'DRD040Z':['fd_home','Meal place'],
                'DRDIFDCD':['fd_usda_code','USDA food code'],
                'DRXIGRMS':['fd_g','Grams'],
                'DRXIKCAL':['fd_cal','Energy (kcal)'],
                'DRXIPROT':['fd_p','Protein (gm)'],
                'DRXICARB':['fd_carb','Carbohydrate (gm)'],
                'DRXIFIBE':['fd_df', 'Dietary fiber (gm)'],
                'DRXITFAT':['fd_f','Total fat (gm)'],
                'DRXICHOL':['fd_chol', 'Cholesterol (mg)'],
                'DRDISODI':['fd_sod', 'Sodium (mg)'],
                'DRXICAFF': ['fd_caf', 'Caffeine (mg)'],
                'DRXIALCO':['fd_alc', 'Alcohol (gm)']
                }

cols_0021_03 = {'SEQN':['subject_id','Respondent sequence number'],
                'DR1ILINE':['fd_entry','Food component number'],
                'DR1CCMNM':['fd_combo_num','Combination food number'],
                'DR1CCMTX':['fd_type','Combination food type'],
                'DR1_020':['fd_time','Time of eating occasion (HH:MM)'],  # mostly blank in 01
                'DR1_030Z':['fd_meal','Meal name'],
                'DR1_040Z':['fd_home','Meal place'],  ### change so home is 1, other is 0
                'DR1IFDCD':['fd_usda_code','USDA food code'],
                'DR1IGRMS':['fd_g','Grams'],
                'DR1IKCAL':['fd_cal','Energy (kcal)'],
                'DR1IPROT':['fd_p','Protein (gm)'],
                'DR1ICARB':['fd_carb','Carbohydrate (gm)'],
                'DR1IFIBE':['fd_df', 'Dietary fiber (gm)'],
                'DR1ITFAT':['fd_f','Total fat (gm)'],
                'DR1ICHOL':['fd_chol', 'Cholesterol (mg)'],
                'DR1ISODI':['fd_sod', 'Sodium (mg)'],
                'DR1ICAFF':['fd_caf', 'Caffeine (mg)'],
                'DR1IALCO':['fd_alc', 'Alcohol (gm)']
                }

cols_0021_04 = {'SEQN':['subject_id','Respondent sequence number'],
                'DR1ILINE':['fd_entry','Food component number'],
                'DR1CCMNM':['fd_combo_num','Combination food number'],
                'DR1CCMTX':['fd_type','Combination food type'],
                'DR1_020':['fd_time','Time of eating occasion (HH:MM)'],  # mostly blank in 01
                'DR1_030Z':['fd_meal','Meal name'],
                'DR1_040Z':['fd_home','Meal place'],  ### change so home is 1, other is 0
                'DR1IFDCD':['fd_usda_code','USDA food code'],
                'DR1IGRMS':['fd_g','Grams'],
                'DR1IKCAL':['fd_cal','Energy (kcal)'],
                'DR1IPROT':['fd_p','Protein (gm)'],
                'DR1ICARB':['fd_carb','Carbohydrate (gm)'],
                'DR1IFIBE':['fd_df', 'Dietary fiber (gm)'],
                'DR1ITFAT':['fd_f','Total fat (gm)'],
                'DR1ICHOL':['fd_chol', 'Cholesterol (mg)'],
                'DR1ISODI':['fd_sod', 'Sodium (mg)'],
                'DR1ICAFF':['fd_caf', 'Caffeine (mg)'],
                'DR1IALCO':['fd_alc', 'Alcohol (gm)']
                }


## Value Mappings for Columns ##

map_fd_type_cat01 = {0:'non-combo',1:'other',2:'beans and veggies',3:'drink',4:'bread',5:'cereal',6:'other',7:'bread',8:'dessert',9:'other',10:'meat, poultry, fish',11:'frozen meal',12:'fruit',
                     13:'bread',14:'meat, poultry, fish',15:'other',17:'meat, poultry, fish',18:'salad',19:'salad',20:'sandwich',21:'soup',22:'tortilla',23:'beans and veggies',90:'other'}

map_fd_type_cat02 = {0:'non-combo',1:'drink',2:'cereal',3:'bread',4:'salad',5:'sandwich',6:'soup',7:'frozen meal',8:'dessert',9:'beans and veggies',10:'fruit',11:'tortilla',12:'meat, poultry, fish',13:'other',14:'other',90:'other'}

map_fd_meal = {6:0,7:6,9:1,10:2,11:3,12:4,13:5,14:4,15:4,16:4,99:0}

map_fd_meal_cat = {1:'Breakfast',2:'Brunch',3:'Lunch',4:'Snack/beverage',5:'Dinner',6:'Other',7:'Extended consumption',8:'Other',9:'Breakfast',10:'Brunch',11:'Lunch',12:'Snack/beverage',
                   13:'Dinner',14:'Snack/beverage',15:'Snack/beverage',16:'Snack/beverage',17:'Snack/beverage',18:'Snack/beverage',19:'Snack/beverage',91:'Other',99:'Other'}

###################################

## Create Table 01 ##
tables = ['0021']
studies = [25501]
col_dict = cols_0021_01
df_0021a = load.create_tables_multiyear(tables,col_dict,studies,inx='fd_entry')

## Fix Data 01 ##
mappings = {i:' ' for i in df_0021a.loc[:,'fd_g':].columns} # format will look like {'col1':' ','col2':' '....}
df_0021a.loc[:,'fd_g':] = df_0021a.loc[:,'fd_g':].replace(mappings, 0).astype(float)
df_0021a['fd_home'] = (df_0021a['fd_home'] == 9) * 1  # making "home" (9) to 1, others to 0
df_0021a['fd_meal'] = df_0021a['fd_meal'].replace(map_fd_meal_cat)
df_0021a['fd_combo_num'] = df_0021a['fd_combo_num'].replace(' ', 0).astype(int)
df_0021a['fd_type'] = df_0021a['fd_type'].replace(map_fd_type_cat01)

###################################

## Create Table 02 ##
tables = ['0021']
studies = [25502]
col_dict = cols_0021_02
df_0021b = load.create_tables_multiyear(tables,col_dict,studies,inx='fd_entry')


### Fix Data 02 ##
mappings = {i:' ' for i in df_0021b.loc[:,'fd_g':].columns} # format will look like {'col1':' ','col2':' '....}
df_0021b.loc[:,'fd_g':] = df_0021b.loc[:,'fd_g':].replace(mappings, 0).astype(float)
df_0021b['fd_home'] = (df_0021b['fd_home'] == '1') * 1  # making "home" (9) to 1, others to 0
df_0021b['fd_meal'] = df_0021b['fd_meal'].replace(map_fd_meal_cat)
df_0021b['fd_type'] = df_0021b['fd_type'].replace(map_fd_type_cat02)

###################################

## Create Table 03 ##
tables = ['0022']
studies = [25503]
col_dict = cols_0021_03
df_0021c = load.create_tables_multiyear(tables,col_dict,studies,inx='fd_entry')


### Fix Data 03 ##
mappings = {i:' ' for i in df_0021c.loc[:,'fd_g':].columns} # format will look like {'col1':' ','col2':' '....}
df_0021c.loc[:,'fd_g':] = df_0021c.loc[:,'fd_g':].replace(mappings, 0).astype(float)
df_0021c['fd_home'] = (df_0021c['fd_home'] == '1') * 1  # making "home" (9) to 1, others to 0
df_0021c['fd_meal'] = df_0021c['fd_meal'].replace(map_fd_meal_cat)
df_0021c['fd_type'] = df_0021c['fd_type'].replace(map_fd_type_cat02)

###################################

## Create Table 04 ##
tables = ['0015']
studies = [25504]
col_dict = cols_0021_04
df_0021d = load.create_tables_multiyear(tables,col_dict,studies,inx='fd_entry')


### Fix Data 04 ##
mappings = {i:' ' for i in df_0021d.loc[:,'fd_g':].columns} # format will look like {'col1':' ','col2':' '....}
df_0021d.loc[:,'fd_g':] = df_0021d.loc[:,'fd_g':].replace(mappings, 0).astype(float)
df_0021d['fd_home'] = (df_0021d['fd_home'] == '1') * 1  # making "home" (9) to 1, others to 0
df_0021d['fd_meal'] = df_0021d['fd_meal'].replace(map_fd_meal_cat)
df_0021d['fd_type'] = df_0021d['fd_type'].replace(map_fd_type_cat02)


## Join all tables ##
df = pd.concat([df_0021a,df_0021b,df_0021c,df_0021d],sort=True)

## Re-order columns
cols = list(df_0021a.columns)
df = df[cols]

## Pickle Data ##
with open('../pickle_data/ds0021.pkl', 'wb') as picklefile:
    pickle.dump(df, picklefile)



