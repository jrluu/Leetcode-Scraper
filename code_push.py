'''
Author: Jonathan Luu


'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import re

TIME_DELAY = 2

algorithms_page_driver = webdriver.Chrome("./chromedriver")
algorithms_page_driver.implicitly_wait(TIME_DELAY)



'''
TODO

#Automate Beautify Process

# git add .
# git commit -m "Pushed LeetCode into Repo"
# git push origin master
'''


def urlify(s):
    '''
    Removes special characters and replaces the white space with a dash

    :param s: string
    :return: string
    '''

    #Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s


def make_directory(path):
    '''
    :param path: String
    :return: NULL
    '''
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def create_file(title, code):
    '''
    Creates the file with the name of title, and inserts the code inside of it

    :param title: string
    :param code:  string
    :return:
    '''

    title = urlify(title)
    extension = ".cpp"

    title = "./leet_code_solutions/" + title + extension

    file = open(title, 'w')
    file.write(code)
    file.close()


def scrape_code(href):
    '''
    This function scrapes the code off Leetcode.
    This is neccessary because Leetcode's code text area is modified to provide highlighting and other features to the
    text.

    TODO:
    FIX STALE ELEMENT ERROR

    :return: string
    '''

    code = ""
    algorithms_page_driver.get(href)
    #time.sleep(TIME_DELAY)
    algorithms_page_driver.find_element_by_class_name("code-btn").click()
    time.sleep(TIME_DELAY)


    #wait = WebDriverWait(algorithms_page_driver, 10)
    confirm_button = algorithms_page_driver.find_element_by_xpath('// *[ @ id = "confirmRecent"] / div / div / div[3] / button[2]')
    #element = wait.until(EC.visibility_of(confirm_button))

    confirm_button.click()
    time.sleep(TIME_DELAY + 2)
    #algorithms_page_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    lines  = algorithms_page_driver.find_elements_by_class_name("ace_line_group")

    algorithms_page_driver.implicitly_wait(0)

    for line in lines:
        characters = line.find_elements_by_tag_name("span")

        for character in characters:
            try:
                code += character.text + " "
            except:
                pass

        code += "\n"

    algorithms_page_driver.implicitly_wait(TIME_DELAY)
    return code


def sign_into_leetcode():
    '''
    This function will ask the user for the preferred method to login(Currently only Facebook or into Leetcode)
    This function will then ask them for their login information, and login them in.

    Currently, there is NO error checking, so if this part crashes here, you will need to rerun the program

    :return: Null
    '''
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


def go_to_algorithms():
    """
    TODO:
    1. FIX STALE ELEMENT ERROR
    2. Select All elements

    This function opens the algorithms and scrapes your code off each problem.
    It then stores it into a file.

    :return:
    """

    make_directory("./leet_code_solutions")

    #Opens algorithms page
    algorithms_page_driver.get("https://leetcode.com/problemset/algorithms/")

    #time.sleep(TIME_DELAY)
    #Shows only problems that are solved
    algorithms_page_driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/form/div[1]/div/select/option[2]').click()

    #time.sleep(TIME_DELAY + 3)

    #Opens every problem and then copies their data into a file
    table = algorithms_page_driver.find_element_by_class_name('reactable-data')

    title_href = {}

    for row in table.find_elements_by_tag_name("tr"):
        title = row.find_element_by_tag_name("a").text
        href = row.find_element_by_tag_name("a").get_attribute("href")
        title_href[title] = href

    for title, href in title_href.iteritems():
        code = scrape_code(href)
        create_file(title, code)

        #To prevent overloading Leedcode's server
        #time.sleep(TIME_DELAY)

if __name__ == "__main__":
    sign_into_leetcode()
    go_to_algorithms()
    algorithms_page_driver.close()
