# 🏠 House Price Prediction Using Linear Regression

A Machine Learning project that uses **Linear Regression** to predict house prices based on:

* 📐 **Living Area (Square Footage)**
* 🛏️ **Number of Bedrooms**
* 🛁 **Number of Full Bathrooms**

The trained Linear Regression model is integrated with a **Streamlit web application**, allowing users to enter house details and receive an estimated house price in **Indian Rupees (INR)** and **US Dollars (USD)**.

---

## 🔗 Project Links

| Resource                 | Link                                                            |
| ------------------------ | --------------------------------------------------------------- |
| 🌐 **Live Demo**         | https://sctml1-bdtensueexcyxnedxc6ktf.streamlit.app/            |
| 💻 **GitHub Repository** | https://github.com/Lohith-CSE-AIML/SCT_ML_1                     |

---

## 📌 Internship Task

**Organization:** SkillCraft Technology
**Track:** Machine Learning
**Task:** SCT_ML_1

### Task Description

> Implement a linear regression model to predict the prices of houses based on their square footage and the number of bedrooms and bathrooms.

This project was developed as part of the **SkillCraft Technology Machine Learning Internship**.

---

## 🎯 Objective

The main objective of this project is to develop a **Linear Regression model** capable of predicting house prices using three selected features:

* `GrLivArea` — Living area in square feet
* `BedroomAbvGr` — Number of bedrooms above ground
* `FullBath` — Number of full bathrooms

The complete project includes:

1. Dataset loading
2. Data understanding
3. Feature selection
4. Train-test splitting
5. Linear Regression model development
6. Model training
7. Prediction
8. Model evaluation
9. Residual analysis
10. Model serialization
11. Streamlit application development
12. Deployment

---

## 🗂️ Dataset

The project uses the **Ames Housing Dataset**.

The dataset contains information about residential properties along with their corresponding sale prices.

### Features Used

| Feature        | Description                             |
| -------------- | --------------------------------------- |
| `GrLivArea`    | Above-ground living area in square feet |
| `BedroomAbvGr` | Number of bedrooms above ground         |
| `FullBath`     | Number of full bathrooms                |

### Target Variable

| Variable    | Description             |
| ----------- | ----------------------- |
| `SalePrice` | Sale price of the house |

> The original dataset contains many additional features, but this project specifically uses the three features required for the Linear Regression task.

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🐼 **Pandas**
* 🔢 **NumPy**
* 🤖 **Scikit-learn**
* 📊 **Matplotlib**
* 💾 **Joblib**
* 🌐 **Streamlit**
* 📓 **Jupyter Notebook**
* 🔧 **Git**
* 💻 **GitHub**

---

## 🔄 Project Workflow

```text
                 Ames Housing Dataset
                          │
                          ▼
                  Data Understanding
                          │
                          ▼
                   Feature Selection
                          │
                          ▼
                    Train/Test Split
                          │
                          ▼
                   Linear Regression
                          │
                          ▼
                    Model Training
                          │
                          ▼
                      Prediction
                          │
                          ▼
                  Model Evaluation
                          │
                          ▼
                  Residual Analysis
                          │
                          ▼
                   Save Trained Model
                          │
                          ▼
                 Streamlit Application
                          │
                          ▼
                       Deployment
```

---

## 🤖 Linear Regression Model

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

The model learns the relationship between the input features and the target variable.

### Input Features

```text
GrLivArea
BedroomAbvGr
FullBath
```

### Target Variable

```text
SalePrice
```

The general Linear Regression equation is:

```text
y = b₀ + b₁x₁ + b₂x₂ + b₃x₃
```

For this project:

```text
SalePrice =
Intercept
+ (GrLivArea × coefficient)
+ (BedroomAbvGr × coefficient)
+ (FullBath × coefficient)
```

### Learned Model Parameters

```text
Intercept        = 52261.7486

GrLivArea        = 104.0263
BedroomAbvGr     = -26655.1654
FullBath         = 30014.3241
```

---

## 📈 Model Performance

The model was evaluated using the test dataset.

### Evaluation Metrics

| Metric       | Result           |
| ------------ | ---------------- |
| **MAE**      | 35,788.06        |
| **MSE**      | 2,806,426,667.25 |
| **RMSE**     | 52,975.72        |
| **R² Score** | **0.6341**       |

### 📌 R² Score

The model achieved an **R² score of 0.6341**.

This means that the model explains approximately **63.4% of the variation in house prices** using the three selected features.

