import pandas as pd
import os


# Save df if does not exist
csv_file_path = '/Users/ajaykallepalli/data/SQL_df.csv'
if not os.path.exists(csv_file_path):
    splits = {'train': 'spider/train-00000-of-00001.parquet', 'validation': 'spider/validation-00000-of-00001.parquet'}
    df_train = pd.read_parquet("hf://datasets/xlangai/spider/" + splits["train"])
    df_train.to_csv(csv_file_path, index=False)
    print("Downloaded data")
else:
    print("Already downloaded")

print()