from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time
import asyncio
import smtplib


chrome_options = Options()
chrome_options.add_argument("--headless")
# web = webdriver.Chrome(options=chrome_options)#Place this inside function to delete window when finished
# web = webdriver.Chrome()
ETH = 1
target = 5

token1_list = ['USDT', 'BTC', 'ETH']
token2_list = ['DOGE', 'DAI', 'BTCH']


token1 = 'USDT'
token2 = 'ETH'

# sender = 'swapiswap8@gmail.com'
# receivers = ['swaplisten123@gmail.com']
# password = "Whocares420"

sushi = 'DOPE'
uni = ''
kyber = ''

prices = []

async def sushi_swap():
    # web = webdriver.Chrome(options=chrome_options)
    # web = webdriver.Chrome()
    # web.set_window_position(-10000,0)
    sushi_web.get('https://app.sushi.com/swap')
    # time.sleep(2)

    coin_select_button = sushi_web.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[1]/button/div/div[2]/div[2]')
    coin_select_button.click()
    # time.sleep(2)

    coin_select_text = sushi_web.find_element_by_xpath('//*[@id="token-search-input"]')
    coin_select_text.send_keys(token1)
    # time.sleep(2)
    await asyncio.sleep(2)

    # coin_select = web.find_element_by_class_name('css-8mokm4')
    coin_select = sushi_web.find_element_by_xpath('//*[@id="token-item-0xdAC17F958D2ee523a2206206994597C13D831ec7"]')
    # time.sleep(2)
    # await asyncio.sleep(5)
    coin_select.click()
    # time.sleep(2)
    await asyncio.sleep(2)

    coin_select_button = sushi_web.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[1]/button/div/div[2]/div[2]/div/div')
    coin_select_button.click()
    # time.sleep(2)
    #
    coin_select_text = sushi_web.find_element_by_xpath('//*[@id="token-search-input"]')
    coin_select_text.send_keys(token2)
    # time.sleep(2)
    await asyncio.sleep(2)
    #
    # coin_select = web.find_element_by_class_name('css-8mokm4')
    coin_select = sushi_web.find_element_by_xpath('//*[@id="token-item-ETHER"]')
    coin_select.click()

    input = sushi_web.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[2]/input')
    input.send_keys(1)
    # time.sleep(2)
    await asyncio.sleep(2)
    #
    read_coin_price = sushi_web.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[2]/input')
    sushi_price = read_coin_price.get_attribute('value')
    print('SUSHI: ', sushi_price)
    global sushi
    sushi = sushi_price
    prices.append(sushi)
    # sushi_web.quit()
    return sushi_price

async def uni_swap():
    # web = webdriver.Chrome()
    # web = webdriver.Chrome(options=chrome_options)
    uni_web.get('https://app.uniswap.org/#/swap')
    # time.sleep(2)

    coin_select_button = uni_web.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[1]/button')
    coin_select_button.click()
    # time.sleep(2)
    await asyncio.sleep(2)

    coin_select_text = uni_web.find_element_by_xpath('//*[@id="token-search-input"]')
    coin_select_text.send_keys(token1)
    # time.sleep(2)
    await asyncio.sleep(2)

    coin_select = uni_web.find_element_by_class_name('css-8mokm4')
    coin_select.click()
    # time.sleep(2)
    await asyncio.sleep(2)

    input = uni_web.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[1]/input')
    input.send_keys(1)

    coin_select_button = uni_web.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[1]/button')
    coin_select_button.click()
    # time.sleep(2)
    await asyncio.sleep(2)

    coin_select_text = uni_web.find_element_by_xpath('//*[@id="token-search-input"]')
    coin_select_text.send_keys(token2)
    # time.sleep(2)
    await asyncio.sleep(2)

    coin_select = uni_web.find_element_by_class_name('css-8mokm4')
    coin_select.click()
    # time.sleep(2)
    await asyncio.sleep(2)

    read_coin_price = uni_web.find_element_by_xpath('//*[@id="swap-currency-output"]/div/div[1]/input')
    uni_price = read_coin_price.get_property('value')

    input = uni_web.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[1]/input')
    # input.send_keys(ETH)
    print('Uni Price: ', uni_price)
    uni = uni_price
    prices.append(uni_price)
    # uni_web.quit()
    return uni_price



