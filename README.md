# Data Pipeline Development

## Internship Credentials
*Company* : CodTech IT Solutions
*Name* : Mohamed Fadhil U.F
*Intern ID* : CITSOD822
*Domain* : Data Science
*Duration* : Neela Santhosh

## Task 1: ETL (Extract, Transform, Load) Pipeline Using Pandas and Scikit-Learn

This project demonstrates how to build a simple data preprocessing pipeline using Python's Pandas and Scikit-learn libraries. It uses the Titanic dataset from Seaborn as an example and showcases basic steps of an ETL process.

## 📊 Project Description

This project demonstrates the development of a basic **ETL (Extract, Transform, Load)** data pipeline using **Pandas** and **Scikit-learn**, two of the most widely used Python libraries for data science and machine learning. The main goal of this project is to prepare data for machine learning tasks by cleaning, transforming, and splitting it into training and testing sets in a reproducible and efficient way.
The pipeline uses the **Titanic dataset**, a well-known dataset commonly used for binary classification problems. It contains passenger data such as name, sex, age, ticket fare, class, and whether or not the passenger survived. The dataset is loaded directly from an online source (Seaborn's public GitHub repository), making it quick and easy to test or extend with different datasets.
Once loaded, the dataset is examined for structure and completeness. The target variable `survived` is separated from the feature set. Then, the feature set is divided into **numerical** and **categorical** columns, as different preprocessing steps are applied to each data type.
For numerical features, the pipeline performs **missing value imputation** using the mean strategy, followed by **standard scaling** to normalize the data. For categorical features, missing values are filled using the most frequent category, followed by **one-hot encoding** to convert categories into binary vectors. These steps are combined using Scikit-learn’s `Pipeline` and `ColumnTransformer`, making the transformation modular and easy to maintain.
After the data is transformed, it is split into **training** and **testing** sets using an 80/20 ratio. This prepares the data for any downstream machine learning models.

The key benefits of this project include:
- **Reusability**: The ETL pipeline can be reused with different datasets or extended with additional steps (e.g., feature selection, text processing).
- **Automation**: All preprocessing steps are handled programmatically, reducing manual effort and improving consistency.
- **Modularity**: Each part of the pipeline is encapsulated, making it easier to test and debug.

This project serves as a foundational step in building robust data pipelines and is suitable for beginners looking to understand preprocessing workflows before applying machine learning models. Future enhancements may include saving the pipeline with `joblib`, adding model training and evaluation, or adapting the pipeline for real-time or batch processing in production environments.

## 🔧 Features

- Loads a public dataset
- Separates features and target
- Identifies numeric and categorical columns
- Applies preprocessing:
  - Imputes missing values
  - Scales numeric features
  - One-hot encodes categorical features
- Combines steps into a reusable pipeline
- Splits data into training and test sets


## 📁 Files

- `etl_pipeline.py` (your script — to be created or renamed from current code)
- `README.md` (project documentation)

## 📦 Requirements

- Python 3.7+
- pandas
- scikit-learn

Install dependencies using:

```bash
pip install pandas scikit-learn
```

🚀 How to Run
Clone the repository or download the script.
Run the Python script:
```bash
python etl_pipeline.py
```

🧪 Dataset
The dataset used is the Titanic dataset from Seaborn:
```bash
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv
```
You can replace this with your own dataset by updating the URL or file path.

📈 Output
After running the script, you'll see output like:


Done By:
Mohamed Fadhil U.F
Data Science Intern
CodTech IT Solutions
