from kedro.pipeline import Pipeline, node

from .nodes import get_filled_age


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=get_filled_age,
                inputs="train",
                outputs="filled_age_train",
                name="filled_age_train"
            )
        ]
    )
