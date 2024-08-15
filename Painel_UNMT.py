import pandas as pd
import requests
import json
from datetime import datetime, timedelta
import time


arq = r"C:\Files\DADOS LEITURAS TEMPO REAL\BASES\LeiturasTempoRealUNMT.csv"

df = pd.read_csv(arq, delimiter=";", low_memory=False)

#PROGRAMADAS
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE')]
programadas_total = len(df_filtrado)

#REALIZADAS
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & (df['VolumeMedido'].notna())]
realizadas_total = df_filtrado['MatriculaClienteImovel'].nunique()

#PERCENTUAL TOTAL DE REALIZADAS
perc_leituras_total = round((realizadas_total / programadas_total ) * 100,ndigits=None)
perc_leituras_total_str = str(round((realizadas_total / programadas_total ) * 100,ndigits=None)) + '%'

# Lista de gerências
gerencias = ['GRBN', 'GRBO', 'GRBS', 'GRCN', 'GRML', 'GRMO', 'GRMS']

# Inicializando dicionários para armazenar os resultados
programadas = {}
realizadas = {}
perc_leituras = {}

for gerencia in gerencias:
    # Filtrando o DataFrame para cada gerência
    df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & (df['Gerencia'] == gerencia)]
    programadas[gerencia] = len(df_filtrado)
    
    df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & (df['VolumeMedido'].notna()) & (df['Gerencia'] == gerencia)]
    realizadas[gerencia] = df_filtrado['MatriculaClienteImovel'].nunique()
    
    perc_leituras[gerencia] = round((realizadas[gerencia] / programadas[gerencia] ) * 100,ndigits=None)

valor_grbn = perc_leituras['GRBN']
grbn = 'GRBN'
valor_grbo = perc_leituras['GRBO']
grbo = 'GRBO'
valor_grbs = perc_leituras['GRBS']
grbs = 'GRBS'
valor_grcn = perc_leituras['GRCN']
grcn = 'GRCN'
valor_grml = perc_leituras['GRML']
grml = 'GRML'
valor_grmo = perc_leituras['GRMO']
grmo = 'GRMO'
valor_grms = perc_leituras['GRMS']
grms = 'GRMS'



#QTD OCORRENCIA 05
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & ((df['Ocorrencia01'] == 5) | (df['Ocorrencia02'] == 5))]
ocorr_05 = len(df_filtrado)

#QTD IMPEDIMENTOS
valores = [90, 45, 43, 22, 17, 15, 11, 8, 5, 4, 3, 2, 1]
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & ((df['Ocorrencia01'].isin(valores)) | (df['Ocorrencia02'].isin(valores)))]
impedimentos = len(df_filtrado)

#PERCENTUAL DE IMPEDIMENTOS
perc_impedimentos = round((impedimentos / realizadas_total ) * 100,ndigits=1)
perc_impedimentos_str = str(round((impedimentos / realizadas_total ) * 100,ndigits=1)) + '%'

#MÉDIA DE LEITURAS PROGRAMADAS POR LEITURISTA
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE')]
qtd_leituristas = df_filtrado['NomeFuncionario'].nunique(dropna=True)
df_filtrado_funcionario = df_filtrado[df_filtrado['NomeFuncionario'].notna()]
qtd_leituras = len(df_filtrado_funcionario['MatriculaClienteImovel'])
avg_leituras = round(qtd_leituras / qtd_leituristas, ndigits=None)

#MÉDIA DE LEITURAS REALIZADAS POR LEITURISTA
avg_leituristas_realizadas = round(realizadas_total / qtd_leituristas, ndigits=None)


