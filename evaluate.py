#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.metrics import accuracy_score

# Load true labels 
y_true = pd.read_csv("data/hidden_labels.csv")

def evaluate_submission(submission_path, name):
    # Load submission
    submission = pd.read_csv(submission_path)

    # Extract predictions
    y_pred = submission["income"]

    # Calculate accuracy
    score = accuracy_score(y_true, y_pred)

    print(f"Score for {name}: {score}")

    # Load leaderboard
    leaderboard = pd.read_csv("leaderboard.csv")

    # Add new score
    new_entry = pd.DataFrame({
        "name": [name],
        "score": [score]
    })

    leaderboard = pd.concat([leaderboard, new_entry], ignore_index=True)

    # Sort leaderboard
    leaderboard = leaderboard.sort_values(by="score", ascending=False)

    # Save updated leaderboard
    leaderboard.to_csv("leaderboard.csv", index=False)

    print("\nUpdated Leaderboard:")
    print(leaderboard)

# Example usage
if __name__ == "__main__":
    evaluate_submission("submission.csv", "your_name")

