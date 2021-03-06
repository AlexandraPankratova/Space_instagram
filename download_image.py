import os
from urllib.parse import unquote, urlsplit

import requests


def ensure_dir(dir_name):
    os.makedirs(dir_name, exist_ok=True)


def parse_file_ext(url):
    unquoted_url = unquote(url)
    parsed_url = urlsplit(unquoted_url)
    return os.path.splitext(parsed_url.path)[1]


def download_image(url, image_name, images_directory):
    file_name = "{}{}".format(images_directory, image_name)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(file_name, "wb") as file:
        file.write(response.content)
