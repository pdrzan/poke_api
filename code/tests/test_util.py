from util import *


def test_clear_teams():
    global teams
    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "pikachu", "charmander"],
    }
    create_team(team_information)
    clear_teams()
    assert teams == {}

    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "notpoke"],
    }
    create_team(team_information)
    clear_teams()
    assert teams == {}


def test_get_new_id():
    error_msg = "Error: Data must be an object"

    assert error_msg == get_new_id("string")
    assert error_msg == get_new_id(10)
    assert error_msg == get_new_id(10.0)
    assert error_msg == get_new_id((1, 1))
    assert error_msg == get_new_id([1, 1])
    assert error_msg == get_new_id({1, 2, 3})

    assert error_msg != get_new_id({"a": "b"})
    assert error_msg != get_new_id({})


def test_get_all_teams():
    clear_teams()

    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "pikachu", "charmander"],
    }
    msg, id_team = create_team(team_information).values()
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
    assert get_all_teams() == expected_teams

    team_information = {
        "user": "joao",
        "team": ["blastoise", "psyduck", "blastoise"],
    }
    msg, id_team = create_team(team_information).values()
    expected_teams[id_team] = {
        "owner": "joao",
        "pokemons": [
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
            {"id": 54, "name": "psyduck", "weight": 196, "height": 8},
        ],
    }
    assert get_all_teams() == expected_teams

    team_information = {
        "user": "pedro",
        "team": ["ditto", "charmander", "blastoise"],
    }
    msg, id_team = create_team(team_information).values()
    expected_teams[id_team] = {
        "owner": "pedro",
        "pokemons": [
            {"id": 4, "name": "charmander", "weight": 85, "height": 6},
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
            {"id": 132, "name": "ditto", "weight": 40, "height": 3},
        ],
    }
    assert get_all_teams() == expected_teams


def test_get_user_teams():
    clear_teams()
    error_msg = "Error: User must be a string"

    assert error_msg == get_user_teams(10)
    assert error_msg == get_user_teams(10.5)
    assert error_msg == get_user_teams({"a": "b"})
    assert error_msg == get_user_teams((1, 1))
    assert error_msg == get_user_teams({1, 2, 3})
    assert error_msg == get_user_teams([1, 2, 3])

    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "pikachu", "charmander"],
    }
    msg, id_team = create_team(team_information).values()
    expected_team = {}
    expected_team["pdrzan"] = {
        "owner": "pdrzan",
        "pokemons": [
            {"id": 4, "name": "charmander", "weight": 85, "height": 6},
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
            {"id": 25, "name": "pikachu", "weight": 60, "height": 4},
        ],
    }
    assert get_user_teams("pdrzan") == expected_team["pdrzan"]
    assert get_user_teams("joao") == {}
    assert get_user_teams("pedro") == {}

    team_information = {
        "user": "joao",
        "team": ["blastoise", "psyduck", "blastoise"],
    }
    msg, id_team = create_team(team_information).values()
    expected_team["joao"] = {
        "owner": "joao",
        "pokemons": [
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
            {"id": 54, "name": "psyduck", "weight": 196, "height": 8},
        ],
    }
    assert get_user_teams("pdrzan") == expected_team["pdrzan"]
    assert get_user_teams("joao") == expected_team["joao"]
    assert get_user_teams("pedro") == {}

    team_information = {
        "user": "pedro",
        "team": ["ditto", "charmander", "blastoise"],
    }
    msg, id_team = create_team(team_information).values()
    expected_team["pedro"] = {
        "owner": "pedro",
        "pokemons": [
            {"id": 4, "name": "charmander", "weight": 85, "height": 6},
            {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
            {"id": 132, "name": "ditto", "weight": 40, "height": 3},
        ],
    }
    assert get_user_teams("pdrzan") == expected_team["pdrzan"]
    assert get_user_teams("joao") == expected_team["joao"]
    assert get_user_teams("pedro") == expected_team["pedro"]


def test_create_team():
    assert create_team(10) == "Error: team_information must be an dict"
    assert create_team(10.0) == "Error: team_information must be an dict"
    assert create_team("String") == "Error: team_information must be an dict"
    assert create_team((1, 1)) == "Error: team_information must be an dict"
    assert create_team({1, 2, 3}) == "Error: team_information must be an dict"
    assert create_team([1, 2, 3]) == "Error: team_information must be an dict"

    assert create_team({}) == "Error: team_information must have a user attribute"
    assert (
        create_team({"user": "pdrzan"})
        == "Error: team_information must have a team attribute"
    )
    assert (
        create_team({"team": ["pikachu", "ditto"]})
        == "Error: team_information must have a user attribute"
    )

    assert (
        create_team({"user": 10, "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": 10.0, "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": [], "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": {}, "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": {1, 2}, "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": (1, 2), "team": ["pikachu", "ditto"]})
        == "Error: team_information['user'] must be a string"
    )
    assert (
        create_team({"user": "pdrzan", "team": (1, 2, 3)})
        == "Error: team_information['team'] must be a list"
    )

    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", 10, "blastoise"]})
        == "Error: All pokemons must be a string. The 10 isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", 10.0, "blastoise"]})
        == "Error: All pokemons must be a string. The 10.0 isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", [], "blastoise"]})
        == "Error: All pokemons must be a string. The [] isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", {}, "blastoise"]})
        == "Error: All pokemons must be a string. The {} isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", {1, 2}, "blastoise"]})
        == "Error: All pokemons must be a string. The {1, 2} isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", (1, 2), "blastoise"]})
        == "Error: All pokemons must be a string. The (1, 2) isn't"
    )
    assert (
        create_team({"user": "pdrzan", "team": ["pikachu", "blastoise", "naopoke"]})
        == "Error: naopoke is not a pokemon name"
    )
    assert (
        create_team({"user": "pdrzan", "team": []})
        == "Error: team_information['team'] can not be empty"
    )

    clear_teams()
    team_information = {
        "user": "pdrzan",
        "team": ["blastoise", "pikachu", "charmander", "ditto"],
    }
    msg, id_team = create_team(team_information).values()
    expected_teams = {
        id_team: {
            "owner": "pdrzan",
            "pokemons": [
                {"id": 4, "name": "charmander", "weight": 85, "height": 6},
                {"id": 9, "name": "blastoise", "weight": 855, "height": 16},
                {"id": 25, "name": "pikachu", "weight": 60, "height": 4},
                {"id": 132, "name": "ditto", "weight": 40, "height": 3},
            ],
        }
    }
    assert teams == expected_teams
    team_information = {
        "user": "pedro",
        "team": ["pikachu", "ditto"],
    }
    msg, id_team = create_team(team_information).values()
    expected_teams[id_team] = {
        "owner": "pedro",
        "pokemons": [
            {"id": 25, "name": "pikachu", "weight": 60, "height": 4},
            {"id": 132, "name": "ditto", "weight": 40, "height": 3},
        ],
    }
    assert teams == expected_teams
