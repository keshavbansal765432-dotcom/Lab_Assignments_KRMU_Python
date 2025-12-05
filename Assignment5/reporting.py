# reporting.py
def save_outputs(df_cleaned, building_summary, daily_df, weekly_df, output_dir="output"):
    import os
    os.makedirs(output_dir, exist_ok=True)

    df_cleaned.to_csv(f"{output_dir}/cleaned_energy_data.csv", index=False)
    building_summary.to_csv(f"{output_dir}/building_summary.csv", index=False)

    total_consumption = df_cleaned['kwh'].sum()
    top_building_row = building_summary.sort_values('sum', ascending=False).iloc[0]
    top_building = top_building_row['building']
    peak_row = df_cleaned.sort_values('kwh', ascending=False).iloc[0]
    peak_time = peak_row['timestamp']

    with open(f"{output_dir}/summary.txt", "w") as f:
        f.write(f"Total campus consumption: {total_consumption} kWh\n")
        f.write(f"Highest-consuming building: {top_building}\n")
        f.write(f"Peak load time: {peak_time}\n")
        # add 2–3 lines describing trends