async def kyber_swap():
    # web = webdriver.Chrome()
    # web = webdriver.Chrome(options=chrome_options)
    kyber_web.get('https://www.kyberswap.com/swap/' + token1 + '-' + token2)
    # time.sleep(2)

    input = kyber_web.find_element_by_xpath('//*[@id="swap-error-trigger"]/input')
    input.send_keys(1)
    # time.sleep(2)

    input = kyber_web.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/input')
    input.send_keys(1)
    # time.sleep(2)
    await asyncio.sleep(2)

    input.click()

    # time.sleep(5)
    await asyncio.sleep(5)

    read_coin_price = kyber_web.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[1]/div/div[1]/div/div[3]/div[3]/div/div/div/span').text
    kyber_price = read_coin_price[9:18] #.get_property('value')
    print('Kyber Price: ', kyber_price)
    global kyber
    kyber = kyber_price
    prices.append(kyber)
    # kyber_web.quit()
    return kyber_price

def do_maths():
    kyber = prices[0]
    sushi = prices[1]
    uni = prices[2]

    sushi = float(sushi)
    uni = float(uni)
    kyber = float(kyber)

    change_percent_sushi_uni = (abs(sushi-uni)/uni)
    change_percent_uni_kyber = (abs(uni-kyber)/kyber)
    change_percent_kyber_sushi = (abs(kyber-sushi)/sushi)

    if change_percent_sushi_uni > target:
        print(token1 + "/" + token2 + " sushi/uni", change_percent_sushi_uni )

        # sendmail("Sushi/Uni percentage differance is " + str(change_percent_sushi_uni))

    if change_percent_uni_kyber > target:
        print(token1 + "/" + token2 + " uni/kyber", change_percent_uni_kyber)

        # sendmail("Uni/Kyber percentage differance is " + str(change_percent_uni_kyber))

    if change_percent_kyber_sushi > target:
        print(token1 + "/" + token2 + " kyber/sushi", change_percent_kyber_sushi)

        # sendmail("Kyber/Sushi percentage differance is " + str(change_percent_kyber_sushi))

    if change_percent_sushi_uni < target and change_percent_sushi_uni < target and change_percent_uni_kyber < target:
        print("No change")
        print(token1, token2)
        print("Sushi/Uni: ", change_percent_sushi_uni)
        print("Uni/Kyber: ", change_percent_uni_kyber)
        print("Kyber/Sushi: ", change_percent_kyber_sushi)
    print("----------------------------------------------------")


    return change_percent_sushi_uni, change_percent_uni_kyber, change_percent_kyber_sushi

# def sendmail(message):
#     message = message
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#
#     server.login(sender, password)
#     print("Login success")
#
#     server.sendmail(sender, receivers, message)
#     print("email has been sent")



# def main():
#     print('enter: ')
#     user_input = input()

#     print(user_input)
#     truth = False
#     if user_input == 'go':
#         truth = True
#     while truth == True:
#         do_maths()
    # time.sleep(5)
async def main():
    global sushi_web
    sushi_web = webdriver.Chrome()
    global uni_web
    uni_web = webdriver.Chrome()
    global kyber_web
    kyber_web = webdriver.Chrome()

    tasks = []
    # for i in range(10):
    # sushi_swap()
    tasks.append(asyncio.ensure_future(sushi_swap()))
    tasks.append(asyncio.ensure_future(uni_swap()))
    tasks.append(asyncio.ensure_future(kyber_swap()))
    # i+=1
    print('hi')
    await asyncio.gather(*tasks)
    # sushi_swap()
    print('hi')

while True:
    # task = []
    # task.append(asyncio.ensure_future(main()))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('PRICES: ', prices)
    do_maths()
    prices.clear()
    # loop.close()




# print("sushi price: ", sushi)
# print("uni price:   ", uni)
# print("kyber price: ", kyber)
# print("-------------------------------------")
# print("sushi/uni:   ", change_percent_sushi_uni)
# print("uni/kyber:   ", change_percent_uni_kyber)
# print("kyber/sushi: ", change_percent_kyber_sushi)



#
# IN2 = web.find_element_by_xpath('/html/body/reach-portal[4]/div[3]/div/div/div/div/div/div/div[3]/div[1]/div/div/div[6]')
# IN2.click()
