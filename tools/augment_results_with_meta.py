import json
from pathlib import Path

# paths
summary_path = Path("results/compare/summary.json")
train_meta_path = Path("results/DQN/train_meta.json")

# load files
with open(summary_path, "r") as f:
    summary = json.load(f)

with open(train_meta_path, "r") as f:
    dqn_meta = json.load(f)

# inject training budget info
summary["DQN_training"] = {
    "algorithm": "DQN",
    "training_steps": dqn_meta.get("total_steps", 50000),
    "original_planned_steps": 200000,
    "note": "Training steps reduced due to hardware constraints"
}

# save back
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)

print("Summary updated with DQN training metadata.")
