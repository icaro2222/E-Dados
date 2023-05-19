from sqlalchemy import create_engine
from colorama import init, Fore, Style
import pandas as pd
import time
import sys

# Abrir o arquivo de log em modo de escrita
log_file = open('/var/www/edados/arquivo_de_teste.txt', 'a')

# Redirecionar a saída padrão para o arquivo de log
sys.stdout = log_file


# Medindo o tempo que a view demora para executar
tempo_inicial = time.time()

LIMIT = " LIMIT 1000"

def banco(filtro_ano):
    if filtro_ano == '2016':
        BANCO = 'enem_2016'
    elif filtro_ano == '2017':
        BANCO = 'enem_2017'
    elif filtro_ano == '2018':
        BANCO = 'enem_2018'
    else:
        BANCO = 'enem_2019_1'
    return BANCO

def connect():
    # Conexão POSTGRESQL
    tipo_db = 'postgresql'
    host = 'localhost'
    user = 'postgres'
    password = 'tatakae22'
    database = 'e-dados'
    porta = 5432

    conexao = f'{tipo_db}://{user}:{password}@{host}:{porta}/{database}'

    # Conectando com o Banco de Dados
    engine = create_engine(conexao, pool_pre_ping=True)

    print("Conexão com o banco bem sucedida!")

    return engine


def filtro_de_ficiencia(filtro_valor):
    if filtro_valor == 'todas':
        variavel_filtro_deficiencia = """
        WHERE "TP_PRESENCA_CN" = '1'
            AND "TP_PRESENCA_CH" = '1'
            AND "TP_PRESENCA_LC" = '1'
            AND "TP_PRESENCA_MT" = '1'
            AND (
                "IN_BAIXA_VISAO" = '1'
                OR "IN_CEGUEIRA" = '1'
                OR "IN_SURDEZ" = '1'
                OR "IN_DEFICIENCIA_AUDITIVA" = '1'
                OR "IN_SURDO_CEGUEIRA" = '1'
                OR "IN_DEFICIENCIA_FISICA" = '1'
                OR "IN_DEFICIENCIA_MENTAL" = '1'
                OR "IN_DEFICIT_ATENCAO" = '1'
                OR "IN_DISLEXIA" = '1'
                OR "IN_DISCALCULIA" = '1'
                OR "IN_AUTISMO" = '1'
                OR "IN_VISAO_MONOCULAR" = '1'
                OR "IN_OUTRA_DEF" = '1'
            )
        """
    elif(filtro_valor=='nenhuma' or filtro_valor=='vazio'):
        variavel_filtro_deficiencia = (""" WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1'  
                AND ("IN_BAIXA_VISAO" ='0'
                AND "IN_CEGUEIRA" ='0'
                AND "IN_SURDEZ" ='0'
                AND "IN_DEFICIENCIA_AUDITIVA" ='0'
                AND "IN_SURDO_CEGUEIRA" ='0'
                AND "IN_DEFICIENCIA_FISICA" ='0'
                AND "IN_DEFICIENCIA_MENTAL" ='0'
                AND "IN_DEFICIT_ATENCAO" ='0'
                AND "IN_DISLEXIA" ='0'
                AND "IN_DISCALCULIA" ='0'
                AND "IN_AUTISMO" ='0'
                AND "IN_VISAO_MONOCULAR" ='0'
                AND "IN_OUTRA_DEF" ='0')""")
    elif(filtro_valor=='todos'):
        variavel_filtro_deficiencia =  """WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1'  """
    else:
        variavel_filtro_deficiencia =  ' WHERE "' + str(filtro_valor) + '" = 1 '

    return variavel_filtro_deficiencia


# Inicialize a biblioteca colorama
init()


print('-------------------- TESTE DOS DADOS NO BANCO DE DADOS -----------------')
print('INICIANDO....')

