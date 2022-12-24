from time import sleep
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


#initialize global variables
PATH = '~/.local/bin/chromedriver'
OPTIONS = Options()
#open in debugger mode
OPTIONS.add_experimental_option('debuggerAddress', '127.0.0.1:9014')
DRIVER = webdriver.Chrome(PATH, options=OPTIONS)
LINKEDIN_URL = '0xc0rvu5'


def launch_browser():
    '''Run a Selenium driven browser and apply for LinkedIn jobs automatically.'''
    DRIVER.get(LINKEDIN_URL)
    
    sleep(5)
    #loop through all job listings, apply to jobs, if > 5 submit buttons move to next job
    all_listings = DRIVER.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
    for listing in all_listings:
        listing.click()

        
        try:
            sleep(2)
            #initial apply button
            apply = DRIVER.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')

            if apply:
                apply.click()
            else:
                sleep(2)
                continue

            sleep(3)
            print(Fore.GREEN + 'Beginning application process...')

            #instantiation of each individual element was deemed necessary to target each individual window. this applies for next1, next2, review and final_submit. five_buttons indicates that the application process will require additional user input which often varies significantly; thus, moving to the next application.
            next1 = DRIVER.find_element(By.CSS_SELECTOR, 'footer button')
            next1.click()

            sleep(2)
            choose_resume_botton = DRIVER.find_element(By.CLASS_NAME, 'jobs-resume-picker__resume-btn-container')
            if choose_resume_botton:
                choose_resume_botton.click()
          
            sleep(2)
            next2 = DRIVER.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            next2.click()

            sleep(2)
            review = DRIVER.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            review.click()

            sleep(2)
            final_submit = DRIVER.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            final_submit.click()

            sleep(3)
            five_buttons = DRIVER.find_element(By.CLASS_NAME, 'artdeco-button--primary')

            #if a fifth button is required move on
            if five_buttons:
                five_buttons.send_keys(Keys.ESCAPE)
                
                sleep(4)
                discard_button = DRIVER.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar button')
                discard_button.click()
                print(Fore.YELLOW + 'Complex application, skipped.')
                sleep(3)
                continue

            else:
                sleep(2)
                close_button = DRIVER.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                close_button.click()

        except NoSuchElementException:
            print(Fore.YELLOW + 'No application button, skipped.')
            continue
    
    sleep(5)
    print(Fore.GREEN + 'Done')
    DRIVER.quit()

    
#initialize selenium browser
try:
    launch_browser()

except KeyboardInterrupt:
    print('See you later.')
