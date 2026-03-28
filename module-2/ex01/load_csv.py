import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame | None:
    """
    Loads a CSV file into a Pandas DataFrame and prints its dimensions.
    Returns None if an error occurs.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

    except PermissionError:
        print("Error: You do not have permission to read the file.")
        return None

    except pd.errors.EmptyDataError:
        print("Error: The file is completely empty.")
        return None

    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None
