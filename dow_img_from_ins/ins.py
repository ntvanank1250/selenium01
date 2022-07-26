from __future__ import barry_as_FLUFL
from random import random
import time
import requests # to get image from the url
import shutil # to save it locally in system
import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver


def main(user_name,folder_name):
    # get all images
    imgs = get_all_images(user_name)
    print(imgs)
    
    # for img in imgs:
    #     # for each image, download it
    #     download(img, folder_name)

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(user_name):
    """
    Returns all image URLs on a single `url`
    """

    insta_url = 'https://www.instagram.com'
    inta_username = user_name

    url = f"{insta_url}/{inta_username}/"
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=chrome_options)

    driver.get(url)

    soup = BeautifulSoup(driver.page_source)
    
    urls = list()
    for img in soup.findAll('a', {'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd'}):
        img_url = img.attrs.get("href")
        if is_valid(img_url):
            urls.append(img_url)


    # soup = bs(requests.get(f"{insta_url}/{inta_username}/",verify=False).text, "html.parser")
    # print(soup)
    # urls = list()

    # for img in tqdm(soup.find_all("shortcode"), "Extracting images"):
    #     print(img)
    #     img_url = img.attrs.get("href")
    #     print(12334)
    #     print(img_url)
    #     if not img_url:
    #         # if img does not contain src attribute, just skip
    #         continue
    # # # make the URL absolute by joining domain with the URL that is just extracted
    # #     img_url = urljoin(url, img_url)
    # #     try:
    # #         pos = img_url.index("?")
    # #         img_url = img_url[:pos]
    # #     except ValueError:
    # #         pass
    # #     # finally, if the url is valid
        # if is_valid(img_url):
        #     urls.append(img_url)
    return(urls)

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    if file_size < 1024 * 100:
        return
   

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
use_name = "quynhphuongmai.430"
folder_name = 'ins01'
main(use_name,folder_name)