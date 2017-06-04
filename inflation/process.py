import csv
import itertools

with open('EC_EI_027.csv', encoding="tis-620") as f:
  csv_reader = csv.reader(f)
  content = itertools.dropwhile(lambda x: len(x) <= 1, csv_reader)
  header = next(content)
  
  print(header)

  for r in content:
    if(len(r) > 0):
      print(r[1])