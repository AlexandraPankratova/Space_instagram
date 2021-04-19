import requests

from download_image import download_image, ensure_dir, parse_file_ext


def fetch_hubble_image(image_id):
    response = requests.get(
        "https://hubblesite.org/api/v3/image/{}".format(image_id),
        verify=False,
    )
    response.raise_for_status()
    decoded_response = response.json()
    image_url= decoded_response["image_files"][-1]["file_url"]
    image_extension = parse_file_ext(image_url)
    download_image("https:{}".format(image_url),
                   "{}{}".format(image_id, image_extension),
                   )


def fetch_hubble_collection_images(collection_name):
    response = requests.get(
        "http://hubblesite.org/api/v3/images/"+collection_name)
    decoded_response = response.json()
    for image_info in decoded_response:
        fetch_hubble_image(image_info["id"])


def main():
    ensure_dir("./images")
    fetch_hubble_image(1)
    fetch_hubble_collection_images("spacecraft")


if __name__ == '__main__':
    main()
