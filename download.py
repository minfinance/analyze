import urllib.request

url = 'https://github.com/minfinance/analyze/raw/master/inflation/EC_EI_027.csv'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('tis-620')

f = open('ec_ei_027.csv','w', encoding='utf-8')
f.write(text)
f.close()
