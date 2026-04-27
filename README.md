# 🧠 Adult Income Prediction ML Competition

Predict whether an individual earns **more than 50K or less than/equal to 50K per year** using demographic and employment data.

---

## 📌 Problem Statement

Given a dataset containing features like age, education, occupation, and working hours, your task is to build a machine learning model that predicts:

👉 **Income: `>50K` or `<=50K`**

---

## 📊 Dataset Description

The dataset includes the following features:

- **age** – Age of the individual  
- **workclass** – Type of employment  
- **education** – Education level  
- **marital_status** – Marital status  
- **occupation** – Job type  
- **relationship** – Family relationship  
- **race** – Ethnicity  
- **sex** – Gender  
- **hours_per_week** – Weekly working hours  
- **native_country** – Country of origin  
- **income** – Target variable (`>50K`, `<=50K`)  

---

## 📁 Files Provided
- data/
- ├── train.csv # Training data (features + target)
- ├── test.csv # Test data (features only)
- ├── sample_submission.csv # Submission format


---

## 🎯 Objective

Build a classification model that accurately predicts income category on unseen data.

---

## 📏 Evaluation Metric

Submissions are evaluated using:

**Accuracy Score**
Accuracy = (Correct Predictions) / (Total Predictions)


---

## 📤 Submission Format

Your submission must:

- Be a CSV file  
- Contain exactly 2 columns:
id,income
0,<=50K
1,>50K


- Match the format of `sample_submission.csv`  
- Contain no missing values  

---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/NandiniP78/Adult-Census-Income.git

cd Adult-Census-Income


---

### 2. Install dependencies
pip install -r requirements.txt


---

### 3. Run baseline model

Open the notebook:
notebooks/Adult_Census_Income.ipynb


---

## 🧪 Baseline Model

A baseline model is provided using:

- Logistic Regression  
- Basic preprocessing  
- One-hot encoding  

Participants are encouraged to improve performance using:
- Feature engineering  
- Hyperparameter tuning  
- Advanced models (Random Forest, XGBoost, etc.)

## 🤖 Models you can try
🔹 Linear Models
    Logistic Regression
🔹 Distance-Based
    KNN
🔹 Tree-Based
    Decision Tree
    Random Forest
🔹 Boosting Models
    XGBoost
    LightGBM
🔹 Others
    Naive Bayes
    SVM

## 🏆 Leaderboard

See latest scores in:

📄 `leaderboard.csv`


