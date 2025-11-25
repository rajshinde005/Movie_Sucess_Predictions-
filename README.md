📌 Movie Success Prediction 
🎯 Project Objective

The aim of this project is to predict the success of movies based on various features such as budget, genre, cast, production house, runtime, social media engagement, and audience sentiments.
The model helps production houses estimate expected revenue / success score before release.

🧠 Tech Stack Used
Area	Tools / Libraries
Programming	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Model Building	Scikit-learn
NLP (if sentiment used)	TextBlob
IDE Used	VS Code / Jupyter Notebook

📂 Project Folder Structure
Movie_Prediction/
│── dataset/                ← Raw & cleaned dataset
│── screenshots/            ← Output & visualization images
│── movie_prediction.py     ← Main ML code
│── model.pkl               ← Saved trained model
│── README.md               ← Project documentation
│── requirements.txt        ← Dependencies

🔍 Workflow of the Project

1️⃣ Import and inspect dataset
2️⃣ Data cleaning & handling missing values
3️⃣ Feature engineering & encoding categorical data
4️⃣ Train/test split
5️⃣ Train multiple ML models (Linear Regression, Random Forest etc.)
6️⃣ Evaluate performance using RMSE & R² score
7️⃣ Visualize patterns and correlations
8️⃣ Export trained model

📊 Dataset Summary
Total Rows	Final Rows After Cleaning	Total Features
1000	838	12
📈 Model Performance
RMSE  : 75.666
R² Score : 0.84 (approx)

🖥 Output Screenshots

Screenshots of:
✔ Dataset
✔ Correlation heatmap
✔ Model performance
✔ Prediction results

(Attached inside screenshots/ folder)

🚀 How to Run the Project
1️⃣ Install required libraries
pip install -r requirements.txt

2️⃣ Run the model
python movie_prediction.py

3️⃣ Predict revenue / success (example)
Enter Budget: 120000000
Enter Runtime: 145
Enter IMDB Rating: 8.1
Prediction → Expected Business: ₹256 Crores

📌 Applications of the Project

🔹 Predict success before release
🔹 Planning & strategy for production houses
🔹 Business decision support for investors
🔹 Improve script / marketing / cast decisions

🧑‍💻 Developer

👤 Raj Shinde
Data Analytics Enthusiast
