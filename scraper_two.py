import urllib.request
from bs4 import BeautifulSoup

# Website being scraped:
# https://en.wikipedia.org/wiki/List_of_World_Series_champions


def main():
    url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page.read(), "lxml")

    tables = soup.find_all("table", class_="wikitable")

    world_series_table = None

    for table in tables:
        text = table.get_text()

        if "Winning team" in text and "Losing team" in text and "Year" in text:
            world_series_table = table
            break

    if world_series_table is None:
        print("World Series table was not found.")
        return

    rows = world_series_table.find_all("tr")

    for row in rows:
        cells = row.find_all(["th", "td"])

        if len(cells) >= 6:
            year = cells[0].get_text(" ", strip=True)
            winner = cells[1].get_text(" ", strip=True)
            series = cells[3].get_text(" ", strip=True)
            loser = cells[4].get_text(" ", strip=True)

            print("Year:", year)
            print("Winner:", winner)
            print("Series:", series)
            print("Loser:", loser)
            print()


if __name__ == "__main__":
    main()