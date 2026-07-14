import csv

from permutation_distribution import *

grouped_teams = {}

with open("dragon_soul_data.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  
  next(reader)  # skip header
  
  rows = [
    (row[0] == "True", int(row[1]))
    for row in reader
  ]

mixed_sample = [row[0] for row in rows]

soul_sample = [row[0] for row in rows if row[1] >= 4]
soul_winrate = sum(soul_sample) / len(soul_sample)
print(f"{soul_winrate=}")
print(f"{len(soul_sample)=}")

print()

soulless_sample = [row[0] for row in rows if row[1] < 4]
soulless_winrate = sum(soulless_sample) / len(soulless_sample)
print(f"{soulless_winrate=}")
print(f"{len(soulless_sample)=}")


def wr_difference(soul_sample, soulless_sample):
  soul_winrate = sum(soul_sample) / len(soul_sample)
  soulless_winrate = sum(soulless_sample) / len(soulless_sample)
  
  return soul_winrate - soulless_winrate


dist = permutation_distribution(
  mixed_sample,
  wr_difference,
  len(soulless_sample)
)

significant_val = significant_value(dist, top_percentile=100 - 5/3)

print("wr difference needed to be significant:", significant_val)
print("observed wr difference:", soul_winrate - soulless_winrate)

print()

print("""
since we are well over the required significant value,
we may reject the null hypothesis
""")