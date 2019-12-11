import requests
import random
import logging
import time
from bs4 import BeautifulSoup

url_base = "https://stackoverflow.com"
url_unencoded = "https://stackoverflow.com/questions/tagged/python?tab=votes&page={}&pagesize=50"
max_pages = 26120
min_sleep = 0.5
max_sleep = 2.5
logging.basicConfig(filename='links.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

for i in range(1, max_pages + 1):
    url_encoded = str.format(url_unencoded, i)
    logging.info("Getting from " + url_encoded)
    raw = requests.get(url_encoded).text
    soup = BeautifulSoup(raw, features="html.parser")
    questions = soup.find("div", {"id": "questions"})
    links = questions.findAll("a", {"class": "question-hyperlink"}, href=True)

    logging.info(f'\tFound %d links', len(links))
    out_file = str.format("out/{}.links", i)
    file = open(out_file, "w+")
    for link in links:
        file.write(url_base + link['href'] + "\n")

    sleep_time = (random.random() * (max_sleep - min_sleep)) + min_sleep
    logging.info(f'\tSleeping for %f seconds', sleep_time)
    time.sleep(sleep_time)