#LEITURISTAS COM MAIS OCORRÊNCIAS
df_filtrado = df[(df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE')]

df_filtered = df_filtrado[(df_filtrado['NomeFuncionario'].notna()) & (df_filtrado['Ocorrencia01'].notna()) & (df_filtrado['Ocorrencia01'] != 0) | (df_filtrado['Ocorrencia01'].notna()) & (df_filtrado['Ocorrencia01'] == 0) & (df_filtrado['Ocorrencia02'] != 0)]

grouped = df_filtered.groupby('NomeFuncionario')['Ocorrencia01'].count()

top_5 = grouped.sort_values(ascending=False).head(5)

nome01, Total_nome01 = top_5.index[0], top_5.iloc[0]
nome02, Total_nome02 = top_5.index[1], top_5.iloc[1]
nome03, Total_nome03 = top_5.index[2], top_5.iloc[2]
nome04, Total_nome04 = top_5.index[3], top_5.iloc[3]
nome05, Total_nome05 = top_5.index[4], top_5.iloc[4]


#OCORRENCIAS
def ocorrencias(df, ocorrencia):
    condicao = (df['MatriculaClienteImovel'].notna()) & (df['Dia'] == 'HOJE') & ((df['Ocorrencia01'] == ocorrencia) | (df['Ocorrencia02'] == ocorrencia))
    return len(df[condicao])
OC1 = ocorrencias(df,1)
OC2 = ocorrencias(df,2)
OC3 = ocorrencias(df,3)
OC4 = ocorrencias(df,4)
OC5 = ocorrencias(df,5)
OC8 = ocorrencias(df,8)
OC11 = ocorrencias(df,11)
OC15 = ocorrencias(df,15)
OC17 = ocorrencias(df,17)
OC22 = ocorrencias(df,22)
OC43 = ocorrencias(df,43)
OC45 = ocorrencias(df,45)
OC90 = ocorrencias(df,90)


#HORA ATUAL
now = datetime.now()
now_minus_3 = now + timedelta(hours=3)
data_hora_atual = now_minus_3.strftime("%Y-%m-%dT%H:%M:%S.000Z")


data = [
    {
        "programadas_total": programadas_total,
        "realizadas_total": realizadas_total,
        "perc_leituras_total": perc_leituras_total,
        "valor_grbn": valor_grbn,
        "grbn": grbn,
        "valor_grbo": valor_grbo,
        "grbo": grbo,
        "valor_grbs": valor_grbs,
        "grbs": grbs,
        "valor_grcn": valor_grcn,
        "grcn": grcn,
        "valor_grml": valor_grml,
        "grml": grml,
        "valor_grmo": valor_grmo,
        "grmo": grmo,
        "valor_grms": valor_grms,
        "grms": grms,
        "ocorr_05": ocorr_05,
        "impedimentos": impedimentos,
        "perc_impedimentos": perc_impedimentos,
        "avg_leituras": avg_leituras,
        "avg_leituristas_realizadas": avg_leituristas_realizadas,
        "min_indicador": 0,
        "max_indicador": programadas_total,
        "datetime_now": data_hora_atual,
        "max_perc": 100,
        "OC1": OC1,
        "OC2": OC2,
        "OC3": OC3,
        "OC4": OC4,
        "OC5": OC5,
        "OC8": OC8,
        "OC11": OC11,
        "OC15": OC15,
        "OC17": OC17,
        "OC22": OC22,
        "OC43": OC43,
        "OC45": OC45,
        "OC90": OC90
    }
]


data1 = [
    {
       "nome01": nome01,
       "Total_nome01": int(Total_nome01) 
    }
]

data2 = [
    {
       "nome01": nome02,
       "Total_nome01": int(Total_nome02) 
    }
]

data3 = [
    {
       "nome01": nome03,
       "Total_nome01": int(Total_nome03) 
    }
]

data4 = [
    {
       "nome01": nome04,
       "Total_nome01": int(Total_nome04) 
    }
]


data5 = [
    {
       "nome01": nome05,
       "Total_nome01": int(Total_nome05) 
    }
]

url = "LINK DO SEU CONJUNTO DE DADOS"
url2 = "LINK DO SEU CONJUNTO DE DADOS"


headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
time.sleep(0.2)
response = requests.post(url2, data=json.dumps(data1), headers=headers)
time.sleep(0.2)
response = requests.post(url2, data=json.dumps(data2), headers=headers)
time.sleep(0.2)
response = requests.post(url2, data=json.dumps(data3), headers=headers)
time.sleep(0.2)
response = requests.post(url2, data=json.dumps(data4), headers=headers)
time.sleep(0.2)
response = requests.post(url2, data=json.dumps(data5), headers=headers)


if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print(f"Erro ao enviar dados: {response.content}")




# Imprimindo os resultados
print(f"{data_hora_atual}")
print(f"Total {programadas_total} Leituras Programadas")
print(f"Total {realizadas_total} Leituras Realizadas")
print(f"Total {perc_leituras_total}% Leituras Realizadas")


print(f"GRBN {valor_grbn}% Leituras Realizadas")

print(f"GRBO {valor_grbo}% Leituras Realizadas")

print(f"GRBS {valor_grbs}% Leituras Realizadas")

print(f"GRCN {valor_grcn}% Leituras Realizadas")

print(f"GRML {valor_grml}% Leituras Realizadas")

print(f"GRMO {valor_grmo}% Leituras Realizadas")

print(f"GRMS {valor_grms}% Leituras Realizadas")

print(f"{ocorr_05} Ocorrências 05")

print(f"{impedimentos} Impedimentos Críticos Registrados ({valores})")
print(f"{perc_impedimentos}% de Leituras com Impedimentos Críticos Registrados")

print(f"{avg_leituras} Média de Leituras Programadas por Leiturista")

print(f"{avg_leituristas_realizadas} Média de Leituras Realizadas por Leiturista")

print(f"{nome01} - {Total_nome01} Ocorrências")
print(f"{nome02} - {Total_nome02} Ocorrências")
print(f"{nome03} - {Total_nome03} Ocorrências")
print(f"{nome04} - {Total_nome04} Ocorrências")
print(f"{nome05} - {Total_nome05} Ocorrências")


print(f"OC1: {OC1}")
print(f"OC2: {OC2}")
print(f"OC3: {OC3}")
print(f"OC4: {OC4}")
print(f"OC5: {OC5}")
print(f"OC8: {OC8}")
print(f"OC11: {OC11}")
print(f"OC15: {OC15}")
print(f"OC17: {OC17}")
print(f"OC22: {OC22}")
print(f"OC43: {OC43}")
print(f"OC45: {OC45}")
print(f"OC90: {OC90}")

