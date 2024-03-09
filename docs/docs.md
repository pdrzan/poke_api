# 🗂 Documentação

Aqui se encontra toda a documentação do repositório. Ele é dividido em:

- <a name="organizacao"> Organização </a>
- <a name="rodaraplicação"> Como rodar a aplicação </a>
- <a name="rodartestes"> Como rodar os testes </a>

### 📋 Organização

Esse repositório está organizado da seguinte forma:

```
├── code
│   ├── tests
│   │   ├── test_api.py
│   │   ├── test_util.py
│   ├── api.py
│   ├── util.py
├── docs
│   ├── docs.md
├── media
│   ├── docs.md
├── .gitignore
├── Dockerfile
├── README.md
└── requeriments.txt
```

#### /code

Aqui está o código da aplicação como tabém seus testes na sub pasta _/tests_

#### /docs

Aqui está a documentação da aplicação

#### /media

Aqui está os arquivos de mídia da aplicação

### Outros arquivos

Os outros arquivos se tratam de configurações do git (.gitignore), configurações do docker (Dockerfile), readme do repositório (README.md) e conjunto de dependências da aplicação (requirements.txt)

### ⚙️ Como rodar a aplicação

Primeiramente vá ao diretório raiz da aplicação

A aplicação pode ser rodada utilizando o Docker ou não. Se você quiser rodar utilizando o Docker siga os próximos passos, caso contrário vá para [Sem docker](#semdocker).

#### Utilizando Docker

Primeiro é preciso criar a imagem do Docker:

```bash
docker build -t poke_api .
```

Agora vamos criar um container:

```bash
docker run --rm -it -p 8000:8000 poke_api:latest
```

Após isso vá para a pasta _code/_

```bash
cd code/
```

Agora podemos rodar a aplicação com o comando:

```bash
uvicorn api:app --reload --host 0.0.0.0
```

Pronto, sua aplicação está rodando no IP _127.0.0.1/api/teams_!

#### <a name=semdocker> Não utilizando o docker </a>

Em primeiro lugar garanta que você possui o python e o pip instalados. Caso você não tenha-os voce pode instalá-los nos respectivos links: [python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/)

Após isso, temos que instalar as dependências da aplicação. Para isso, execute o comando:

```bash
pip install --no-cache-dir -r requirements.txt
```

Agora vamos para a pasta _code_:

```bash
cd code/
```

Por fim, para rodar nossa aplicação dê o comando:

```bash
uvicorn api:app --reload
```

Pronto, sua aplicação está rodando no IP _127.0.0.1/api/teams_!

### 📝 Como rodar os testes

OBS 1: Para que os testes sejam executados corretamente é preciso que a aplicação esteja rodando no IP _127.0.0.1:8000/api/teams/_ e que todas as dependências estejam instaladas

OBS 2: Os testes assumem que você não tenha criado nenhum time anteriormente

Vá para a pasta _code/_:

```bash
cd code/
```

Agora basta executar esse comando:

```bash
python3 -m pytest
```

Pronto, os testes foram executados!
