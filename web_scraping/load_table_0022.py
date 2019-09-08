import load_table_functions as load
import pandas as pd
import pickle

###  File 0022 - Diet (Subject Summary)  ###

## Column Mappings ##
cols_0022a1 = {'SEQN':['subject_id','Respondent sequence number'],
             'DRXTKCAL':['food_cal','Energy (kcal)'],
             'DRXTPROT':['food_p','Protein (gm)'],
             'DRXTCARB':['food_carb','Carbohydrate (gm)'],
             'DRXTTFAT':['food_f','Total fat (gm)'],
             'DRXTSFAT':['food_stf','Total saturated fatty acids (gm)'],
             'DRXTMFAT': ['food_mfa', 'Total monounsaturated fatty acids (gm)'],
             'DRXTPFAT': ['food_pfa', 'Total polyunsaturated fatty acids (gm)'],
             'DRXTCHOL': ['food_chol', 'Cholesterol (mg)'],
             'DRXTFIBE': ['food_df', 'Dietary fiber (gm)'],
      #       'DRXTVAIU': ['food_a1', 'Vitamin A (IU)'],
      #       'DRXTVARE': ['food_a2', 'Vitamin A (RE)'],
      #       'DRXTCARO': ['food_car', 'Carotene (RE)'],
             'DRXTVB1': ['food_thiam', 'Thiamin (Vitamin B1) (mg)'],
             'DRXTVB2': ['food_ribo', 'Riboflavin (Vitamin B2) (mg)'],
             'DRXTNIAC': ['food_niac', 'Niacin (mg)'],
             'DRXTVB6': ['food_b6', 'Vitamin B6 (mg)'],
             'DRXTFOLA': ['food_fol', 'Total Folate (mcg)'],
             'DRXTVB12': ['food_b12', 'Vitamin B12 (mcg)'],
             'DRXTVC': ['food_c', 'Vitamin C (mg)'],
        #     'DRXTVE': ['food_e', 'Vitamin E (ATE) (mg)'],
             'DRXTCALC': ['food_calc', 'Calcium (mg)'],
             'DRXTPHOS': ['food_phos', 'Phosphorus (mg)'],
             'DRXTMAGN': ['food_magn', 'Magnesium (mg)'],
             'DRXTIRON': ['food_i', 'Iron (mg)'],
             'DRXTZINC': ['food_z', 'Zinc (mg)'],
             'DRXTCOPP': ['food_cop', 'Copper (mg)'],
             'DRDTSODI': ['food_sod', 'Sodium (mg)'],
             'DRXTPOTA': ['food_pot', 'Potassium (mg)'],
             'DRXTSELE': ['food_sel', 'Selenium (mcg)'],
             'DRXTCAFF': ['food_caf', 'Caffeine (mg)'],
             'DRXTTHEO': ['food_theo', 'Theobromine (mg)'],
             'DRXTALCO': ['food_alc', 'Alcohol (gm)'],
             'DRXTS040': ['food_f01', 'SFA 4:0 (Butanoic) (gm)'],  # Fatty Acid
             'DRXTS060': ['food_f02', 'SFA 6:0 (Hexanoic) (gm)'],  # Fatty Acid
             'DRXTS080': ['food_f03', 'SFA 8:0 (Octanoic) (gm)'],  # Fatty Acid
             'DRXTS100': ['food_f04', 'SFA 10:0 (Decanoic) (gm)'],  # Fatty Acid
             'DRXTS120': ['food_f05', 'SFA 12:0 (Dodecanoic) (gm)'],  # Fatty Acid
             'DRXTS140': ['food_f06', 'SFA 14:0 (Tetradecanoic) (gm)'],  # Fatty Acid
             'DRXTS160': ['food_f07', 'SFA 16:0 (Hexadecanoic) (gm)'],  # Fatty Acid
             'DRXTS180': ['food_f08', 'SFA 18:0 (Octadecanoic) (gm)'],  # Fatty Acid
             'DRXTM161': ['food_f09', 'MFA 16:1 (Hexadecenoic) (gm)'],  # Fatty Acid
             'DRXTM181': ['food_f10', 'MFA 18:1 (Octadecenoic) (gm)'],  # Fatty Acid
             'DRXTM201': ['food_f11', 'MFA 20:1 (Eicosenoic) (gm)'],  # Fatty Acid
             'DRXTM221': ['food_f12', 'MFA 22:1 (Docosenoic) (gm)'],  # Fatty Acid
             'DRXTP182': ['food_f13', 'PFA 18:2 (Octadecadienoic) (gm)'],  # Fatty Acid
             'DRXTP183': ['food_f14', 'PFA 18:3 (Octadecatrienoic) (gm)'],  # Fatty Acid
             'DRXTP184': ['food_f15', 'PFA 18:4 (Octadecatetraenoic) (gm)'],  # Fatty Acid
             'DRXTP204': ['food_f16', 'PFA 20:4 (Eicosatetraenoic) (gm)'],  # Fatty Acid
             'DRXTP205': ['food_f17', 'PFA 20:5 (Eicsapentaenoic) (gm)'],  # Fatty Acid
             'DRXTP225': ['food_f18', 'PFA 22:5 (Docosapentaenoic) (gm)'],  # Fatty Acid
             'DRXTP226': ['food_f19', 'PFA 22:6 (Docosahexaenoic) (gm)']  # Fatty Acid
            }


