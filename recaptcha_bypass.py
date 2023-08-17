import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import speech_recognition as sr
import urllib
import pydub
from selenium import webdriver


driver = webdriver.Chrome()
url = "https://www.google.com/recaptcha/api2/demo"

driver.get(url)
html_content = driver.page_source


frames = driver.find_elements(By.TAG_NAME, "iframe")
print(frames)
driver.switch_to.frame(frames[0])

driver.find_elements(By.CLASS_NAME, "recaptcha-checkbox-border")[0].click()
print("Captcha box clicked")
time.sleep(random.randint(2, 3))


driver.switch_to.default_content()
frames = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[4]").find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[0])
time.sleep(random.randint(2, 3))

driver.find_element(By.ID, "recaptcha-audio-button").click()
time.sleep(random.randint(2, 3))

driver.switch_to.default_content()
frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[-1])
time.sleep(random.randint(2, 3))


driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/button").click()

time.sleep(random.randint(2, 3))
src = driver.find_element(By.ID, "audio-source").get_attribute("src")
print("[INFO] Audio src: %s" % src)

time.sleep(random.randint(2, 3))
urllib.request.urlretrieve(src, os.getcwd()+"/sample.mp3")

sound = pydub.AudioSegment.from_mp3(os.getcwd()+"/sample.mp3")
sound.export(os.getcwd()+"/sample.wav", format="wav")
sample_audio = sr.AudioFile(os.getcwd()+"/sample.wav")
r = sr.Recognizer()

time.sleep(random.randint(2, 3))

with sample_audio as source:
    audio = r.record(source)
    print("Converting Audio To Text ..... ")


try:
    text = r.recognize_google(audio)
    print("Decoded Text : {}".format(text))

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Could not request results. check your internet connection", e)

time.sleep(2)
driver.find_element(By.ID, "audio-response").send_keys(text.lower())
driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.ID, "recaptcha-demo-submit").click()
driver.switch_to.default_content()
time.sleep(2)
print(driver.find_element(By.CLASS_NAME, "recaptcha-success").text)
driver.quit()



