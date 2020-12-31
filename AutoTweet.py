from selenium import webdriver
from time import sleep
import getpass
import name

def clicks(element):
    driver.find_element_by_xpath(element).click()

def sending(elem,text):
    driver.find_element_by_xpath(elem).send_keys(text)

twitter_pass = getpass.getpass("Enter your Twitter password : ")
your_tweet = input('Enter your tweet : ')

info_dict = {
    'username' : name.user_name,
    'password' : twitter_pass,
    'url' : 'https://twitter.com/login',
    'email' : '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input',
    'passw' : '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input',
    'loginPath' : '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div',
    'tweetText' : '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div',
    'tweetButton' : '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
}

driver = webdriver.Edge('/Users/HP/Downloads/msedgedriver')
driver.get(info_dict['url'])
sleep(3)
sending(info_dict['email'],info_dict['username'])
sending(info_dict['passw'],info_dict['password'])
clicks(info_dict['loginPath'])
sleep(3)
sending(info_dict['tweetText'],your_tweet)
clicks(info_dict['tweetButton'])

