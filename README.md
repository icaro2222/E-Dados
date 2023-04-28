# E-Dados: Plataforma de Análise de Dados do ENEM

O E-Dados (Enem Dados) é uma plataforma de análise de dados do ENEM que realiza todo o processo de coleta, manipulação, tratamento, análise e geração de resultados, entregando ao usuário tabelas e gráficos simples e intuitivos com fácil compreensão.

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

Para inserir 5513747 registros no banco de 2018, siga as instruções contidas no arquivo [conf banco.md](conf banco.md)
.

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
