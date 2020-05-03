from selenium import webdriver
from time import sleep
import smtplib
import re
from datetime import datetime

def Corona(countries):
    driver = webdriver.Chrome(r'C:\Users\Sri\Downloads\chromedriver')
    driver.minimize_window()
    driver.get("https://www.worldometers.info/coronavirus/")
    sleep(2)
    for i in range(1,300):
                country = driver.find_element_by_xpath(('//*[@id="main_table_countries_today"]/tbody[1]/tr[{0}]/td[1]'.format(str(i))))
                if(country.text == countries):
                    india = country.find_element_by_xpath("./..")
                    data = india.text.split(" ")
                    total_cases = data[1]
                    total_deaths = data[2]
                    active_cases = data[4]
                    total_recovered = data[3]

                    print("Country: " + country.text)
                    print("Total cases: " + total_cases)
                    print("Total deaths: " + total_deaths)
                    print("Active cases: " + active_cases)
                    print("Total recovered: " + total_recovered)
                    send_mail(country.text, total_cases, total_deaths, active_cases, total_recovered)
                    break

def send_mail(country_element, total_cases, total_deaths, active_cases, total_recovered):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('zbogets@gmail.com', 'Legends@2')

    subject = 'Coronavirus stats in your country today!'

    body = 'Today in ' + country_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases +'\
        \nTotal deaths: ' + total_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Coronavirus',
        'rsenthilkumars@gmail.com',
        msg
    )
    print('Hey Email has been sent!')

    server.quit()

Corona("India")
