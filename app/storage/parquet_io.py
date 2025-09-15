from pathlib import Path

import pandas as pd

BASE_DIR = Path("data")


def write_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def append_by_concat(df_new: pd.DataFrame, path: Path) -> None:
    if path.exists():
        df_old = pd.read_parquet(path)
        df = pd.concat([df_old, df_new], axis=0, ignore_index=True)
        df = df.drop_duplicates(subset=["time"], keep="last")
    else:
        df = df_new.copy()
    write_parquet(df, path)
