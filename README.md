# 🏥 Chronic Disease Progression Predictor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/SanyogSingh07/Chronic-Disease-Progression-Predictor/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://GitHub.com/SanyogSingh07/Chronic-Disease-Progression-Predictor/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/SanyogSingh07/Chronic-Disease-Progression-Predictor?style=social)](https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor/stargazers)

A professional Machine Learning pipeline for predicting the progression rate of chronic diseases using the **U.S. Chronic Disease Indicators (CDI)** dataset. This tool provides a high-performance command-line interface (CLI) to train models and perform inference on specific disease types with real-time feedback.

---

## 📊 Project Workflow

The following diagram illustrates the end-to-end data processing and machine learning pipeline:

```mermaid
graph TD
    A[Raw CDI Dataset] --> B{Preprocessing}
    B --> C[Handle Mixed Types]
    B --> D[Detect Key Columns]
    C --> E[Feature Selection]
    D --> E
    E --> F[Scaling & Normalization]
    F --> G[Model Training]
    G --> H[Linear Regression]
    G --> I[Random Forest Regressor]
    H --> J[Metric Evaluation]
    I --> J
    J --> K{Selection}
    K --> |Best Score| L[Serialized Model Deployment]
```

---

## 🛠️ System Architecture & Flow

This flowchart describes the interactive logic of the CLI application:

```mermaid
flowchart LR
    Start([Start app.py]) --> Menu{Interactive Menu}
    Menu -->|Choice 1| Train[Train Models]
    Menu -->|Choice 2| Predict[Disease Inference]
    
    subgraph Training
    Train --> Load[Load CSV]
    Load --> Pre[Preprocess & Scale]
    Pre --> Fit[Train Regressors]
    Fit --> Save[Save Best .pkl]
    end
    
    subgraph Inference
    Predict --> Input[User Input: Disease Name]
    Input --> Filter[Filter Dataset by Disease]
    Filter --> Scale[Apply Saved Scaler]
    Scale --> Run[Run Prediction]
    end
    
    Save --> End([Display Results & Exit])
    Run --> End
```

---

## 🚀 Key Features

- **Professional Terminal UI**: Uses `rich` for elegant panels, animated status indicators, and color-coded results.
- **Intelligent Preprocessing**: Automatic identification of patient IDs, temporal features, and target variables.
- **Comparative Modeling**: Benchmarks multiple regression algorithms (Random Forest, Linear Regression) to ensure maximum accuracy.
- **Scalable Inference**: Modular design allows for easy integration of new models or additional healthcare indicators.
- **Resource Optimized**: Efficient data handling using `pandas` and `scikit-learn` with memory-safe loading.

## 🔬 Technical Details

### Data Preprocessing
- **Mixed Type Handling**: Configured to process large-scale CSVs without dtype warnings.
- **Normalization**: Utilizes `MinMaxScaler` for uniform feature representation.
- **Sequence Engineering**: (Optional) Framework support for temporal sequence generation for longitudinal studies.

### Algorithms
- **Random Forest Regressor**: Handles non-linear relationships and feature importance.
- **Linear Regression**: Baseline model for variance analysis.
- **Serialization**: Models and scalers are persisted using `joblib` for zero-latency inference.

## 📁 Repository Tags
`machine-learning` `python` `healthcare-ai` `chronic-disease` `data-science` `scikit-learn` `predictive-analytics` `cli-dashboard`

---

## ⚙️ Installation & Usage

### Setup
```bash
git clone https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor.git
cd Chronic-Disease-Progression-Predictor
python -m venv .venv
# Activate venv:
# Windows: .venv\Scripts\activate | Unix: source .venv/bin/activate
pip install -r requirements.txt
```

### Running the App
```bash
python app.py
```

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.

## 👤 Author
**Sanyog Singh**
- [GitHub Profile](https://github.com/SanyogSingh07)
- [Project Repository](https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor)
