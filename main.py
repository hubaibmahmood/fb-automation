from firefox_selenium import Selenium as s
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import platform
from deep_translator import GoogleTranslator



selenium = s()

# preference_btn = "//button[@role='menuitem']"
# preference_btn = "//panel-item[@data-l10n-id='preferences-addon-button']//button"
preference_btn = "//button[text()='Preferences']"
extension_tab = "extension"
more_options_for_extension = "//button[@aria-label='More Options']"
restore_data_btn = '//*[@id="restoreUserDataButton"]'
file_picker_id = "restoreFilePicker"
upload_file_xpath = "//button[@tooltip-title='Export/Import']"
profile_pic = '//a[@href="#"]'

accounts_class_at_login = "//a[contains(@class, '_1gbd')]"

marketplace_url = "https://www.facebook.com/marketplace/category/motorcycles"

marketplace_content_div_xpath = "//div[contains(@class, 'x1xfsgkm xqmdsaz x1cnzs8')]"
actual_products = "//a[contains(@class, 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lku1pv')]"

message_btn_xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/div[1]/div/div/div[1]"

text_area = "//textarea[contains(@class, 'x1i10hfl xggy1nq x1s07b3s xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xyorhqc xaqh0s9 x1a2a7pz x6ikm8r x10wlt62 x1pi30zi x1swvt13 xtt52l0 xh8yej3')]"

marketplace_not_available = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xi81zsa x2b8uid')]"
marketplace_not_available2 = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xi81zsa x2b8uid')]"

no_products_available = "//span[contains(@class ,'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xi81zsa x2b8uid')]"


account_not_available = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x14z4hjw x3x7a5m xngnso2 x1qb5hxa x1xlr1w8 xzsf02u x2b8uid')]"
                                                
fb_logo_at_login_place = "//img[contains(@class, 'fb_logo _8ilh img')]"

# send_message_btn = "//span[text()= 'Send Message']"
# send_message_btn_2 = "//span[text()= 'Send message']"

send_message_btn = "//span[contains(@class, 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft')]"

limit_prompt = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xzsf02u x1yc453h')]"

limit_prompt_text = "Something went wrong"


if platform.system().lower() == "darwin":
                    #  x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f x1qq9wsj
    location_selection = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f x1qq9wsj')]"

elif platform.system().lower() == "windows":
    location_selection = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f x1qq9wsj')]"

location_input_field = "//input[contains(@class, 'x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4')]"
# location_confirmation = "//div[contains(@class, 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xsyo7zv x16hj40l x10b6aqq x1yrsyyn')]"


location_radius = "//div[contains(@class, 'xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1swvt13 x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z')]"

location_radius_confirmation_id = "//div[contains(@class, 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c xdj266r xat24cr x1344otq x1de53dj xz9dl7a xsag5q8 x1n2onr6 x16tdsg8 x1ja2u2z')]"

location_confirmation = "//div[contains(@class, 'x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x4uap5 xkhd6sd xz9dl7a xsag5q8 x1n2onr6 x1ja2u2z')]"

# location_apply_btn = "//div[contains(@class,'x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67')]"
failed_buyer_message = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa')]"
                                                    
failed_buyer_message_prompt = "not all buyers can message this seller."


# location_apply_btn = "//span[text()='Apply']"

#location_apply_btn = "//div[contains(@class, 'x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67')]"
location_apply_btn = "//span[contains(@class, 'x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft')]"
confirm_identity_for_marketplace = "//span[contains(@class, 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1ill7wo x41vudc x1q74xe4 xyesn5m x1xlr1w8 xzsf02u')]"

confirm_identity_text = "confirm your identity"


driver = selenium.get("about:addons", headless=False)


if selenium.__wait_for_element__(extension_tab, "name", 10):
    user = driver.find_element("name", extension_tab)
    user.click()



if selenium.__wait_for_element__(more_options_for_extension, "xpath", 10):
    user = driver.find_element("xpath", more_options_for_extension)
    user.click()

# selenium.__random_sleep__(3, 5)

# more_option = "/html/body/div/div[2]/div/addon-list/section[1]/addon-card/div/addon-options/panel-list"
# more_option = "/html/body/div/div[2]/div/addon-card/div/addon-options/panel-list/panel-item[3]"
more_option = "//panel-item[@action='preferences']"
if selenium.__wait_for_element__(more_option, "xpath", 10):
    user = driver.find_element("xpath", more_option).click()

