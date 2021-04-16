import os

from dotenv import load_dotenv
from instabot import Bot
from PIL import Image

from fetch_hubble import fetch_hubble_collection_images, fetch_hubble_images
from fetch_spacex import fetch_spacex_last_launch

load_dotenv()


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def format_images():
    ensure_dir("./formated_images")
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

    fetch_spacex_last_launch()

    fetch_hubble_images(1)

    fetch_hubble_collection_images("spacecraft")

    format_images()

    instagram_username = os.getenv("INSTAGRAM_USERNAME")
    instagram_password = os.getenv("INSTAGRAM_PASSWORD")
    upload_to_instagram(instagram_username, instagram_password)


if __name__ == '__main__':
    main()
