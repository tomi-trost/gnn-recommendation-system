"""
Inspect top items per Louvain community in the item-item projection.
Run from the graph_analysis/ directory with the same environment as analysis.ipynb.

    python inspect_communities.py

Output: prints top-15 items by weighted degree for each community,
        sorted by community size (largest first).
"""

import pickle
import ast
import networkx as nx
import networkx.algorithms.community as nx_comm


# ── 1. Load item projection ────────────────────────────────────────────────
with open("artifacts/item_proj.pkl", "rb") as f:
    item_proj = pickle.load(f)

print(f"Item projection: {item_proj.number_of_nodes()} nodes, "
      f"{item_proj.number_of_edges()} edges")


# ── 2. Rebuild item names from raw data ───────────────────────────────────
item_names: dict = {}
with open("../australian_users_items.json", encoding="utf-8") as f:
    for line in f:
        user = ast.literal_eval(line)
        for item in user["items"]:
            node = ("item", item["item_id"])
            if node not in item_names:
                item_names[node] = item.get("item_name", "unknown")

print(f"Item names loaded: {len(item_names)}\n")


# ── 3. Filter projection and run Louvain (same params as notebook) ─────────
def filter_graph(G, min_weight: float = 10.0) -> nx.Graph:
    H = nx.Graph()
    for u, v, d in G.edges(data=True):
        if d.get("weight", 0) >= min_weight:
            H.add_edge(u, v, weight=d["weight"])
    return H


filtered = filter_graph(item_proj, min_weight=10)
communities = nx_comm.louvain_communities(filtered, seed=42)

sizes = sorted([len(c) for c in communities], reverse=True)
print(f"Detected {len(communities)} communities, sizes: {sizes}\n")
print("=" * 60)


# ── 4. Print top-15 items per community by weighted degree ─────────────────
for rank, comm in enumerate(sorted(communities, key=len, reverse=True), start=1):
    sub = item_proj.subgraph(comm)
    top = sorted(sub.degree(weight="weight"), key=lambda x: x[1], reverse=True)[:15]
    print(f"\nCommunity {rank}  ({len(comm)} items)")
    print("-" * 50)
    for node, strength in top:
        print(f"  {item_names.get(node, str(node)):<45}  strength={strength:,.0f}")

print("\nDone.")
