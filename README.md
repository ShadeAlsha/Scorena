# ⚽ Soccer Talent AI – National Talent Identification System

An end-to-end open-source platform to **identify**, **analyze**, and **track soccer talents** across schools and public areas using **AI, computer vision**, and **coach collaboration**. This system supports video-based talent discovery, team dynamics analysis, skill extraction, and feedback loops — all stored in a unified national talent database.

---

## 📽️ Slides

👉 [Project Overview Slides](https://docs.google.com/presentation/d/1W6x9Wbt0_04RL9eieCt5hsVjvkODNwmzuZ-AVU7mc9Q/edit?usp=sharing)

---

## 🚀 Project Goals

- Analyze match videos to extract individual and team-level soccer skills.
- Create a **comprehensive national talent database**.
- Offer AI-driven insights and uncertainty detection.
- Provide feedback and experimentation suggestions to coaches.
- Track player development over time and suggest training paths.

---

## 🧱 System Architecture

- 🎥 **Video Capture**: Matches from schools/public fields are recorded.
- 🧠 **Computer Vision**: Detect players, estimate poses, recognize actions, track positions.
- 📊 **Feature Extraction**: Calculate performance metrics (speed, passes, shots, movement).
- 🗂️ **Data Storage**: Sync structured data to a scalable player database.
- 🧑‍🏫 **Coach Feedback**: Get suggestions from AI, confirmed/refined by human experts.
- 📉 **Uncertainty Detection**: Highlight unknowns (e.g., unexplored positions).
- 🖥️ **Dashboard**: Central place to explore talent profiles, videos, and analytics.

---

## 🗂️ Repository Structure

```bash
soccer-talent-ai/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .env.example
│
├── config/
│   └── config.yaml                     # Model paths, DB connections, env setup
│
├── data/
│   ├── raw/                            
│   ├── processed/                      
│   └── database/                       # SQL, Mongo, or Firebase snapshots
│
├── models/
│   ├── pose_estimation/
│   │   ├── hrnet_infer.py
│   │   └── openpose_infer.py
│   ├── action_recognition/
│   │   ├── i3d_infer.py
│   │   └── tsn_infer.py
│   ├── tracking/
│   │   ├── deep_sort.py
│   │   └── bytetrack.py
│   ├── multimodal/
│   │   └── vlm_captioning.py          # LLaVA or similar VLM to caption scenes
│   └── prediction/
│       ├── gnn_synergy.py             # Team dynamics analysis
│       ├── transformer_skills.py      # Player time-series modeling
│       └── rl_simulator.py            # Tactical simulations using RL
│
├── video_processing/
│   ├── extract_frames.py
│   ├── segment_matches.py
│   ├── player_localization.py
│   ├── annotate_video.py
│   └── compress_video.py
│
├── feature_extraction/
│   ├── extract_speed.py
│   ├── calculate_accuracy.py
│   ├── detect_skills.py
│   ├── build_player_profile.py
│   └── uncertainty_zones.py
│
├── database_management/
│   ├── player_model.py                
│   ├── db_utils.py
│   ├── sync_data.py
│   └── update_profile.py
│
├── coach_feedback/
│   ├── suggest_positions.py
│   ├── generate_reports.py
│   └── feedback_loop.py
│
├── dashboard/
│   ├── app.py
│   ├── components/
│   │   ├── PlayerStatsCard.jsx
│   │   ├── MatchVideoComponent.jsx
│   │   └── CoachFeedbackForm.jsx
│   └── api/
│       ├── routes.py
│       └── database_api.py
│
└── utils/
    ├── logger.py
    ├── visualizer.py
    └── helpers.py
```

#  Setup Guide

## Step 1: Clone and Install
```bash
git clone https://github.com/shadealsha/scorena.git
cd scorena
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 2: Environment & Config
```bash
cp .env.example .env
```

Edit config/config.yaml with:

Paths to models
Video sources
Database credentials

## Quickstart Examples

### 1. Run Pose Estimation on a New Match
```bash

python video_processing/extract_frames.py --video data/raw/match1.mp4
python models/pose_estimation/hrnet_infer.py --input data/processed/frames
```
### 2. Extract Player Metrics
```bash

python feature_extraction/extract_speed.py --pose-dir data/processed/poses
python feature_extraction/detect_skills.py
```
### 3. Update Player Profile

python database_management/update_profile.py --player-id 30182
### 4. Get Position Suggestion
```bash

python coach_feedback/suggest_positions.py --player-id 30182
```
