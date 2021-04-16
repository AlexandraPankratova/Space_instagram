import os
from urllib.parse import unquote, urlsplit

import requests
from dotenv import load_dotenv
from instabot import Bot
from PIL import Image

load_dotenv()


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


def download_hubble_collection_images(collection_name):
    response = requests.get(
        "http://hubblesite.org/api/v3/images/"+collection_name)
    decoded_response = response.json()
    for image in decoded_response:
        download_hubble_images(image["id"])


def format_images():
    for image in os.listdir("./images"):
        image_to_edit = Image.open("./images/{}".format(image))
        if image_to_edit.height > image_to_edit.width:
            if image_to_edit.height > 1080:
                image_to_edit.thumbnail((image_to_edit.width, 1080))
        else:
            if image_to_edit.width > 1080:
                image_to_edit.thumbnail((1080, image_to_edit.height))
        new_image_name = "./formated_images/{}.jpg".format(
            os.path.splitext(image)[0])
        image_to_edit.convert('RGB').save(new_image_name, format="JPEG")


def upload_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    for counter, image in enumerate(os.listdir("./formated_images")):
        bot.upload_photo(
            "./formated_images/{}".format(image),
            caption="Test upload {}. Let's try this again.".format(counter+1),
        )


def main():
    ensure_dir("./images/")

    download_image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        "hubble.jpeg",
                     )

    fetch_spacex_last_launch()

    download_hubble_images(1)

    download_hubble_collection_images("spacecraft")

    format_images()

    instagram_username = os.getenv("INSTAGRAM_USERNAME")
    instagram_password = os.getenv("PASSWORD")
    upload_to_instagram(instagram_username, instagram_password)


if __name__ == '__main__':
    main()
