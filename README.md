<p align="center">
    <img src="./media/pokeapi.png" alt="PokeAPI image">
</p>

# Desafio Triágil

Nesse repositório se encontra uma solução do [desafio Triágil](https://github.com/triagilbr/desafio-triagil). O desafio consiste em criar uma api utilzando a [pokeapi.co](https://pokeapi.co/) que tenha as seguintes rotas:

- GET /api/teams - Deverá retornar todos os times registrados em um JSON [nesse fomato](#formatoteams)
- GET /api/teams/{user} - Busca um time registrado por usuário e retorna um JSON [nesse formato](#formatouser)
- POST /api/teams - Rota para criação de um time, que recebe um JSON [nesse formato](#formatocreateinput) e retorna um JSON [nesse formato](#formatocreateoutput)

### 🗂 Documentação

A documentação pode ser encontrada nesse [link](/docs/docs.md) ou no arquivo _docs.md_ dentro da pasta _docs_. Lá se encontram informações sobre como rodar a aplicação, organização do repositório e outras informações.

### 📐 Formatos

<a name="formatouser">Output GET /api/teams</a>:

```json
{
  "1": {
    "owner": "sleao",
    "pokemons": [
      {
        "id": 9,
        "name": "blastoise",
        "weight": 855,
        "height": 16
      },
      {
        "id": 25,
        "name": "pikachu",
        "weight": 60,
        "height": 4
      }
    ]
  },
  "2": {
    "owner": "sleao",
    "pokemons": [
      {
        "id": 9,
        "name": "blastoise",
        "weight": 855,
        "height": 16
      },
      {
        "id": 25,
        "name": "pikachu",
        "weight": 60,
        "height": 4
      },
      {
        "id": 3,
        "name": "venusaur",
        "weight": 1000,
        "height": 20
      },
      {
        "id": 6,
        "name": "charizard",
        "weight": 905,
        "height": 17
      },
      {
        "id": 131,
        "name": "lapras",
        "weight": 2200,
        "height": 25
      },
      {
        "id": 54,
        "name": "psyduck",
        "weight": 196,
        "height": 8
      }
    ]
  }
}
```

<a name="formatouser">Output GET /api/teams/{user}</a>:

```json
{
  "owner": "sleao",
  "pokemons": [
    {
      "id": 9,
      "name": "blastoise",
      "weight": 855,
      "height": 16
    },
    {
      "id": 25,
      "name": "pikachu",
      "weight": 60,
      "height": 4
    }
  ]
}
```

<a name="formatocreateinput">Input POST /api/teams</a>:

```json
{
  "user": "sleao",
  "team": [
    "blastoise",
    "pikachu",
    "charizard",
    "venusaur",
    "lapras",
    "dragonite"
  ]
}
```

<a name="formatocreateoutput">Output POST /api/teams</a>:

```json
{
  "msg": "Success! The team was created",
  "id_team": "10"
}
```
