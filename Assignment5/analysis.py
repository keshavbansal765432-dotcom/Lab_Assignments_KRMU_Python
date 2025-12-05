# analysis.py
import pandas as pd

def calculate_daily_totals(df):
    # assumes df has timestamp as datetime and index
    daily = df.resample('D')['kwh'].sum().reset_index()
    return daily

def calculate_weekly_aggregates(df):
    weekly = df.resample('W')['kwh'].sum().reset_index()
    return weekly

def building_wise_summary(df):
    summary = df.groupby('building')['kwh'].agg(['mean', 'min', 'max', 'sum']).reset_index()
    return summary
