import os

import requests
from dotenv import load_dotenv

from download_image import download_image, ensure_dir, parse_file_ext


def fetch_spacex_last_launch(images_directory):
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    decoded_response = response.json()
    spacex_images_urls = decoded_response["links"]["flickr"]["original"]
    for counter, image_url in enumerate(spacex_images_urls, start=1):
        download_image(
            image_url,
            "spacex{}{}".format(counter, parse_file_ext(image_url)),
            images_directory,
        )


def main():
    load_dotenv()

    images_directory = os.getenv("DIRECTORY_FOR_IMAGES")

    ensure_dir(images_directory)

    fetch_spacex_last_launch(images_directory)


if __name__ == "__main__":
    main()
