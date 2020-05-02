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
	names = soup.findAll('div', class_='nameEvent')
	allnames = ("Дата рождения:",
"Место рождения:",
"Место проживания:",
"Лагерное управление: ",
"Национальность:",
"Дата ареста:",
"Кем приговорен:",
"Приговор:",
"Книга Памяти:")

	j = 0
	for i in range(len(fields)):
		print(names[i].text)
		if names[i].text in allnames:
			#print(fields[i].text)
			while (j < len(allnames)) and (allnames[j] != names[i].text):
				fieldstxt.append("NA")
				j += 1
			fieldstxt.append(fields[i].text)
			j+=1

	df = pd.DataFrame(data=fieldstxt)
	df = df.T
	return df
	#dframe.append(df)

main_page = requests.get("https://bessmertnybarak.ru/pamyatnik/")
main_soup = BeautifulSoup(main_page.text, "html.parser")
#main_df = pd.DataFrame()
links = []
links = main_soup.findAll('a', class_='story-name')

dfw = pd.DataFrame()
dfw = dfw.append((pd.DataFrame(data=("Дата рождения:",
"Место рождения:",
"Место проживания:",
"Лагерное управление: ",
"Национальность:",
"Дата ареста:",
"Кем приговорен:",
"Приговор:",
"Книга Памяти:"))).T)

for i in range(100):
	dfa = rower("https://bessmertnybarak.ru" + links[i]["href"])
	dfw = dfw.append(dfa)
	print("traceN = ", i)
	print(dfw)
	print("___________________________________________________")

writer = pd.ExcelWriter('data.xlsx', engine="openpyxl", mode='w') 
dfw.to_excel(writer, 'Sheet1') 
writer.save()