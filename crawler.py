from bs4 import BeautifulSoup
import requests
import json

 
# 指定要抓取的網頁URL
url = "http://eureka.didispace.com/"
 
# 使用requests.get() 來得到網頁回傳內容
r = requests.get(url)
 
# request.get()回傳的是一個物件 
# 若抓成功(即r.status_code==200), 則網頁原始碼會放在物件的text屬性, 我們把它存在一個變數 'web_content'
web_content = r.text

 
# 以 Beautiful Soup 解析 HTML 程式碼 : 
soup = BeautifulSoup(web_content, 'html.parser')
 
# 找出所有class為"board-name"的div elements


#---------------------------------------------------------------------#
rows = soup.find_all('table', id='instances')[2].tbody.find_all('tr')

for row in rows:
	all_tds = row.find_all('td')
	#print (all_tds[0].text.split(), all_tds[1].text.split(), all_tds[2].text.split(), all_tds[3].text.split())

	print (all_tds[1].text.split()[1])
	print (all_tds[2].text.split()[0])
	print (all_tds[3].text.split()[1])

	if all_tds[1].text.split()[1] == all_tds[2].text.split()[0] == all_tds[3].text.split()[1]:
		print (all_tds[0].text.split())


#---------------------------------------------------------------------#

#head_list = []

#for i in range(len(soup.find_all('table', id='instances')[2].thead.find_all('th'))):

	#head = soup.find_all('table', id='instances')[2].thead.find_all('th')[i].text

	#head_list.append(head)

#print (head_list)


#body_list = []

#for i in range(len(soup.find_all('table', id='instances')[2].tbody.find_all('td'))):

	#body = soup.find_all('table', id='instances')[2].tbody.find_all('td')[i].text.split()

	#if body != '-' or body != ',':

		#body_list.append(body)



#python2json = {}

#python2json["body_list"] = body_list

#json_str = json.dumps(python2json)
#print (json_str)
