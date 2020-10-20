import pandas as pd


def get_filled_age(df: pd.DataFrame) -> pd.Series:
    return df.groupby(['Sex', 'Pclass'])['Age'].apply(lambda x: x.fillna(x.median()))


def get_filled_embarked(df: pd.DataFrame) -> pd.Series:
    return df['Embarked'].fillna('S')
