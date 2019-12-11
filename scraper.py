import requests
import time
import random
import logging
from bs4 import BeautifulSoup

max_pages = 26120
min_sleep = 0.5
max_sleep = 2.5

logging.basicConfig(filename='application.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

for i in range(1, max_pages + 1):
    out_file = str.format("out/{}.links", i)
    logging.info("Opening " + out_file)
    with open(out_file) as fp:
        for cnt, line in enumerate(fp):
            logging.info("\tGetting from " + line.strip())
            text = requests.get(line.strip()).text
            soup = BeautifulSoup(text, features="html.parser")
            code_snippets = soup.findAll("code")
            sleep_time = (random.random() * (max_sleep - min_sleep)) + min_sleep
            logging.info(f'\tSleeping for %f seconds', sleep_time)
            time.sleep(sleep_time)
