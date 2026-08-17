# Chronic Disease Progression Predictor

> Explainable AI (XAI) for Healthcare Prediction using Scikit-learn, SHAP, LIME, and CDC Chronic Disease Indicators.

[Repository](https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor)

---

## Overview

**Chronic Disease Progression Predictor** is a machine learning pipeline and explainability system built to forecast chronic disease progression risk while providing transparent feature attribution for clinical decision support.

---

## Pipeline & Explainability Architecture

```
  DATA
   ↓
PREPROCESS
   ↓
FEATURE ENGINEERING
   ↓
MODEL TRAINING
   ↓
EVALUATION
   ↓
SHAP + LIME
   ↓
EXPLANATION (Global & Local)
```

---

## What Explainable AI (XAI) Means in Healthcare

In medical machine learning, predictive accuracy alone is insufficient. Black-box algorithms (e.g., ensemble trees or deep networks) can identify risk patterns but fail to explain *why* a specific prediction was produced.

**Explainable AI** provides interpretable explanations of model behavior:
- **Why Explain the Model?**: Clinicians require actionable insights into risk factors to validate predictions against medical knowledge and avoid biased predictions.
- **Global Explanations**: Identifies overall feature importance across the entire patient population using SHAP Summary Plots.
- **Local Explanations**: Deconstructs individual patient predictions using LIME surrogate models and SHAP Force Plots, highlighting specific patient measurements driving elevated risk.

---

## Dataset & Feature Engineering

* **Dataset**: CDC Chronic Disease Indicators (CDI) public healthcare dataset.
* **Features**: Demographic indicators, behavioral risk factors, historical disease prevalence metrics, and clinical measurement rates.
* **Preprocessing**: Imputation of missing indicators, standard scaling, and categorical encoding.

---

## Model Evaluation & Benchmarks

Model performance was evaluated across multiple algorithms using stratified cross-validation on CDC risk metrics:

| Model | Accuracy | Precision | Recall | F1-Score | Status |
|:---|:---:|:---:|:---:|:---:|:---|
| **Logistic Regression** (Baseline) | Evaluated | Evaluated | Evaluated | Evaluated | Baseline |
| **Random Forest Classifier** | Evaluated | Evaluated | Evaluated | Evaluated | Primary Model |
| **XGBoost Classifier** | Evaluated | Evaluated | Evaluated | Evaluated | Primary Model |

---

## Explainability Output Examples

1. **SHAP Global Feature Attribution**: Ranks top population-level risk indicators (e.g., age-adjusted prevalence rates, physical inactivity metrics).
2. **LIME Local Case Explanations**: Generates patient-specific risk factor breakdowns directly rendered in the Rich CLI terminal.

---

## Project Structure

```
Chronic-Disease-Progression-Predictor/
├── README.md
├── requirements.txt
├── main.py                # Rich CLI Interface & Prediction Pipeline
├── src/
│   ├── data_loader.py     # CDC CDI Data Preprocessing
│   ├── model_trainer.py   # Scikit-learn Model Training & Tuning
│   └── explainability.py  # SHAP & LIME Explainer Engine
└── data/                  # Cleaned Dataset Files
```

---

## Installation & Usage

```bash
git clone https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor.git
cd Chronic-Disease-Progression-Predictor
pip install -r requirements.txt

# Launch Rich CLI Interactive Explainer
python main.py
```

---

## Limitations & Non-Clinical Disclaimer

- **Limitations**: The model is trained on aggregated regional public health statistics rather than longitudinal individual electronic health records (EHR).
- **Disclaimer**: This software is an academic engineering project intended solely for research and educational purposes. It is not a clinical diagnostic tool.
