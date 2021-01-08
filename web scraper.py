import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Mwils/Desktop/New folder/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
#driver.quit()

for element in soup.findAll(attrs='blog-card__content-wrapper'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
print(csv_reader)
