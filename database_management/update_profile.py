from player_model import create_player, update_player_metric, get_player
from feature_extraction.extract_speed import extract_speed

def update_profile(player_id):
    create_player(player_id)
    speed = extract_speed("data/processed/poses.json")
    update_player_metric(player_id, "avg_speed", speed)
    print(f"Updated profile for player {player_id}:\n", get_player(player_id))

if __name__ == '__main__':
    update_profile("30182")
