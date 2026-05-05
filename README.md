# Assignment-2

##  Project Structure

​```
├── q1_houses.py
├── q2_books.py
├── q3_characters.py
├── houses.txt
├── books.csv
├── characters.xlsx
└── README.md
​```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| `requests` | Fetching data from API |
| `csv` | Writing CSV files |
| `openpyxl` | Creating Excel (.xlsx) files |

---

##  Installation

​```bash
pip install requests openpyxl
​```

---

##  How to Run

​```bash
python q1_houses.py       # Generates houses.txt
python q2_books.py        # Generates books.csv
python q3_characters.py   # Generates characters.xlsx
​```

---

##  Output Files

| File | Question | Description |
|------|----------|-------------|
| `houses.txt` | Q1 | All houses with regions, sorted alphabetically |
| `books.csv` | Q2 | Book name, pages, release date, ISBN, publisher |
| `characters.xlsx` | Q3 | Characters sorted by number of TV season appearances |

---

##  API Reference

- Houses: https://anapioficeandfire.com/api/houses  
- Books: https://anapioficeandfire.com/api/books  
- Characters: https://anapioficeandfire.com/api/characters  
