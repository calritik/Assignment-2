import requests
import csv

BASE_URL = "https://anapioficeandfire.com/api/books"
books_dict = {}

url = f"{BASE_URL}?pageSize=50"
while url:
    response = requests.get(url)
    data = response.json()
    
    for book in data:
        book_name = book.get("name", "Unknown")
        books_dict[book_name] = [
            book.get("numberOfPages", ""),
            book.get("released", ""),
            book.get("isbn", ""),
            book.get("publisher", "")
        ]
    
    # Pagination
    link_header = response.headers.get("Link", "")
    url = None
    for part in link_header.split(","):
        if 'rel="next"' in part:
            url = part.split(";")[0].strip().strip("<>")

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["book_name", "pages", "date_of_release", "ISBN", "publisher"])
    for name, details in books_dict.items():
        writer.writerow([name] + details)

print(f" Done! {len(books_dict)} books saved to books.csv")
print("Dictionary preview:", dict(list(books_dict.items())[:2]))