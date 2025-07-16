# Data-pipeline-development-

import pandas as pd from sklearn.preprocessing import StandardScaler, OneHotEncoder from sklearn.compose import ColumnTransformer from sklearn.pipeline import Pipeline from sklearn.impute import SimpleImputer from sklearn.model_selection import train_test_split

## Load dataset (using example dataset - replace with your own if needed)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv" df = pd.read_csv(url)

## Display basic info

print("Initial Data Info:") print(df.info())
Split features and target
X = df.drop("survived", axis=1) y = df["survived"]

## Define numeric and categorical columns

numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist() categorical_features = X.select_dtypes(include=['object']).columns.tolist()

## Numeric pipeline

numeric_pipeline = Pipeline([ ('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler()) ])

## Categorical pipeline

categorical_pipeline = Pipeline([ ('imputer', SimpleImputer(strategy='most_frequent')), ('encoder', OneHotEncoder(handle_unknown='ignore')) ])

## Combine into full pipeline

preprocessor = ColumnTransformer([ ('num', numeric_pipeline, numeric_features), ('cat', categorical_pipeline, categorical_features) ])

## Apply pipeline

X_transformed = preprocessor.fit_transform(X)

## Train-test split

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
print("\nETL process completed. Transformed feature shape:", X_train.shape)
