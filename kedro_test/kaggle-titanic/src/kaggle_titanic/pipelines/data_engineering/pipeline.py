from kedro.pipeline import Pipeline, node

from .nodes import *


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=combine_kaggle_dataset,
                inputs=["train_raw", "test_raw"],
                outputs="combined_raw",
                name="Combine raw data"
            ),
            node(
                func=get_filled_age,
                inputs="combined_raw",
                outputs="preprocessed_age",
                name="clean \"Age\""
            ),
            node(
                func=get_filled_embarked,
                inputs="combined_raw",
                outputs="preprocessed_embarked",
                name="clean \"Embarked\""
            ),
            node(
                func=get_filled_fare,
                inputs="combined_raw",
                outputs="preprocessed_fare",
                name="clean \"Fare\""
            ),
            node(
                func=get_deck_from_cabin,
                inputs="combined_raw",
                outputs="preprocessed_deck",
                name="calculate \"Deck\" from \"Cabin\""
            ),
            node(
                func=get_title_from_name,
                inputs="combined_raw",
                outputs="preprocessed_title",
                name="calculate \"Title\" from \"Name\""
            ),
            node(
                func=get_surname_from_name,
                inputs="combined_raw",
                outputs="preprocessed_surname",
                name="calculate \"Surname\" from \"Name\""
            ),
            node(
                func=get_master_table,
                inputs=[
                    "combined_raw",
                    "preprocessed_age",
                    "preprocessed_embarked",
                    "preprocessed_fare",
                    "preprocessed_deck",
                    "preprocessed_title",
                    "preprocessed_surname"
                ],
                outputs="master_table",
                name="Combine cleaned data"
            ),
            node(
                func=identity,
                inputs="train_1_raw",
                outputs="train_2_raw",
                name="Dummy"
            )
        ]
    )
