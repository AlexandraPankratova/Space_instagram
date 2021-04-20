# Space Instagram

This project allow you to download pictures from following sources:
- `SpaceX`
- `Hubble images`
- `Hubble collections`

And upload them to your instagram account.

### How to install

1. Download code.
2. Python3 should be already installed.
3. Create virtual environment using `venv`:
```bash
python3 -m venv your_virtual_env_name
```
4. Activate virtual environment:
```bash
source your_virtual_env_name/bin/activate
```

5. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```
6. Now you need to create file `.env`. It should look like this:
```
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
DIRECTORY_FOR_IMAGES=./images/
DIRECTORY_FOR_FORMATTED_IMAGES=./formatted_images
```
### How to run
1. You need to download images from `SpaceX`:
```bash
python3 fetch_spacex.py
```
2. Then you need to download images and collection from `Hubble`:
```bash
python3 fetch_hubble.py
```
3. Finally you need to format images and upload them to your instagram account:
```bash
python3 main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).