Banco = banco("2018")
print(Banco)
print('- DEFINININDO O BANCO')
print(Fore.GREEN + '- BANCO DEFINIDO - OK')
# Restaure as configurações de estilo padrão
print(Style.RESET_ALL)
print('- DEFINININDO Conecxão com o banco')
Conecxao_com_banco = connect()
print(Fore.GREEN + '- Conecxão com o banco estabelecida - OK')

# Restaure as configurações de estilo padrão
print(Style.RESET_ALL)
print('-----------------------------------------------------------------------')

print('- PREPARANDO Filtros....')
Filtro=""
# FILTROS= "TP_COR_RACA", "NU_IDADE", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT
# Filtro = " AND " + '"TP_SEXO" = \'M\'' + """ AND "IN_SEM_RECURSO" ='1' """
# Filtro = " AND " + """ "TP_ESCOLA"='2' """
# Filtro = " AND " + """ "TP_ANO_CONCLUIU"='1' """
# Filtro = " AND " + """ "TP_ANO_CONCLUIU"='1' """

print(Fore.GREEN + '- Filtros PREPARADA - OK')
print(Style.RESET_ALL)

print('- PREPARANDO QUERY DE CONSULTA....')
query = """SELECT count("TP_SEXO") FROM """ + Banco + """
                WHERE "TP_PRESENCA_CN"='1'
                AND "TP_PRESENCA_CH"='1'
                AND "TP_PRESENCA_LC"='1'
                AND "TP_PRESENCA_MT"='1' """+ Filtro + LIMIT

# Adicionar AQUI querys vindas da plataforma:
# query = """SELECT  "TP_SEXO", "TP_COR_RACA", "NU_IDADE", "NU_NOTA_CN", "NU_NOTA_CH",
# "NU_NOTA_LC", "NU_NOTA_MT" FROM "enem_2019_1" WHERE "IN_BAIXA_VISAO" = '1' """
# query= """
# COPY enem_2018 ("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")
# FROM '/media/icaro/Icaro-Dias/Microdados do Enem/que_eu_to_usando/MICRODADOS_ENEM_2018.csv' 
# WITH DELIMITER ';' CSV HEADER ENCODING 'iso-8859-1';"""

print(Fore.GREEN + '- QUERY PREPARADA - OK')
print(Style.RESET_ALL)
print(query)

print('-----------------------------------------------------------------------')

print('- INICIANDO "SELECT" NO BANCO')

print(Fore.GREEN + '- SELECT - OK')
print(Style.RESET_ALL)
    
print('- EXECUTANDO "SELECT" NO BANCO')
print(Fore.GREEN + '- BUSCA CONCLUÍDA - OK')
print(Style.RESET_ALL)

df = pd.read_sql(query, Conecxao_com_banco)
df = pd.DataFrame(df)

# Captura o tempo de fim da execução
tempo_final = time.time()
tempo = tempo_final - tempo_inicial

print(Fore.GREEN + '- RESULTADO: ')
print('- tempo: '+ str(tempo))
print(Style.RESET_ALL)

print('-----------------------------------------------------------------------')
print(df)
print('-----------------------------------------------------------------------')

# SELECT count("TP_ESTADO_CIVIL") FROM "enem_2018" WHERE "TP_PRESENCA_CN"='1'
#                 AND "TP_PRESENCA_CH"='1'
#                 AND "TP_PRESENCA_LC"='1'
#                 AND "TP_PRESENCA_MT"='1'   AND "TP_ESTADO_CIVIL" ='1' ;
# TRUNCATE TABLE enem_2018;

# inscritos que compareceram no enem de 2019: 3702008
# inscritos do sexo feminino que compareceram no enem de 2019: 2201217
# inscritos do sexo masculino que compareceram no enem de 2019: 1500791

# Seu código aqui...

# Fechar o arquivo de log
log_file.close()

# Restaurar a saída padrão para o terminal
sys.stdout = sys.__stdout__