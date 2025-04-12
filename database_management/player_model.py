PLAYER_DB = {}

def create_player(player_id):
    PLAYER_DB[player_id] = {
        "id": player_id,
        "metrics": {},
        "recommendations": []
    }

def update_player_metric(player_id, key, value):
    PLAYER_DB[player_id]["metrics"][key] = value

def get_player(player_id):
    return PLAYER_DB.get(player_id, None)
