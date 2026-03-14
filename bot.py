import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from googleapiclient.discovery import build

NUVOLA_USER = "TUO_USERNAME"
NUVOLA_PASS = "TUA_PASSWORD"

def get_homework():

    driver = webdriver.Chrome()

    driver.get("https://nuvola.madisoft.it")

    time.sleep(3)

    driver.find_element(By.ID,"username").send_keys(NUVOLA_USER)
    driver.find_element(By.ID,"password").send_keys(NUVOLA_PASS)

    driver.find_element(By.TAG_NAME,"button").click()

    time.sleep(5)

    driver.get("https://nuvola.madisoft.it/area-studente/compiti")

    time.sleep(5)

    homework = driver.find_elements(By.CLASS_NAME,"card")

    tasks = []

    for h in homework:
        tasks.append(h.text)

    driver.quit()

    return tasks

def add_to_calendar(tasks):

    service = build("calendar","v3")

    for task in tasks:

        event = {
            "summary": "Compiti",
            "description": task
        }

        service.events().insert(
            calendarId="primary",
            body=event
        ).execute()

if __name__ == "__main__":

    tasks = get_homework()

    add_to_calendar(tasks)
