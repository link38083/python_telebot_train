import requests
from bs4 import BeautifulSoup as BS

r = requests.get("http://japancats.ru/")
html = BS(r.content, "html.parser")
for main_page_brand in html.select(".main > table#brand"):
    brands = main_page_brand.select("a")
    for brand in brands:
        brand_name = brand.text
        brand_link = brand.get("href")
        print(brand_name)
        p = requests.get("http://japancats.ru"+brand_link)
        #print("http://japancats.ru"+brand_link)
        html_brand = BS(p.content, "html.parser")
        for car_title in html_brand.select(".CTreeView, .CGridView > ul"):
            car_titles = car_title.select(".tp, .mp, .bp, .m, .b, .t, .CGridView")
            for car in car_titles:
                if "javascript:submit" in str(car):
                    car_name = "------ " + car.text
                    print(car_name)
                elif "CGridView" in str(car):
                    car_name = "------ " + car.text + " \n"
                    print(car_name)
                else:
                    car_name = "--- " + car.text
                    print(car_name)