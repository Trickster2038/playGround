from bs4 import BeautifulSoup
import pandas as pd
import requests

def rower(dframe,url):
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
	dframe.append(df)

main_page = requests.get("https://bessmertnybarak.ru/pamyatnik/")
main_soup = BeautifulSoup(main_page.text, "html.parser")
main_df = pd.DataFrame()
links = []
links = main_soup.findAll('a', class_='story-name')

for i in range(100):
	rower(main_df, "https://bessmertnybarak.ru" + links[i]["href"])
	print("https://bessmertnybarak.ru" + links[i]["href"])


pageh = requests.get("https://bessmertnybarak.ru/Shalamov_Varlam_/")
souph = BeautifulSoup(pageh.text, "html.parser")

# people = []
# people = soup.findAll('a', class_='story-name')

headss = []
headstxt = []
heads = souph.findAll('div', class_='nameEvent')

for i in range(len(heads)):
	print(heads[i].text)
	headstxt.append(heads[i].text)


# print("Give target URL")
# url = input()



# Specify a writer
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
main_df.to_excel(writer, 'Sheet1', header = headstxt)

# Save the result 
writer.save()