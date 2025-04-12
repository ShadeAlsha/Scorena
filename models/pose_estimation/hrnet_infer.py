import os
import json

def dummy_pose_estimation(frame_dir, output_path):
    result = {
        "frame_0001.jpg": {"keypoints": [(100, 200), (105, 210), (110, 215)]},
        "frame_0002.jpg": {"keypoints": [(102, 202), (106, 212), (111, 216)]},
    }
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f)
    print(f"Pose estimation results saved to {output_path}")

if __name__ == "__main__":
    dummy_pose_estimation("data/processed/frames", "data/processed/poses.json")
