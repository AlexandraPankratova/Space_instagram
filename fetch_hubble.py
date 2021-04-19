import requests

from download_image import download_image, ensure_dir, parse_file_ext


def fetch_hubble_image(image_id):
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
        fetch_hubble_image(image["id"])


def main():
    ensure_dir("./images")
    fetch_hubble_image(1)
    fetch_hubble_collection_images("spacecraft")


if __name__ == '__main__':
    main()
