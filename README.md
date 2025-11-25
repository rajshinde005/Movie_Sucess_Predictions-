# 🎬 Movie Success Prediction – Data Analytics Project

## 📌 Project Overview

This project aims to **predict the success of movies** using **data analytics and machine learning techniques**.
The model evaluates various influencing factors such as budget, cast, director, genre, runtime, ratings, social buzz, and audience sentiments to estimate overall success in terms of **Revenue / IMDB Rating / Popularity Score**.

---

## 🚀 Key Objectives

* Identify major factors that impact movie success
* Perform **exploratory data analysis (EDA)**
* Build ML models to predict movie performance
* Visualize trends and insights for better decision-making
* Provide actionable inputs for film production and marketing teams

---

## 📂 Project Structure

```
Movie_Prediction/
│
├── dataset/                  # Raw & cleaned datasets
├── notebooks/                # EDA and ML Jupyter notebooks
├── src/                      # Model training and utility scripts
├── saved_models/             # Trained ML models
├── dashboard/                # Power BI visualizations (PDF / PBIX)
├── screenshots/              # Output & result screenshots
├── README.md                 # Documentation file
└── requirements.txt          # Python dependencies
```

---

## 🧠 Machine Learning Models Used

| Model                   | Performance               |
| ----------------------- | ------------------------- |
| Linear Regression       | Good baseline performance |
| Random Forest Regressor | Best accuracy             |
| XGBoost                 | Competitive and stable    |
| Decision Tree           | Moderate results          |

🔹 Final chosen model: **Random Forest (best R² score)**
🔹 RMSE score: **75.666**

---

## 📊 Tech Stack & Libraries

| Category              | Tools                       |
| --------------------- | --------------------------- |
| Programming           | Python                      |
| ML                    | Scikit-Learn, XGBoost       |
| Data Analysis         | NumPy, Pandas               |
| Visualization         | Matplotlib, Seaborn, Plotly |
| Dashboard             | Power BI                    |
| Deployment (optional) | Streamlit / Flask           |

---

## 🔍 Insights from the Project

✔ Higher budgets correlate with higher box-office success
✔ Genres like Action, Thriller & Sci-Fi perform best commercially
✔ IMDB ratings and social buzz strongly influence performance
✔ Starcast influence varies — a strong marketing strategy is equally important

---

## 📈 Dashboard

A **Power BI dashboard** was created to visualize:

* Genre-wise movie performance
* Rating distribution
* Revenue by year
* Correlation heatmap of key factors

(`dashboard/` folder contains PBIX + PDF export)

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/Movie_Prediction.git
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the model

```bash
python src/model_train.py
```

### 4️⃣ Predict with new data

```bash
python src/predict.py
```

---

## 📌 Future Enhancements

🔹 Deploy prediction system as a Web App
🔹 Use deep learning for trailers sentiment + NLP screenplay analysis
🔹 Add Hindi / Multilingual movie dataset

---

## 💡 Author

👤 **Raj Shinde**
📧 *[rajudayshinde@gmail.com ]*

