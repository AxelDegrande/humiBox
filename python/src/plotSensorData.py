"""Plot temperature and humidity over time from a sensor CSV.

Reads ../../data/measurements.csv (relative to this script) and only plots data
from the current day (the day the script is run). The plot is saved in the
same ../../data folder as plot.png (overwritten on each run).

Expected columns: time, temperature (typo "temerature" also works), humidity, status

Usage:
    python plot_sensor.py
    python plot_sensor.py --keep-errors   # don't drop status == error rows

Requires: pandas, matplotlib  (pip install pandas matplotlib)
"""

import argparse
import sys
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"  # ../../data
CSV_FILE = DATA_DIR / "measurements.csv"


def find_column(df, prefix):
    """Find a column whose name starts with the given prefix (case-insensitive)."""
    for col in df.columns:
        if col.strip().lower().startswith(prefix):
            return col
    sys.exit(f"Error: no column starting with '{prefix}'. Found: {list(df.columns)}")


def main():
    p = argparse.ArgumentParser(description="Plot today's temperature and humidity.")
    p.add_argument("--keep-errors", action="store_true",
                   help="Keep rows where status is 'error' (they are dropped by default)")
    args = p.parse_args()

    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {CSV_FILE}")

    df.columns = df.columns.str.strip()
    time_col = find_column(df, "time")
    temp_col = find_column(df, "tem")
    hum_col = find_column(df, "hum")

    df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
    df = df.dropna(subset=[time_col]).sort_values(time_col)

    # Only keep rows from today (the day the script is run, in local time)
    today = pd.Timestamp.now().date()
    df = df[df[time_col].dt.date == today]
    if df.empty:
        sys.exit(f"Error: no data found for today ({today}).")

    # Rows with status "error" (e.g. 0 / 0 readings) are sensor failures, not real data
    n_errors = 0
    if "status" in df.columns and not args.keep_errors:
        is_error = df["status"].astype(str).str.strip().str.lower() == "error"
        n_errors = int(is_error.sum())
        df = df[~is_error]

    if df.empty:
        sys.exit("Error: no valid rows left to plot.")

    fig, (ax_t, ax_h) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    ax_t.plot(df[time_col], df[temp_col], marker="o", color="tab:red")
    ax_t.set_ylabel("Temperature (C)")
    ax_t.grid(True, alpha=0.3)

    ax_h.plot(df[time_col], df[hum_col], marker="o", color="tab:blue")
    ax_h.set_ylabel("Humidity (%)")
    ax_h.set_xlabel("Time")
    ax_h.grid(True, alpha=0.3)

    ax_h.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    fig.autofmt_xdate()

    title = f"Temperature and humidity - {today}"
    if n_errors:
        title += f"  ({n_errors} error row{'s' if n_errors != 1 else ''} excluded)"
    fig.suptitle(title)
    fig.tight_layout()

    out_file = DATA_DIR / "plot.png"
    fig.savefig(out_file, dpi=150)
    print(f"Saved plot to {out_file}")


if __name__ == "__main__":
    main()