
from edados.formularios.filtros.formulario_1_filtros import Formulario_filtros
from edados.formularios.formulario_3.formulario_3 import Formulario_3
from edados.formularios.formulario_3.formulario_3 import Formulario_3_2
from django.contrib.auth.decorators import login_required
from django.utils.html import format_html_join
from edados.database import bd_formulario_3
from django.shortcuts import render
import plotly.graph_objects as go
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

CONTAGEM = 0
CONTAGEMMicrodado_Amostra = 0
prova_pdf = ""

def formatar(valor):
    return "{:,.2f}".format(valor)

def prova_nome_pdf(filtro_cor_da_prova, filtro_ano):
    
    print( "filtro_cor_da_prova:"+ str(filtro_cor_da_prova)+ "  filtro_ano:"+ str(filtro_ano))
    
    if(filtro_ano=="2019"):
        if('503'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('504'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('505'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('506'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('507'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('508'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('509'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('510'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('511'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('512'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('513'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('514'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('515'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('516'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('517'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('518'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('519'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('520'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('521'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('522'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('523'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('524'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('525'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('526'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('527'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('528'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('529'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO_AMPLIADA.pdf"
        elif('530'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_02_DIA_1_AMARELO_SUPERAMPLIADA.pdf"
        elif('531'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('532'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('533'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('534'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('535'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('536'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('537'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA_AMPLIADA.pdf"
        elif('538'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_06_DIA_2_CINZA_SUPERAMPLIADA.pdf"
        elif('539'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('540'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('541'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('542'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('543'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('544'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('545'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('546'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_08_DIA_2_ROSA.pdf"
        elif('547'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('548'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('549'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('550'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('551'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('552'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('553'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('554'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('555'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('556'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('557'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('558'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_08_DIA_2_ROSA.pdf"
        elif('559'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('560'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('561'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('562'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('563'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('564'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('565'==filtro_cor_da_prova):
            prova_pdf="ENEM_2019_P2_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
    elif(filtro_ano=="2018"):
        if('447'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('448'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('449'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('450'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('451'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('452'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('453'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('454'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('455'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('456'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('457'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('458'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('459'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('460'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('461'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('462'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('463'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('464'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('465'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('466'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('467'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('468'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('469'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('470'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('471'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('472'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('473'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_02_DIA_1_AMARELO_AMPLIADA.pdf"
        elif('574'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_02_DIA_1_AMARELO_SUPERAMPLIADA.pdf"
        elif('475'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('476'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('477'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('478'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('479'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('480'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('481'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_06_DIA_2_CINZA_AMPLIADA.pdf"
        elif('482'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_06_DIA_2_CINZA_SUPERAMPLIADA.pdf"
        elif('483'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('484'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('485'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('486'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('487'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('488'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('489'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('490'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_08_DIA_2_ROSA.pdf"
        elif('491'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('492'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('493'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('494'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('495'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('496'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('497'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('498'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('499'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('500'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('501'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('502'==filtro_cor_da_prova):
            prova_pdf="ENEM_2018_P2_CAD_08_DIA_2_ROSA.pdf"
            
    elif(filtro_ano=="2017"):
        if('391'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('392'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('393'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('394'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('395'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('396'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('397'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('398'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('399'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('400'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('401'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('402'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('403'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('404'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('405'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('406'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('407'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('408'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('409'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('410'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('411'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('412'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('413'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('414'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('415'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_01_DIA_1_AZUL.pdf"
        elif('416'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_02_DIA_1_AMARELO.pdf"
        elif('417'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_02_DIA_1_AMARELO_AMPLIADA.pdf"
        elif('418'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_02_DIA_1_AMARELO_SUPERAMPLIADA.pdf"
        elif('419'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_03_DIA_1_BRANCO.pdf"
        elif('420'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_04_DIA_1_ROSA.pdf"
        elif('421'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_09_DIA_1_LARANJA_LEDOR.pdf"
        elif('422'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_10_DIA_1_VERDE_LIBRAS.pdf"
        elif('423'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_05_DIA_2_AMARELO.pdf"
        elif('424'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_06_DIA_2_CINZA.pdf"
        elif('425'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_06_DIA_2_CINZA_AMPLIADA.pdf"
        elif('426'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_06_DIA_2_CINZA_SUPERAMPLIADA.pdf"
        elif('427'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_07_DIA_2_AZUL.pdf"
        elif('428'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_08_DIA_2_ROSA.pdf"
        elif('429'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_11_DIA_2_LARANJA_LEDOR.pdf"
        elif('430'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P1_CAD_12_DIA_2_VERDE_LIBRAS.pdf"
        elif('431'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('432'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('433'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('434'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_08_DIA_2_ROSA.pdf"
        elif('435'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('436'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('437'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('438'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('439'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_01_DIA_1_AZUL.pdf"
        elif('440'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_02_DIA_1_AMARELO.pdf"
        elif('441'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_03_DIA_1_BRANCO.pdf"
        elif('442'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_04_DIA_1_ROSA.pdf"
        elif('443'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_05_DIA_2_AMARELO.pdf"
        elif('444'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_06_DIA_2_CINZA.pdf"
        elif('445'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_07_DIA_2_AZUL.pdf"
        elif('446'==filtro_cor_da_prova):
            prova_pdf="ENEM_2017_P2_CAD_08_DIA_2_ROSA.pdf"
        else:
            prova_pdf="desenvolvimento.pdf"
            
    print(prova_pdf)
    return prova_pdf

def nome_prova(codigo, filtro_ano): 
    print(codigo)
    print("=============================================")   
    print(filtro_ano)
    if (filtro_ano=="2019"):
        if( codigo == '503' or 
            codigo == '504' or
            codigo == '505' or
            codigo == '506' or
            codigo == '519' or
            codigo == '523' or
            codigo == '543' or
            codigo == '544' or
            codigo == '545' or
            codigo == '546'):
            nome_prova = 'CO_PROVA_CN'
        elif(
            codigo == '507' or 
            codigo == '508' or
            codigo == '509' or
            codigo == '510' or
            codigo == '520' or
            codigo == '524' or
            codigo == '547' or
            codigo == '548' or
            codigo == '549' or
            codigo == '550' or
            codigo == '564'):
            nome_prova = 'CO_PROVA_CH'
        elif(
            codigo == '511' or 
            codigo == '512' or
            codigo == '513' or
            codigo == '514' or
            codigo == '521' or
            codigo == '525' or
            codigo == '551' or
            codigo == '552' or
            codigo == '553' or
            codigo == '554' or
            codigo == '565'):
            nome_prova = 'CO_PROVA_LC'
        elif(
            codigo == '515' or
            codigo == '516' or
            codigo == '517' or
            codigo == '518' or
            codigo == '522' or
            codigo == '526' or
            codigo == '555' or
            codigo == '556' or
            codigo == '557' or
            codigo == '558'):
            nome_prova = 'CO_PROVA_MT'
    elif (filtro_ano=="2018"):
        if( codigo == '447' or 
            codigo == '448' or
            codigo == '449' or
            codigo == '450' or
            codigo == '463' or
            codigo == '467' or
            codigo == '487' or
            codigo == '488' or
            codigo == '489' or
            codigo == '490'):
            nome_prova = 'CO_PROVA_CN'
        elif(
            codigo == '451' or 
            codigo == '452' or
            codigo == '453' or
            codigo == '454' or
            codigo == '464' or
            codigo == '468' or
            codigo == '491' or
            codigo == '492' or
            codigo == '493' or
            codigo == '494'):
            nome_prova = 'CO_PROVA_CH'
        elif(
            codigo == '455' or 
            codigo == '456' or
            codigo == '457' or
            codigo == '458' or
            codigo == '465' or
            codigo == '469' or
            codigo == '495' or
            codigo == '496' or
            codigo == '497' or
            codigo == '498' ):
            nome_prova = 'CO_PROVA_LC'
        elif(
            codigo == '459' or
            codigo == '460' or
            codigo == '461' or
            codigo == '462' or
            codigo == '466' or
            codigo == '470' or
            codigo == '499' or
            codigo == '500' or
            codigo == '501' or
            codigo == '502'):
            nome_prova = 'CO_PROVA_MT'
    elif (filtro_ano=="2017"):
        if( codigo == '391' or 
            codigo == '392' or
            codigo == '393' or
            codigo == '394' or
            codigo == '407' or
            codigo == '411' or
            codigo == '431' or
            codigo == '432' or
            codigo == '433' or
            codigo == '434'):
            nome_prova = 'CO_PROVA_CN'
        elif(
            codigo == '395' or 
            codigo == '396' or
            codigo == '397' or
            codigo == '398' or
            codigo == '408' or
            codigo == '412' or
            codigo == '435' or
            codigo == '436' or
            codigo == '437' or
            codigo == '438'):
            nome_prova = 'CO_PROVA_CH'
        elif(
            codigo == '399' or 
            codigo == '400' or
            codigo == '401' or
            codigo == '402' or
            codigo == '409' or
            codigo == '413' or
            codigo == '439' or
            codigo == '440' or
            codigo == '441' or
            codigo == '442'):
            nome_prova = 'CO_PROVA_LC'
        elif(
            codigo == '403' or
            codigo == '404' or
            codigo == '405' or
            codigo == '406' or
            codigo == '410' or
            codigo == '414' or
            codigo == '443' or
            codigo == '444' or
            codigo == '445' or
            codigo == '446'):
            nome_prova = 'CO_PROVA_MT'
    else:
        nome_prova = 'DEU_RUIM'
           
    return nome_prova

@login_required
def formulario_2(request):

    if request.method == 'GET':
        menssagem = 'Quantidade de acertos e erros por questão:'
        menssagem_informativa = """ Aplicar filtros para visualizar resultados entre diferentes grupos de alunos, como sexo, região, entre outros critérios de filtragem.
        Contrastar subgrupos específicos de alunos para diferentes provas e questões selecionadas, proporcionando uma análise mais segmentada e personalizada.
        Comparar múltiplas provas, visando a compreensão das disparidades e desigualdades presentes nos resultados.
        Compreender as questões em que os alunos apresentam maior ou menor desempenho."""
        
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>•{}</p>', ((line,) for line in menssagem_informativa))
        
        form = Formulario_3_2()
        form_filtro_grupo_A = Formulario_filtros(prefix='grupo_A')
        form_filtro_grupo_B = Formulario_filtros(prefix='grupo_B')

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,            
            'form_filtro_grupo_A' : form_filtro_grupo_A,
            'form_filtro_grupo_B' : form_filtro_grupo_B,
        }
        return render(request, 'base/formulario_3/quest_formulario_3_2.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_3_2(request.POST)
        # form_filtro = Formulario_filtros(request.POST)
        
        form_filtro_grupo_A = Formulario_filtros(request.POST, prefix='grupo_A')
        form_filtro_grupo_B = Formulario_filtros(request.POST, prefix='grupo_B')

        acerto_erro = form.data['acerto_erro']
        filtro_ano = form.data['ano']

        if form_filtro_grupo_A.is_valid() and form_filtro_grupo_B.is_valid():
            
            # Formulario de Filtro do GRUPO A
            filtro_deficiencia = form_filtro_grupo_A.cleaned_data['deficiencia']
            filtro_estado_civil = form_filtro_grupo_A.cleaned_data['estado_civil']
            filtro_cor = form_filtro_grupo_A.cleaned_data['cor']
            filtro_sexo = form_filtro_grupo_A.cleaned_data['sexo']
            filtro_estado = form_filtro_grupo_A.cleaned_data['estado']
            filtro_cidade = form_filtro_grupo_A.cleaned_data['cidade']
            filtro_amostra = form_filtro_grupo_A.cleaned_data['amostra']
            filtro_recurso = form_filtro_grupo_A.cleaned_data['recurso']
            filtro_localizacao_da_escola = form_filtro_grupo_A.cleaned_data['localizacao_da_escola']
        
            # Formulario de Filtro do GRUPO B
            filtro_deficiencia_grupo_B = form_filtro_grupo_B.cleaned_data['deficiencia']
            filtro_estado_civil_grupo_B = form_filtro_grupo_B.cleaned_data['estado_civil']
            filtro_cor_grupo_B = form_filtro_grupo_B.cleaned_data['cor']
            filtro_sexo_grupo_B = form_filtro_grupo_B.cleaned_data['sexo']
            filtro_estado_grupo_B = form_filtro_grupo_B.cleaned_data['estado']
            filtro_cidade_grupo_B = form_filtro_grupo_B.cleaned_data['cidade']
            filtro_amostra_grupo_B = form_filtro_grupo_B.cleaned_data['amostra']
            filtro_recurso_grupo_B = form_filtro_grupo_B.cleaned_data['recurso']
            filtro_localizacao_da_escola_grupo_B = form_filtro_grupo_B.cleaned_data['localizacao_da_escola']
        
        if(filtro_ano=="2019"):
            filtro_cor_da_prova1 = request.POST.get('prova1')
            filtro_cor_da_prova2 = request.POST.get('prova2')
            filtro_cor_da_prova3 = request.POST.get('prova3')
            filtro_cor_da_prova4 = request.POST.get('prova4')            
            questao1 = request.POST.get('questao1')
            questao2 = request.POST.get('questao2')
            questao3 = request.POST.get('questao3')
            questao4 = request.POST.get('questao4')
        elif(filtro_ano=="2018"):
            filtro_cor_da_prova1 = request.POST.get('prova1_2018')
            filtro_cor_da_prova2 = request.POST.get('prova2_2018')
            filtro_cor_da_prova3 = request.POST.get('prova3_2018')
            filtro_cor_da_prova4 = request.POST.get('prova4_2018')            
            questao1 = request.POST.get('questao1_2018')
            questao2 = request.POST.get('questao2_2018')
            questao3 = request.POST.get('questao3_2018')
            questao4 = request.POST.get('questao4_2018')
        elif(filtro_ano=="2017"):
            filtro_cor_da_prova1 = request.POST.get('prova1_2017')
            filtro_cor_da_prova2 = request.POST.get('prova2_2017')
            filtro_cor_da_prova3 = request.POST.get('prova3_2017')
            filtro_cor_da_prova4 = request.POST.get('prova4_2017')            
            questao1 = request.POST.get('questao1_2017')
            questao2 = request.POST.get('questao2_2017')
            questao3 = request.POST.get('questao3_2017')
            questao4 = request.POST.get('questao4_2017')
        
        if (questao3=="Nenhuma"):
            filtro_cor_da_prova3 = "Nenhuma"
        if (questao4=="Nenhuma"):
            filtro_cor_da_prova4 = "Nenhuma"

        prova_pdf = prova_nome_pdf(filtro_cor_da_prova=filtro_cor_da_prova1, filtro_ano=filtro_ano)
        if(filtro_ano=="2019"):
            prova_pdf = '/pdf/PROVAS_E_GABARITOS/'+prova_pdf
        elif(filtro_ano=="2018"):
            prova_pdf = '/pdf/PROVAS E GABARITOS_2018/'+prova_pdf
        elif(filtro_ano=="2017"):
            prova_pdf = '/pdf/PROVAS E GABARITOS_2017/'+prova_pdf
            
        prova = nome_prova(filtro_cor_da_prova1, filtro_ano=filtro_ano)
        
        
        # Formulario de Filtro
        if prova == 'CO_PROVA_LC':
            respostas = "TX_RESPOSTAS_LC"
            gabarito = "TX_GABARITO_LC"
        elif prova == 'CO_PROVA_CN':
            respostas = "TX_RESPOSTAS_CN"
            gabarito = "TX_GABARITO_CN"
        elif prova == 'CO_PROVA_MT':
            respostas = "TX_RESPOSTAS_MT"
            gabarito = "TX_GABARITO_MT"
        elif prova == 'CO_PROVA_CH':
            respostas = "TX_RESPOSTAS_CH"
            gabarito = "TX_GABARITO_CH"

        if(filtro_sexo != 'todos'):
            Amostra = [prova, 'TP_SEXO', respostas, gabarito]
            Microdado_Prova1 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
                filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova1, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_cor=filtro_cor, 
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_ano=filtro_ano)
            Microdado_Prova2 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo_grupo_B, 
                filtro_cidade=filtro_cidade_grupo_B, 
                filtro_cor_da_prova=filtro_cor_da_prova2, 
                filtro_deficiencia=filtro_deficiencia_grupo_B,
                filtro_amostra=filtro_amostra_grupo_B, 
                filtro_cor=filtro_cor_grupo_B,   
                filtro_estado=filtro_estado_grupo_B, 
                filtro_recurso=filtro_recurso_grupo_B,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                filtro_estado_civil=filtro_estado_civil_grupo_B, 
                filtro_ano=filtro_ano)
            if(filtro_cor_da_prova3!='Nenhuma'):                
                Microdado_Prova3 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova3, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
            if(filtro_cor_da_prova4!='Nenhuma'):                
                Microdado_Prova4 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova4, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
        else:
            Amostra = [prova, respostas, gabarito]
            Microdado_Prova1 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
                filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova1, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra,    
                filtro_cor=filtro_cor, 
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_ano=filtro_ano)
            
            Microdado_Prova2 = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo_grupo_B, 
                filtro_cidade=filtro_cidade_grupo_B, 
                filtro_cor_da_prova=filtro_cor_da_prova2, 
                filtro_deficiencia=filtro_deficiencia_grupo_B,
                filtro_amostra=filtro_amostra_grupo_B,    
                filtro_cor=filtro_cor_grupo_B, 
                filtro_estado=filtro_estado_grupo_B, 
                filtro_recurso=filtro_recurso_grupo_B,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                filtro_estado_civil=filtro_estado_civil_grupo_B, 
                filtro_ano=filtro_ano)
        
            if(filtro_cor_da_prova3!='Nenhuma'):                
                Microdado_Prova3 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova3, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
            if(filtro_cor_da_prova4!='Nenhuma'):                
                Microdado_Prova4 = bd_formulario_3.buscar_dataframe_no_banco(
                    Amostra, 
                    filtro_sexo=filtro_sexo_grupo_B, 
                    filtro_cidade=filtro_cidade_grupo_B, 
                    filtro_cor_da_prova=filtro_cor_da_prova4, 
                    filtro_deficiencia=filtro_deficiencia_grupo_B,
                    filtro_amostra=filtro_amostra_grupo_B, 
                    filtro_cor=filtro_cor_grupo_B,   
                    filtro_estado=filtro_estado_grupo_B, 
                    filtro_recurso=filtro_recurso_grupo_B,
                    filtro_localizacao_da_escola=filtro_localizacao_da_escola_grupo_B, 
                    filtro_estado_civil=filtro_estado_civil_grupo_B, 
                    filtro_ano=filtro_ano)
                
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            # CONTAGEMMicrodado_Amostra = 3893743
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
        CONTAGEM = Microdado_Prova1[prova].count()
        
        menssagem = 'Quantidade de acertos e erros por questão:'
        
        # Resetar o índice do DataFrame Microdado_Prova1
        Microdado_Prova1.reset_index(inplace=True)

        # Extrair as respostas da prova 1
        resposta = Microdado_Prova1[respostas]
        quantidade_de_respostas =  (Microdado_Prova1[respostas].count()-1)
        quantidadeParcial_grupo_A = Microdado_Prova1[respostas].count() 
        gabarito_prova1 = Microdado_Prova1[gabarito]

        acertos = [0] * 2
        acertos_porcentagem = [0] * 1

        if quantidade_de_respostas >= 0:
            linha_do_gabarito = gabarito_prova1.iloc[quantidade_de_respostas]
        

        j = 1
        questao1 = int(questao1)-1

        for i in range(quantidade_de_respostas):
            if resposta[i] == '':
                resposta[i] = "............................................."
            linha_da_resposta = resposta[i]

            resposta_gabarito = linha_do_gabarito[questao1]
            resposta_candidato = linha_da_resposta[questao1]

            if acerto_erro == 'acertos':
                if resposta_candidato == resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''
            else:
                if resposta_candidato != resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''

        acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

        acertos_pd_prova1 = pd.DataFrame(acertos_porcentagem)
        acertos_pd_prova1 = acertos_pd_prova1.reset_index(drop=True)
        acertos_pd_prova1.index = acertos_pd_prova1.index + int(questao1)

        # Resetar o índice do DataFrame Microdado_Prova2
        Microdado_Prova2.reset_index(inplace=True)

        # Extrair as respostas da prova 2
        resposta = Microdado_Prova2[respostas]
        quantidade_de_respostas = Microdado_Prova2[respostas].count() - 1
        quantidadeParcial_grupo_B = Microdado_Prova2[respostas].count()
        gabarito_prova2 = Microdado_Prova2[gabarito]

        acertos = [0] * 2
        acertos_porcentagem = [0] * 1

        if quantidade_de_respostas >= 0:
            linha_do_gabarito = gabarito_prova2.iloc[quantidade_de_respostas]

        j = 1
        questao2 = int(questao2)-1

        for i in range(quantidade_de_respostas):
            if resposta[i] == '':
                resposta[i] = "............................................."
            linha_da_resposta = resposta[i]

            resposta_gabarito = linha_do_gabarito[questao2]
            resposta_candidato = linha_da_resposta[questao2]

            if acerto_erro == 'acertos':
                if resposta_candidato == resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''
            else:
                if resposta_candidato != resposta_gabarito:
                    acertos[j] += 1
                    resposta_candidato = ''

        acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

        acertos_pd_prova2 = pd.DataFrame(acertos_porcentagem)
        acertos_pd_prova2 = acertos_pd_prova2.reset_index(drop=True)
        acertos_pd_prova2.index = acertos_pd_prova2.index + int(questao2)
        
        # PROVA 3
        
        if(filtro_cor_da_prova3!='Nenhuma'):  
            # Resetar o índice do DataFrame Microdado_Prova3
            Microdado_Prova3.reset_index(inplace=True)

            # Extrair as respostas da prova 3
            resposta = Microdado_Prova3[respostas]
            quantidade_de_respostas = Microdado_Prova3[respostas].count() - 1
            gabarito_prova3 = Microdado_Prova3[gabarito]

            acertos = [0] * 2
            acertos_porcentagem = [0] * 1

            if quantidade_de_respostas >= 0:
                linha_do_gabarito = gabarito_prova3.iloc[quantidade_de_respostas]

            j = 0
            questao3 = int(questao3)-1

            for i in range(quantidade_de_respostas):
                if resposta[i] == '':
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[questao3]
                resposta_candidato = linha_da_resposta[questao3]

                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''

            acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

            acertos_pd_prova3 = pd.DataFrame(acertos_porcentagem)
            acertos_pd_prova3 = acertos_pd_prova3.reset_index(drop=True)
            acertos_pd_prova3.index = acertos_pd_prova3.index + int(questao3)            
        # FINAL PROVA 3
        
        # PROVA 4        
        if(filtro_cor_da_prova4!='Nenhuma'):  
            # Resetar o índice do DataFrame Microdado_Prova3
            Microdado_Prova4.reset_index(inplace=True)

            # Extrair as respostas da prova 3
            resposta = Microdado_Prova4[respostas]
            quantidade_de_respostas = Microdado_Prova4[respostas].count() - 1
            quantidadeParcial_grupo_B = Microdado_Prova4[respostas].count()
            gabarito_prova4 = Microdado_Prova4[gabarito]

            acertos = [0] * 2
            acertos_porcentagem = [0] * 1

            if quantidade_de_respostas >= 0:
                linha_do_gabarito = gabarito_prova4.iloc[quantidade_de_respostas]

            j = 0
            questao4 = int(questao4)-1

            for i in range(quantidade_de_respostas):
                if resposta[i] == '':
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[questao4]
                resposta_candidato = linha_da_resposta[questao4]

                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] += 1
                        resposta_candidato = ''

            acertos_porcentagem[0] = (acertos[j] / quantidade_de_respostas) * 100

            acertos_pd_prova4 = pd.DataFrame(acertos_porcentagem)
            acertos_pd_prova4 = acertos_pd_prova4.reset_index(drop=True)
            acertos_pd_prova4.index = acertos_pd_prova4.index + int(questao4)
            
        # FINAL PROVA 4
        
        # Colocando nome no DataFrame
        acertos_pd_prova1.columns = ['porcentagem_de_acertos']
        texto = acertos_pd_prova1.porcentagem_de_acertos

        # Colocando nome no DataFrame
        acertos_pd_prova2.columns = ['porcentagem_de_acertos']
        texto = acertos_pd_prova2.porcentagem_de_acertos        
        
        # Colocando nome no DataFrame PROVA 3        
        if(filtro_cor_da_prova3!='Nenhuma'):  
            acertos_pd_prova3.columns = ['porcentagem_de_acertos']
            texto = acertos_pd_prova3.porcentagem_de_acertos

        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova4!='Nenhuma'):  
            acertos_pd_prova4.columns = ['porcentagem_de_acertos']
            texto = acertos_pd_prova4.porcentagem_de_acertos

        relatorio_em_grafico = go.Figure()

        relatorio_em_grafico.add_bar(
            y=acertos_pd_prova1['porcentagem_de_acertos'],
            x=(acertos_pd_prova1.index+1),
            text=acertos_pd_prova1['porcentagem_de_acertos'],
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=filtro_cor_da_prova1
        )

        relatorio_em_grafico.add_bar(
            y=acertos_pd_prova2['porcentagem_de_acertos'],
            x=(acertos_pd_prova2.index+1),
            text=acertos_pd_prova2['porcentagem_de_acertos'],
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=filtro_cor_da_prova2
        )
        
        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova3!='Nenhuma'):  
            relatorio_em_grafico.add_bar(
                y=acertos_pd_prova3['porcentagem_de_acertos'],
                x=(acertos_pd_prova3.index+1),
                text=acertos_pd_prova3['porcentagem_de_acertos'],
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=filtro_cor_da_prova3
            )

        # Colocando nome no DataFrame PROVA 4       
        if(filtro_cor_da_prova4!='Nenhuma'):  
            relatorio_em_grafico.add_bar(
                y=acertos_pd_prova4['porcentagem_de_acertos'],
                x=(acertos_pd_prova4.index+1),
                text=acertos_pd_prova4['porcentagem_de_acertos'],
                texttemplate='%{text:.2f}%',
                textposition='auto',
                name=filtro_cor_da_prova4
            )
            
        if(filtro_cor_da_prova3=='Nenhuma' and filtro_cor_da_prova4=='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1 ]
        elif(filtro_cor_da_prova3!='Nenhuma' and filtro_cor_da_prova4=='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao3)+1]
        elif(filtro_cor_da_prova3=='Nenhuma' and filtro_cor_da_prova4!='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao4)+1]
        elif(filtro_cor_da_prova3!='Nenhuma' and filtro_cor_da_prova4!='Nenhuma'):
            indexes = [int(questao1)+1, int(questao2)+1, int(questao3)+1, int(questao4)+1]
                    
        relatorio_em_grafico.update_layout(
            xaxis=dict(
                tickvals=indexes,
                tickmode="array",
                titlefont=dict(size=10),
            ),
            title="Percentual de " + acerto_erro + " nas questões na prova de " + prova + " no ano de " + filtro_ano,
            height=500,
            margin={'t': 50, 'l': 50},
            yaxis={'domain': [0, 1]},
            xaxis2={'anchor': 'y2'},
            xaxis_title=("Número da da questão na prova: " + prova),
            yaxis_title="Desempenho em percentual de acertos.",
            yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )

        relatorio = relatorio_em_grafico.to_html()


        
        menssagem1 = 'PDF da prova de '+prova
        anotacao_mensagem = 'Q1, Q2, Q3, Q4, ..., Corresponde ao numero da questão na prova '+ prova
        anotacao = """Através deste gráfico, é possível visualizar a proporção em 
        porcentagem de quantos alunos acertaram ou erraram a questão especificada pelo 
        "Q". Dessa forma, é possível identificar em qual questão da prova deve-se 
        fazer uma análise para entender o motivo de a questão ter uma maior porcentagem 
        de alunos que erraram."""
        
        # Cria a mensagem de anotação
        informativo = '<h5 class="mb-0">Informativo:</h5>'

        # Formata a mensagem em HTML
        anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao}<hr class="mt-0">{anotacao_mensagem}</div>'
        
        context = {
            'form' : form,
            'menssagem':menssagem,
            'relatorio'  :relatorio,
            'anotacao_mensagem' : anotacao_mensagem,
            'menssagem1' : menssagem1,
            'prova_pdf'  :  prova_pdf,
            'form_filtro_grupo_A' : form_filtro_grupo_A,
            'form_filtro_grupo_B' : form_filtro_grupo_B,
            'quantidadeParcial_grupo_A' : quantidadeParcial_grupo_A,
            'quantidadeParcial_grupo_B' : quantidadeParcial_grupo_B,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
        }

    return render(request, 'base/formulario_3/relatorio_formulario_3_2.html', context=context)


@login_required
def formulario_3(request):

    if request.method == 'GET':
        menssagem = 'Quantidade de acertos e erros por prova:'
        menssagem_informativa = """ Permitir ao usuário filtrar os dados dos microdados do ENEM por ano, sexo, região e outros critérios relevantes.
        Gerar gráfico de barras com a porcentagem de alunos que acertaram ou erraram cada questão da prova.
        Compreender as questões em que os alunos apresentam maior ou menor desempenho."""
        
        menssagem_informativa = menssagem_informativa.split('\n')
        menssagem_informativa = format_html_join('\n', '<p>•{}</p>', ((line,) for line in menssagem_informativa))
        

        form = Formulario_3()
        form_filtro = Formulario_filtros()

        context = {
            'form' : form,
            'menssagem' : menssagem,
            'menssagem_informativa' : menssagem_informativa,
            'form_filtro' : form_filtro
        }
        return render(request, 'base/formulario_3/quest_formulario_3.html', context=context)
    else:


        # Recebendo fomulario da tela
        form = Formulario_3(request.POST)
        form_filtro = Formulario_filtros(request.POST)

        filtro_deficiencia = form.data['deficiencia']
        acerto_erro = form.data['acerto_erro']

        # Formulario de Filtro
        filtro_deficiencia = form_filtro.data['deficiencia']
        filtro_estado_civil = form_filtro.data['estado_civil']
        filtro_cor = form_filtro.data['cor']
        filtro_sexo = form_filtro.data['sexo']
        filtro_ano = form_filtro.data['ano']
        filtro_escola = form_filtro.data['escola']
        filtro_nacionalidade = form_filtro.data['nacionalidade']
        filtro_estado = form_filtro.data['estado']
        filtro_cidade = form_filtro.data['cidade']
        filtro_amostra = form_filtro.data['amostra']
        filtro_recurso = form_filtro.data['recurso']
        filtro_localizacao_da_escola = form_filtro.data['localizacao_da_escola']
        filtro_ltp_adm_escola = form_filtro.data['tp_adm_escola']
        filtro_ano_de_conclusao = form_filtro.data['ano_de_conclusao']
        
        # Variáveis vindas do Formulario
        if (filtro_ano=="2019"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2019')
        elif (filtro_ano=="2018"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2018')
        elif (filtro_ano=="2017"):
            filtro_cor_da_prova = request.POST.get('cor_da_prova_2017')

        prova_pdf = prova_nome_pdf(filtro_cor_da_prova=filtro_cor_da_prova, filtro_ano=filtro_ano)
        if(filtro_ano=="2019"):
            prova_pdf = '/pdf/PROVAS_E_GABARITOS/'+prova_pdf
        elif(filtro_ano=="2018"):
            prova_pdf = '/pdf/PROVAS E GABARITOS_2018/'+prova_pdf
        elif(filtro_ano=="2017"):
            prova_pdf = '/pdf/PROVAS E GABARITOS_2017/'+prova_pdf
            
        prova = nome_prova(filtro_cor_da_prova, filtro_ano=filtro_ano)
        
        
        # Formulario de Filtro
        if prova == 'CO_PROVA_LC':
            respostas = "TX_RESPOSTAS_LC"
            gabarito = "TX_GABARITO_LC"
        elif prova == 'CO_PROVA_CN':
            respostas = "TX_RESPOSTAS_CN"
            gabarito = "TX_GABARITO_CN"
        elif prova == 'CO_PROVA_MT':
            respostas = "TX_RESPOSTAS_MT"
            gabarito = "TX_GABARITO_MT"
        elif prova == 'CO_PROVA_CH':
            respostas = "TX_RESPOSTAS_CH"
            gabarito = "TX_GABARITO_CH"

        if(filtro_sexo != 'todos'):
            Amostra = [prova, 'TP_SEXO', respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
            filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_cor=filtro_cor, 
                filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
                filtro_ano_de_conclusao=filtro_ano_de_conclusao,     
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_escola=filtro_escola, 
                filtro_nacionalidade=filtro_nacionalidade,
                filtro_ano=filtro_ano)
        else:
            Amostra = [prova, respostas, gabarito]
            Microdado_Amostra = bd_formulario_3.buscar_dataframe_no_banco(
                Amostra, 
                filtro_sexo=filtro_sexo, 
            filtro_cidade=filtro_cidade, 
                filtro_cor_da_prova=filtro_cor_da_prova, 
                filtro_deficiencia=filtro_deficiencia,
                filtro_amostra=filtro_amostra, 
                filtro_ltp_adm_escola=filtro_ltp_adm_escola,            
                filtro_ano_de_conclusao=filtro_ano_de_conclusao,     
                filtro_cor=filtro_cor, 
                filtro_estado=filtro_estado, 
                filtro_recurso=filtro_recurso,
                filtro_localizacao_da_escola=filtro_localizacao_da_escola, 
                filtro_estado_civil=filtro_estado_civil, 
                filtro_escola=filtro_escola, 
                filtro_nacionalidade=filtro_nacionalidade,
                filtro_ano=filtro_ano)
        
        if(filtro_ano=="2019"):
            CONTAGEMMicrodado_Amostra = 3702008
        elif(filtro_ano=="2018"):
            # CONTAGEMMicrodado_Amostra = 3893743
            CONTAGEMMicrodado_Amostra = 3893671
        elif(filtro_ano=="2017"):
            CONTAGEMMicrodado_Amostra = 4426755
        CONTAGEM = Microdado_Amostra[prova].count()
        
        menssagem = 'Quantidade de acertos e erros por prova:'

        Microdado_Amostra.reset_index(inplace=True)
        resposta = Microdado_Amostra[respostas]
        quantidade_de_respostas = (Microdado_Amostra[respostas].count()-1)
        gabarito = Microdado_Amostra[gabarito]

        acertos = [0]*46
        acertos_porcentagem = [0]*46
        if(quantidade_de_respostas >= 0):
            linha_do_gabarito = gabarito[quantidade_de_respostas]

        for j in range(0, 45):
            for i in range(0, quantidade_de_respostas):
                if(resposta[i] == ''):
                    resposta[i] = "............................................."
                linha_da_resposta = resposta[i]

                resposta_gabarito = linha_do_gabarito[j]
                resposta_candidato = linha_da_resposta[j]
                
                if acerto_erro == 'acertos':
                    if resposta_candidato == resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''
                else:
                    if resposta_candidato != resposta_gabarito:
                        acertos[j] = acertos[j] + 1
                        resposta_candidato = ''

            acertos_porcentagem[j+1] = (acertos[j] / quantidade_de_respostas)*100
        
        acertos_porcentagem = acertos_porcentagem[1:]
        acertos_pd = pd.DataFrame(acertos_porcentagem)
        
        # Colocando nome no DataFrame
        acertos_pd.columns = ['porcentagem_de_acertos']
        texto = acertos_pd.porcentagem_de_acertos
        
        relatorio_em_grafico = go.Figure()
        nome = "Percentual Conforme os critérios estabelecidos"
        relatorio_em_grafico.add_bar(
            y=(acertos_pd['porcentagem_de_acertos']),
            x=(acertos_pd.index).map(lambda x: f"Q{x+1}"),
            text=(acertos_pd['porcentagem_de_acertos']),
            texttemplate='%{text:.2f}%',
            textposition='auto',
            name=nome
        )
        relatorio_em_grafico.update_layout(
            xaxis=dict(
                tickvals =acertos_pd.index,
                tickmode="array",
                titlefont=dict(size=10),
            ),
            title="Percentual de " + acerto_erro + " nas questões na prova de " + prova + " no ano de " + filtro_ano + " dos inscritos que possuem " + filtro_deficiencia + " deficiência.",
            height = 500,
            margin = {'t':50, 'l':50},
            yaxis = {'domain': [0, 1]},
            xaxis2 = {'anchor': 'y2'},
            xaxis_title=("Número da da questão na prova: "+prova),
            yaxis_title="Desempenho em percentual de acertos.",
            yaxis2 = {'domain': [.6, 1], 'anchor': 'x2', 'title': 'Goals'},
            legend_title="Legenda",
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        )
        relatorio = relatorio_em_grafico.to_html()
        
        menssagem1 = 'PDF da prova de '+prova
        anotacao_mensagem = 'Q1, Q2, Q3, Q4, ..., Corresponde ao numero da questão na prova '+ prova
        anotacao = """Através deste gráfico, é possível visualizar a proporção em 
        porcentagem de quantos alunos acertaram ou erraram a questão especificada pelo 
        "Q". Dessa forma, é possível identificar em qual questão da prova deve-se 
        fazer uma análise para entender o motivo de a questão ter uma maior porcentagem 
        de alunos que erraram."""
        
        # Cria a mensagem de anotação
        informativo = '<h5 class="mb-0">Informativo:</h5>'

        # Formata a mensagem em HTML
        anotacao_mensagem = f'<div class="col-md-11 border"><div class="col-md-11 mt-2">{informativo}</div><hr class="mt-0">{anotacao}<hr class="mt-0">{anotacao_mensagem}</div>'
        
        context = {
            'form' : form,
            'menssagem':menssagem,
            'relatorio'  :relatorio,
            'anotacao_mensagem' : anotacao_mensagem,
            'menssagem1' : menssagem1,
            'prova_pdf'  :  prova_pdf,
            'form_filtro' : form_filtro,
            'quantidadeParcial' : CONTAGEM,
            'quantidadeTotal' : CONTAGEMMicrodado_Amostra,
        }

    return render(request, 'base/formulario_3/relatorio_formulario_3.html', context=context)

