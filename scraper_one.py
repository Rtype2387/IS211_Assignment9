import urllib.request
from bs4 import BeautifulSoup

# Website being scraped:
# https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions


def main():
    url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page.read(), "lxml")

    tables = soup.find_all("table", class_="wikitable")

    super_bowl_table = None

    for table in tables:
        if "Winning team" in table.get_text() and "Losing team" in table.get_text():
            super_bowl_table = table
            break

    if super_bowl_table is None:
        print("Super Bowl table was not found.")
        return

    rows = super_bowl_table.find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 6:
            game = cells[0].get_text(" ", strip=True)
            date = cells[1].get_text(" ", strip=True)
            winner = cells[2].get_text(" ", strip=True)
            winning_score = cells[3].get_text(" ", strip=True)
            loser = cells[4].get_text(" ", strip=True)
            losing_score = cells[5].get_text(" ", strip=True)

            print("Super Bowl:", game)
            print("Date:", date)
            print("Winner:", winner)
            print("Winning Score:", winning_score)
            print("Loser:", loser)
            print("Losing Score:", losing_score)
            print()


if __name__ == "__main__":
    main()