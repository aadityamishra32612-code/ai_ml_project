
# ☀️ Solar Irradiation Prediction and Rooftop Solar Cost Estimation in India Using Machine Learning

An Applied Machine Learning project that uses historical solar irradiation and weather data from NASA POWER to predict daily solar irradiation across 10 Indian cities using regression models. The predicted irradiation will support rooftop solar electricity generation, panel capacity estimation, and installation cost calculations.

## 📌 Project OVerview

Solar energy is an important renewable energy resource in India. However, solar irradiation varies across geographical locations, seasons, and weather conditions.

This project aims to develop a Machine Learning-based prediction system that estimates daily solar irradiation using historical meteorological data.

The project also aims to integrate these predictions into a rooftop solar calculator to estimate electricity generation, required solar panel capacity, number of panels, and approximate installation costs.

### 🎯 Objectives

- Collect historical solar and weather data using NASA POWER API.
- Analyze solar irradiation patterns across 10 Indian cities.
- Perform Exploratory Data Analysis (EDA) and feature engineering.
- Develop and compare multiple regression models.
- Optimize model performance using hyperparameter tuning.
- Predict daily solar irradiation for selected Indian cities.
- Estimate rooftop solar electricity generation and installation costs.
- Develop an interactive prediction interface using Jupyter Widgets.


**Course:** Applied Machine Learning  
**Project Type:** Regression

## 📊 Dataset Information

The dataset is collected from the NASA POWER (Prediction Of Worldwide Energy Resources) API.

- **Dataset Source:** https://power.larc.nasa.gov/
- **Documentation:** https://power.larc.nasa.gov/docs/
- **Data Period:** 2016–2025
- **Geographical Coverage:** 10 Indian cities
- **Total Records:** 36,530
- **Records per City:** 3,653

### Cities Covered

1. Bhopal
2. Dehradun
3. Gurugram
4. Jaipur
5. Lucknow
6. Ludhiana
7. New Delhi
8. Patna
9. Shimla
10. Srinagar

### Dataset Features

| Feature | Description |
|---|---|
| ALLSKY_SFC_SW_DWN | All-sky surface shortwave downward irradiation |
| T2M | Temperature at 2 metres |
| T2M_MAX | Maximum temperature |
| T2M_MIN | Minimum temperature |
| RH2M | Relative humidity |
| WS10M | Wind speed at 10 metres |
| PRECTOTCORR | Corrected precipitation |
| CITY | City name |
| STATE | State name |
| LATITUDE | Geographic latitude |
| LONGITUDE | Geographic longitude |

**Target Variable:** `ALLSKY_SFC_SW_DWN`  
**Unit:** kWh/m²/day

## ⚙️ Project Methodology

### 1. Data Collection

- Retrieved historical meteorological data using NASA POWER API.
- Collected daily observations for 10 Indian cities.
- Combined individual city datasets into a single CSV file.

### 2. Data Preprocessing

- Handled missing values and checked data consistency.
- Checked duplicate records.
- Converted date columns into appropriate datetime formats.
- Created seasonal and date-based features.

### 3. Exploratory Data Analysis (EDA)

Performed visual and statistical analysis, including:

- Average solar irradiation across cities.
- Monthly solar irradiation trends.
- Correlation heatmaps.
- Distribution of solar irradiation.
- Yearly irradiation comparisons.
- Seasonal irradiation analysis.
- Outlier detection.

### 4. Feature Engineering

Created additional features to improve model performance:

- Year
- Month
- Day
- Day of year
- Weekday
- Month sine and cosine transformations
- Day-of-year sine and cosine transformations
- Seasonal classification

### 5. Dataset Splitting

Used chronological data splitting to preserve the time-series order and reduce data leakage.

- Training dataset
- Validation dataset
- Testing dataset

### 6. Machine Learning Models

The following regression algorithms were implemented and compared:

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

### 7. Hyperparameter Tuning

Performed hyperparameter tuning for XGBoost to improve predictive performance.

Also conducted:

