from api import *
import requests, json


def test_teams():
    response = requests.get("http://127.0.0.1:8000/api/teams/")
    assert json.loads(response.content) == {}

    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "pikachu", "charmander"],
    }
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg, id_team = json.loads(response.content).values()
    response = requests.get("http://127.0.0.1:8000/api/teams/")
    expected_teams = {
        id_team: {
            "owner": "pdrzan",
            "pokemons": [
                {"id": 4, "name": "charmander", "weight": 85, "height": 6},
                {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
                {"id": 25, "name": "pikachu", "weight": 60, "height": 4},
            ],
        }
    }
    assert json.loads(response.content) == expected_teams


def test_teams_user():
    response = requests.get("http://127.0.0.1:8000/api/teams/pedro")
    assert json.loads(response.content) == {}

    team_information = {
        "user": "pedro",
        "team": ["charmander", "blastoise"],
    }
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg, id_team = json.loads(response.content).values()

    expected_teams = {
        "owner": "pedro",
        "pokemons": [
            {"id": 4, "name": "charmander", "weight": 85, "height": 6},
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
        ],
    }

    response = requests.get("http://127.0.0.1:8000/api/teams/pedro")
    assert json.loads(response.content) == expected_teams


def test_create_team():
    team_information = {"team": [], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: team_information['team'] can not be empty"

    team_information = {"team": ["pikachu", 10, "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: All pokemons must be a string. The 10 isn't"

    team_information = {"team": ["pikachu", 10.0, "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: All pokemons must be a string. The 10.0 isn't"

    team_information = {"team": ["pikachu", {}, "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: All pokemons must be a string. The {} isn't"

    team_information = {"team": ["pikachu", [], "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: All pokemons must be a string. The [] isn't"

    team_information = {"team": ["pikachu", (1, 2), "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: All pokemons must be a string. The [1, 2] isn't"

    team_information = {"team": ["pikachu", "notpoke", "charmander"], "user": "pdrzan"}
    response = requests.post("http://127.0.0.1:8000/api/teams/", json=team_information)
    msg = json.loads(response.content)
    assert msg == "Error: notpoke is not a pokemon name"
