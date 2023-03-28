from urllib.request import ( urlopen, urlretrieve)
from bs4 import BeautifulSoup
import os

outpath="data/"

htmldata = urlopen('https://www.google.com/search?q=phong+c%E1%BA%A3nh+%C4%91%E1%BA%B9p+vi%E1%BB%87t+nam&sxsrf=AOaemvJqVqfrMfPFVx9U7lOn1MskKWVgyQ:1642174572635&source=lnms&tbm=isch&sa=X&ved=2ahUKEwir-r2AybH1AhWSF4gKHVSGDLUQ_AUoAXoECAEQAw&biw=1280&bih=577&dpr=2')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

for item in images:
    urlretrieve(item["src"], os.path.join(outpath, item["src"].split("/")[-1]))
    print(item['src'])
