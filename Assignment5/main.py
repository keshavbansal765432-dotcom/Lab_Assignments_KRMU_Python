# main.py
import pandas as pd
from data_ingestion import load_energy_data
from analysis import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from visualization import create_dashboard
from reporting import save_outputs
from models import BuildingManager

def main():
    
    df = load_energy_data("data")
    print(df.columns)   # debug line
    print(df.head())    # debug line

    if df.empty:
        print("No data loaded.")
        return

    # ensure timestamp is datetime and set index
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    df = df.set_index('timestamp')

    daily_df = calculate_daily_totals(df)
    weekly_df = calculate_weekly_aggregates(df)
    summary_df = building_wise_summary(df)

    manager = BuildingManager()
    manager.add_from_dataframe(df.reset_index())

    create_dashboard(daily_df, weekly_df, summary_df)
    save_outputs(df.reset_index(), summary_df, daily_df, weekly_df)

if __name__ == "__main__":
    main()
