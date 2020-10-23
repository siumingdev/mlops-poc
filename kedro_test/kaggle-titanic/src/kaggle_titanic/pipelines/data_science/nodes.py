from typing import Dict, List, Tuple, Any
import logging
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


def one_hot_encoding(
        master_table_df: pd.DataFrame,
        params_model_input: Dict[str, List[str]]
) -> Tuple[pd.DataFrame, Dict[str, OneHotEncoder]]:
    cat_features = params_model_input["categorical"]
    df = master_table_df

    encoded_features = []
    encoders = dict()
    for feature in cat_features:
        encoder = OneHotEncoder()
        encoded_feat = encoder.fit_transform(df[feature].values.reshape(-1, 1)).toarray()
        n = df[feature].nunique()
        cols = ['{}_{}'.format(feature, n) for n in range(1, n + 1)]
        encoded_df = pd.DataFrame(encoded_feat, columns=cols)
        encoded_df.index = df.index
        encoded_features.append(encoded_df)
        encoders[feature] = encoder

    return pd.concat(encoded_features, axis=1), encoders


def combine_features(
        master_table_df: pd.DataFrame,
        categorical_features_df: pd.DataFrame,
        params_model_input: Dict[str, List[str]]
) -> pd.DataFrame:
    num_features_df = master_table_df[params_model_input["numerical"]]
    return pd.concat([num_features_df, categorical_features_df], axis=1)


def node_train_test_split(
        master_table_df: pd.DataFrame,
        all_features: pd.DataFrame,
        model_output: str,
        test_size: float
) -> Tuple[np.array, np.array, np.array, np.array]:
    X = all_features.values
    y = master_table_df[model_output]
    return train_test_split(X, y, test_size=test_size)


def train_random_forest(
        X: np.array,
        y: np.array,
        model_params: Dict[str, Any]
) -> RandomForestClassifier:
    clf = RandomForestClassifier(**model_params)
    clf.fit(X, y)
    return clf


def report_accuracy(
        model: RandomForestClassifier,
        X_train: np.array,
        X_test: np.array,
        y_train: np.array,
        y_test: np.array
) -> None:
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    logging.info("Model accuracy on train set: %0.2f%%", train_score * 100)
    logging.info("Model accuracy on test set: %0.2f%%", test_score * 100)
