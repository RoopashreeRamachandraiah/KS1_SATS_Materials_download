import requests
from bs4 import BeautifulSoup
import os

url = "https://www.gov.uk/government/collections/national-curriculum-assessments-practice-materials#key-stage-1-past-papers"
baseurl="https://www.gov.uk"

response = requests.get(url)
 
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
 
# Find all hyperlinks present on webpage
links = soup.find_all('a')

cwd=os.getcwd()

os.mkdir(cwd+'/'+'Materials')

path= cwd+'/Materials/'
 
i = 0

urls=[]
 
# From all links check for pdf link and
# if present download file
for link in links:
    if ('key-stage-1' in link.get('href')):
        #print(link.get('href'))
        urls.append(baseurl+link.get('href'))

#print(urls)
for each_url in urls:
    response=requests.get(each_url)
    soup1=BeautifulSoup(response.text, 'html.parser')

    material_links=soup1.find_all('a')
    print('material_links')
    print(material_links)


    for m_link in material_links:
        if ('.pdf' in m_link.get('href')):
            i+=1
            response = requests.get(m_link.get('href'))
            name=m_link.get('href').split('/')[-1]
            parts=name.split('_')
            if parts[0] == '2023' or parts[0] == '2022' or parts[0] ==  '2019':
                folder='_'.join(parts[:6])
            else:
                folder='_'.join(parts[1:4])
            if not os.path.exists(path+folder):
                os.mkdir(path+folder)
            pdf = open(path+folder+'/'+name+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", i, " downloaded")


