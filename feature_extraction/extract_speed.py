import json
import math

def compute_speed(pose_data):
    speeds = []
    frames = list(pose_data.keys())
    for i in range(1, len(frames)):
        p1 = pose_data[frames[i-1]]['keypoints'][0]
        p2 = pose_data[frames[i]]['keypoints'][0]
        dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        speed = dist * 0.04
        speeds.append(speed)
    return sum(speeds) / len(speeds)

def extract_speed(pose_path):
    with open(pose_path) as f:
        pose_data = json.load(f)
    avg_speed = compute_speed(pose_data)
    print(f"Average speed: {avg_speed:.2f} m/s")
    return avg_speed

if __name__ == '__main__':
    extract_speed("data/processed/poses.json")
