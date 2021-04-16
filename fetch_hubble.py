import os
from urllib.parse import unquote, urlsplit

import requests


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


def fetch_hubble_images(image_id):
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


def fetch_hubble_collection_images(collection_name):
    response = requests.get(
        "http://hubblesite.org/api/v3/images/"+collection_name)
    decoded_response = response.json()
    for image in decoded_response:
        fetch_hubble_images(image["id"])
