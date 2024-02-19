import csv
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://nocodenolife.net/ann/page/#/content"

# 使用Selenium打開瀏覽器
driver = webdriver.Chrome()  # 請確保已安裝Chrome webdriver

# 前往指定的網址
driver.get(url)

# 等待會員專區元素出現
member_area_text_css = 'a[href="#/user"] span.p-menuitem-text'
member_area_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, member_area_text_css))
)

# 模擬點擊
member_area_text.click()
time.sleep(3)

# 定義函數，用於將數據填充到註冊表單中
def fill_registration_form(account, password):
    # 等待一段時間（可自行調整）
    time.sleep(3)

    # 定位登入頁帳號輸入框，輸入帳號
    login_account_input_css = 'div.login-data input[type="text"][placeholder="請輸入您的帳號"]'
    login_account_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, login_account_input_css))
    )
    login_account_input.send_keys(account)  # 填入的帳號進行登入

    # 定位登入頁密碼輸入框，輸入密碼
    login_password_input_css = 'div.login-data input[type="password"][placeholder="請輸入您的密碼"]'
    login_password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, login_password_input_css))
    )
    login_password_input.send_keys(password)  # 使用註冊時填入的密碼進行登入

    # 等待一段時間（可自行調整）
    time.sleep(3)

    # 定位到包含 OTP 值的 span 元素
    otp_value_span_css = 'div.otp span'
    otp_value_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, otp_value_span_css))
    )

    # 獲取 span 元素的文本值
    otp_value = otp_value_span.text

    # 定位到 OTP 輸入框
    otp_input_css = 'div.otp input[type="text"]'
    otp_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, otp_input_css))
    )

    # 將 OTP 值輸入到 OTP 輸入框
    otp_input.send_keys(otp_value)
    
    # 定位登入按鈕
    login_button_css = 'div.login-data div.submit button.button_confirm'
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, login_button_css))
    )
    # 模擬點擊登入按鈕
    login_button.click()
    time.sleep(4)

    # 定位並點擊不訂閱
   # 等待不定閱按钮可点击并点击
    not_subscribe_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='news2']/div[2]")))
    not_subscribe_button.click()
    
   
    # 等待2秒
    time.sleep(2)

  # 定位并点击“储存变更”按钮
    
    #save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button_confirm')))
    
   # save_button.click()
    
    button_confirm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/div[9]/button[2]')))
    button_confirm.click()



    time.sleep(5)  # 等待5秒

# 等待 p-toast-message 元素可見和可互動
    toast_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'p-toast-message')),
        "Timeout waiting for p-toast-message to be visible"
    )    

# 在 p-toast-message 元素內定位到 i 元素
    close_button = toast_message.find_element(By.CSS_SELECTOR, 'i.pi.pi-times')

    # 點擊該按鈕
    close_button.click()
    time.sleep(5)   

    user_icon = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pi-user'))
    )
    
    # 点击父级元素，打开下拉窗
    user_icon.click()
    time.sleep(2)
    # 等待并定位登出按钮
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button_confirm:nth-of-type(2)'))
    )
    # 点击登出按钮
    logout_button.click()

    # 等待并定位目标按钮
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.p-button-secondary[aria-label="確定"]'))
    )

    # 點擊確認
    confirm_button.click()
    


# 從CSV文件中讀取數據
csv_filename = 'register_account.csv'

try:
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 使用從CSV文件中讀取的帳號和密碼填充註冊表單
            fill_registration_form(row['帳號'], row['密碼'])
            time.sleep(5)  # 等待一段時間（可自行調整）

except Exception as e:
    print("讀取CSV文件時發生錯誤:", str(e))
    # 關閉瀏覽器
    driver.quit()
