import requests
import os


def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def picture_download(url, picture_name):
    filename = "./images/{}".format(picture_name)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()
    decoded_response = response.json()
    spacex_pictures_links = decoded_response["links"]["flickr"]["original"]
    for counter, picture in enumerate(spacex_pictures_links):
        picture_download(
            picture,
            "spacex{}.jpg".format(counter+1),
        )


def main():
    ensure_dir("./images/")
    picture_download(
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
        "hubble.jpeg",
                     )
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