cols_0022a2 = {'SEQN':['subject_id','Respondent sequence number'],
             'DRXTKCAL':['food_cal','Energy (kcal)'],
             'DRXTPROT':['food_p','Protein (gm)'],
             'DRXTCARB':['food_carb','Carbohydrate (gm)'],
             'DRXTTFAT':['food_f','Total fat (gm)'],
             'DRXTCHOL': ['food_chol', 'Cholesterol (mg)'],
             'DRXTCAFF': ['food_caf', 'Caffeine (mg)'],
             'DRXTALCO': ['food_alc', 'Alcohol (gm)']
            }

cols_0022b1 = {'SEQN':['subject_id','Respondent sequence number'],
             'DR1TKCAL':['food_cal','Energy (kcal)'],
             'DR1TPROT':['food_p','Protein (gm)'],
             'DR1TCARB':['food_carb','Carbohydrate (gm)'],
             'DR1TTFAT':['food_f','Total fat (gm)'],
             'DR1TSFAT':['food_stf','Total saturated fatty acids (gm)'],
             'DR1TMFAT': ['food_mfa', 'Total monounsaturated fatty acids (gm)'],
             'DR1TPFAT': ['food_pfa', 'Total polyunsaturated fatty acids (gm)'],
             'DR1TCHOL': ['food_chol', 'Cholesterol (mg)'],
             'DR1TFIBE': ['food_df', 'Dietary fiber (gm)'],
     #        'DR1TVAIU': ['food_a1', 'Vitamin A (IU)'],
     #        'DR1TVARE': ['food_a2', 'Vitamin A (RE)'],
     #        'DR1TCARO': ['food_car', 'Carotene (RE)'],
             'DR1TVB1': ['food_thiam', 'Thiamin (Vitamin B1) (mg)'],
             'DR1TVB2': ['food_ribo', 'Riboflavin (Vitamin B2) (mg)'],
             'DR1TNIAC': ['food_niac', 'Niacin (mg)'],
             'DR1TVB6': ['food_b6', 'Vitamin B6 (mg)'],
             'DR1TFOLA': ['food_fol', 'Total Folate (mcg)'],
             'DR1TVB12': ['food_b12', 'Vitamin B12 (mcg)'],
             'DR1TVC': ['food_c', 'Vitamin C (mg)'],
       #      'DR1TVE': ['food_e', 'Vitamin E (ATE) (mg)'],
             'DR1TCALC': ['food_calc', 'Calcium (mg)'],
             'DR1TPHOS': ['food_phos', 'Phosphorus (mg)'],
             'DR1TMAGN': ['food_magn', 'Magnesium (mg)'],
             'DR1TIRON': ['food_i', 'Iron (mg)'],
             'DR1TZINC': ['food_z', 'Zinc (mg)'],
             'DR1TCOPP': ['food_cop', 'Copper (mg)'],
             'DR1TSODI': ['food_sod', 'Sodium (mg)'],
             'DR1TPOTA': ['food_pot', 'Potassium (mg)'],
             'DR1TSELE': ['food_sel', 'Selenium (mcg)'],
             'DR1TCAFF': ['food_caf', 'Caffeine (mg)'],
             'DR1TTHEO': ['food_theo', 'Theobromine (mg)'],
             'DR1TALCO': ['food_alc', 'Alcohol (gm)'],
             'DR1TS040': ['food_f01', 'SFA 4:0 (Butanoic) (gm)'],  # Fatty Acid
             'DR1TS060': ['food_f02', 'SFA 6:0 (Hexanoic) (gm)'],  # Fatty Acid
             'DR1TS080': ['food_f03', 'SFA 8:0 (Octanoic) (gm)'],  # Fatty Acid
             'DR1TS100': ['food_f04', 'SFA 10:0 (Decanoic) (gm)'],  # Fatty Acid
             'DR1TS120': ['food_f05', 'SFA 12:0 (Dodecanoic) (gm)'],  # Fatty Acid
             'DR1TS140': ['food_f06', 'SFA 14:0 (Tetradecanoic) (gm)'],  # Fatty Acid
             'DR1TS160': ['food_f07', 'SFA 16:0 (Hexadecanoic) (gm)'],  # Fatty Acid
             'DR1TS180': ['food_f08', 'SFA 18:0 (Octadecanoic) (gm)'],  # Fatty Acid
             'DR1TM161': ['food_f09', 'MFA 16:1 (Hexadecenoic) (gm)'],  # Fatty Acid
             'DR1TM181': ['food_f10', 'MFA 18:1 (Octadecenoic) (gm)'],  # Fatty Acid
             'DR1TM201': ['food_f11', 'MFA 20:1 (Eicosenoic) (gm)'],  # Fatty Acid
             'DR1TM221': ['food_f12', 'MFA 22:1 (Docosenoic) (gm)'],  # Fatty Acid
             'DR1TP182': ['food_f13', 'PFA 18:2 (Octadecadienoic) (gm)'],  # Fatty Acid
             'DR1TP183': ['food_f14', 'PFA 18:3 (Octadecatrienoic) (gm)'],  # Fatty Acid
             'DR1TP184': ['food_f15', 'PFA 18:4 (Octadecatetraenoic) (gm)'],  # Fatty Acid
             'DR1TP204': ['food_f16', 'PFA 20:4 (Eicosatetraenoic) (gm)'],  # Fatty Acid
             'DR1TP205': ['food_f17', 'PFA 20:5 (Eicsapentaenoic) (gm)'],  # Fatty Acid
             'DR1TP225': ['food_f18', 'PFA 22:5 (Docosapentaenoic) (gm)'],  # Fatty Acid
             'DR1TP226': ['food_f19', 'PFA 22:6 (Docosahexaenoic) (gm)']  # Fatty Acid
            }


