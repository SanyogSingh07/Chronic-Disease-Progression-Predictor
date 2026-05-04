# 🏥 Chronic Disease Progression Predictor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/SanyogSingh07/Chronic-Disease-Progression-Predictor/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://GitHub.com/SanyogSingh07/Chronic-Disease-Progression-Predictor/pulls)

A professional Machine Learning pipeline for predicting the progression rate of chronic diseases using the **U.S. Chronic Disease Indicators (CDI)** dataset. This tool provides a command-line interface (CLI) to train models and perform inference on specific disease types.

## 🚀 Key Features

- **Automated Preprocessing**: Intelligent detection of patient IDs, time sequences, and target variables.
- **Multi-Model Training**: Compares Linear Regression and Random Forest Regressors to select the best-performing model.
- **Interactive CLI**: Easy-to-use menu system built with `typer` and `rich`.
- **Disease-Specific Inference**: Predict average progression rates for specific conditions (e.g., Diabetes, Cardiovascular Disease).
- **Extensible Architecture**: Modular codebase structured for scalability and academic research.

## 📁 Project Structure

```text
.
├── data/               # Dataset storage (U.S._Chronic_Disease_Indicators.csv)
├── models/             # Serialized models and scalers
├── outputs/            # Generated reports and visualizations
├── src/                # Source code
│   ├── data/           # Data loading and preprocessing logic
│   ├── models/         # Training and evaluation modules
│   └── cli.py          # CLI command definitions
├── app.py              # Main entry point
└── requirements.txt    # Project dependencies
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor.git
   cd Chronic-Disease-Progression-Predictor
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the main application to access the interactive menu:

```bash
python app.py
```

### Commands

- **Train Model**: Loads the dataset, preprocesses features, trains multiple regressors, and saves the best model.
- **Predict Disease**: Allows you to enter a disease name and get the predicted progression rate based on historical data.

## 📊 Dataset

The project uses the **U.S. Chronic Disease Indicators (CDI)**, which includes 124 indicators across 18 topic areas (e.g., Cancer, Diabetes, Heart Disease).

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

## 👤 Author

**Sanyog Singh**
- GitHub: [@SanyogSingh07](https://github.com/SanyogSingh07)
- Project Link: [Chronic-Disease-Progression-Predictor](https://github.com/SanyogSingh07/Chronic-Disease-Progression-Predictor)
