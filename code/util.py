import requests
import json
import uuid

teams = {}


def clear_teams():
    """
    Cleans the teams object

    Parameters:
        None

    Returns:
        None
    """
    global teams
    teams.clear()
    return


def get_new_id(data):
    """
    Creates a new id to an object in data

    Parameters:
        data(dict): A data object

    Returns
        id(str): The new id created
    """
    try:
        assert isinstance(data, dict)
    except AssertionError:
        return "Error: Data must be an object"
    id = uuid.uuid4()
    while id in data:
        id = uuid.uuid4()
    return str(id)


def get_all_teams():
    """
    Returns all the teams

    Parameters:
        None

    Returns:
        teams(dict): Object with all the teams
    """
    return teams


def get_user_teams(user):
    """
    Returns a team registered by a user

    Parameters:
        user(str): Name of the user

    Returns:
        team(dict): A team registered by the user in the format:
            {
                "owner": <user>(str),
                "pokemons": <pokemon_list>(list)
            }
    """
    try:
        assert isinstance(user, str)
    except AssertionError:
        return "Error: User must be a string"

    for id_team, team in teams.items():
        if team["owner"] == user:
            return team
    return {}


def create_team(team_information):
    """
    Creates a team

    Parameters:
        team_information(dict): Information about the team in the format
            {
                "user": <name_user>(str),
                "teams" <pokemon_list>(list)
            }

    Returns:
        result(dict): A object with the resulted operation in the format:
            {
                "msg": <message>(str),
                "id_team": <id_of_the_team>(str)
            }
    """
    global teams
    try:
        assert isinstance(team_information, dict)
    except AssertionError:
        return "Error: team_information must be an dict"

    try:
        assert "user" in team_information
    except AssertionError:
        return "Error: team_information must have a user attribute"

    try:
        assert isinstance(team_information["user"], str)
    except AssertionError:
        return "Error: team_information['user'] must be a string"

    try:
        assert "team" in team_information
    except AssertionError:
        return "Error: team_information must have a team attribute"

    try:
        assert isinstance(team_information["team"], list)
    except AssertionError:
        return "Error: team_information['team'] must be a list"

    try:
        assert len(team_information["team"]) > 0
    except AssertionError:
        return "Error: team_information['team'] can not be empty"

    for i in range(len(team_information["team"])):
        pokemon = team_information["team"][i]
        try:
            assert isinstance(pokemon, str)
        except AssertionError:
            return f"Error: All pokemons must be a string. The {pokemon} isn't"

    pokemons = []
    for pokemon in set(team_information["team"]):
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        if request.status_code != 200:
            return f"Error: {pokemon} is not a pokemon name"

        content = json.loads(request.content)
        new_pokemon = {
            "id": content["id"],
            "name": pokemon,
            "weight": content["weight"],
            "height": content["height"],
        }
        pokemons.append(new_pokemon)

    if len(set(team_information["team"])) != len(team_information["team"]):
        print("Warning: You repeated a pokemon name")
    pokemons.sort(key=lambda x: x["id"])

    id = get_new_id(teams)
    teams[id] = {"owner": team_information["user"], "pokemons": pokemons}

    result = {"msg": "Success! The team was created", "id_team": id}
    return result
