import time
from config import email, password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
  button_resident = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/button[1]")))
  button_resident.click()
  time.sleep(1)

  button_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='teetime-login']/div/p[1]/button")))
  button_login.click()
  time.sleep(1)

  input_email = driver.find_element(By.XPATH, "//*[@id='login_email']")
  input_email.send_keys(email)

  input_password = driver.find_element(By.XPATH, "//*[@id='login_password']")
  input_password.send_keys(password)

  button_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login']/div/div[3]/div/button[1]")))
  button_submit.click()
  time.sleep(1)

  print("Login Successful!")

def open_non_resident(driver):
  button_non_resident = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='content']/div/button[2]")))
  button_non_resident.click()
  time.sleep(1)

def find_tee_time(driver, date, courses):
  input_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='date-field']")))
  input_date.send_keys(Keys.CONTROL + "a")
  input_date.send_keys(Keys.DELETE)
  input_date.send_keys(date.strftime("%m-%d-%Y"))
  input_date.send_keys(Keys.RETURN)
  time.sleep(1)

  select_course = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "schedule_select"))))
  select_course.select_by_visible_text(courses[0])
  time.sleep(1)

  button_time_morning = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav']/div/div[4]/div[1]/div[1]/a[1]")))
  button_time_morning.click()
  time.sleep(1)

  for course in courses:
    try:
      time_tile = driver.find_element(By.CLASS_NAME, "booking-start-time-label")
      time_tile.click()
      print("Tee-Time Found!")
      break

    except NoSuchElementException:
      print("No Tee-Time: " + course)

      select_course = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "schedule_select"))))
      select_course.select_by_visible_text(course)
      time.sleep(1)

  print("Checked All Courses!")