# visualization.py
import matplotlib.pyplot as plt

def create_dashboard(daily_df, weekly_df, building_summary, output_path="output/dashboard.png"):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # 1) Trend line
    axes[0].plot(daily_df['timestamp'], daily_df['kwh'])
    axes[0].set_title("Daily Campus Consumption")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("kWh")

    # 2) Bar chart by building using building_summary
    axes[1].bar(building_summary['building'], building_summary['mean'])
    axes[1].set_title("Average Usage by Building")
    axes[1].set_xlabel("Building")
    axes[1].set_ylabel("Average kWh")

    # 3) For scatter, you can use hourly or daily peak values
    # placeholder: axes[2].scatter(...)

    fig.tight_layout()
    fig.savefig(output_path)
