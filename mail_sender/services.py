import json
import datetime
import sys
import requests
import os
import mail_sender
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def newsService(count=5):
    path = os.path.dirname(mail_sender.__file__)
    # print(path)
    f = open(os.path.join(path, "apis.txt"), "r")
    api = f.readlines()
    today = datetime.date.today()
    today = today.strftime("%A, %B %d, %Y")
    app_id = api[5].split(":")[1].strip()
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + app_id
    final_data = "fresh news of {}.\n".format(today)
    r = requests.get(url)
    data = json.loads(r.content)
    news = data["articles"]
    for i in range(count):
        thistitle = "{}. {}\n".format(i, news[i]["title"])
        final_data += thistitle

    final_data += "God bye for today, see you again next day."
    print(final_data)
    return final_data


def keep_awake_site(url):
    try:
        print("requesting url : "+bcolors.UNDERLINE+bcolors.OKBLUE+url+bcolors.ENDC)
        start_time = time.time()
        r = requests.get(url)
        print("Site loading time {} seconds.".format(round((time.time() - start_time), 3)))
        if r.status_code != 200:
            print(bcolors.FAIL + "some error occured with status ========> " + str(r.status_code) + bcolors.ENDC)
        else:
            print(bcolors.OKCYAN + "Website is Up with status =========> 200" + bcolors.ENDC)
    except Exception as e:
        print(bcolors.FAIL + "some error occured ========> " + bcolors.ENDC)
        print(e)
