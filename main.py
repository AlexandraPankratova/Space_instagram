import os

from dotenv import load_dotenv
from instabot import Bot
from PIL import Image

load_dotenv()


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def format_images():
    ensure_dir("./formated_images")
    max_image_dimension = 1080
    for image_name in os.listdir("./images"):
        image_to_edit = Image.open("./images/{}".format(image_name))
        if image_to_edit.height > max_image_dimension \
                or image_to_edit.width > max_image_dimension:
            image_to_edit.thumbnail((max_image_dimension, max_image_dimension))
        new_image_path = "./formated_images/{}.jpg".format(
            os.path.splitext(image_name)[0])
        image_to_edit.convert('RGB').save(new_image_path, format="JPEG")


def upload_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    for counter, image in enumerate(os.listdir("./formated_images"), start=1):
        bot.upload_photo(
            "./formated_images/{}".format(image),
            caption="Test upload {}. Let's try this again.".format(counter),
        )


def main():
    format_images()

    instagram_username = os.getenv("INSTAGRAM_USERNAME")
    instagram_password = os.getenv("INSTAGRAM_PASSWORD")
    upload_to_instagram(instagram_username, instagram_password)


if __name__ == '__main__':
    main()
