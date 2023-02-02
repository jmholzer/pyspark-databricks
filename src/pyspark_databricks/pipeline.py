from kedro.pipeline import Pipeline, node, pipeline

from .nodes import load_csv, identity


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=load_csv,
                inputs=["example_data"],
                outputs="intermediate_save",
                name="save_spark_dataset",
            ),
            node(
                func=identity,
                inputs=["intermediate_save"],
                outputs="output",
                name="load_spark_dataset",
            )
        ]
    )