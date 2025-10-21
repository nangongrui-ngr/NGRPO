import pandas as pd
import os

def convert_json_to_parquet(json_path, parquet_path):
    if not os.path.exists(json_path):
        print(f"file '{json_path}' not exists.")
        return

    try:
        print(f"reading: {json_path}...")
        df = pd.read_json(json_path)
        
        print("read successful:")
        print(df.info())
        
        print(f"\nwriting parquet 文件: {parquet_path}...")
        
        df.to_parquet(parquet_path, engine='pyarrow', index=False)
        
        print("\nwrite success!")
    except Exception as e:
        print(f"\nunknown error: {e}")

if __name__ == "__main__":
    input_path = "dapo-math-17k.json"
    output_path = "dapo-math-17k.parquet"
    convert_json_to_parquet(input_path, output_path)
