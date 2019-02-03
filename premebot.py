
from selenium import webdriver
from config import keys
import time

def timer(method):
    def wrap(*args, **kw):
        starter = int(round(time.time() * 1000))
        result = method(*args, **kw)
        end = int(round(time.time() * 1000))
        print((end - start)/1000, 's')
        return result
    return wrap

@timer
def Main():
    driver.find_element_by_name('commit').click()

    time.sleep(0.5)
    checkout = driver.find_element_by_class_name('checkout')
    checkout.click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys['card_cvv'])
    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])

    payment = driver.find_element_by_xpath('//*[@id="pay]/input')
    payment.click()

if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')
    driver.get(key['product_url'])
    Main()