import pandas as pd
import argparse
import os

def convert_parquet_to_json(parquet_path, json_path):
    if not os.path.exists(parquet_path):
        print(f"file '{parquet_path}' not exists.")
        return

    try:
        print(f"reading: {parquet_path}...")
        
        df = pd.read_parquet(parquet_path, engine='pyarrow')
        
        print("read successful:")
        print(df.info())

        to_json_params = {
            'path_or_buf': json_path,
            'orient': 'records',
            'force_ascii': False
        }
        
        to_json_params['lines'] = False
        to_json_params['indent']=4
        print(f"\nwriting: {json_path}...")
        
        df.to_json(**to_json_params)
        
        print("write success!")

    except Exception as e:
        print(f"\nunknown error: {e}")

if __name__ == "__main__":
    input_path = "dapo-math-17k.parquet"
    output_path = "dapo-math-17k.json"
    convert_parquet_to_json(input_path, output_path)
