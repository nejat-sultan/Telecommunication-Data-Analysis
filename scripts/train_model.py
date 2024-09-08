import mlflow # type: ignore
import mlflow.sklearn # type: ignore
import joblib # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import pandas as pd # type: ignore
from sklearn.metrics import mean_squared_error # type: ignore

combined_df = pd.read_csv('data.csv')
X = combined_df[['engagement_score', 'experience_score']]
y = combined_df['satisfaction_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mlflow.start_run()
mlflow.log_param("Model Type", "LinearRegression")
mlflow.log_metric("Mean Squared Error", mean_squared_error(y_test, y_pred))
mlflow.sklearn.log_model(model, "model")
mlflow.end_run()

joblib.dump(model, 'model.pkl')

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
