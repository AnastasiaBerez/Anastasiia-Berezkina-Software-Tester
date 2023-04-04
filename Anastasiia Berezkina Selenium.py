import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(50)
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
log_buttom = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
log_buttom.click()
driver.implicitly_wait(50)
# assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
    print ("True")
else:
    print("False")
time.sleep(3)
driver.save_screenshot("LogIn.png")
exit_buttom = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span")
exit_buttom.click()
logout = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
logout.click()
driver.implicitly_wait(50)
# assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
    print("True")
else:
    print("False")
time.sleep(3)
driver.save_screenshot("Logout.png")

driver.quit()



