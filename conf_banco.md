Você pode seguir os seguintes passos para instalar o PostgreSQL no Ubuntu:

1. Abra o terminal no seu Ubuntu.

2. Atualize a lista de pacotes do sistema com o comando abaixo:
   ```
   sudo apt-get update
   ```

3. Instale o pacote do PostgreSQL com o comando abaixo:
   ```
   sudo apt-get install postgresql postgresql-contrib
   ```

4. Verifique se o serviço do PostgreSQL foi iniciado automaticamente após a instalação com o comando abaixo:
   ```
   systemctl status postgresql.service
   ```

5. Caso o serviço não tenha sido iniciado, inicie-o manualmente com o comando abaixo:
   ```
   sudo systemctl start postgresql.service
   ```

6. Defina uma senha para o usuário "postgres" que é criado automaticamente durante a instalação do PostgreSQL com o comando abaixo:
   ```
   sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'nova_senha';"
   ```
   Substitua 'nova_senha' pela senha que deseja definir.

7. Verifique a instalação do PostgreSQL com o comando abaixo:
   ```
   psql -U postgres -h localhost
   ```
   Será solicitada a senha definida no passo 6. Após digitar a senha, você deve entrar no console interativo do PostgreSQL.

Agora você tem o PostgreSQL instalado em seu sistema Ubuntu.


Para criar um banco de dados no Postgres, siga os passos abaixo:

1. Certifique-se de que o servidor do Postgres esteja em execução. Você pode verificar isso digitando o seguinte comando no terminal:

```
sudo service postgresql status
```

Se o servidor não estiver em execução, você pode iniciar o serviço com o seguinte comando:

```
sudo service postgresql start
```

2. Conecte-se ao servidor do Postgres como usuário superusuário (postgres) usando o seguinte comando:

```
sudo -u postgres psql
```

3. Agora que você está conectado ao servidor do Postgres, pode criar um novo banco de dados usando o seguinte comando:

```
CREATE DATABASE nome_do_banco;
```

Substitua "nome_do_banco" pelo nome que você deseja dar ao banco de dados.

4. Para verificar se o banco de dados foi criado corretamente, você pode listar todos os bancos de dados existentes usando o seguinte comando:

```
\l
```

O novo banco de dados que você criou deve aparecer na lista.

5. Para sair do console do PostgreSQL, digite o seguinte comando:

```
\q
```

Pronto! Agora você criou um novo banco de dados no PostgreSQL.