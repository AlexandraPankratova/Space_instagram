import os
from urllib.parse import unquote, urlsplit

import requests


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def parse_file_ext(url):
    unquoted_link = unquote(url)
    link = urlsplit(unquoted_link)
    return os.path.splitext(link.path)[1]


def download_image(url, image_name):
    filename = "./images/{}".format(image_name)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    decoded_response = response.json()
    spacex_images_links = decoded_response["links"]["flickr"]["original"]
    for counter, image in enumerate(spacex_images_links):
        download_image(
            image,
            "spacex{}{}".format(counter+1, parse_file_ext(image)),
        )


def main():
    ensure_dir("./images/")

    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
