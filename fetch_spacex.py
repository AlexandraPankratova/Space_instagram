import requests

from download_image import download_image, ensure_dir, parse_file_ext


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    decoded_response = response.json()
    spacex_images_urls = decoded_response["links"]["flickr"]["original"]
    for counter, image_url in enumerate(spacex_images_urls, start=1):
        download_image(
            image_url,
            "spacex{}{}".format(counter, parse_file_ext(image_url)),
        )


def main():
    ensure_dir("./images/")

    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
