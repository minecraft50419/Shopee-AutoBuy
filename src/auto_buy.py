# -*- coding: utf-8 -*
from selenium import webdriver
import time

from data_structure import CookiesToJSON, JcookiesExport


'''     搶購資料        '''
buy_page = 'https://shopee.tw/buyer/login/otp?next=https%253A%252F%252Fshopee.tw%252Fcart'
phone_number = '0970758296'
item_keyword_flag = True
item_keyword = ['time每日計劃本']
item_values = 190

# 0="貨到付款" 1=街口支付(無) 2=信用卡/金融卡 4=分期付款(無) 5=銀行轉帳
payment_method = ["貨到付款", "信用卡/金融卡", "銀行轉帳"]
# 0=7-11 1=萊爾富 2=全家 3=OK MART 4=黑貓宅急便
delivery_method = ["全家", "萊爾富", "全家", "OK mart", "黑貓宅急便"]

'''     瀏覽器設定       '''
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_argument('--headless')

options.add_experimental_option("prefs", prefs)
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(chrome_options=options)


'''     空變數設置      '''
function_return_flag = False
btnflag = False
web_loaded_flag = False
textflag = False


def DebugLoad():
    global function_return_flag
    # debug
    if function_return_flag == False:
        browser.get('https://shopee.tw/%E7%89%9B%E7%9A%AE%E7%B4%99%E8%A8%88%E5%8A%83%E7%AD%86%E8%A8%98%E6%9C%AC-%E6%AF%8F%E6%97%A5%E8%A1%8C%E7%A8%8B%E8%A8%88%E5%8A%83%E6%9C%AC-%E9%80%B1%E8%A8%88%E7%95%AB-%E6%9C%88%E8%A8%88%E5%8A%83%E6%9C%AC-%E6%97%A5%E8%A8%98%E6%9C%AC-%E8%A8%98%E4%BA%8B%E6%9C%AC-%E7%84%A1%E5%8D%B0%E9%A2%A8%E3%80%90RC2260%E3%80%91%E3%80%8AJami%E3%80%8B-i.6948899.145802362?adsid=0&campaignid=0&position=-1')
        # browser.get('https://shopee.tw/checkout/?state=H8KLCAAAAAAAAAPDlVXDncKKw5tGFH7Cl8K5dkDCkmXDicO2wqssZhhpwo7CvMODSjPDisOMaMKxCcKGw5BALsKSQMKuWsKaNsK0wpQSw6hNfggpXSjDtGnDqsKNw7ctembCpMKRw5VAIMOkLsK6w5jClcOOw6%2FDt8KdPz8gwrTCrCxZX8OEwpsZwrHCogFjWcOTwpJ1wpwlWcK2XMOFw4toRsOMwqVqwpXDpsKgDcOaPcOwwp9kw53DvxfCnMKswpN8wr7DjMKSw7wwI8OCQsOTw5vCuDfCp8OLw6dZFMOnw4l8wpXDjUjCozjDlE7CuMKIwrMoT8OTZMKeL2bChHFOwpXCpBxYTX3CtFXCskrDoxzCgxk6w6hMV1AXwpDCrCtWG8Oow7PDkMKtVl3Dq11IwrxMw6J4wpnDpsKreRotw6bDmSLDjVMyI8O3OybCrcKweyRzQHLCtcOaCmNFaRx2DcKlahrCkBw4LS%2FCmcKUDhlqZFfDl0jCpMOow7bCoF16DcOGUMOOLHNOwpbDrcKCDMKTw57DvcO9w6jDtsOFH8OHDx8oPsOHNy9PP8K%2Bw754w7N7w79ywrzDucOuw6PCq19Ow7%2FCvD%2FDvcO1w7bDn8KbwofCt2%2FDvlxlwqcXwr%2FCrsKWw7jCh3jDjj7CsMOdwrfCgMOoRsKBwq9YwpwuwpYIw4FADcKlRXgBw7cZJ1nDj8KjKFrCuMOGwojCthVyw6vCqxBPfFoNFWjCjW%2FCrsOkw5fCoMO3w5TDtcKWwppaWW%2FDrHluwqYebMKPw6XCsCHDicOIOXwPWVNMPDsLXR9UawU2ScOISnkHw4wqMA7Dk3wMUjB5RSVrwpAsOT5%2Fd8O7w4PCu8Ojw4vCp3c%2Fw718w7zDvsOxw63Cq8OXd08ewp5%2Be8KGZcKBXSsQKXo5w4Mowr3Cl0RJwo5yw6%2FDrilmc8KcIx9adk0BGsONw5Isw4vCk2zDp8KfFMOhwpHDgyfDuMK8I8OCRsOnCHVYDMKDeHHDkHDDnmFnA8OwA8OqWsKtGsOlw5kEw6TCnQFaKiHDjTh7wpUGwqxjKMO8wrXDqsOKSxzClcOAw74zWsKEwoBlw6PDgsKwwqLDhmJrYMOGQXBdw7DDtMOkJERjwrZIC2nDl8OAwrTCpMKNw5JAB8OZw6Fzw6lLXMKtw4HCoMKtwpnCrcKUbsKCw47DrcOjwqbDn8OhT0TDuFpew5HCqcKCw6IEaCZLOMOTZcKdVcKUwrVtwr3Dv8Kfw6XCoHfCgMOMNcOtwqcoTMOBEMKew4PCtShhwqQVPnlPbsO4wqzCkAXDqFYLaXvCuVVyw4s7ScKLwprClVfChcOaw7XDkn4fw4PCjE46wobCs2DChzVyc1kLwq%2FDr8OLw63DljVkw7fDr3wow5FYwr7DqVHDm8OLwpLCrMKtw67DoAsvw4XDhcOmG8K%2BE8OhwqBjfTjDrFzCuy%2FCok3CoMKDIcOGw60iX3NUw7rDkF3DqxZ5bMOWMG%2FCqsKzGMOIwrU%2BVGsEwodnw54qw4tqwrLDjiLDv0zCgMOjw6rClMKqw4PDnsKewo3CpsOqIMKlBVRuX8KCw7kkVMORSV7Cg8O%2Fwp0xE33Cv8KCw71vCcOSwp9ow5DCpwHDrcKKwokywpgkwo7DkxDDkzUawofDki3CtcK3w6%2FDq2d3wpJWMEzDpMOkGsKOw5clZMO1AsK3wrp%2Bw4EEw7DCoHDDvcKBw6HDsMOgwrHDoADDjVnDmRMdw5Mmw5EUDTbCs2nDuxzDkcOhw7AfwqbCr17CncOdBwAA')
        # cookies加載
        browser.delete_all_cookies()

        for cookie in JcookiesExport():
            browser.add_cookie(cookie)

        print('cookies update over')
        browser.refresh()


