import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyautogui
from tkinter import filedialog, Tk
import os

# extended from https://github.com/fabricio-aguiar/Easy-Apply-bot
# Updates:
#   - New Easy Apply card classes
#   - try except to bypass new tab applications
# Future Updates needed:
#   - In order to apply to anything that has an Easy Apply button
#   there will need to a reference file in asset containing questions from
#   the applications.  (i.e. How many years experience do you have in X industry)
#   - There need to be helper function made in order to deal with subforms introduced
#   by the new tab; however, I am currently breaking since the ratio seems substantially
#   smaller than applications that go through.

# I am taking into account that you already have a LinkedIn account and that you
# have a resume already uploaded to your profile.  The reason I do not automate
# the login is because LinkedIn is pretty good at detecting automated input
# which introduces the CAPTCHa requirement.  The processes should not fail and
# apply to 60-80% of the jobs under the 'position' on 
class EasyApplyBot:

    MAX_APPLICATIONS = 100000

    def __init__(self, language):
        self.language = language
        self.options = self.browser_options()
        chromepath = './assets/chromedriver.exe'
        self.browser = webdriver.Chrome(options=self.options, executable_path=chromepath)
        self.start_linkedin()

    def browser_options(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("user-agent=Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")
        return options

    def start_linkedin(self):
        self.browser.get("https://linkedin.com/uas/login")

    def wait_for_login(self):
        time.sleep(15)

    def fill_data(self):
        self.browser.set_window_size(0, 0)
        self.browser.set_window_position(2000, 2000)
        os.system("reset")

        position = input("What jobs would you like to apply for?")
        self.position = position.replace(" ", "%20")
        location = input("Where are the jobs located? " + 
                         "(i.e. Global, Country (United States), State (California), City (San Francisco): ") 
        self.location = "&location=" + location.replace(" ", "%20") + "&sortBy=DD"

        time.sleep(1)
        root = Tk()
        self.resumeloctn = ''

        root.destroy()

    def start_apply(self):
        self.wait_for_login()
        self.fill_data()
        self.applications_loop()

    def applications_loop(self):
        count_application = 0
        count_job = 0
        jobs_per_page = 0

        os.system("reset")

        self.browser.set_window_position(0, 0)
        self.browser.maximize_window()
        self.browser, _ = self.next_jobs_page(jobs_per_page)

        while count_application < self.MAX_APPLICATIONS:
            # sleep to make sure everything loads, add random to make us look human.
            time.sleep(random.uniform(3.5, 6.9))

            page = BeautifulSoup(self.browser.page_source, 'lxml')

            jobs = self.get_job_links(page)

            if not jobs:
                print("Jobs not found")
                break

            for job in jobs:
                count_job += 1
                job_page = self.get_job_page(job)
                print(self.got_easy_apply(job_page))
                if self.got_easy_apply(job_page):
                    print('here')
                    string_easy = "* has Easy Apply Button"
                    xpath = self.easy_apply_xpath()
                    self.click_button(xpath)
                    self.send_resume()
                    count_application += 1

                else:
                    string_easy = "* Doesn't have Easy Apply Button"

                position_number = str(count_job + jobs_per_page)
                print(f"\nPosition {position_number}:\n {self.browser.title} \n {string_easy} \n")

                if count_job == len(jobs):
                    jobs_per_page = jobs_per_page + 25
                    count_job = 0
                    print("Going to next jobs page !")
                    self.avoid_lock()
                    self.browser, jobs_per_page = self.next_jobs_page(jobs_per_page)

        self.finish_apply()

    def get_job_links(self, page):
        links = []
        for link in page.find_all('a'):
            url = link.get('href')

            if url:
                if '/jobs/view' in url:
                    links.append(url)
        return set(links)

    def get_job_page(self, job):
        root = 'www.linkedin.com'
        if root not in job:
            job = 'https://www.linkedin.com'+job
        self.browser.get(job)
        self.job_page = self.load_page(sleep=0.5)
        return self.job_page

    def got_easy_apply(self, page):
        button = page.find("button", class_="jobs-apply-button")
        return len(str(button)) > 4

    def get_easy_apply_button(self):
        # jobs-s-apply--fadein inline-flex mr2 jobs-s-apply:::possibly old html classes
        button_class = "jobs-apply-button--top-card ember-view"
        button = self.job_page.find("div", class_=button_class)
        return button

    def easy_apply_xpath(self):
        button = self.get_easy_apply_button()
        button_inner_html = str(button)
        list_of_words = button_inner_html.split()
        time.sleep(.5)
        next_word = [word for word in list_of_words if "ember" in word and "id" in word]
        ember = next_word[-1][:-1]
        xpath = '//*[@'+ember+']'
        print(xpath)
        return xpath

    def click_button(self, xpath):
        triggerDropDown = self.browser.find_element_by_xpath(xpath)
        time.sleep(0.5)
        triggerDropDown.click()
        time.sleep(1.5)

    def send_resume(self):
        submit_button = None
        time.sleep(1)
        while not submit_button:
            try:
                submit_button = self.browser.find_element_by_xpath("//*[contains(text(), 'Submit application')]")
                submit_button.click()
                time.sleep(random.uniform(1.5, 2.5))
            except:
                break

    def load_page(self, sleep=1):
        scroll_page = 0
        while scroll_page < 4000:
            self.browser.execute_script("window.scrollTo(0,"+str(scroll_page)+" );")
            scroll_page += 200
            time.sleep(sleep)

        if sleep != 1:
            self.browser.execute_script("window.scrollTo(0,0);")
            time.sleep(sleep * 3)

        page = BeautifulSoup(self.browser.page_source, "lxml")
        return page

    def avoid_lock(self):
        x, _ = pyautogui.position()
        pyautogui.moveTo(x+200, None, duration=1.0)
        pyautogui.moveTo(x, None, duration=0.5)
        pyautogui.keyDown('ctrl')
        pyautogui.press('esc')
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)
        pyautogui.press('esc')

    def next_jobs_page(self, jobs_per_page):
        self.browser.get(
            "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=" +
            self.position + self.location + "&start="+str(jobs_per_page))
        self.avoid_lock()
        self.load_page()
        return (self.browser, jobs_per_page)

    def finish_apply(self):
        self.browser.close()


if __name__ == '__main__':

    bot = EasyApplyBot('en')
    bot.start_apply()
