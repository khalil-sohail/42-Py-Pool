import pandas as pd
def load(path: str, max_rows=60) -> pd.core.frame.DataFrame:
    pd.options.display.max_rows = max_rows
    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df