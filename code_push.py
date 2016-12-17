'''
Author: Jonathan Luu


'''

from selenium import webdriver

algorithms_page_driver = webdriver.Chrome("./chromedriver")
problem_page_driver = webdriver.Chrome("./chromedriver")


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

def sign_into_leetcode():
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    #need to logout
    algorithms_page_driver.get("https://leetcode.com/accounts/login/")

def go_to_algorithms():
    algorithms_page_driver.get( "https://leetcode.com/problemset/algorithms/")


if __name__ == "__main__":
    sign_into_leetcode()
    go_to_algorithms()

    algorithms_page_driver.close()
    problem_page_driver.close()
