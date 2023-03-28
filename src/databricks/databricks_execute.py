from kedro.framework.session import KedroSession
from kedro.framework.startup import configure_project


def main():
    package_name = "pyspark-databricks"
    configure_project(package_name)
    with KedroSession.create(package_name, conf_source="/dbfs/dbx/test-conf") as session:
        session.run()


if __name__ == "__main__":
    main()
