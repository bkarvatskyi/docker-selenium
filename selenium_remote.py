from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)
driver.get("https://www.google.com")

driver.maximize_window()
driver.save_screenshot('screen.png')

# close the browser
driver.close()
driver.quit()
