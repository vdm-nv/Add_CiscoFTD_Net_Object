from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(r"C:\Users\Operator\PycharmProjects\pythonProject\drivers\chromedriver.exe", options=options)
driver.maximize_window()
user_name = "mylogin"
password = "mypassword"
#
# Login to FTD
#
driver.get("https://MY_IPADD_OF_FTD/#/login")
driver.set_page_load_timeout(10)
username = driver.find_element_by_id("username")
username.send_keys(user_name)
pwd = driver.find_element_by_id("password")
pwd.send_keys(password)
driver.find_element_by_xpath('//*[@id="ember12"]/form/button').click() # press login button
print('Login is Good')
print('#'*100)
time.sleep(2)
#
# Find Object Button in Menu and Press Enter
#
but_objects = driver.find_element_by_xpath('/html/body/div[2]/div[2]/nav/div[2]/ul[1]/li[3]').click()
time.sleep(4)
#ip_list = ['10.121.96.54','10.121.96.84','10.121.97.18','10.121.97.19','10.121.97.82','10.121.96.64']
with open(r"C:\Python\TP\66.txt") as f:
    lines = f.read().splitlines()
    #for ip in ip_list:
    for ip in lines:
        host = "Host_IP_" + ip[7:]
        time.sleep(1)
# Find "+" button and press to add new Object
        add_obj = driver.find_element_by_xpath('//*[@id="main"]/div/section/div/div/div[1]/div/button[1]/i').click()
        name_net_obj = driver.find_element_by_xpath('//*[@id="name-input"]')
        name_net_obj.send_keys(host)
        time.sleep(2)
# Choice radio button with host
        button_host_radio = driver.find_element_by_xpath(
            '/html/body/div[2]/div[5]/div/div/div/div[2]/div/form/div/div[3]/div/div/div[2]/label/input').click()
# Find field with IP address
        host_ip = driver.find_element_by_id("ip-input")
        host_ip.send_keys(ip)
        time.sleep(1)
        button_ok = driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/div/div/div[3]/div/button[2]").click()
        time.sleep(4)
        print(host)
print("LIST with IP addresses are ended!!")
print("Login to FTD and make new Deploy for applying new changes")
time.sleep(4)
driver.quit()
