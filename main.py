import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
block = int(input("write block number"))
data = []
def start_webdrive(block):
    options = Options()
    options.add_argument('headless')
    options.add_argument("window-size=1800,1000")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get('https://polygonscan.com/blocks?ps=100&p=1')
    while True:
        data.clear()
        browser.find_element(By.XPATH, value="/html/body/div[1]/header/div/div/nav/div[3]/div[2]/form/div/input[1]").send_keys(block)
        try:
            pars_data(browser, block)
        except:
            print("block error")
        block = block - 1
        if len(data) < 1:
            print("0")
            continue
        else:

            with open("Transactions.txt", "a") as file:
                file.write(str(f"{block}\n"))
                for elem in data:
                    file.write(f"{elem}\n")
def pars_data(browser, block):
    browser.find_element(By.XPATH, value="/html/body/div[1]/header/div/div/nav/div[3]/div[2]/form/div/div[2]").click()
    browser.find_element(By.XPATH,
                         value="/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div/div[3]/div/div[2]/a[1]").click()
    time.sleep(1)
    i = 0
    while i == 0:
        a = browser.find_elements(By.XPATH,
                                  value='/html/body/div[1]/main/div[2]/div/div/div[3]/table/tbody/tr/td[7]')
        b = browser.find_elements(By.XPATH,
                                  value='/html/body/div[1]/main/div[2]/div/div/div[3]/table/tbody/tr/td[9]')
        transact_1_list = [x.text for x in a]
        transact_2_list = [x.text for x in b]
        transact_all = [f'{i}   {j}' for i, j in zip(transact_1_list, transact_2_list)]
        data.extend(transact_all)
        try:
            browser.find_element(By.XPATH, value="/html/body/div[1]/main/div[2]/div/div/div[2]/nav/ul/li[4]/a").click()
        except:
            print(f"all Transactions block {block}  write ")
            i += 1


start_webdrive(block)









