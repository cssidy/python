#! python3

from selenium import webdriver

# this throws an error, 'geckodriver' executable needs to be in PATH
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')

# direct to a url
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % elem.tag_name)
except:
    print('Was not able to find an element with that name.')


# click the page
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
linkElem.click()  # follows the 'Read It Online' link

# fill out form
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('example@gmail.com')
passwordElem = browser.find_element_by_id('Password')
passwordElem.send_keys('12345')
passwordElem.submit()