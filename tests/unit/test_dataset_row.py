from mcptune.schema.dataset import DatasetRow


def test_dataset_row_structure():
    row = DatasetRow(
        tool_name="test",
        arguments={"a": 1},
        request={"jsonrpc": "2.0"}
    )

    assert row.tool_name == "test"
    assert row.arguments["a"] == 1
    assert row.request["jsonrpc"] == "2.0"