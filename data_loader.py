import pandas as pd

def data_loader(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

books_df = data_loader(r"data/books.csv")
print(books_df.shape)
print(books_df.head())
