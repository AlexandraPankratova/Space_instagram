import requests

from download_image import download_image, ensure_dir, parse_file_ext


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
