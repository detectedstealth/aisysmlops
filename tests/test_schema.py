import json
from pathlib import Path


def test_feature_schema_exists():
    schema_path = Path("outputs/feature_schema.json")
    assert schema_path.exists(), "schema_schema.json does not exist"


def test_feature_schema_valid():
    schema_path = Path("outputs/feature_schema.json")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    assert isinstance(schema, dict), "schema_schema.json is not a valid JSON"


def test_feature_schema_has_content():
    schema_path = Path("outputs/feature_schema.json")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    assert len(schema) > 0, "schema_schema.json is empty"