import requests
import os

def ensure_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def main():
    ensure_dir("./images/")
    filename = "./images/hubble.jpeg"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)



if __name__ == '__main__':
    main()


