from database_management.player_model import get_player

def suggest_position(player_id):
    player = get_player(player_id)
    speed = player["metrics"].get("avg_speed", 0)
    if speed > 3:
        pos = "Winger or Fullback"
    elif speed > 2:
        pos = "Midfielder"
    else:
        pos = "Defender or Goalkeeper"
    player["recommendations"].append(f"Suggested position: {pos}")
    print(f"[Coach Suggestion] Player {player_id} -> {pos}")

if __name__ == '__main__':
    suggest_position("30182")
