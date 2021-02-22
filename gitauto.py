email = 'gopianandakumar@gmail.com'
pwd = 'he19MA95'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time
import os

repository = input("enter your Repository Name   >>>>>>>>>>>>>>$ ")

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://github.com/login')

user = driver.find_element_by_id('login_field')
user.send_keys(email)

pwds = driver.find_element_by_id('password')
pwds.send_keys(pwd)

signin = driver.find_element_by_xpath(
    '/html/body/div[3]/main/div/div[4]/form/input[14]')
signin.submit()

newrepo = driver.find_element_by_xpath(
    '/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')

newrepo.click()

new = driver.find_element_by_xpath(
    '/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
new.send_keys(repository)

addmef = driver.find_element_by_id('repository_auto_init')

addmef.click()

create = driver.find_element_by_xpath(
    '/html/body/div[4]/main/div/form/div[4]/button')
create.submit()

clone = driver.find_element_by_xpath(
    '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[2]/span/get-repo/details/summary'
)

clone.click()

copythepaths = driver.find_element_by_xpath(
    '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/tab-container/div[2]/div/div/clipboard-copy'
)
copythepaths.click()

git_url = clipboard.paste()

print(git_url)

os.system('git init')
os.system('git add  . ')
os.system('git status')
os.system('git commit -m  "initial commit" ')
os.system('git remote add origin ' + git_url)
os.system('git push origin master ')

print(" task completed successfully")

print(10 * '**', 'TaskCompleted Successfully', 10 * '**')
