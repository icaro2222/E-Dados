# E-Dados: Plataforma de Análise de Dados do ENEM

O E-Dados (Enem Dados) é uma plataforma de análise de dados do ENEM que realiza todo o processo de coleta, manipulação, tratamento, análise e geração de resultados, entregando ao usuário tabelas e gráficos simples e intuitivos com fácil compreensão.

### Funcionalidades da Plataforma:

1. Dados Brutos:
   - Realizar filtros em um grande volume de dados, possibilitando a análise específica de milhões de registros.
   - Disponibilizar o download dos dados em formato CSV, com opção de selecionar colunas específicas.
   - Apresentar um quadro resumido do CSV completo, fornecendo uma visão geral dos principais dados e métricas.
   - Visualizar o quadro de distribuição com a quantidade de alunos em cada resposta do questionário socioeconômico.

2. Gráficos:
   - Realizar análise exploratória que correlaciona os microdados socioeconômicos e demográficos do ENEM.
   - Especificar filtros para análises refinadas e segmentadas nos dados disponíveis.
   - Gerar um relatório final abrangente com estatísticas, gráficos e insights relevantes.

3. Desempenho no Exame:
   - Identificar padrões e correlações entre o desempenho e fatores socioeconômicos.
   - Exibir a distribuição dos alunos em cada resposta da questão socioeconômica e analisar os resultados.
   - Aplicar filtros para segmentar os resultados por critérios específicos.
   - Contrastar as notas mínimas, médias e máximas entre os grupos filtrados.
   - Gerar um relatório final com estatísticas, gráficos e insights relevantes.

4. Quantidade de acertos e erros por prova:
   - Filtrar os dados dos microdados do ENEM por critérios relevantes.
   - Gerar gráfico de barras com a porcentagem de alunos que acertaram ou erraram cada questão da prova.

5. Quantidade de acertos e erros por questão:
   - Visualizar resultados entre diferentes grupos de alunos.
   - Contrastar subgrupos específicos de alunos para diferentes provas e questões selecionadas.
   - Comparar múltiplas provas e compreender as disparidades nos resultados.

6. Mapa Temático:
   - Identificar disparidades regionais.
   - Analisar correlações entre notas e localização.
   - Avaliar a distribuição de alunos por estado.
   - Compreender a relação entre a idade dos alunos e a localização.

Sobre a Plataforma:
- Desenvolvedor: Ícaro Dias (e-mail: icarodias2222@gmail.com)
- Orientador: Prof. Dr. Woquiton Lima Fernandes (e-mail: woquiton@gmail.com)
- Coorientadora: Prof. Dra. Daniele Trindade (e-mail: daniele.trindade@ifbaiano.edu.br)
- Instituição: Instituto Federal Baiano, campus Guanambi

Informações Adicionais:
- A plataforma é uma solução para análise de microdados socioeconômicos do ENEM.
- Utiliza dados dos anos de 2017, 2018 e 2019.
- Foram considerados apenas os dados dos inscritos presentes em todas as provas.
- Possui recursos avançados de filtragem, visualização e exportação de dados.
- Requer login com usuário e senha cadastrados.
- Permite gerenciamento de permissões de acesso.
- Oferece recursos de exportação e download de dados no formato CSV.

## Instalação

Antes de iniciar a instalação, certifique-se de que possui o Git e o Python3 instalados em sua máquina.

1. Atualize o sistema: `sudo apt-get update`
2. Atualize os pacotes instalados: `sudo apt-get upgrade`
3. Instale o Git: `sudo apt-get install git`
4. Clone o repositório: `git clone https://github.com/icaro2222/E-Dados.git`
5. Instale o pip3: `sudo apt-get install python3-pip`
6. Instale o virtualenv: `sudo apt-get install virtualenv` ou `pip3 install virtualenv`
7. Verifique a versão do virtualenv: `virtualenv --version`
8. Crie um ambiente virtual: `virtualenv venv -p python3`
9. Ative o ambiente virtual: `source venv/bin/activate`
10. Instale as dependências: `pip3 install -r requirements.txt`

## Migrações do banco de dados

Para migrar as tabelas do banco de dados, execute o seguinte comando:

```
python3 manage.py migrate
```

## Configuração do firewall

1. Atualize o sistema: `sudo apt-get update`
2. Instale o firewall: `sudo apt-get install ufw`
3. Permita a porta 8000: `sudo ufw allow 8000/tcp`
4. Ative o firewall: `sudo ufw enable`
5. Verifique o status do firewall: `sudo ufw status`

## Instalação e configuração do PostgreSQL

Para inserir 5513747 registros no banco de 2018, siga as instruções contidas no arquivo [conf_banco.md](conf_banco.md)

## Instruções para executar a aplicação

1. Abra o VS Code
2. Clone o repositório: `git clone https://github.com/icaro2222/E-Dados.git` no terminal
3. Abra a pasta criada com o VS Code
4. Crie um ambiente virtual:
```
sudo apt-get install python3-pip
pip3 install virtualenv
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```
5. Instale o Django: `pip install django==3.2.8`
6. Execute o servidor: `python manage.py runserver 0.0.0.0:8000`
7. Abra o seu browser e acesse o endereço `<seu endereço IP>:8000` para visualizar a aplicação.

A imagem a seguir mostra a aparência da aplicação:

![Captura de tela de 2023-03-28 14-50-35](https://user-images.githubusercontent.com/71037296/228325365-a3def359-e01a-4c9d-83f1-3877616fd55b.png)

## Tecnologias

- Python
- SQL
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Ferramentas

- Google Colab
- Github
- Git

## Métodos

- Pré-processamento de dados
- Limpeza de dados
- Análise exploratória de dados
- Visualização de dados
- Modelagem de dados
