from bs4 import BeautifulSoup
import pandas as pd
import requests

print("Give target URL")
url = input()
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# people = []
# people = soup.findAll('a', class_='story-name')

fields = []
fieldstxt = []
fields = soup.findAll('div', class_='dataEvent')

for i in range(len(fields)):
	print(fields[i].text)
	fieldstxt.append(fields[i].text)

df = pd.DataFrame(data=fieldstxt)
df = df.T
# Specify a writer
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
df.to_excel(writer, 'Sheet1')

# Save the result 
writer.save()