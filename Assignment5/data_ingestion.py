from pathlib import Path
import pandas as pd

def load_energy_data(data_dir="data"):
    data_path = Path(data_dir)
    all_dfs = []

    for csv_file in data_path.glob("*.csv"):
        try:
            df = pd.read_csv(csv_file, on_bad_lines="skip")

            # ensure expected cols exist
            # df should already have 'timestamp' and 'kwh'

            # derive building + month from filename, e.g. building_a_jan.csv
            name = csv_file.stem  # "building_a_jan"
            parts = name.split("_")  # ["building", "a", "jan"]

            if len(parts) >= 3:
                building_code = parts[1]        # "a"
                month_name = parts[2]           # "jan"
            else:
                building_code = name
                month_name = ""

            df["building"] = f"Building_{building_code.upper()}"
            df["month"] = month_name.capitalize()

            all_dfs.append(df)

        except FileNotFoundError:
            print(f"Missing file: {csv_file}")
        except Exception as e:
            print(f"Error in {csv_file}: {e}")

    if not all_dfs:
        return pd.DataFrame()

    df_combined = pd.concat(all_dfs, ignore_index=True)
    return df_combined
