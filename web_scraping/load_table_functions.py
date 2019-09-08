import pandas as pd

## File path to Raw Data
read_path = '../data/'

def create_tables_multiyear(tables,col_dict,studies,inx='subject_id',add_study=False):
    '''
    Import tables for multiple studies
    '''
    df = pd.DataFrame()
    for study, table in zip(studies,tables):
        path = read_path + 'ICPSR_{}_all/DS{}/{}-{}-Data.tsv'.format(study,table,study,table)
        df_new = pd.read_csv(path, delimiter='\t',usecols=col_dict.keys())
        df_new.columns = [i[0] for i in col_dict.values()]
        if add_study == True:
            df_new['study'] = study
        df_new.set_index(inx, inplace=True)
        df = pd.concat([df,df_new])
    return df

