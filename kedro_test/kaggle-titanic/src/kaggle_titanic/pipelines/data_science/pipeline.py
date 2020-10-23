from kedro.pipeline import Pipeline, node

from .nodes import *


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=one_hot_encoding,
                inputs=["master_table", "params:model_input"],
                outputs=["categorical_features", "one_hot_encoders"],
                name="One hot encoding for categorical features"
            ),
            node(
                func=combine_features,
                inputs=["master_table", "categorical_features", "params:model_input"],
                outputs="all_features",
                name="Combine categorical features and numerical features"
            ),
            node(
                func=node_train_test_split,
                inputs=["master_table", "all_features", "params:model_output", "params:test_size"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="Train test split"
            ),
            node(
                func=train_random_forest,
                inputs=["X_train", "y_train", "params:random_forest_classifier_params"],
                outputs="random_forest_model",
                name="Train with sklearn.ensemble.RandomForestClassifier"
            ),
            node(
                func=report_accuracy,
                inputs=["random_forest_model", "X_train", "X_test", "y_train", "y_test"],
                outputs=None,
                name="Record training result"
            ),
        ]
    )
