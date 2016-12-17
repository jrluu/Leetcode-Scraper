'''
Author: Jonathan Luu


'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import re
import sys

algorithms_page_driver = webdriver.Chrome("./chromedriver")
problem_page_driver = webdriver.Chrome("./chromedriver")

'''
TODO
# Gather code
# Create .cpp file for it

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


def scrape_code():
    '''
    This function scrapes the code off Leetcode.
    This is neccessary because Leetcode's code text area is modified to provide highlighting and other features to the
    text.

    :return: string
    '''

    code = ""
    lines  = problem_page_driver.find_elements_by_class_name("ace_line_group")

    for line in lines:
        characters = line.find_elements_by_tag_name("span")

        for character in characters:
            code += character.text + " "

        code += "\n"

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
    This function opens the algorithms and scrapes your code off each problem.
    It then stores it into a file.

    TODO:
    Copy Data from Site

    :return:
    """

    make_directory("./leet_code_solutions")

    #Opens algorithms page
    algorithms_page_driver.get( "https://leetcode.com/problemset/algorithms/")

    '''
    #Shows only problems that are solved
    algorithms_page_driver.find_element_by_xpath('// *[ @ id = "question-app"] / div '
                                                 '/ div[2] / form / div[1] / div / select / option[2]').click()
    '''
    #Opens every problem and then copies their data into a file
    table = algorithms_page_driver.find_element_by_class_name('reactable-data')

    for row in table.find_elements_by_tag_name("tr"):
        href = row.find_element_by_tag_name("a").get_attribute("href")
        problem_page_driver.get(href)

        #code = problem_page_driver.find_element_by_xpath('//textarea[@class = "ace_text-input"]').text()
#        code = problem_page_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/div/div/div/div/textarea")

        code = scrape_code()

        title = row.find_element_by_tag_name("a").text
        create_file(title, code)

        #time.sleep(3)

if __name__ == "__main__":
#    sign_into_leetcode()
    go_to_algorithms()

    algorithms_page_driver.close()
#    problem_page_driver.close()
