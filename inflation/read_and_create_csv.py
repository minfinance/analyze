import csv
import itertools
import urllib.request

url = 'https://github.com/minfinance/analyze/raw/master/inflation/EC_EI_027.csv'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('tis-620').replace('\0','')

csv_lines = csv.reader(text.split('\n'))

content = itertools.islice(csv_lines, 5, None)
years_text = next(content)

years = [ int(year[:4]) - 543 for year in years_text[2:]]

inflation_gen = itertools.dropwhile(lambda l:len(l) >= 2 and "ดัชนีราคาผู้บริโภคทั่วไป" not in l[1], content)

def convert_na(x):
  return x if x != 'n.a.' else ''

headline_cpi = next(inflation_gen)[2:]
headline_cpi_delta = next(inflation_gen)[2:]
core_cpi = map(convert_na, next(inflation_gen)[2:])
core_cpi_delta = map(convert_na, next(inflation_gen)[2:])

writing_content = zip(years, headline_cpi, headline_cpi_delta, core_cpi, core_cpi_delta)

with open('thailand_cpi_2017.csv','w') as out_csv:
  writer = csv.writer(out_csv)
  writer.writerow(['Year','Headline CPI', 'Headline CPI Delta', 'Core CPI', 'Core CPI Delta'])
  for l in writing_content:
    writer.writerow(l)