# selenium.__random_sleep__(3, 5)

windows = driver.window_handles

driver.switch_to.window(windows[-1])
#driver.maximize_window()


selenium.__random_sleep__(2, 3)


# print(driver.current_url)

url = driver.current_url.replace("options.html", "cookies.html?parent_url=")
# print(url)

cookies = [file for file in os.listdir(os.path.join(os.getcwd(), "cookies"))]

with open("Locations.txt", "r") as file_m:
    locations = file_m.readlines()

locations = [loc.strip() for loc in locations]
location_index = 0


for cookie in cookies:

    print(f"Using cookie {cookie}")

    marketplace = True
    account_available = True
    account_logged_in = True

    driver.get(url)
    selenium.__random_sleep__(2, 3)


    if selenium.__wait_for_element__(upload_file_xpath, "xpath", 10):
        driver.find_element("xpath", upload_file_xpath).click()
        file_input = driver.find_element("id", "file_elem")
        file_input.send_keys(os.path.join(os.getcwd(), os.path.join("cookies", cookie)))
        # file_input.send_keys(f"/Users/mac/Documents/Fiverr/Projects/Firefox automation/cookies/{cookie}")



    selenium.__random_sleep__(2, 3)

    driver.get("https://facebook.com/")

    selenium.__random_sleep__(2, 3)

    if selenium.__wait_for_element__(account_not_available, "xpath", 1):
        text_account = driver.find_element("xpath", account_not_available).text
        translated = GoogleTranslator(source='auto', target='en').translate(text_account)


        if "we need to confirm that this account belongs to you" in translated:
            account_available = False

    if account_available:

        if selenium.__wait_for_element__(fb_logo_at_login_place, "xpath", 2):
            img = driver.find_element("xpath", fb_logo_at_login_place)
            
            if "facebook" in img.get_attribute("alt").lower():
                account_logged_in = False

        if account_logged_in:
            if selenium.__wait_for_element__(profile_pic, "xpath", 2):
                driver.find_element("xpath", profile_pic).click()

            selenium.__random_sleep__(2, 3)

            driver.get(marketplace_url)

            selenium.__random_sleep__(2, 3)

            if selenium.__wait_for_element__(marketplace_not_available, "xpath", 3):
                not_available_text = driver.find_element("xpath", marketplace_not_available).text

                translated = GoogleTranslator(source='auto', target='en').translate(not_available_text)
                
                if "marketplace isn't available to you" in translated:
                    marketplace = False

            selenium.__random_sleep__(2, 3)


            if selenium.__wait_for_element__(no_products_available, "xpath", 3):
                not_available_text = driver.find_element("xpath", no_products_available).text

                translated = GoogleTranslator(source='auto', target='en').translate(not_available_text)

                if "no products in your area" in translated:
                    marketplace = False

            if "ineligible" in driver.current_url:
                marketplace = False

            # input("wait")
            if marketplace: 

                print(f"Cookie {cookie} is logged in and has marketplace too")


                selenium.__random_sleep__(2, 3)

                if selenium.__wait_for_element__(location_selection, "xpath", 10):
                    driver.find_element("xpath", location_selection).click()


                selenium.__random_sleep__(2, 3)


                if selenium.__wait_for_element__(location_input_field, "xpath", 10):
                    
                    loc = driver.find_element("xpath", location_input_field)
                    loc.clear()
                    loc.send_keys(locations[location_index])
                
                    selenium.__random_sleep__(2, 3)

                    # location_confirmation = f"//span[text()='{locations[location_index]}']"

                    if selenium.__wait_for_element__(location_confirmation, "xpath", 10):
                        el = driver.find_elements("xpath", location_confirmation)
                        el[-1].click()


                    if location_index == len(locations) - 1:
                        location_index = 0
                    else:
                        location_index += 1



                selenium.__random_sleep__(1, 2)


                if selenium.__wait_for_element__(location_radius, "xpath", 10):
                    driver.find_element("xpath", location_radius).click()
            
                    selenium.__random_sleep__(1, 2)

                    if selenium.__wait_for_element__(location_radius_confirmation_id, "xpath", 10):
                        ele = driver.find_elements("xpath", location_radius_confirmation_id)
                        ele[0].click()


                selenium.__random_sleep__(1, 2)
                
                if selenium.__wait_for_element__(location_apply_btn, 'xpath', 5):
                    btn = driver.find_element("xpath", location_apply_btn)
                    translated = GoogleTranslator(source='auto', target='en').translate(btn.text.lower())

                    if "apply" in translated:
                        btn.click()
                    

                # input("wait")
                selenium.__random_sleep__(2, 3)

                marketplace_url = driver.current_url
                change_account = False

                product_links = []
                index = 0
                messages_index = 0
                links_before = -1

                with open("Messages.txt", "r") as file_m:
                    messages = file_m.readlines()

                messages = [msg.strip() for msg in messages]


                while True:
                    count_message_failed = 0
                    

                    if selenium.__wait_for_element__(marketplace_content_div_xpath, "xpath", 10):
                        # div = driver.find_element("xpath", marketplace_content_div_xpath)
                        links = driver.find_elements("xpath", actual_products)

                    selenium.__random_sleep__(2, 3)

                    print(f"Links found {len(links)=}")

                    if links_before == len(links) and links_before >= 0:
                        print("All listings done...")
                        break
                    else:
                        links_before = len(links)

                    for link in links:
                        if link.get_attribute("href") not in product_links:
                            product_links.append(link.get_attribute("href"))


                    for _ in range(index, len(product_links)):


                        print(f"{index=} with {product_links[index]=}")
                        driver.get(product_links[index])
                        # input("wait")

                        selenium.__random_sleep__(2, 3)

                        if selenium.__wait_for_element__(message_btn_xpath, "xpath", 3):
                            # div = driver.find_element("xpath", marketplace_content_div_xpath)
                            send_message_btn_ = driver.find_element("xpath", message_btn_xpath)

                            translated = GoogleTranslator(source='auto', target='en').translate(send_message_btn_.text.lower())
                            
                            if "message again" in translated:

                                index += 1
                                continue
                            else:
                                send_message_btn_.click()

                        selenium.__random_sleep__(1, 2)
                        
                            
                        if selenium.__wait_for_element__(text_area, "xpath", 3):
                            text = driver.find_element("xpath", text_area)
                            text.clear()
                            text.send_keys(messages[messages_index])

                        selenium.__random_sleep__(2, 3)

                        if selenium.__wait_for_element__(send_message_btn, "xpath", 3):
                            btns = driver.find_elements("xpath", send_message_btn)
                            btns[-1].click()

                        # elif selenium.__wait_for_element__(send_message_btn_2, "xpath", 3):
                        #     btns = driver.find_elements("xpath", send_message_btn_2)
                        #     btns[-1].click()

                        selenium.__random_sleep__(2, 4)
                        
                        #checking for Not all buyers can message this seller.
                        if selenium.__wait_for_element__(failed_buyer_message, "xpath", 2):
                            prompt = driver.find_element("xpath", failed_buyer_message).text

                            translated = GoogleTranslator(source='auto', target='en').translate(prompt)


                            if failed_buyer_message_prompt in translated.lower():
                                print("Can't send message to this buyer")
                                # change_account= True

                                index += 1

                                if count_message_failed >=3:
                                    break
                                else:
                                    count_message_failed += 1
                                    continue

                        elif selenium.__wait_for_element__(limit_prompt, "xpath", 2):
                            prompt = driver.find_element("xpath", limit_prompt).text

                            translated = GoogleTranslator(source='auto', target='en').translate(prompt)

                            if limit_prompt_text in translated:
                                print("Message sending limit reached!")
                                # change_account= True
                                break

                        selenium.__random_sleep__(2, 4)

                        if selenium.__wait_for_element__(confirm_identity_for_marketplace, "xpath", 3):
                            prompt = driver.find_element("xpath", confirm_identity_for_marketplace).text

                            translated = GoogleTranslator(source='auto', target='en').translate(prompt)
                            
                            if "confirm your identity" in translated.lower():
                                print("Identity required for the marketplace!")
                                # change_account= True
                                break

                        if messages_index == len(messages) - 1:
                            messages_index = 0

                        else:
                            messages_index += 1

                        index += 1

                    # if change_account:
                    #     break  
                    else:
                        driver.get(marketplace_url)
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        selenium.__random_sleep__(3, 5)

                        continue

                    break  

                    # input("Wait kro re baba")

            else:
                print("Marketplace or products are not available...")

        else:
            print("Account not logged in....")

    else:
        print("Account not available...")