cols_0022b2 = {'SEQN':['subject_id','Respondent sequence number'],
             'DR1TKCAL':['food_cal','Energy (kcal)'],
             'DR1TPROT':['food_p','Protein (gm)'],
             'DR1TCARB':['food_carb','Carbohydrate (gm)'],
             'DR1TTFAT':['food_f','Total fat (gm)'],
             'DR1TCHOL': ['food_chol', 'Cholesterol (mg)'],
             'DR1TCAFF': ['food_caf', 'Caffeine (mg)'],
             'DR1TALCO': ['food_alc', 'Alcohol (gm)']
            }

## Create Table ##
tables = ['0022','0022']
studies = [25501,25502]
col_dict = cols_0022a2
df_0022 = load.create_tables_multiyear(tables,col_dict,studies)

## Create Table ##
tables = ['0024','0017']
studies = [25503,25504]
col_dict = cols_0022b2
df_0022_04 = load.create_tables_multiyear(tables,col_dict,studies)

## Combine Tables
df_0022 = pd.concat([df_0022,df_0022_04])

## Fix Data ##
mappings = {i:' ' for i in df_0022.columns} # format will look like {'col1':' ','col2':' '....}
df_0022 = df_0022.replace(mappings, 0).astype(float)

## Pickle Data ##
with open('../pickle_data/ds0022.pkl', 'wb') as picklefile:
    pickle.dump(df_0022, picklefile)

    
    