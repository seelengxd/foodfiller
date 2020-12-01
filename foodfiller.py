#https://towardsdatascience.com/using-python-and-selenium-to-automate-filling-forms-and-mouse-clicks-f87c74ed5c0f
#reference

#chromedriver should be downloaded and be in the same folder as the file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time
import os

# chromedriver_location = "/Users/seelengxd/Downloads/chromedriver"
chromedriver_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
driver = None
tomorrow = datetime.now() + timedelta(days=1)
confirm = ''
while tomorrow.weekday() not in range(5) or confirm !='x':
    while tomorrow.weekday() not in range(5):
        tomorrow += timedelta(days=1)
    confirm = input(f'x to confirm order on {tomorrow.strftime("%Y-%m-%d, %A")}: ')
    if confirm != 'x':
        tomorrow += timedelta(days=1)

mydata = {
    'name':'your name',
    'level':'sh2',
    'class':'19SH07',
    'collectionMethod':'Self-Collection',
    'mobile':'your class',
    'date':tomorrow.strftime('%d %B %Y'),

}

breaks = [('9:00am', '12:30pm'), ('9:30am', '1:30pm'), ('9:30am', '12:30pm'), ('10:30am',), ('9:00am',)]

def formfiller(pickup, order):
    xpaths = {
    'name':'/html/body/div/div[7]/div/main/div/div/div[1]/div[1]/div/div/div/input',
    'level':'/html/body/div/div[7]/div/main/div/div/div[1]/div[2]/div[2]/div/div/div/div/div',
    'class':'/html/body/div/div[7]/div/main/div/div/div[1]/div[3]/div[2]/div/div/div/div/div',
    'collectionMethod':'/html/body/div/div[7]/div/main/div/div/div[1]/div[4]/div[2]/div/div/div/div/div',
    'mobile':'/html/body/div/div[7]/div/main/div/div/div[1]/div[5]/div[2]/div/div/input',
    'date':'/html/body/div/div[7]/div/main/div/div/div[1]/div[6]/div/div/div/div/div/div/input',
    'payment':'/html/body/div/div[7]/div/main/div/div/div[1]/div[9]/div[3]/div/div/div/div/div',
    'break':'/html/body/div/div[7]/div/main/div/div/div[1]/div[7]/div[2]/div/div/div/div/div',
    'stall':'/html/body/div/div[7]/div/main/div/div/div[1]/div[8]/div[2]/div/div/div/div/div'
    }
    xpaths = {
        'name': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[1]/div/div/div/input',
        'level': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[2]/div[2]/div/div/div/div/div',
        'class': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[3]/div[2]/div/div/div/div/div',
        'collectionMethod': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[4]/div[2]/div/div/div/div/div',
        'mobile': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[5]/div[2]/div/div/input',
        'date': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[6]/div/div/div/div/div/div/input',
        'break': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[7]/div[2]/div/div/div/div/div',
        'stall': '/html/body/div[1]/div[6]/div/main/div/div/div[1]/div[8]/div[2]/div/div/div/div/div'
    }
    driver.get('https://airtable.com/shrmftcIPk4DxkuF5')
    time.sleep(1)
    print(driver.find_elements_by_tag_name('input'))
    for k, v in mydata.items():
        time.sleep(0.5)
        driver.find_element_by_xpath(xpaths[k]).send_keys(f'{v}\n')
    time.sleep(0.5)
    driver.find_element_by_xpath(xpaths['break']).send_keys(f'{pickup}\n')
    driver.find_element_by_xpath(xpaths['stall']).send_keys(f'{order}\n')


def menu():
    global driver
    #get order
    stalls = ['The Big Wok', 'Take Your Pick', 'Western Delicacies', \
        'Mumbo No. 5', 'Tropicana', 'Surf Shack', 'Chinese Cuisine',\
        'Noodle Shop', 'Asian Delights', 'Malay Kitchen', 'Prata Hut']
    tmrBreaks = breaks[tomorrow.weekday()]
    print(f"tomorrow's break(s): {tmrBreaks}")
    orders = []
    print("menu")
    for i, v in enumerate(stalls, 1):
        print(f'{i}:{v}')
    for time1 in tmrBreaks:
        print(f'break: {time1}')
        stallChoice = input('Enter comma separated digits of stalls: ').split(',')
        for stall in stallChoice:
            if stall:
                orders.append((time1, int(stall)-1))
        print()
    
    #autofill
    driver = webdriver.Chrome(chromedriver_location)

    for time1, order in orders:
        formfiller(time1, stalls[order])
        if (time1, order) != orders[-1]:
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)
    
    x = ''
    while x != 'x':
        x = input('enter x if done: ')
    driver.quit()

menu()
    
    



    
        