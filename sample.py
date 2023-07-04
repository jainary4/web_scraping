import requests
from bs4 import BeautifulSoup
import soupsieve

def find_string_difference(str1, str2):
    count = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            count += 1
    count += abs(len(str1) - len(str2))  # Consider remaining characters in longer string
    
    return count
def extract_substring(string, start_char, end_char):
    start_index = string.find(start_char) + len(start_char)
    end_index = string.find(end_char, start_index)
    if start_index < end_index:
        return string[start_index:end_index]
    else:
        return ""

url = "https://www.bestbuy.ca/en-ca/collection/lenovo-tablets-on-sale/337159?icmp=top_deals_offer_computing_all_lenovo_tablets_onsale_20230629"


header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15", 
    "X-Amzn-Trace-Id": "Root=1-64a1d4b5-4daad60a3819c29a09f03dad"}


url2= "https://www.amazon.ca/Amazon-Essentials-Regular-Fit-Short-Sleeve-Crewneck/dp/B06XWN8K4N/ref=sr_1_1_ffob_sspa?crid=I0F8ASTJWVGL&keywords=t-shirt&qid=1688329127&sprefix=tshirt%2Caps%2C97&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"



page= requests.get(url,headers=header)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

soup2= BeautifulSoup(soup.prettify(), "html.parser") #this line has all the html code of the webpage url we entered

title = soup2.find("div",{'class': 'productItemName_3IZ3c'}).get_text()
price = soup2.find("div",{"class": 'price_2j8lL medium_1n4Qn salePrice_3B6QJ'})
# Find all <a> elements with the specified class containing the coffee product names

print(title.strip())

html=str(price)
sub= extract_substring(html,"$","<")
print(sub)
