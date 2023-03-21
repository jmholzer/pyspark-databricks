from kedro.framework.session import KedroSession
from kedro.framework.startup import configure_project


def main():
    package_name = "pyspark_databricks"
    configure_project(package_name)
    with KedroSession.create(package_name) as session:
        session.run()
