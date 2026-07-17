"""Integration coverage using bundled public datasets."""

from examples.open_dataset_validation import run_validation


def test_all_reference_families_run_on_open_datasets() -> None:
    result = run_validation()

    assert result["datasets"] == {
        "iris": (150, 4),
        "wine": (178, 13),
        "breast_cancer": (569, 30),
        "karate_club": (34, 78),
    }
    assert result["lis_length"] > 0
    assert result["knapsack_value"] > 0
    assert result["matrix_chain_cost"] > 0
    assert result["graph_path_length"] > 0
    assert result["mst_weight"] > 0
