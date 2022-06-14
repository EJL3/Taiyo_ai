from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

url = "https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

ps = soup.get_text()

with open('contracts.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(('title', 'intro', 'tagline'))
    writer.writerow(ps)
    print("Successful conversion")