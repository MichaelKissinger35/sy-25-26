Eddie- Software Developer
Izaiah- QA
Michael-Product/Project Manager


import requests
from bs4 import BeautifulSoup

def scrape_all_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    
    print("Scraping data... please wait.")
    
    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = book.h3.a['title']
            
            price_text = book.find('p', class_='price_color').text
            price = float(price_text.replace('£', ''))
            
            all_books.append({'title': title, 'price': price})

    sorted_books = sorted(all_books, key=lambda x: x['price'], reverse=True)
    return sorted_books

if __name__ == "__main__":
    books = scrape_all_books()
    
    print(f"\nTotal books found: {len(books)}")
    print("-" * 50)
    print(f"{'Price':<10} | {'Book Title'}")
    print("-" * 50)
    
    for book in books[:20]:
        print(f"£{book['price']:<9} | {book['title']}")
