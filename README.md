# Steam Recommendation System – Network Analysis

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

Download dataset from Kaggle:

Steam Video Game and Bundle Data
https://www.kaggle.com/datasets/pypiahmad/steam-video-game-and-bundle-data

Place the file:

```
australian_users_items.json
```

in the project root directory.

---

## Run

Execute your analysis script:

```bash
python main.py
```

---

## Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
└── australian_users_items.json
```

---

## Notebooks

During development, multiple Jupyter notebook files were used experimentally to explore different approaches. For the final results, we primarily used [`combined_link_prediction.ipynb`](combined_link_prediction.ipynb), which was run on a **T4 GPU via Google Colab**.

---

## Notes

* Graph is modeled as a bipartite network (users ↔ items)
* Analysis includes:

  * Basic statistics
  * Degree distributions
  * Projection graphs
  * Community detection
* Later stages include GNN-based recommendation (PyTorch Geometric)

---
