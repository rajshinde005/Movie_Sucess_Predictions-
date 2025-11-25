import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# --------------------------------------------------------
# 1) Load dataset
# --------------------------------------------------------
file_path = r"C:\Movie_Prediction\imdb_movie_dataset.csv"
df = pd.read_csv(file_path)

print("Initial shape:", df.shape)

# --------------------------------------------------------
# 2) Clean data
# --------------------------------------------------------
# Drop rows where revenue is missing because it is target variable
df = df.dropna(subset=["Revenue (Millions)"]).copy()
df.reset_index(drop=True, inplace=True)

# Convert runtime and year to numeric if needed
df["Runtime (Minutes)"] = pd.to_numeric(df["Runtime (Minutes)"], errors="coerce")
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Drop any rows containing NaN after conversion
df = df.dropna().copy()

print("Shape after cleaning:", df.shape)

# --------------------------------------------------------
# 3) Feature selection
# --------------------------------------------------------
target = "Revenue (Millions)"
drop_columns = ["Title", "Description", "Director", "Actors", target]

X = df.drop(columns=drop_columns)
y = df[target]

# Identify categorical and numeric columns
categorical_cols = ["Genre"]
numeric_cols = [col for col in X.columns if col not in categorical_cols]

# --------------------------------------------------------
# 4) Preprocessing + Model Pipeline
# --------------------------------------------------------
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

model = RandomForestRegressor(random_state=42, n_estimators=300)

pipeline = Pipeline(steps=[
    ("preprocess", preprocess),
    ("model", model)
])

# --------------------------------------------------------
# 5) Train-test split and training
# --------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

# --------------------------------------------------------
# 6) Prediction and evaluation
# --------------------------------------------------------
y_pred = pipeline.predict(X_test)

rmse = mean_squared_error(y_test, y_pred) ** 0.5   # FIXED — no squared argument
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print(f"RMSE  : {rmse:.3f}")
print(f"R² Score : {r2:.3f}")


# --------------------------------------------------------
# 7) Show some actual vs predicted values
# --------------------------------------------------------
comparison = pd.DataFrame({
    "Actual Revenue": y_test.values,
    "Predicted Revenue": y_pred
}).head(20)

print("\n===== SAMPLE PREDICTIONS =====")
print(comparison)
