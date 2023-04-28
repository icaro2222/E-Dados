-- Criei o Banco do enem do ano de 2017 e 2018 com esses codigos;

-- Colocar no banco os dados do enem de 2018

COPY enem_2019_1 ("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_TEMPO_ADICIONAL", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025")
FROM '/home/icaro/documentos/arquivo1.csv' 
WITH DELIMITER ';' CSV HEADER ENCODING 'iso-8859-1';

CREATE TABLE "enem_2019_1" (
	"NU_INSCRICAO" VARCHAR(12) , 
	"NU_ANO" INT , 
	"CO_MUNICIPIO_RESIDENCIA" VARCHAR(17) , 
	"NO_MUNICIPIO_RESIDENCIA" VARCHAR(45) , 
	"CO_UF_RESIDENCIA" VARCHAR(2) , 
	"SG_UF_RESIDENCIA" VARCHAR(2) , 
	"NU_IDADE" INT , 
	"TP_SEXO" VARCHAR(1) , 
	"TP_ESTADO_CIVIL" VARCHAR(1) , 
	"TP_COR_RACA" VARCHAR(1) , 
	"TP_NACIONALIDADE" VARCHAR(1) , 
	"CO_MUNICIPIO_NASCIMENTO" VARCHAR(17), 
	"NO_MUNICIPIO_NASCIMENTO" VARCHAR(45), 
	"CO_UF_NASCIMENTO" VARCHAR(2), 
	"SG_UF_NASCIMENTO" VARCHAR(2), 
	"TP_ST_CONCLUSAO" VARCHAR(1) , 
	"TP_ANO_CONCLUIU" VARCHAR(2) , 
	"TP_ESCOLA" VARCHAR(1) , 
	"TP_ENSINO" VARCHAR(1), 
	"IN_TREINEIRO" VARCHAR(1) , 
	"CO_ESCOLA" VARCHAR(18), 
	"CO_MUNICIPIO_ESC" VARCHAR(17), 
	"NO_MUNICIPIO_ESC" VARCHAR(45), 
	"CO_UF_ESC" VARCHAR(2), 
	"SG_UF_ESC" VARCHAR(2), 
	"TP_DEPENDENCIA_ADM_ESC" VARCHAR(1), 
	"TP_LOCALIZACAO_ESC" VARCHAR(1), 
	"TP_SIT_FUNC_ESC" VARCHAR(1), 
	"IN_BAIXA_VISAO" INT , 
	"IN_CEGUEIRA" INT , 
	"IN_SURDEZ" INT , 
	"IN_DEFICIENCIA_AUDITIVA" INT , 
	"IN_SURDO_CEGUEIRA" INT , 
	"IN_DEFICIENCIA_FISICA" INT , 
	"IN_DEFICIENCIA_MENTAL" INT , 
	"IN_DEFICIT_ATENCAO" INT , 
	"IN_DISLEXIA" INT , 
	"IN_DISCALCULIA" INT , 
	"IN_AUTISMO" INT , 
	"IN_VISAO_MONOCULAR" INT , 
	"IN_OUTRA_DEF" INT , 
	"IN_GESTANTE" INT , 
	"IN_LACTANTE" INT , 
	"IN_IDOSO" INT , 
	"IN_ESTUDA_CLASSE_HOSPITALAR" INT , 
	"IN_SEM_RECURSO" INT , 
	"IN_BRAILLE" INT NULL, 
	"IN_AMPLIADA_24" INT , 
	"IN_AMPLIADA_18" INT , 
	"IN_LEDOR" INT , 
	"IN_ACESSO" INT , 
	"IN_TRANSCRICAO" INT , 
	"IN_LIBRAS" INT , 
	"IN_TEMPO_ADICIONAL" INT , 
	"IN_LEITURA_LABIAL" INT , 
	"IN_MESA_CADEIRA_RODAS" INT , 
	"IN_MESA_CADEIRA_SEPARADA" INT , 
	"IN_APOIO_PERNA" INT , 
	"IN_GUIA_INTERPRETE" INT , 
	"IN_COMPUTADOR" INT , 
	"IN_CADEIRA_ESPECIAL" INT , 
	"IN_CADEIRA_CANHOTO" INT , 
	"IN_CADEIRA_ACOLCHOADA" INT , 
	"IN_PROVA_DEITADO" INT , 
	"IN_MOBILIARIO_OBESO" INT , 
	"IN_LAMINA_OVERLAY" INT , 
	"IN_PROTETOR_AURICULAR" INT , 
	"IN_MEDIDOR_GLICOSE" INT , 
	"IN_MAQUINA_BRAILE" INT , 
	"IN_SOROBAN" INT , 
	"IN_MARCA_PASSO" INT , 
	"IN_SONDA" INT , 
	"IN_MEDICAMENTOS" INT , 
	"IN_SALA_INDIVIDUAL" INT , 
	"IN_SALA_ESPECIAL" INT , 
	"IN_SALA_ACOMPANHANTE" INT , 
	"IN_MOBILIARIO_ESPECIFICO" INT , 
	"IN_MATERIAL_ESPECIFICO" INT , 
	"IN_NOME_SOCIAL" INT , 
	"CO_MUNICIPIO_PROVA" VARCHAR(17) , 
	"NO_MUNICIPIO_PROVA" VARCHAR(45) , 
	"CO_UF_PROVA" VARCHAR(2) , 
	"SG_UF_PROVA" VARCHAR(2) , 
	"TP_PRESENCA_CN" VARCHAR(1) , 
	"TP_PRESENCA_CH" VARCHAR(1) , 
	"TP_PRESENCA_LC" VARCHAR(1) , 
	"TP_PRESENCA_MT" VARCHAR(1) , 
	"CO_PROVA_CN" VARCHAR(3), 
	"CO_PROVA_CH" VARCHAR(3), 
	"CO_PROVA_LC" VARCHAR(3), 
	"CO_PROVA_MT" VARCHAR(3), 
	"NU_NOTA_CN" REAL,
	"NU_NOTA_CH" REAL,
	"NU_NOTA_LC" REAL,
	"NU_NOTA_MT" REAL,
	"TX_RESPOSTAS_CN" VARCHAR(45), 
	"TX_RESPOSTAS_CH" VARCHAR(45), 
	"TX_RESPOSTAS_LC" VARCHAR(50), 
	"TX_RESPOSTAS_MT" VARCHAR(45), 
	"TP_LINGUA" VARCHAR(1) , 
	"TX_GABARITO_CN" VARCHAR(45), 
	"TX_GABARITO_CH" VARCHAR(45), 
	"TX_GABARITO_LC" VARCHAR(50), 
	"TX_GABARITO_MT" VARCHAR(45), 
	"TP_STATUS_REDACAO" VARCHAR(1), 
	"NU_NOTA_COMP1" REAL,
	"NU_NOTA_COMP2" REAL,
	"NU_NOTA_COMP3" REAL,
	"NU_NOTA_COMP4" REAL,
	"NU_NOTA_COMP5" REAL,
	"NU_NOTA_REDACAO" REAL,
	"Q001" VARCHAR(1) , 
	"Q002" VARCHAR(1) , 
	"Q003" VARCHAR(1) , 
	"Q004" VARCHAR(1) , 
	"Q005" VARCHAR(2) , 
	"Q006" VARCHAR(1) , 
	"Q007" VARCHAR(1) , 
	"Q008" VARCHAR(1) , 
	"Q009" VARCHAR(1) , 
	"Q010" VARCHAR(1) , 
	"Q011" VARCHAR(1) , 
	"Q012" VARCHAR(1) , 
	"Q013" VARCHAR(1) , 
	"Q014" VARCHAR(1) , 
	"Q015" VARCHAR(1) , 
	"Q016" VARCHAR(1) , 
	"Q017" VARCHAR(1) , 
	"Q018" VARCHAR(1) , 
	"Q019" VARCHAR(1) , 
	"Q020" VARCHAR(1) , 
	"Q021" VARCHAR(1) , 
	"Q022" VARCHAR(1) , 
	"Q023" VARCHAR(1) , 
	"Q024" VARCHAR(1) , 
	"Q025" VARCHAR(1)
);


-- Colocar no banco os dados do enem de 2018

COPY enem_2018 ("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")
FROM '/home/icaro/documentos/microdados_enem_2018/MICRODADOS_ENEM_2018.csv' 
WITH DELIMITER ';' CSV HEADER ENCODING 'iso-8859-1';


CREATE TABLE "enem_2018" (
	"NU_INSCRICAO" VARCHAR(12) , 
	"NU_ANO" INT , 
	"CO_MUNICIPIO_RESIDENCIA" VARCHAR(7) , 
	"NO_MUNICIPIO_RESIDENCIA" VARCHAR(50) , 
	"CO_UF_RESIDENCIA" VARCHAR(2) , 
	"SG_UF_RESIDENCIA" VARCHAR(2) , 
	"NU_IDADE" INT , 
	"TP_SEXO" VARCHAR(1) , 
	"TP_ESTADO_CIVIL" VARCHAR(1) , 
	"TP_COR_RACA" VARCHAR(1) , 
	"TP_NACIONALIDADE" VARCHAR(1) , 
	"CO_MUNICIPIO_NASCIMENTO" VARCHAR(7), 
	"NO_MUNICIPIO_NASCIMENTO" VARCHAR(50), 
	"CO_UF_NASCIMENTO" VARCHAR(2), 
	"SG_UF_NASCIMENTO" VARCHAR(2), 
	"TP_ST_CONCLUSAO" VARCHAR(1) , 
	"TP_ANO_CONCLUIU" VARCHAR(2) , 
	"TP_ESCOLA" VARCHAR(1) , 
	"TP_ENSINO" VARCHAR(1), 
	"IN_TREINEIRO" VARCHAR(1) , 
	"CO_ESCOLA" VARCHAR(8), 
	"CO_MUNICIPIO_ESC" VARCHAR(7), 
	"NO_MUNICIPIO_ESC" VARCHAR(50), 
	"CO_UF_ESC" VARCHAR(2), 
	"SG_UF_ESC" VARCHAR(2), 
	"TP_DEPENDENCIA_ADM_ESC" VARCHAR(1), 
	"TP_LOCALIZACAO_ESC" VARCHAR(1), 
	"TP_SIT_FUNC_ESC" VARCHAR(1), 
	"IN_BAIXA_VISAO" INT , 
	"IN_CEGUEIRA" INT , 
	"IN_SURDEZ" INT , 
	"IN_DEFICIENCIA_AUDITIVA" INT , 
	"IN_SURDO_CEGUEIRA" INT , 
	"IN_DEFICIENCIA_FISICA" INT , 
	"IN_DEFICIENCIA_MENTAL" INT , 
	"IN_DEFICIT_ATENCAO" INT , 
	"IN_DISLEXIA" INT , 
	"IN_DISCALCULIA" INT , 
	"IN_AUTISMO" INT , 
	"IN_VISAO_MONOCULAR" INT , 
	"IN_OUTRA_DEF" INT , 
	"IN_GESTANTE" INT , 
	"IN_LACTANTE" INT , 
	"IN_IDOSO" INT , 
	"IN_ESTUDA_CLASSE_HOSPITALAR" INT , 
	"IN_SEM_RECURSO" INT , 
	"IN_BRAILLE" INT NULL, 
	"IN_AMPLIADA_24" INT , 
	"IN_AMPLIADA_18" INT , 
	"IN_LEDOR" INT , 
	"IN_ACESSO" INT , 
	"IN_TRANSCRICAO" INT , 
	"IN_LIBRAS" INT , 
	"IN_LEITURA_LABIAL" INT , 
	"IN_MESA_CADEIRA_RODAS" INT , 
	"IN_MESA_CADEIRA_SEPARADA" INT , 
	"IN_APOIO_PERNA" INT , 
	"IN_GUIA_INTERPRETE" INT , 
	"IN_COMPUTADOR" INT , 
	"IN_CADEIRA_ESPECIAL" INT , 
	"IN_CADEIRA_CANHOTO" INT , 
	"IN_CADEIRA_ACOLCHOADA" INT , 
	"IN_PROVA_DEITADO" INT , 
	"IN_MOBILIARIO_OBESO" INT , 
	"IN_LAMINA_OVERLAY" INT , 
	"IN_PROTETOR_AURICULAR" INT , 
	"IN_MEDIDOR_GLICOSE" INT , 
	"IN_MAQUINA_BRAILE" INT , 
	"IN_SOROBAN" INT , 
	"IN_MARCA_PASSO" INT , 
	"IN_SONDA" INT , 
	"IN_MEDICAMENTOS" INT , 
	"IN_SALA_INDIVIDUAL" INT , 
	"IN_SALA_ESPECIAL" INT , 
	"IN_SALA_ACOMPANHANTE" INT , 
	"IN_MOBILIARIO_ESPECIFICO" INT , 
	"IN_MATERIAL_ESPECIFICO" INT , 
	"IN_NOME_SOCIAL" INT , 
	"CO_MUNICIPIO_PROVA" VARCHAR(7) , 
	"NO_MUNICIPIO_PROVA" VARCHAR(50) , 
	"CO_UF_PROVA" VARCHAR(2) , 
	"SG_UF_PROVA" VARCHAR(2) , 
	"TP_PRESENCA_CN" VARCHAR(1) , 
	"TP_PRESENCA_CH" VARCHAR(1) , 
	"TP_PRESENCA_LC" VARCHAR(1) , 
	"TP_PRESENCA_MT" VARCHAR(1) , 
	"CO_PROVA_CN" VARCHAR(3), 
	"CO_PROVA_CH" VARCHAR(3), 
	"CO_PROVA_LC" VARCHAR(3), 
	"CO_PROVA_MT" VARCHAR(3), 
	"NU_NOTA_CN" REAL,
	"NU_NOTA_CH" REAL,
	"NU_NOTA_LC" REAL,
	"NU_NOTA_MT" REAL,
	"TX_RESPOSTAS_CN" VARCHAR(45), 
	"TX_RESPOSTAS_CH" VARCHAR(45), 
	"TX_RESPOSTAS_LC" VARCHAR(50), 
	"TX_RESPOSTAS_MT" VARCHAR(45), 
	"TP_LINGUA" VARCHAR(1) , 
	"TX_GABARITO_CN" VARCHAR(45), 
	"TX_GABARITO_CH" VARCHAR(45), 
	"TX_GABARITO_LC" VARCHAR(50), 
	"TX_GABARITO_MT" VARCHAR(45), 
	"TP_STATUS_REDACAO" VARCHAR(1), 
	"NU_NOTA_COMP1" REAL,
	"NU_NOTA_COMP2" REAL,
	"NU_NOTA_COMP3" REAL,
	"NU_NOTA_COMP4" REAL,
	"NU_NOTA_COMP5" REAL,
	"NU_NOTA_REDACAO" REAL,
	"Q001" VARCHAR(1) , 
	"Q002" VARCHAR(1) , 
	"Q003" VARCHAR(1) , 
	"Q004" VARCHAR(1) , 
	"Q005" VARCHAR(2) , 
	"Q006" VARCHAR(1) , 
	"Q007" VARCHAR(1) , 
	"Q008" VARCHAR(1) , 
	"Q009" VARCHAR(1) , 
	"Q010" VARCHAR(1) , 
	"Q011" VARCHAR(1) , 
	"Q012" VARCHAR(1) , 
	"Q013" VARCHAR(1) , 
	"Q014" VARCHAR(1) , 
	"Q015" VARCHAR(1) , 
	"Q016" VARCHAR(1) , 
	"Q017" VARCHAR(1) , 
	"Q018" VARCHAR(1) , 
	"Q019" VARCHAR(1) , 
	"Q020" VARCHAR(1) , 
	"Q021" VARCHAR(1) , 
	"Q022" VARCHAR(1) , 
	"Q023" VARCHAR(1) , 
	"Q024" VARCHAR(1) , 
	"Q025" VARCHAR(1) , 
	"Q026" VARCHAR(1) ,
	"Q027" VARCHAR(1) 
);

-- Colocar no banco os dados do enem de 2017

COPY enem_2017 ("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")
FROM '/home/icaro/documentos/microdados_enem_2018/MICRODADOS_ENEM_2017.csv' 
WITH DELIMITER ';' CSV HEADER ENCODING 'iso-8859-1';


CREATE TABLE "enem_2017" (
	"NU_INSCRICAO" VARCHAR(12) , 
	"NU_ANO" INT , 
	"CO_MUNICIPIO_RESIDENCIA" VARCHAR(7) , 
	"NO_MUNICIPIO_RESIDENCIA" VARCHAR(50) , 
	"CO_UF_RESIDENCIA" VARCHAR(2) , 
	"SG_UF_RESIDENCIA" VARCHAR(2) , 
	"NU_IDADE" INT , 
	"TP_SEXO" VARCHAR(1) , 
	"TP_ESTADO_CIVIL" VARCHAR(1) , 
	"TP_COR_RACA" VARCHAR(1) , 
	"TP_NACIONALIDADE" VARCHAR(1) , 
	"CO_MUNICIPIO_NASCIMENTO" VARCHAR(7), 
	"NO_MUNICIPIO_NASCIMENTO" VARCHAR(50), 
	"CO_UF_NASCIMENTO" VARCHAR(2), 
	"SG_UF_NASCIMENTO" VARCHAR(2), 
	"TP_ST_CONCLUSAO" VARCHAR(1) , 
	"TP_ANO_CONCLUIU" VARCHAR(2) , 
	"TP_ESCOLA" VARCHAR(1) , 
	"TP_ENSINO" VARCHAR(1), 
	"IN_TREINEIRO" VARCHAR(1) , 
	"CO_ESCOLA" VARCHAR(8), 
	"CO_MUNICIPIO_ESC" VARCHAR(7), 
	"NO_MUNICIPIO_ESC" VARCHAR(50), 
	"CO_UF_ESC" VARCHAR(2), 
	"SG_UF_ESC" VARCHAR(2), 
	"TP_DEPENDENCIA_ADM_ESC" VARCHAR(1), 
	"TP_LOCALIZACAO_ESC" VARCHAR(1), 
	"TP_SIT_FUNC_ESC" VARCHAR(1), 
	"IN_BAIXA_VISAO" INT , 
	"IN_CEGUEIRA" INT , 
	"IN_SURDEZ" INT , 
	"IN_DEFICIENCIA_AUDITIVA" INT , 
	"IN_SURDO_CEGUEIRA" INT , 
	"IN_DEFICIENCIA_FISICA" INT , 
	"IN_DEFICIENCIA_MENTAL" INT , 
	"IN_DEFICIT_ATENCAO" INT , 
	"IN_DISLEXIA" INT , 
	"IN_DISCALCULIA" INT , 
	"IN_AUTISMO" INT , 
	"IN_VISAO_MONOCULAR" INT , 
	"IN_OUTRA_DEF" INT , 
	"IN_GESTANTE" INT , 
	"IN_LACTANTE" INT , 
	"IN_IDOSO" INT , 
	"IN_ESTUDA_CLASSE_HOSPITALAR" INT , 
	"IN_SEM_RECURSO" INT , 
	"IN_BRAILLE" INT NULL, 
	"IN_AMPLIADA_24" INT , 
	"IN_AMPLIADA_18" INT , 
	"IN_LEDOR" INT , 
	"IN_ACESSO" INT , 
	"IN_TRANSCRICAO" INT , 
	"IN_LIBRAS" INT , 
	"IN_LEITURA_LABIAL" INT , 
	"IN_MESA_CADEIRA_RODAS" INT , 
	"IN_MESA_CADEIRA_SEPARADA" INT , 
	"IN_APOIO_PERNA" INT , 
	"IN_GUIA_INTERPRETE" INT , 
	"IN_COMPUTADOR" INT , 
	"IN_CADEIRA_ESPECIAL" INT , 
	"IN_CADEIRA_CANHOTO" INT , 
	"IN_CADEIRA_ACOLCHOADA" INT , 
	"IN_PROVA_DEITADO" INT , 
	"IN_MOBILIARIO_OBESO" INT , 
	"IN_LAMINA_OVERLAY" INT , 
	"IN_PROTETOR_AURICULAR" INT , 
	"IN_MEDIDOR_GLICOSE" INT , 
	"IN_MAQUINA_BRAILE" INT , 
	"IN_SOROBAN" INT , 
	"IN_MARCA_PASSO" INT , 
	"IN_SONDA" INT , 
	"IN_MEDICAMENTOS" INT , 
	"IN_SALA_INDIVIDUAL" INT , 
	"IN_SALA_ESPECIAL" INT , 
	"IN_SALA_ACOMPANHANTE" INT , 
	"IN_MOBILIARIO_ESPECIFICO" INT , 
	"IN_MATERIAL_ESPECIFICO" INT , 
	"IN_NOME_SOCIAL" INT , 
	"CO_MUNICIPIO_PROVA" VARCHAR(7) , 
	"NO_MUNICIPIO_PROVA" VARCHAR(50) , 
	"CO_UF_PROVA" VARCHAR(2) , 
	"SG_UF_PROVA" VARCHAR(2) , 
	"TP_PRESENCA_CN" VARCHAR(1) , 
	"TP_PRESENCA_CH" VARCHAR(1) , 
	"TP_PRESENCA_LC" VARCHAR(1) , 
	"TP_PRESENCA_MT" VARCHAR(1) , 
	"CO_PROVA_CN" VARCHAR(3), 
	"CO_PROVA_CH" VARCHAR(3), 
	"CO_PROVA_LC" VARCHAR(3), 
	"CO_PROVA_MT" VARCHAR(3), 
	"NU_NOTA_CN" REAL,
	"NU_NOTA_CH" REAL,
	"NU_NOTA_LC" REAL,
	"NU_NOTA_MT" REAL,
	"TX_RESPOSTAS_CN" VARCHAR(45), 
	"TX_RESPOSTAS_CH" VARCHAR(45), 
	"TX_RESPOSTAS_LC" VARCHAR(50), 
	"TX_RESPOSTAS_MT" VARCHAR(45), 
	"TP_LINGUA" VARCHAR(1) , 
	"TX_GABARITO_CN" VARCHAR(45), 
	"TX_GABARITO_CH" VARCHAR(45), 
	"TX_GABARITO_LC" VARCHAR(50), 
	"TX_GABARITO_MT" VARCHAR(45), 
	"TP_STATUS_REDACAO" VARCHAR(1), 
	"NU_NOTA_COMP1" REAL,
	"NU_NOTA_COMP2" REAL,
	"NU_NOTA_COMP3" REAL,
	"NU_NOTA_COMP4" REAL,
	"NU_NOTA_COMP5" REAL,
	"NU_NOTA_REDACAO" REAL,
	"Q001" VARCHAR(1) , 
	"Q002" VARCHAR(1) , 
	"Q003" VARCHAR(1) , 
	"Q004" VARCHAR(1) , 
	"Q005" VARCHAR(2) , 
	"Q006" VARCHAR(1) , 
	"Q007" VARCHAR(1) , 
	"Q008" VARCHAR(1) , 
	"Q009" VARCHAR(1) , 
	"Q010" VARCHAR(1) , 
	"Q011" VARCHAR(1) , 
	"Q012" VARCHAR(1) , 
	"Q013" VARCHAR(1) , 
	"Q014" VARCHAR(1) , 
	"Q015" VARCHAR(1) , 
	"Q016" VARCHAR(1) , 
	"Q017" VARCHAR(1) , 
	"Q018" VARCHAR(1) , 
	"Q019" VARCHAR(1) , 
	"Q020" VARCHAR(1) , 
	"Q021" VARCHAR(1) , 
	"Q022" VARCHAR(1) , 
	"Q023" VARCHAR(1) , 
	"Q024" VARCHAR(1) , 
	"Q025" VARCHAR(1) , 
	"Q026" VARCHAR(1) ,
	"Q027" VARCHAR(1) 
);


-- Criando Banco de dados do enem de 2016:

CREATE TABLE "enem_2016" (
	"NU_INSCRICAO" VARCHAR(12) , 
	"NU_ANO" INT , 
	"CO_MUNICIPIO_RESIDENCIA" VARCHAR(7) , 
	"NO_MUNICIPIO_RESIDENCIA" VARCHAR(45) , 
	"CO_UF_RESIDENCIA" VARCHAR(2) , 
	"SG_UF_RESIDENCIA" VARCHAR(2) , 
	"NU_IDADE" INT , 
	"TP_SEXO" VARCHAR(1) , 
	"TP_ESTADO_CIVIL" VARCHAR(1) , 
	"TP_COR_RACA" VARCHAR(1) , 
	"TP_NACIONALIDADE" VARCHAR(1) , 
	"CO_MUNICIPIO_NASCIMENTO" VARCHAR(7), 
	"NO_MUNICIPIO_NASCIMENTO" VARCHAR(45), 
	"CO_UF_NASCIMENTO" VARCHAR(2), 
	"SG_UF_NASCIMENTO" VARCHAR(2), 
	"TP_ST_CONCLUSAO" VARCHAR(1) , 
	"TP_ANO_CONCLUIU" VARCHAR(2) , 
	"TP_ESCOLA" VARCHAR(1) , 
	"TP_ENSINO" VARCHAR(1), 
	"IN_TREINEIRO" VARCHAR(1) , 
	"CO_ESCOLA" VARCHAR(8), 
	"CO_MUNICIPIO_ESC" VARCHAR(7), 
	"NO_MUNICIPIO_ESC" VARCHAR(45), 
	"CO_UF_ESC" VARCHAR(2), 
	"SG_UF_ESC" VARCHAR(2), 
	"TP_DEPENDENCIA_ADM_ESC" VARCHAR(1), 
	"TP_LOCALIZACAO_ESC" VARCHAR(1), 
	"TP_SIT_FUNC_ESC" VARCHAR(1), 
	"IN_BAIXA_VISAO" INT , 
	"IN_CEGUEIRA" INT , 
	"IN_SURDEZ" INT , 
	"IN_DEFICIENCIA_AUDITIVA" INT , 
	"IN_SURDO_CEGUEIRA" INT , 
	"IN_DEFICIENCIA_FISICA" INT , 
	"IN_DEFICIENCIA_MENTAL" INT , 
	"IN_DEFICIT_ATENCAO" INT , 
	"IN_DISLEXIA" INT , 
	"IN_DISCALCULIA" INT , 
	"IN_AUTISMO" INT , 
	"IN_VISAO_MONOCULAR" INT , 
	"IN_OUTRA_DEF" INT , 
	"IN_SABATISTA" INT , 
	"IN_GESTANTE" INT , 
	"IN_LACTANTE" INT , 
	"IN_IDOSO" INT , 
	"IN_ESTUDA_CLASSE_HOSPITALAR" INT , 
	"IN_SEM_RECURSO" INT , 
	"IN_BRAILLE" INT NULL, 
	"IN_AMPLIADA_24" INT , 
	"IN_AMPLIADA_18" INT , 
	"IN_LEDOR" INT , 
	"IN_ACESSO" INT , 
	"IN_TRANSCRICAO" INT , 
	"IN_LIBRAS" INT , 
--	"IN_TEMPO_ADICIONAL" INT , 
	"IN_LEITURA_LABIAL" INT , 
	"IN_MESA_CADEIRA_RODAS" INT , 
	"IN_MESA_CADEIRA_SEPARADA" INT , 
	"IN_APOIO_PERNA" INT , 
	"IN_GUIA_INTERPRETE" INT , 
	"IN_MACA" INT , 
	"IN_COMPUTADOR" INT , 
	"IN_CADEIRA_ESPECIAL" INT , 
	"IN_CADEIRA_CANHOTO" INT , 
	"IN_CADEIRA_ACOLCHOADA" INT , 
	"IN_PROVA_DEITADO" INT , 
	"IN_MOBILIARIO_OBESO" INT , 
	"IN_LAMINA_OVERLAY" INT , 
	"IN_PROTETOR_AURICULAR" INT , 
	"IN_MEDIDOR_GLICOSE" INT , 
	"IN_MAQUINA_BRAILE" INT , 
	"IN_SOROBAN" INT , 
	"IN_MARCA_PASSO" INT , 
	"IN_SONDA" INT , 
	"IN_MEDICAMENTOS" INT , 
	"IN_SALA_INDIVIDUAL" INT , 
	"IN_SALA_ESPECIAL" INT , 
	"IN_SALA_ACOMPANHANTE" INT , 
	"IN_MOBILIARIO_ESPECIFICO" INT , 
	"IN_MATERIAL_ESPECIFICO" INT , 
	"IN_NOME_SOCIAL" INT , 

	-----------------------------------------

	-- colunas que não tem nos outros anos;

	"IN_CERTIFICADO" INT , 
	"NO_ENTIDADE_CERTIFICACAO" VARCHAR(95), 
	"CO_UF_ENTIDADE_CERTIFICACAO" VARCHAR(2), 
	"SG_UF_ENTIDADE_CERTIFICACAO" VARCHAR(2),

	-----------------------------------------
	
	"CO_MUNICIPIO_PROVA" VARCHAR(7) , 
	"NO_MUNICIPIO_PROVA" VARCHAR(45) , 
	"CO_UF_PROVA" VARCHAR(2) , 
	"SG_UF_PROVA" VARCHAR(2) , 
	"TP_PRESENCA_CN" VARCHAR(1) , 
	"TP_PRESENCA_CH" VARCHAR(1) , 
	"TP_PRESENCA_LC" VARCHAR(1) , 
	"TP_PRESENCA_MT" VARCHAR(1) , 
	"CO_PROVA_CN" VARCHAR(3), 
	"CO_PROVA_CH" VARCHAR(3), 
	"CO_PROVA_LC" VARCHAR(3), 
	"CO_PROVA_MT" VARCHAR(3), 
	"NU_NOTA_CN" REAL,
	"NU_NOTA_CH" REAL,
	"NU_NOTA_LC" REAL,
	"NU_NOTA_MT" REAL,
	"TX_RESPOSTAS_CN" VARCHAR(45), 
	"TX_RESPOSTAS_CH" VARCHAR(45), 
	"TX_RESPOSTAS_LC" VARCHAR(50), 
	"TX_RESPOSTAS_MT" VARCHAR(45), 
	"TP_LINGUA" VARCHAR(1) , 
	"TX_GABARITO_CN" VARCHAR(45), 
	"TX_GABARITO_CH" VARCHAR(45), 
	"TX_GABARITO_LC" VARCHAR(50), 
	"TX_GABARITO_MT" VARCHAR(45), 
	"TP_STATUS_REDACAO" VARCHAR(1), 
	"NU_NOTA_COMP1" REAL,
	"NU_NOTA_COMP2" REAL,
	"NU_NOTA_COMP3" REAL,
	"NU_NOTA_COMP4" REAL,
	"NU_NOTA_COMP5" REAL,
	"NU_NOTA_REDACAO" REAL,
	"Q001" VARCHAR(1) , 
	"Q002" VARCHAR(1) , 
	"Q003" VARCHAR(1) , 
	"Q004" VARCHAR(1) , 
	"Q005" VARCHAR(2) , 
	"Q006" VARCHAR(1) , 
	"Q007" VARCHAR(1) , 
	"Q008" VARCHAR(1) , 
	"Q009" VARCHAR(1) , 
	"Q010" VARCHAR(1) , 
	"Q011" VARCHAR(1) , 
	"Q012" VARCHAR(1) , 
	"Q013" VARCHAR(1) , 
	"Q014" VARCHAR(1) , 
	"Q015" VARCHAR(1) , 
	"Q016" VARCHAR(1) , 
	"Q017" VARCHAR(1) , 
	"Q018" VARCHAR(1) , 
	"Q019" VARCHAR(1) , 
	"Q020" VARCHAR(1) , 
	"Q021" VARCHAR(1) , 
	"Q022" VARCHAR(1) , 
	"Q023" VARCHAR(1) , 
	"Q024" VARCHAR(1) , 
	"Q025" VARCHAR(1) , 
	"Q026" VARCHAR(1) ,
	"Q027" VARCHAR(1) ,
	"Q028" VARCHAR(1) ,
	"Q029" VARCHAR(1) ,
	"Q030" VARCHAR(1) ,
	"Q031" VARCHAR(1) ,
	"Q032" VARCHAR(1) ,
	"Q033" VARCHAR(1) ,
	"Q034" VARCHAR(1) ,
	"Q035" VARCHAR(1) ,
	"Q036" VARCHAR(1) ,
	"Q037" VARCHAR(1) ,
	"Q038" VARCHAR(1) ,
	"Q039" VARCHAR(1) ,
	"Q040" VARCHAR(1) ,
	"Q041" VARCHAR(1) ,
	"Q042" VARCHAR(1) ,
	"Q043" VARCHAR(1) ,
	"Q044" VARCHAR(1) ,
	"Q045" VARCHAR(1) ,
	"Q046" VARCHAR(1) ,
	"Q047" VARCHAR(1) ,
	"Q048" VARCHAR(1) ,
	"Q049" VARCHAR(1) ,
	"Q050" VARCHAR(1)
);


-- lista das coolunas do enem de 2016
("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE",                 "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE",            "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL",                                                                                                             "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")

("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_SABATISTA", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_MACA", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "IN_CERTIFICADO", "NO_ENTIDADE_CERTIFICACAO", "CO_UF_ENTIDADE_CERTIFICACAO", "SG_UF_ENTIDADE_CERTIFICACAO", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027", "Q028", "Q029", "Q030", "Q031", "Q032", "Q033", "Q034", "Q035", "Q036", "Q037", "Q038", "Q039", "Q040", "Q041", "Q042", "Q043", "Q044", "Q045", "Q046", "Q047", "Q048", "Q049", "Q050")
("NU_INSCRICAO", "NU_ANO", "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_CERTIFICADO", "NO_ENTIDADE_CERTIFICACAO", "CO_UF_ENTIDADE_CERTIFICACAO", "SG_UF_ENTIDADE_CERTIFICACAO", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027", "Q028", "Q029", "Q030", "Q031", "Q032", "Q033", "Q034", "Q035", "Q036", "Q037", "Q038", "Q039", "Q040", "Q041", "Q042", "Q043", "Q044", "Q045", "Q046", "Q047", "Q048", "Q049", "Q050")




-- No enem de 2016 não tem as seguintes:
, "IN_GESTANTE",

-- No enem de 2016 tem as seguintes a mais do que outros anos:
"IN_SABATISTA", "IN_GESTANTE", "IN_MACA,"IN_CERTIFICADO", "NO_ENTIDADE_CERTIFICACAO", "CO_UF_ENTIDADE_CERTIFICACAO", "SG_UF_ENTIDADE_CERTIFICACAO", "

-- Códigos anteriores

("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")


COPY enem_2018_1 ("NU_INSCRICAO", "NU_ANO", "CO_MUNICIPIO_RESIDENCIA", "NO_MUNICIPIO_RESIDENCIA", "CO_UF_RESIDENCIA", "SG_UF_RESIDENCIA", "NU_IDADE", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_NACIONALIDADE", "CO_MUNICIPIO_NASCIMENTO", "NO_MUNICIPIO_NASCIMENTO", "CO_UF_NASCIMENTO", "SG_UF_NASCIMENTO", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU", "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "CO_ESCOLA", "CO_MUNICIPIO_ESC", "NO_MUNICIPIO_ESC", "CO_UF_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC", "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "IN_BAIXA_VISAO", "IN_CEGUEIRA", "IN_SURDEZ", "IN_DEFICIENCIA_AUDITIVA", "IN_SURDO_CEGUEIRA", "IN_DEFICIENCIA_FISICA", "IN_DEFICIENCIA_MENTAL", "IN_DEFICIT_ATENCAO", "IN_DISLEXIA", "IN_DISCALCULIA", "IN_AUTISMO", "IN_VISAO_MONOCULAR", "IN_OUTRA_DEF", "IN_GESTANTE", "IN_LACTANTE", "IN_IDOSO", "IN_ESTUDA_CLASSE_HOSPITALAR", "IN_SEM_RECURSO", "IN_BRAILLE", "IN_AMPLIADA_24", "IN_AMPLIADA_18", "IN_LEDOR", "IN_ACESSO", "IN_TRANSCRICAO", "IN_LIBRAS", "IN_LEITURA_LABIAL", "IN_MESA_CADEIRA_RODAS", "IN_MESA_CADEIRA_SEPARADA", "IN_APOIO_PERNA", "IN_GUIA_INTERPRETE", "IN_COMPUTADOR", "IN_CADEIRA_ESPECIAL", "IN_CADEIRA_CANHOTO", "IN_CADEIRA_ACOLCHOADA", "IN_PROVA_DEITADO", "IN_MOBILIARIO_OBESO", "IN_LAMINA_OVERLAY", "IN_PROTETOR_AURICULAR", "IN_MEDIDOR_GLICOSE", "IN_MAQUINA_BRAILE", "IN_SOROBAN", "IN_MARCA_PASSO", "IN_SONDA", "IN_MEDICAMENTOS", "IN_SALA_INDIVIDUAL", "IN_SALA_ESPECIAL", "IN_SALA_ACOMPANHANTE", "IN_MOBILIARIO_ESPECIFICO", "IN_MATERIAL_ESPECIFICO", "IN_NOME_SOCIAL", "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA", "CO_UF_PROVA", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "CO_PROVA_CN", "CO_PROVA_CH", "CO_PROVA_LC", "CO_PROVA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "TX_RESPOSTAS_CN", "TX_RESPOSTAS_CH", "TX_RESPOSTAS_LC", "TX_RESPOSTAS_MT", "TP_LINGUA", "TX_GABARITO_CN", "TX_GABARITO_CH", "TX_GABARITO_LC", "TX_GABARITO_MT", "TP_STATUS_REDACAO", "NU_NOTA_COMP1", "NU_NOTA_COMP2", "NU_NOTA_COMP3", "NU_NOTA_COMP4", "NU_NOTA_COMP5", "NU_NOTA_REDACAO", "Q001", "Q002", "Q003", "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011", "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019", "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", "Q026", "Q027")
FROM '/media/icaro/Icaro-Dias/MICRODADOS_ENEM_2018.csv' 
WITH DELIMITER ';' CSV HEADER;

/*LOAD DATA LOCAL INFILE "/home/icaro/Downloads/microdados_enem_2019_completo/DADOS/MICRODADOS_ENEM_2019.csv"
INTO TABLE enem
CHARACTER SET ASCII
FIELDS TERMINATED BY ";" 
LINES TERMINATED BY "\n"
IGNORE 1 LINES;*/