'''
Author: Jonathan Luu


'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

algorithms_page_driver = webdriver.Chrome("./chromedriver")
problem_page_driver = webdriver.Chrome("./chromedriver")

'''
# https://leetcode.com/accounts/login/
# Go to https://leetcode.com/problemset/algorithms/
# Filter by solved problems
# show "All rows"

# Use another browser to click on links
# Gather code
# Create .cpp file for it

# git add .
# git commit -m "Pushed LeetCode into Repo"
# git push origin master
'''

def sign_into_leetcode():
    algorithms_page_driver.get("https://leetcode.com/accounts/logout")

    use_facebook = raw_input("Do you want to use facebook to login?")
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")

    if (use_facebook.lower() == "y"):
        algorithms_page_driver.get("https://leetcode.com/accounts/facebook/login/")
        algorithms_page_driver.find_element_by_xpath('// *[ @ id = "email"]').send_keys(username)
        algorithms_page_driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        algorithms_page_driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
    else:
        algorithms_page_driver.get("https://leetcode.com/accounts/login/")
        algorithms_page_driver.find_element_by_xpath('// *[ @ id = "id_login"]').send_keys(username)
        algorithms_page_driver.find_element_by_xpath('// *[ @ id = "id_password"]').send_keys(password)
        algorithms_page_driver.find_element_by_xpath('// *[ @ id = "id_password"]').send_keys(Keys.ENTER)


    time.sleep(5)


def go_to_algorithms():
    algorithms_page_driver.get( "https://leetcode.com/problemset/algorithms/")


if __name__ == "__main__":
    sign_into_leetcode()
    go_to_algorithms()

    algorithms_page_driver.close()
    problem_page_driver.close()
