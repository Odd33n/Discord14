from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random


# prints 236736

driver = webdriver.Chrome("C:\Windows\chromedriver")

driver.get("https://discord.com/login")
time.sleep(6)

username_input = driver.find_element_by_name('email')
username_input.send_keys("even.odden@live.no")


password_input = driver.find_element_by_name('password')
password_input.send_keys("61rywSoC1.1")


#login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login_button = driver.find_element_by_css_selector("[type=submit]").click()
#login_button.click()
time.sleep(5)
driver.get("https://discord.com/channels/922782545752510504/922931006976188467")

time.sleep(5)
#element = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div/span/span/span")
time.sleep(2)
#element.send_keys("hey guys")
#element.send_keys(Keys.RETURN)


words = [
"Love the sneakZ!",
"WAGMI",
"We are all going to the moon bros",
"This project is incredible",
"The artwork is sick",
"wagmeeee!!",
"lfg?!!",
"NFT's for life",
"Gang",
"Is C-01 gang alive?"
"How much time will this WL cost me?",
"LF G team!",
"Anyone knows how long it will take to level to 10?",
"This work is crazy",
"I hope this WL will be worth it,",
"Any Norwegians in the chat?",
"Does this Rocket to 1 eth floor?!",
"This community is actually lit ",
"You only live today",
"Will hold this so long!",
"Keep it up guys!",
"Spread the word",
"Chat is on fire today",
"Non stop grinding",
"So many scam dm's...",
"All dms are scams!",
"The future is looking bright guys",
"Who loves C-01??",
"Gotta sell my car for this",
"!rank",
"Whitelist next"
"How old r people?"
"Are you guys excited about this?"
"SUIII"
"Get this to Elon Musk!"
"How many NFt's do you guys own?"
]


items = driver.find_elements_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/div[1]/div[2]/div/ol")
print(len(items))
'''for item in items:
    text = item.text
    print(text)
'''
i = 0

while i < 2000:
    
    #if i % 2 == 0:
    num = random.randint(0,len(words)-1)
    element = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div/span/span/span")
    element.send_keys(words[num] + " ")
    element.send_keys(Keys.RETURN)
       
    '''else: 
        items = driver.find_elements_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/div[1]/div[2]/div/ol")
        element = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div/span/span/span")
        element.send_keys(items[5].text)
        element.send_keys(Keys.RETURN)
   
    '''
    i = i +1
    time.sleep(65)

'''
for word in words:
    num = random.randint(0,236735)
    element = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div/span/span/span")
    element.send_keys(word + " " +  word_list[num])
    element.send_keys(Keys.RETURN)
    time.sleep(65)
'''