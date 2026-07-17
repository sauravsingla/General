"""Run the public reference APIs against bundled open datasets.

The datasets are distributed with scikit-learn or NetworkX, so this example is
reproducible and does not depend on network downloads at runtime.
"""

from __future__ import annotations

from math import isclose

import networkx as nx
from sklearn.datasets import load_breast_cancer, load_iris, load_wine

from general_reference import (
    DisjointSet,
    FenwickTree,
    binary_search,
    breadth_first_path,
    dijkstra_shortest_path,
    edit_distance,
    kmp_search,
    kruskal_minimum_spanning_forest,
    longest_increasing_subsequence,
    longest_increasing_subsequence_dp,
    matrix_chain_order,
    merge_sort,
    online_mean_variance,
    topological_sort,
    zero_one_knapsack,
    z_function,
)


def run_validation() -> dict[str, object]:
    """Exercise every public reference family on multiple open datasets."""
    iris = load_iris()
    wine = load_wine()
    cancer = load_breast_cancer()

    iris_values = [float(row[0]) for row in iris.data]
    wine_values = [float(row[0]) for row in wine.data]
    cancer_values = [float(row[0]) for row in cancer.data]

    sorted_iris = merge_sort(iris_values)
    median_value = sorted_iris[len(sorted_iris) // 2]
    median_index = binary_search(sorted_iris, median_value)
    assert median_index is not None and sorted_iris[median_index] == median_value

    baseline_length, _ = longest_increasing_subsequence_dp(wine_values[:60])
    fast_length, _ = longest_increasing_subsequence(wine_values[:60])
    assert baseline_length == fast_length

    statistics = online_mean_variance(cancer_values)
    assert statistics.count == len(cancer_values)

    weights = [max(1, int(value)) for value in iris.data[:20, 0]]
    values = [float(value) for value in iris.data[:20, 2]]
    knapsack_value, selected = zero_one_knapsack(weights, values, capacity=35)
    assert knapsack_value >= 0 and sum(weights[index] for index in selected) <= 35

    dimensions = [iris.data.shape[1], wine.data.shape[1], cancer.data.shape[1], 2]
    matrix_cost, parenthesization = matrix_chain_order(dimensions)
    assert matrix_cost > 0 and parenthesization

    target_text = " ".join(map(str, iris.target_names))
    assert edit_distance(str(iris.target_names[0]), str(wine.target_names[0])) >= 0
    assert kmp_search(target_text, str(iris.target_names[1]))
    assert len(z_function(target_text)) == len(target_text)

    tree = FenwickTree(iris_values[:50])
    assert isclose(tree.range_sum(0, 50), sum(iris_values[:50]))

    groups = DisjointSet(range(6))
    groups.union(0, 1)
    groups.union(1, 2)
    assert groups.connected(0, 2)

    graph = nx.karate_club_graph()
    unweighted = {node: list(graph.neighbors(node)) for node in graph.nodes}
    path = breadth_first_path(unweighted, 0, 33)
    assert path[0] == 0 and path[-1] == 33

    weighted = {
        node: [(neighbour, float(data.get("weight", 1.0))) for neighbour, data in graph[node].items()]
        for node in graph.nodes
    }
    cost, weighted_path = dijkstra_shortest_path(weighted, 0, 33)
    assert cost >= 0 and weighted_path[0] == 0 and weighted_path[-1] == 33

    forest_weight, forest = kruskal_minimum_spanning_forest(
        graph.nodes,
        [(float(data.get("weight", 1.0)), first, second) for first, second, data in graph.edges(data=True)],
    )
    assert len(forest) == graph.number_of_nodes() - 1 and forest_weight > 0

    ordering = topological_sort({"load": ["clean"], "clean": ["analyse"], "analyse": []})
    assert ordering.index("load") < ordering.index("clean") < ordering.index("analyse")

    return {
        "datasets": {
            "iris": iris.data.shape,
            "wine": wine.data.shape,
            "breast_cancer": cancer.data.shape,
            "karate_club": (graph.number_of_nodes(), graph.number_of_edges()),
        },
        "lis_length": fast_length,
        "knapsack_value": knapsack_value,
        "matrix_chain_cost": matrix_cost,
        "graph_path_length": len(path) - 1,
        "mst_weight": forest_weight,
    }


if __name__ == "__main__":
    for key, value in run_validation().items():
        print(f"{key}: {value}")
