#LeetCode Scraper

LeetCode Scraper is a python program that logins into your LeetCode account, and copies your code for your solved problems into its corresponding file.

For example, your solution to the problem FizzBizz will be stored in the file Fizzbizz.extension

##Requirements
* [Python 2.7](https://www.python.org/downloads/)
* [Selenium Package](http://selenium-python.readthedocs.io/installation.html)
* [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/)

##Steps to install and run
1. Download the .py file
``git clone https://github.com/jrluu/Leetcode-Scraper.git``
2. Install [Selenium]((http://selenium-python.readthedocs.io/installation.html)
``pip install selenium``
3. Download the latest [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/) and put it in the same directory as the .py file
4. ``python leetcode_scraper.py``
5. Follow instructions based on the command prompt
(This will ask you whether or not you want to login with Facebook, and then it will ask you for your username and password)


##Where to find your files
Your files will be located in the folder called leet\_code\_solutions


##Ways to contribute:
1. Currently, this program does not take in spaces or indents(Leetcode's code area is modified, so I am unable to parse it)
2. Add a GUI
3. Add a functionality to select the default extension(currently only .cpp)
4. Add more ways to login(Currently there are only two options to login, either through Facebook or Leetcode accounts)


##For more information on installing
1. [Python 2.7 Beginners guide] (https://wiki.python.org/moin/BeginnersGuide)
2. [How to install Selenium] (http://selenium-python.readthedocs.io/installation.html)
3. [Google Chrome Driver Download](https://sites.google.com/a/chromium.org/chromedriver/)




##Contact:
If you have any inquires or comments, please feel free them to send them to jrluu@yahoo.com with the subject line: [LeetCode_Scraper] title.


##Authors:
Jonathan Luu