def Login():
    global btnflag, web_loaded_flag
    btnflag = False
    browser.get(
        'https://shopee.tw/buyer/login/otp?next=https%253A%252F%252Fshopee.tw%252Fcart')  # sms登入頁面

    browser.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input').send_keys(phone_number)
    browser.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[5]/div/div[2]/div[2]/div[1]/div/input').send_keys("2")

    while btnflag != True:
        btnflag = browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').is_enabled()
    browser.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()

    while web_loaded_flag != True:
        try:
            browser.find_element_by_xpath(
                '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button')
        except:
            print("網頁未更新")
            continue
        web_loaded_flag = True
    web_loaded_flag = False

    btnflag = False
    while btnflag != True:
        btnflag = browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').is_enabled()
    browser.find_element_by_xpath(
        '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()

    time.sleep(1)

    # cookies保存
    cookies = browser.get_cookies()
    CookiesToJSON(cookies)

    browser.get(buy_page)


def SelectItem():
    global function_return_flag, btnflag, web_loaded_flag, item_keyword_flag
    # 以下單鈕確定網頁加載狀況
    try:
        browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')
    except:
        print("重新加載 selectitem")
        function_return_flag = True
        SelectItem()
    function_return_flag = False

    # item選擇
    if item_keyword_flag == True:
        print("items調整中")
        for i in range(len(item_keyword)):

            # 按鈕狀態確認
            btnaddress = '//div[contains(@class,"flex items-center")]/button[text()="' + \
                item_keyword[i]+'"]'
            # 確認是否有此按鈕
            try:
                browser.find_element_by_xpath(btnaddress)
            except:
                print("未有此選項:"+item_keyword[i])
                i += 1
                continue
            # 確認是否售完
            btnflag = False
            btnflag = browser.find_element_by_xpath(btnaddress).is_enabled()
            if btnflag == False:
                print(item_keyword[i]+"售完")
                i += 1
                continue

            # 點擊選項
            browser.find_element_by_xpath(btnaddress).click()
            try:
                browser.find_element_by_xpath(
                    '//button[contains(@class,"selected")]')
            except:
                browser.find_element_by_xpath(btnaddress).click()

            btnflag = False
            item_keyword_flag = False
            break
    return


def SelectValues():
    if item_values != 1:
        print("values調整中")

        browser.find_element_by_xpath(
            '//input[@class="_2KdYzP iRO3yj"]').send_keys(u'\ue003')
        browser.find_element_by_xpath(
            '//input[@class="_2KdYzP iRO3yj"]').send_keys(item_values)

        textflag = True

        try:
            l = browser.find_element_by_class_name('_2wnKts')
            print(l)
        except:
            textflag = False
            print("textflag false")

        while textflag == True:
            print("超過額定數量")
            c_item_values = item_values
            c_item_values -= 1
            browser.find_element_by_xpath(
                '//button[contains(@class,"_2KdYzP")][1]').click()
            try:
                browser.find_element_by_class_name('_2wnKts')
            except:
                textflag = False

    return


def SelectDelivery():
    time.sleep(0.5)
    element = browser.find_element_by_xpath('//div[text()="變更"][1]')
    browser.execute_script("arguments[0].click();", element)
    for i in range(len(delivery_method)):
        try:
            browser.find_element_by_xpath(
                '//div[@class="sd0aWc _1uZ1aQ"]//div[text()="'+delivery_method[i]+'"]')
        except:
            print("未找到"+delivery_method[i])
            i += 1
            continue
        browser.find_element_by_xpath(
            '//div[@class="sd0aWc _1uZ1aQ"]//div[text()="'+delivery_method[i]+'"]').click()
        browser.find_element_by_xpath(
            '//div[@class="_3CHZBR"]//button[text()="完成"]').click()
        break


def SelectPayment():
    global btnflag, textflag
    btnflag = False
    textflag = False

    for j in range(len(payment_method)):
        btnaddress = '//div[contains(@class,"flex items-center")]/button[text()="' + \
            payment_method[j]+'"]'

        try:
            browser.find_element_by_xpath(btnaddress)
        except:
            j += 1
            continue

        btnflag = browser.find_element_by_xpath(btnaddress).is_enabled()
        if btnflag == True:
            browser.find_element_by_xpath(
                '//button[text()="'+payment_method[j]+'"]').click()
            if payment_method[j] == "信用卡/金融卡":
                textflag = True
            btnflag = False
            break
        j += 1
    if textflag == True:
        browser.find_element_by_xpath(
            '//div[@class="checkout-payment-setting__main-option"]').click()
    textflag = False


'''---------------------------------------------------------------------------------'''


def main():
    global web_loaded_flag

    DebugLoad()
    time_start = time.time()
    SelectItem()
    SelectValues()
    # 下單
    element = browser.find_element_by_xpath('//button[text()="直接購買"]')
    browser.execute_script("arguments[0].click();", element)

    web_loaded_flag = False
    while web_loaded_flag != True:
        try:
            browser.find_element_by_xpath('//span[text()="去買單"]')
        except:
            print("網頁未更新")
            continue
        web_loaded_flag = True

    web_loaded_flag = False

    print("跳轉")
    element = browser.find_element_by_xpath('//span[text()="去買單"]')
    browser.execute_script("arguments[0].click();", element)

    web_loaded_flag = False
    while web_loaded_flag != True:
        try:
            browser.find_element_by_xpath('//div[text()="變更"][1]')
        except:
            print("網頁未更新")
            continue
        web_loaded_flag = True

    web_loaded_flag = False

    SelectDelivery()
    time_end = time.time()
    print("時間為")
    print((time_end-time_start))


if __name__ == '__main__':
    main()
