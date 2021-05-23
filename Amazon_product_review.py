import requests
import pandas as pd
from bs4 import BeautifulSoup

# getting the page address


def get_soup(page):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    url = f"https://www.amazon.co.uk/New-Apple-iPhone-Pro-128GB/product-reviews/B08L5Q84BW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={page}"
    r = requests.get(url, headers = header)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def get_reviews(soup):
    reviews = soup.find_all("div",{"data-hook":"review"})
    for item in reviews:
        product_review={
            "product" : soup.title.text.replace("Amazon.co.uk:Customer reviews", "").strip(),
            "review": item.find("a", {"data-hook":"review-title"}).text.strip(),
            "rating" : float(item.find("i", {"data-hook":"review-star-rating"}).text.replace("out of 5 stars", "").strip()),
            "Customer_names" : item.find("span", class_ = "a-profile-name").text.strip(),
            "review_date" : item.find("span", {"data-hook":"review-date"}).text.replace("Reviewed in the United Kingdom on", "").strip(),
            "body" : item.find("span", {"data-hook":"review-body"}).text.strip(),
            "help" : item.find("span", {"data-hook":"helpful-vote-statement"}).text.replace("people found this helpful","").strip()
            }
        review_list.append(product_review)

review_list = []
for i in range(0,100):
    print(f'getting page,{i}')
    c = get_soup(0)
    get_reviews(c)
    print(len(review_list))

# df = pd.DataFrame(review_list)
# df.to_csv("r.csv", index= False)












# # print(r.text)
# # create the beautiful soup object
# soup = BeautifulSoup(r.content, "html.parser")
# # print(soup.text.title())
#
# # get the reviews
# reviews = soup.find_all("a", class_="review-title-content")
# print(reviews)
