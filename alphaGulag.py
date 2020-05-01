from bs4 import BeautifulSoup
import pandas as pd
import requests
import openpyxl

def rower(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")

	# people = []
	# people = soup.findAll('a', class_='story-name')

	fields = []
	fieldstxt = []
	fields = soup.findAll('div', class_='dataEvent')

	for i in range(len(fields)):
		#print(fields[i].text)
		fieldstxt.append(fields[i].text)

	df = pd.DataFrame(data=fieldstxt)
	df = df.T
	return df
	#dframe.append(df)

main_page = requests.get("https://bessmertnybarak.ru/pamyatnik/")
main_soup = BeautifulSoup(main_page.text, "html.parser")
#main_df = pd.DataFrame()
links = []
links = main_soup.findAll('a', class_='story-name')

# writer1 = pd.ExcelWriter('data.xlsx', engine="openpyxl", mode='w')  
# df1 = pd.DataFrame()
# df1.to_excel(writer1, 'Sheet1') 
# writer1.save()

#change range to 100
#writer = pd.ExcelWriter('data.xlsx', engine="openpyxl", mode='a') 
dfw = pd.DataFrame()
for i in range(15):
	dfa = rower("https://bessmertnybarak.ru" + links[i]["href"])
	dfw = dfw.append(dfa)
	print("traceN = ", i)
	print(dfw)

writer = pd.ExcelWriter('data.xlsx', engine="openpyxl", mode='w') 
dfw.to_excel(writer, 'Sheet1') 
writer.save()
	#print("https://bessmertnybarak.ru" + links[i]["href"])
#writer.save()
#print(main_df)

# pageh = requests.get("https://bessmertnybarak.ru/Shalamov_Varlam_/")
# souph = BeautifulSoup(pageh.text, "html.parser")

# heads = []
# headstxt = []
# heads = souph.findAll('div', class_='nameEvent')

# for i in range(len(heads)):
# 	#print(heads[i].text)
# 	headstxt.append(heads[i].text)

# writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')  
# main_df.to_excel(writer, 'Sheet1') 
# writer.save()