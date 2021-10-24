import pandas as pd
import os

def getFullPathName(fileName):
    directorio = '../Data'
    return os.path.join(directorio, fileName)

fname_parques = getFullPathName('arbolado-en-espacios-verdes.csv')
fname_veredas = getFullPathName('arbolado-publico-lineal-2017-2018.csv')

df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)

especies_parques = ['Tipuana Tipu']
especies_veredas = ['Tipuana tipu']

cols_sel_parques = ['diametro', 'altura_tot']
cols_sel_veredas = ['diametro_altura_pecho', 'altura_arbol']

df_parques_filtrados = df_parques['nombre_cie'].isin(especies_parques)
df_veredas_filtrados = df_veredas['nombre_cientifico'].isin(especies_veredas)

df_tipas_parques = (df_parques[cols_sel_parques])[df_parques_filtrados].copy()
df_tipas_veredas = (df_veredas[cols_sel_veredas])[df_veredas_filtrados].copy()

renamed_columns = {
    'diametro': 'diametro_altura_pecho',
    'altura_tot': 'altura_arbol'
}
df_tipas_parques.rename(columns=renamed_columns, inplace=True)

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')
df_tipas.boxplot('altura_arbol', by = 'ambiente')
