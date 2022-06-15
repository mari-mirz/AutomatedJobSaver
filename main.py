from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

url = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&geoId=104769905&keywords=junior%20developer&location" \
      "=Sydney%2C%20New%20South%20Wales%2C%20Australia "
path = "/Users/marianamirzoyan/Desktop/Development/chromedriver"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(url=url)

login_button = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
login_button.click()

# login to account
username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
signin_button = driver.find_element(By.CSS_SELECTOR, ".from__button--floating")
signin_button.click()

# creating list of jobs
job_list = []
id_list = []
listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list li .job-card-container "
                                                 ".job-card-list__entity-lockup .artdeco-entity-lockup__content "
                                                 ".artdeco-entity-lockup__title")

for item in listings:
    job_list.append(item.text)
    id = item.get_attribute("id")
    id_list.append(id)

# combining lists into dictionary
job_dictionary = {}

for key in job_list:
    for value in id_list:
        job_dictionary[key] = value
        id_list.remove(value)
        break

print(job_dictionary)

# applying to jobs
job_details = (driver.find_element(By.ID, "job-details")).text

for job in job_dictionary:
    element = driver.find_element(By.ID, f"{job_dictionary[job]}")
    element.click()
    time.sleep(0.5)
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_button.click()
