"""Rebuild data/combined_categories.csv from the 100 raw category files.

Usage:  python scripts/combine_data.py
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"

files = sorted((DATA / "raw").glob("pis_*.csv"), key=lambda f: int(f.stem.split("_")[1]))
df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

print(f"{len(files)} files -> {len(df)} rows, {df['category'].nunique()} categories, "
      f"{df['clicks'].isna().sum()} missing clicks")
df.to_csv(DATA / "combined_categories.csv", index=False, lineterminator="\n")