Since this project is based on only three input features, the model is considered a **baseline Linear Regression model**.

---

## 📊 Residual Analysis

Residual analysis was performed to understand the prediction errors of the Linear Regression model.

The residual is calculated as:

```text
Residual = Actual Price - Predicted Price
```

The residual analysis helps evaluate how the prediction errors are distributed and whether there are noticeable patterns in the model's errors.

### 📈 Residual Plot

---

## 🖥️ Streamlit Application

The trained Linear Regression model was integrated into a **Streamlit web application**.

The application allows users to:

1. Enter the living area of the house.
2. Enter the number of bedrooms.
3. Enter the number of full bathrooms.
4. Generate a house price prediction.
5. View the estimated price in Indian Rupees.
6. View the estimated price in US Dollars.

---

## 📸 Application Screenshots
<img width="1007" height="860" alt="Screenshot 2026-08-26 083110" src="https://github.com/user-attachments/assets/06e5ee69-4d6e-49a3-b021-e2b1b848f396" />

### 🏠 House Price Prediction Interface

The application provides input fields for:

* 📐 Living Area
* 🛏️ Number of Bedrooms
* 🛁 Number of Full Bathrooms

---

### 💰 House Price Prediction Result

The application displays the estimated house price in:

* 🇮🇳 **Indian Rupees (INR)**
* 🇺🇸 **US Dollars (USD)**

---

## 🌐 Live Demo
https://sctml1-bdtensueexcyxnedxc6ktf.streamlit.app/
### 🚀 Try the Application

👉 **Open House Price Prediction Application**

The application is deployed using **Streamlit Community Cloud**.

Users can enter house details and receive an estimated house price directly through the web application.

---

## 💻 GitHub Repository

The complete source code, trained model, notebook, screenshots, and application files are available on GitHub.

👉 [**View GitHub Repository**](https://github.com/Lohith-CSE-AIML/SCT_ML_1)

---

## 📁 Project Structure

```text
SCT_ML_1/
│
├── data/
│   └── train.csv
│
├── model/
│   └── house_price_linear_regression.pkl
│
├── notebooks/
│   └── house_price_linear_regression.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── prediction.png
│   └── residual_plot.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File/Folder        | Description                                  |
| ------------------ | -------------------------------------------- |
| `data/`            | Contains the housing dataset                 |
| `model/`           | Contains the trained Linear Regression model |
| `notebooks/`       | Complete model development and analysis      |
| `screenshots/`     | Application and analysis screenshots         |
| `app.py`           | Streamlit application                        |
| `requirements.txt` | Required Python libraries                    |
| `README.md`        | Project documentation                        |
| `.gitignore`       | Files excluded from Git                      |

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Lohith-CSE-AIML/SCT_ML_1.git
```

### 2. Navigate to the Project

```bash
cd SCT_ML_1
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💾 Model Serialization

After training, the Linear Regression model was saved using **Joblib**.

```text
model/house_price_linear_regression.pkl
```

The Streamlit application loads this saved model to make predictions without retraining the model every time the application starts.

```python
model = joblib.load("model/house_price_linear_regression.pkl")
```

---

## ⚠️ Limitations

This project uses only three features:

* Living Area
* Number of Bedrooms
* Number of Full Bathrooms

However, house prices can depend on many other factors, including:

* 📍 Location
* 🏘️ Neighborhood
* ⭐ Overall house quality
* 📅 Year built
* 🚗 Garage
* 🏠 Basement
* 📐 Lot size
* 🔨 Renovations
* 🏊 Pool
* And many other property characteristics

Therefore, this model should be considered a **baseline prediction model** rather than a production-level house valuation system.

---

## 🚀 Future Improvements

Possible improvements for future versions include:

* Add more relevant housing features.
* Perform feature engineering.
* Improve outlier handling.
* Perform cross-validation.
* Compare multiple regression algorithms.
* Perform hyperparameter tuning.
* Experiment with ensemble models.
* Improve the Streamlit user interface.
* Add interactive visualizations.
* Use real-time currency conversion.
* Improve prediction accuracy using additional features.

---

## 👨‍💻 Author

### Lohith

**B.Tech — Computer Science and Engineering (AI & ML)**

### GitHub

💻 [Lohith-CSE-AIML](https://github.com/Lohith-CSE-AIML)

---

## ⭐ Acknowledgement

This project was developed as part of the **SkillCraft Technology Machine Learning Internship**.

