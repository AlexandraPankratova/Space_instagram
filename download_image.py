import os
from urllib.parse import unquote, urlsplit

import requests
from dotenv import load_dotenv

load_dotenv()
images_directory = os.getenv("DIRECTORY_FOR_IMAGES")


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def parse_file_ext(url):
    unquoted_url = unquote(url)
    parsed_url = urlsplit(unquoted_url)
    return os.path.splitext(parsed_url.path)[1]


def download_image(url, image_name):
    file_name = "{}{}".format(images_directory, image_name)

    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)
