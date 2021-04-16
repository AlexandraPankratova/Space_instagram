import os
from urllib.parse import urlsplit, unquote

import requests


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


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


def parse_file_ext(url):
    unquoted_link = unquote(url)
    link = urlsplit(unquoted_link)
    return os.path.splitext(link.path)[1]


def download_hubble_images(image_id):
    response = requests.get(
        "https://hubblesite.org/api/v3/image/{}".format(image_id),
        verify=False,
    )
    response.raise_for_status()
    decoded_response = response.json()
    image_link = decoded_response["image_files"][-1]["file_url"]
    images_extensions = parse_file_ext(image_link)
    download_image("https:{}".format(image_link),
                   "{}{}".format(image_id, images_extensions),
                   )


def main():
    ensure_dir("./images/")

    download_image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        "hubble.jpeg",
                     )

    fetch_spacex_last_launch()

    download_hubble_images(1)


if __name__ == '__main__':
    main()
