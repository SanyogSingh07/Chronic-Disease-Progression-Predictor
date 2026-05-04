import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_numeric_dtype

def preprocess(df, id_col, time_col, target_col):
    if id_col and id_col in df.columns:
        df = df.drop(columns=[id_col])

    if time_col and time_col in df.columns:
        df = df.sort_values(by=time_col)
        df = df.drop(columns=[time_col])

    if not is_numeric_dtype(df[target_col]):
        df[target_col] = LabelEncoder().fit_transform(df[target_col].astype(str))

    df = df.fillna(df.mean(numeric_only=True))
    
    # Process categorical columns memory efficiently
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if df[col].nunique() <= 10:
            # One-hot encode low cardinality
            dummies = pd.get_dummies(df[[col]], drop_first=True)
            df = pd.concat([df, dummies], axis=1)
            df = df.drop(columns=[col])
        else:
            # Label encode high cardinality to avoid memory blowup
            df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    return df