- Feature importance analysis.
- Permutation feature importance.
- Actual vs. predicted visualization.
- City-wise prediction error analysis.

## 📈 Model Performance

The following results were obtained from the model experiments.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.7175 | 0.9409 | 0.6512 |
| Random Forest | 0.5974 | 0.8082 | 0.7427 |
| XGBoost | 0.5754 | 0.7738 | 0.7641 |

### Tuned XGBoost Performance

| Metric | Original XGBoost | Tuned XGBoost |
|---|---:|---:|
| MAE | 0.5754 | 0.5735 |
| RMSE | 0.7738 | 0.7685 |
| R² | 0.7641 | 0.7673 |

### Final Test Results

| Metric | Result |
|---|---:|
| MAE | 0.5748 |
| RMSE | 0.7866 |
| R² Score | 0.7529 |

**Observation:** XGBoost performed better than Linear Regression and Random Forest in the reported model comparison. Hyperparameter tuning provided a modest improvement in validation performance.

## 🖥️ Interactive Prediction Interface

An interactive prediction interface has been developed using `ipywidgets`.

Users can:

- Select an Indian city.
- Choose a prediction date.
- Enter average temperature.
- Enter maximum and minimum temperatures.
- Enter relative humidity.
- Enter wind speed.
- Enter precipitation.
- Generate solar irradiation predictions using the trained XGBoost model.

The model is saved as a `.pkl` file and loaded for reusable predictions.

## 🏠 Rooftop Solar Calculator (In Development)

The next component integrates predicted solar irradiation with rooftop solar calculations.

Planned functionalities:

- Daily electricity generation estimation.
- Monthly and annual electricity generation.
- Required solar system capacity estimation.
- Solar panel quantity calculation.
- Approximate installation cost in Indian Rupees.
- Estimated electricity bill savings.
- Solar investment payback period.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| XGBoost | Gradient boosting regression |
| Jupyter Notebook | Model development and experimentation |
| ipywidgets | Interactive prediction interface |
| Requests | NASA POWER API communication |
| Joblib | Model serialization |

## 📂 Project Structure

```text
solar-irradiation-ml/
│
├── data/
│   ├── raw/
│   │   └── india_solar_combined.csv
│   │
│   └── processed/
│       └── solar_processed.csv
│
├── models/
│   └── solar_irradiation_xgboost.pkl
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_rooftop_solar_calculator.ipynb
│
├── src/
│   └── data_collection.py
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

*The structure represents the intended organization of the project. Notebook filenames and folders can be adjusted to match the final repository.*

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Visual Studio Code
- Jupyter Notebook

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/solar-irradiation-ml.git
```

### 2. Navigate to the Project Directory

```bash
cd solar-irradiation-ml
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

Alternatively, open the project directly in Visual Studio Code and select the `.venv` Python kernel.

## 📊 Evaluation Metrics

The models are evaluated using three regression metrics:

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted irradiation.
- **RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors.
- **R² Score:** Measures how much variation in the target variable is explained by the model.

## 🔮 Future Improvements

- Integrate live weather data from external weather APIs.
- Improve predictions using additional meteorological variables.
- Experiment with advanced models such as LightGBM and CatBoost.
- Develop a web-based application using Streamlit or Flask.
- Integrate rooftop solar cost estimation with city-specific predictions.
- Add solar subsidy and government scheme information.
- Improve model accuracy through further feature engineering and optimization.

## ⚠️ Disclaimer

This project is developed for academic and educational purposes.

Solar irradiation predictions and rooftop solar cost estimates are approximations. Actual electricity generation and installation costs depend on local weather conditions, equipment specifications, installation quality, location, and other factors.

The current prediction model requires user-provided weather parameters and does not independently forecast future weather.

## 📜 Data Source and References

- NASA POWER: https://power.larc.nasa.gov/
- NASA POWER Documentation: https://power.larc.nasa.gov/docs/
- Scikit-learn: https://scikit-learn.org/
- XGBoost: https://xgboost.readthedocs.io/

---


