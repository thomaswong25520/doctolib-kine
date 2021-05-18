#Libraries
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.keys import Keys
#Chrome Options
chrome_options = Options()
# chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--window-size=1920x1080")
#chrome_options.add_argument("--window-size=1920,1080")
#chromedriver = f"/chrome/chrome90/chromedriver.exe"


#Notification window
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

#driver = webdriver.Chrome(chromedriver, options=chrome_options)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
url = "https://www.doctolib.fr/"


# driver.find_element_by_id("didomi-notice-disagree-button").click()

looked_skill = "Rééducation de l'épaule"
practicians_skills_shoulder = []

title = "Masseur-kinésithérapeute"
location = "Paris"

driver.get(url)

# Refuse cookie
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="didomi-notice-disagree-button"]'))).click()

#Medecin et ou have the same XPath
#text_fields returns a list of 2 WebElements
text_fields = driver.find_elements_by_xpath('//*[@id="autocomplete-default"]')

# editor = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="autocomplete-default"]')))
# editor2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="autocomplete-default"]')))



text_fields[0].send_keys(title)
text_fields[1].send_keys(location)

# confirm_paris = driver.find_element_by_xpath('//*[@id="ChIJD7fiBh9u5kcRYJSMaMOCCwQ"]/span/strong')
confirm_paris = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ChIJD7fiBh9u5kcRYJSMaMOCCwQ"]/span/strong')))
confirm_paris.click()

enter = driver.find_element_by_xpath('//*[@id="doctor_search_bar"]/form/div[2]/button/span/span')
enter.click()

height = driver.execute_script("return document.body.scrollHeight")
    # Scroll to load all results
for i in range(0,height-1000,500):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(0.2) # slow down scrolling to allow results to load

# list_of_practicians = driver.find_elements_by_class_name("dl-button-primary dl-button js-search-result-path")
text_fields = driver.find_elements_by_xpath('//*[@id="autocomplete-default"]')

# list_of_practicians = driver.find_elements_by_class_name("dl-search-result")
# print(list_of_practicians)
#
#
# list_of_practicians2 = driver.find_elements_by_xpath("//div[starts-with(@class,'dl-search-result-name')]/div[1]/div[1]/div[2]/h3/a")
# print(list_of_practicians2)

list_of_practicians_xpath = ["/html/body/div[7]/div/div[1]/div[1]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[2]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[3]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[4]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[5]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[6]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[7]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[8]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[9]/div[1]/div[3]/a",
                             "/html/body/div[7]/div/div[1]/div[10]/div[1]/div[3]/a"]


practician_1_xpath = list_of_practicians_xpath[-1]
print(f"practician: {practician_1_xpath}")
practician = driver.find_element_by_xpath(practician_1_xpath)
practician.click()

e = driver.find_elements_by_xpath('//*[@id="skills"]/div[2]/div[2]/a')
if e:
    e[0].click()
list_of_skills_elements = driver.find_elements_by_class_name("dl-profile-skill-chip")
lists_of_skills_names = [el.text for el in list_of_skills_elements]
if looked_skill in lists_of_skills_names:
    practicians_skills_shoulder.append(driver.current_url)

#
# for practician in list_of_practicians:
#     practician.click()
#     e = driver.find_elements_by_xpath('//*[@id="skills"]/div[2]/div[2]/a')
#     if e:
#         e[0].click()
#     list_of_skills_elements = driver.find_elements_by_class_name("dl-profile-skill-chip")
#     lists_of_skills_names = [el.text for el in list_of_skills_elements]
#     if looked_skill in lists_of_skills_names:
#         practicians_skills_shoulder.append(driver.current_url)
#
# print(practicians_skills_shoulder)


# Check if "Voir plus" exists
# e = driver.find_elements_by_xpath('//*[@id="skills"]/div[2]/div[2]/a')
# if e:
#     e[0].click()