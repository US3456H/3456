#!/usr/bin/env python3
"""
parse_and_stats.py
Usage:
  python scripts/parse_and_stats.py data/example_data.csv --out stats --recent-window 10

Produces:
 - stats/summary.json
 - stats/number_frequency.csv
 - stats/frequency.png (柱状图)
"""
import sys
import json
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path, parse_dates=['draw_date'])
    # Ensure numeric columns n1..n6 exist
    nums = [c for c in df.columns if c.startswith('n')]
    if len(nums) < 1:
        raise SystemExit("CSV must contain columns like n1,n2,...")
    return df.sort_values('draw_date', ascending=True), nums

def number_frequency(df, nums):
    # Flatten all number columns into one series and count
    s = pd.Series(df[nums].values.ravel())
    freq = s.value_counts().sort_index()
    return freq

def recent_counts(df, nums, window):
    recent = df.tail(window)
    s = pd.Series(recent[nums].values.ravel())
    return s.value_counts().sort_index()

def omissions(df, nums, max_number=50):
    # current omission: distance since last appearance
    # build last index map
    all_draws = df.reset_index(drop=True)
    last_seen = {}
    for idx, row in all_draws.iterrows():
        for c in nums:
            val = int(row[c])
            last_seen[val] = idx
    total = len(all_draws)
    omissions = {}
    # assume numbers in range 1..max_number
    for n in range(1, max_number+1):
        if n in last_seen:
            omissions[n] = total - 1 - last_seen[n]
        else:
            omissions[n] = total  # never seen
    return omissions

def value_sum_stats(df, nums):
    sums = df[nums].sum(axis=1)
    return {
        'mean': float(sums.mean()),
        'median': float(sums.median()),
        'min': int(sums.min()),
        'max': int(sums.max()),
        'hist': sums.value_counts().sort_index().to_dict()
    }

def save_outputs(outdir, freq, omissions_map, summary, freq_png=True):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    freq_df = freq.rename_axis('number').reset_index(name='count')
    freq_df.to_csv(outdir / 'number_frequency.csv', index=False)
    with open(outdir / 'summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    if freq_png:
        plt.figure(figsize=(10,5))
        freq.sort_index().plot(kind='bar')
        plt.title('Number Frequency')
        plt.xlabel('Number')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(outdir / 'frequency.png', dpi=150)
        plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', help='input CSV file (draw_date,draw_no,n1..n6)')
    parser.add_argument('--out', default='stats', help='output directory')
    parser.add_argument('--recent-window', type=int, default=10, help='last N draws to consider for hot/cold')
    parser.add_argument('--max-number', type=int, default=50, help='maximum possible number (for omissions)')
    args = parser.parse_args()

    df, nums = load_data(args.csv)
    total_draws = len(df)
    freq = number_frequency(df, nums)
    recent = recent_counts(df, nums, args.recent_window)
    omissions_map = omissions(df, nums, args.max_number)
    sums_stats = value_sum_stats(df, nums)

    summary = {
        'total_draws': total_draws,
        'numbers_columns': nums,
        'freq_top10': freq.sort_values(ascending=False).head(10).to_dict(),
        'recent_top10': recent.sort_values(ascending=False).head(10).to_dict(),
        'omissions_sample': {k: omissions_map[k] for k in list(omissions_map)[:20]},
        'sums_stats': sums_stats
    }

    save_outputs(args.out, freq, omissions_map, summary)
    print("Done. Outputs written to:", args.out)

if __name__ == '__main__':
    main()
