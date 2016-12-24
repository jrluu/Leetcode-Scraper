'''
Author: Jonathan Luu

LeetCode Scraper is a python program that logins into your LeetCode account, and copies your code for your solved 
problems into its corresponding file.

For example, your solution to the problem FizzBizz will be stored in the file Fizzbizz.extension
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re
import Tkinter as tk

TIME_DELAY = 2

CODE_DRIVER = webdriver.Chrome("./chromedriver")

ROOT = tk.Tk()
ROOT.withdraw()

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

    language = CODE_DRIVER.find_element_by_class_name("select2-selection__rendered").text
    if language == "C++":
        extension = ".cpp"
    elif language == "Java":
        extension = ".java"
    elif language == "Python":
        extension = ".py"
    elif language == "C":
        extension = ".c"
    elif language == "C#":
        extension = ".cs"
    elif language == "JavaScript":
        extension = ".js"
    elif language == "Ruby":
        extension = ".rb"
    elif language == "Swift":
        extension = ".swift"
    else:
        extension = ".go"

    title = "./leet_code_solutions/" + title + extension

    file = open(title, 'w')
    file.write(code)
    file.close()


def scrape_code(href):
    '''
    This function scrapes the code off Leetcode.
    This is neccessary because Leetcode's code text area is modified to provide highlighting and other features to the
    text.

    TODO: Remove time.sleep() for the "lines" portion of the code.

    :return: string
    '''

    wait = WebDriverWait(CODE_DRIVER,10)
    code = ""

    CODE_DRIVER.get(href)

    reset_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "code-btn")))
    reset_button.click()

    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "confirmRecent"]'
                                                                      ' / div / div / div[3] / button[2]')))
    confirm_button.click()

    CODE_DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(TIME_DELAY + 2)

    code_elem = CODE_DRIVER.find_element_by_class_name("ace_text-input")
    code_elem.send_keys(Keys.LEFT_CONTROL, 'a')
    code_elem.send_keys(Keys.LEFT_CONTROL, 'c')

    code = ROOT.clipboard_get()
    '''
    lines  = CODE_DRIVER.find_elements_by_class_name("ace_line_group")

    #Trying to remove time.sleep()
    #if wait.until(EC.staleness_of(lines)) :
    #    lines = CODE_DRIVER.find_elements_by_class_name("ace_line_group")


    for line in lines:
        characters = line.find_elements_by_tag_name("span")

        for character in characters:
            try:
                code += character.text + " "
            except:
                pass

        code += "\n"
    '''

    return code


def sign_into_leetcode():
    '''
    This function will ask the user for the preferred method to login(Currently only Facebook or into Leetcode)
    This function will then ask them for their login information, and login them in.

    :return: Null
    '''
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    CODE_DRIVER.get("https://leetcode.com/accounts/logout")

    valid_choice = False

    while ( not valid_choice):
        valid_choice = True

        option = raw_input("Type in method to login \n 1. Leetcode \n 2. Facebook \n 3. Google \n 4. Linkedin \n 5. Github \n")
        username = raw_input("Enter your username: ")
        password = raw_input("Enter your password: ")

        if option == "1":
            CODE_DRIVER.get("https://leetcode.com/accounts/login/")
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "id_login"]').send_keys(username)
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "id_password"]').send_keys(password)
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "id_password"]').send_keys(Keys.ENTER)
        elif option == '2':
            CODE_DRIVER.get("https://leetcode.com/accounts/facebook/login/")
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "email"]').send_keys(username)
            CODE_DRIVER.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
            CODE_DRIVER.find_element_by_xpath('//*[@id="pass"]').send_keys(Keys.ENTER)
        elif option == '3':
            CODE_DRIVER.get("https://leetcode.com/accounts/google/login/")
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "Email"]').send_keys(username)
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "Email"]').send_keys(Keys.ENTER)
            CODE_DRIVER.find_element_by_xpath('//*[@id="Passwd"]').send_keys(password)
            CODE_DRIVER.find_element_by_xpath('//*[@id="Passwd"]').send_keys(Keys.ENTER)
        elif option == '4':
            CODE_DRIVER.get("https://leetcode.com/accounts/linkedin/login/")
            CODE_DRIVER.find_element_by_name('session_key').send_keys(username)
            CODE_DRIVER.find_element_by_name('session_password').send_keys(password)
            CODE_DRIVER.find_element_by_name('session_password').send_keys(Keys.ENTER)
        elif option == '5':
            CODE_DRIVER.get("https://leetcode.com/accounts/github/login/")
            CODE_DRIVER.find_element_by_xpath('// *[ @ id = "login_field"]').send_keys(username)
            CODE_DRIVER.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            CODE_DRIVER.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
        else:
            valid_choice = False
            print "Invalid Choice. Please choose a number from 1 to 5 \n"

    CODE_DRIVER.implicitly_wait(0)

def go_to_algorithms():
    """
    This function opens the algorithms and scrapes your code off each problem.
    It then stores it into a file.

    :return:
    """

    #Using Implicitly Waits for find_elements
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    make_directory("./leet_code_solutions")

    #Opens algorithms page
    CODE_DRIVER.get("https://leetcode.com/problemset/algorithms/")

    #Shows only problems that are solved
    solved_dropdown = CODE_DRIVER.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/form/div[1]'
                                                        '/div/select/option[2]')
    solved_dropdown.click()
    all_dropdown = CODE_DRIVER.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div'
                                                     '/table/tbody[2]/tr/td/span/select/option[4]')
    all_dropdown.click()

    #Opens every problem and then copies their data into a file
    table = CODE_DRIVER.find_element_by_class_name('reactable-data')

    title_href = {}

    for row in table.find_elements_by_tag_name("tr"):
        title = row.find_element_by_tag_name("a").text
        href = row.find_element_by_tag_name("a").get_attribute("href")
        title_href[title] = href

    CODE_DRIVER.implicitly_wait(0)

    for title, href in title_href.iteritems():
        code = scrape_code(href)
        create_file(title, code)


if __name__ == "__main__":
    sign_into_leetcode()
    go_to_algorithms()
    CODE_DRIVER.close()
