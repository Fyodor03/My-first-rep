# import time
# from selenium import webdriver
import lxml
from bs4 import BeautifulSoup
# import pandas as pd
import xlsxwriter

# функция получения html кода страницы
def get_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(
            executable_path = "C:\\Users\\Admin\\Desktop\\питон\\Парсинг\\chromedriver.exe",
            options=options
            )
        driver.get(url=url)
        time.sleep(5)

        # запись html кода в отдельный файл
        with open("catalog_of_iphones_dns_2.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def pars():
    # просмотр html кода из нашего файла
    with open("catalog_of_iphones_dns_2.html", encoding="utf-8") as file:
       src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # парсинг данных
    all_cards = soup.find_all(class_="catalog-product__name ui-link ui-link_black")
    for item in all_cards:
        item_text = item.text
        item_href = item.get("href")
        # print(f"{item_text}: https://dns-shop.ru/{item_href}")
    all_prices = soup.find_all(class_="product-buy__price")
    for i in all_prices:
        i_text = i.text
        # print(i_text)

    # workbook = xlsxwriter.Workbook('catalog_of_iphone.xlsx')
    # worksheet = workbook.add_worksheet()
    # row = 0
    # clumn = 0
    # for ut in i_text:
    #     worksheet.write(row, column, ut)
    #     row += 1
    # workbook.close()
            


   
def save_in_exel():
    fn = "catalog_of_iphone.xlsx"
    # wb = openpyxl.Workbook()
    # wb.save(fn)
    ws = openpyxl.load_workbook(fn)
    wg = ws["Sheet"]
    # wg["A1"] = "Названия"
    # wg["B1"] = "Ссылки"

    for i in item_text:
        wg[2:str(i)] = i
    
    ws.save(fn)
    ws.close()            
    
    

def main():
    # get_data("https://www.dns-shop.ru/search/?q=iphone")
    pars()
    # save_in_exel()
    
if __name__ == "__main__":
    main()


