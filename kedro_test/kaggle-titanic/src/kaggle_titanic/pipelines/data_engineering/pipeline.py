from kedro.pipeline import Pipeline, node

from .nodes import get_filled_age, get_filled_embarked


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=get_filled_age,
                inputs="train",
                outputs="train_filled_age",
                name="train_filled_age"
            ),
            node(
                func=get_filled_embarked,
                inputs="train",
                outputs="train_filled_embarked",
                name="train_filled_embarked"
            ),
        ]
    )
