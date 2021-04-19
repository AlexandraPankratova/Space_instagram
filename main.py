import os

from dotenv import load_dotenv
from instabot import Bot
from PIL import Image

load_dotenv()
images_directory = os.getenv("DIRECTORY_FOR_IMAGES")
formated_images_directory = os.getenv("DIRECTORY_FOR_FORMATED_IMAGES")


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def format_images():
    ensure_dir("{}".format(formated_images_directory))
    max_image_dimension = 1080
    for image_name in os.listdir("{}".format(images_directory)):
        image_to_edit = Image.open("{}{}".format(images_directory, image_name))
        if image_to_edit.height > max_image_dimension \
                or image_to_edit.width > max_image_dimension:
            image_to_edit.thumbnail((max_image_dimension, max_image_dimension))
        new_image_path = "{}/{}.jpg".format(
            formated_images_directory,
            os.path.splitext(image_name)[0])
        image_to_edit.convert('RGB').save(new_image_path, format="JPEG")


def upload_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    for counter, image in enumerate(
            os.listdir("{}".format(formated_images_directory)),
            start=1):
        bot.upload_photo(
            "{}/{}".format(formated_images_directory, image),
            caption="Test upload {}. Let's try this again.".format(counter),
        )


def main():
    format_images()

    instagram_username = os.getenv("INSTAGRAM_USERNAME")
    instagram_password = os.getenv("INSTAGRAM_PASSWORD")
    upload_to_instagram(instagram_username, instagram_password)


if __name__ == '__main__':
    main()
