
import os
from selenium import webdriver
from colorama import Fore
import random
from selenium.webdriver.common.keys import Keys
from time import time, strftime, gmtime, sleep
import threading
import time


print(f"""
░█████╗░░██████╗██████╗░███████╗░█████╗░████████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
███████║╚█████╗░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░
██╔══██║░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░
██║░░██║██████╔╝██║░░░░░███████╗╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░ Mail.com Account Maker By DumbDannyLol.
""")
accountssmade = [0]
def titlebar():
    while True:
        os.system(f"title Mail.com account maker v1 ^| {accountssmade} accounts made ^|")
titlethread = threading.Thread(target=titlebar)
titlethread.start()
print("Please verify you have a emails.txt file next to this file.")
print("How many Email Accounts would you like to make?")
numberofaccountstomake = int(input("Number Of Accounts to make:  "))
print("What email would you like the account recovery to be set to?")
recover = input("Recovery Email:  ")
print("Generating", numberofaccountstomake, "Accounts...")
accountstocreate = []

for x in range(numberofaccountstomake):
    accountstocreate.append(1)

def makeaccountmail():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://signup.mail.com")
    time.sleep(7)
    print(f"{Fore.GREEN}[+] Starting Signup Process..{Fore.RESET}")
    findaccept = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div[2]/div/div/button")
    webdriver.ActionChains(driver).move_to_element(findaccept).perform()
    webdriver.ActionChains(driver).click(findaccept).perform()
    findfirstnamebox = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[1]/div/div[2]/pos-input/input")
    webdriver.ActionChains(driver).move_to_element(findfirstnamebox).perform()
    webdriver.ActionChains(driver).click(findfirstnamebox).perform()S
    names = [Bob, Joe, Liam, Hudson, Joshua, Thomas, Andrew, Chris, Asher, Jackson, Lincoln, Dylan, Luna, Grace, Emily, Nora, Chloe, Hannah, Isla, Kinsley, Savannah, Savannah, Skylar, Anna, Eva]
    namechosen = random.random.choice(names)
    print(f"{Fore.CYAN}[+] Typing Name{Fore.RESET}", namechosen, f"{Fore.CYAN}...{Fore.RESET}")
    findfirstnamebox.send_keys(namechosen)
   
    time.sleep(3)
    findlastnamebox = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[2]/div/div[2]/pos-input/input")
    webdriver.ActionChains(driver).move_to_element(findlastnamebox).perform()
    webdriver.ActionChains(driver).click(findlastnamebox).perform()
    time.sleep(3)
    lastnames = [Smith, Johnson, Lee, Wilson, Moore, Thompson, Perez, White, Wright, Carter, Hall, Rivera, Nelson, Green, Adams]
    lastnamechosen = random.random.choice(lastnames)
    print(f"{Fore.CYAN}[+] Typing last name{Fore.RESET}", lastnamechosen, f"{Fore.CYAN}...{Fore.RESET}")
    findlastnamebox.send_keys(lastnamechosen)
    
    print(f"{Fore.GREEN}[+] Finding Email Adress element...{Fore.RESET}")
    findemailspot = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input")
    webdriver.ActionChains(driver).click(findemailspot).perform()
    lettersandnumbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWSYZ1234567890"
    madeemail = ''.join(random.choices(lettersandnumbers, k = 12))
    findemailspot.send_keys(madeemail)
    print(f"{Fore.CYAN}[+] Typed {Fore.RESET}", madeemail, f"{Fore.CYAN}In email spot...{Fore.RESET}")
    time.sleep(5)

    mrormrs = random.randint(1,2)
    if mrormrs == 1:
        print(f"{Fore.CYAN}[+] Choosing Mr Title...")
        findmrtitle = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div[1]/div/onereg-radio-wrapper[2]/pos-input-radio/label/i/span")
        webdriver.ActionChains(driver).move_to_element(findmrtitle).perform()
        webdriver.ActionChains(driver).click(findmrtitle).perform()
    elif mrormrs == 2:
        print(f"{Fore.CYAN}[+] Choosing Mrs Title...")
        findmrstitle = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[1]/pos-input-radio/label/i/span")
        webdriver.ActionChains(driver).move_to_element(findmrstitle).perform()
        webdriver.ActionChains(driver).click(findmrstitle).perform()
    time.sleep(5)

    print(f"{Fore.GREEN}[+] Finding State Element...")
    findstatechoice = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[2]/div/div/pos-input/select")
    webdriver.ActionChains(driver).move_to_element(findstatechoice).perform()
    webdriver.ActionChains(driver).click(findstatechoice).perform()
    states = 'acdfghiklymnopsrvw'
    statechoice = ''.join(random.choice(states))
    findstatechoice.send_keys(statechoice, Keys.ENTER)
    print(f"{Fore.CYAN}[+] Chose random state...{Fore.RESET}")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Finding Birth Month Element...{Fore.RESET}")
    birthmonth = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[1]/input")
    webdriver.ActionChains(driver).move_to_element(birthmonth).perform()
    webdriver.ActionChains(driver).click(birthmonth).perform()
    monthdates = '123456789'
    randommonth = ''.join(random.choice(monthdates))
    birthmonth.send_keys(0, randommonth)
    print(f"{Fore.CYAN}[+] Set Birth Month to a random month...{Fore.RESET}")
    print(f"{Fore.GREEN}[+] Finding Birth Day Element...{Fore.RESET}")
    birthday = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[2]/input")
    webdriver.ActionChains(driver).move_to_element(birthday).perform()
    webdriver.ActionChains(driver).click(birthday).perform()
    borthday = random.randint(1,29)
    birthday.send_keys(borthday)
    print(f"{Fore.CYAN}[+] Set Birthday as", borthday)
    print(f"{Fore.GREEN}[+] Finding Birth Year Element...{Fore.RESET}")
    birthyear = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[3]/input")
    randombirthyear = random.randint(70,99)
    webdriver.ActionChains(driver).move_to_element(birthday).perform()
    webdriver.ActionChains(driver).click(birthday).perform()
    birthyear.send_keys(19, randombirthyear)
    print(f"{Fore.GREEN}[+] Finding Password Element...{Fore.RESET}")
    findpassword = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[1]/div/div/pos-input/input")
    webdriver.ActionChains(driver).move_to_element(findpassword).perform()
    webdriver.ActionChains(driver).click(findpassword).perform()
    password = ''.join(random.choices(lettersandnumbers, k = 8))
    findpassword.send_keys(password)
    print(f"{Fore.CYAN}[+] Set {Fore.RESET}", password,f"{Fore.CYAN}as password...{Fore.RESET}" )
    print(f"{Fore.CYAN}[+] Repeating Password...{Fore.RESET}")
    findrepeatpassword = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div/pos-input/input")
    webdriver.ActionChains(driver).move_to_element(findrepeatpassword).perform()
    webdriver.ActionChains(driver).click(findrepeatpassword).perform()
    findrepeatpassword.send_keys(password)
    unclicksmsverify = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[3]/onereg-checkbox-wrapper/pos-input-checkbox/label/i")
    webdriver.ActionChains(driver).move_to_element(unclicksmsverify).perform()
    webdriver.ActionChains(driver).click(unclicksmsverify).perform()
    selectrecoveryemail = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[4]/onereg-checkbox-wrapper/pos-input-checkbox/label/i")
    webdriver.ActionChains(driver).move_to_element(selectrecoveryemail).perform()
    webdriver.ActionChains(driver).click(selectrecoveryemail).perform()
    recoveremail = driver.find_element_by_xpath("/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div[2]/pos-input/input")
    webdriver.ActionChains(driver).move_to_element(recoveremail).perform()
    webdriver.ActionChains(driver).click(recoveremail).perform()
    recoveremail.send_keys(recover)
    

    #reCaptcha stuff
    solvecaptcha = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
    webdriver.ActionChains(driver).move_to_element(solvecaptcha).perform()
    webdriver.ActionChains(driver).click(solvecaptcha).perform()

    with open('emails.txt', 'a') as  file_object:
      file_object.write('\n')
      file_object.write("Email: ")
      file_object.write(madeemail)
      file_object.write('@mail.com')
      file_object.write('\n')
      file_object.write('Password: ')
      file_object.write(password)
      file_object.write('\n')
      file_object.write('----------------------')



    
    
for x in accountstocreate:
  makeaccountmail()
  accountssmade.append(+1)









