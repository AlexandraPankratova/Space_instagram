import os
from urllib.parse import urlsplit, unquote

import requests


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def picture_download(url, picture_name):
    filename = "./images/{}".format(picture_name)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    decoded_response = response.json()
    spacex_pictures_links = decoded_response["links"]["flickr"]["original"]
    for counter, picture in enumerate(spacex_pictures_links):
        picture_download(
            picture,
            "spacex{}.jpg".format(counter+1),
        )


def file_ext(url):
    unquoted_link = unquote(url)
    link = urlsplit(unquoted_link)
    return os.path.splitext(link.path)[1]

def main():
    ensure_dir("./images/")

    picture_download(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        "hubble.jpeg",
                     )

    fetch_spacex_last_launch()

    response = requests.get("https://hubblesite.org/api/v3/image/1")
    decoded_response = response.json()
    for file in decoded_response["image_files"]:
        link = file["file_url"]
        print(file_ext(link))


if __name__ == '__main__':
    main()
