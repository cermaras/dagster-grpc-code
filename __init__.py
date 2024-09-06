from dagster import asset, op


@asset
def git_dummy_asset():
    pass


@asset
def asset_test():
    pass


@op
def op_test():
    pass
