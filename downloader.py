from requests import get  # to make GET request


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

base_url = "https://data.cityofnewyork.us/resource/"
extension = "?$limit=100000"
# url = "https://data.cityofnewyork.us/resource/hvrh-b6nb.csv"
# urllib.urlretrieve (url, "file.csv")

with open("exts.txt") as f:
    for line in f:
        line = line.strip()
        url = base_url + line + extension
        with open(line, "wb") as file:
            response = get(url)
            file.write(response.content)