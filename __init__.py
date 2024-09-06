from dagster import asset


@asset
def git_dummy_asset():
    pass


@asset
def asset_test():
    pass
