import requests
import re
from bs4 import BeautifulSoup as BS

r = requests.get("http://japancats.ru/Daihatsu/")
html = BS(r.content, "html.parser")
n = 0
for car_title in html.select(".CTreeView > ul"):
    brands = car_title.select(".tp, .mp, .bp, .m, .b, .t")
    for brand in brands:
        if "dF" in str(brand):
            brand_name = "--- "+brand.text
            print(brand_name)
        else:
            brand_name = brand.text
            print(brand_name)