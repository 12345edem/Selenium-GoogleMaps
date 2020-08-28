from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import random as rand
from urllib.request import urlretrieve
#chrome_options = Options()  
#chrome_options.add_argument("--headless")  

lg = 0
lt = 0
i = 0

wd = webdriver.Chrome('D:\\Soft\\Projects\\Programs\\MapsParser\\chromedriver.exe')#,chrome_options=chrome_options)
wd.get('http://www.google.com/maps')
while(i < 20):
	elem = wd.find_element_by_id("searchboxinput")
	elem.clear()
	lg = rand.uniform(-89.999, 89.999)
	lt = rand.uniform(-179.999, 179.999)
	string = str(lg) + ' ' + str(lt)
	elem.send_keys(str(string))
	elem.send_keys(Keys.RETURN)
	wait = WebDriverWait(wd, 30)
	answer = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='pane']/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]")))
	country = wd.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]")
	###############IMAGES#################
	answer = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='pane']/div/div[1]/div/div/div[1]/div[1]/button/img")))
	img = wd.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[1]/div[1]/button/img")
	src = img.get_attribute('src')
	path = 'Photos\\img' + str(i) + '.png'
	urlretrieve(src, path)
	################NAME##################
	print(country.text)
	f = open('log.log', 'a')
	f.write(str(i) + '	' +' Ш(' + str(lg) +')' + ', ' + 'Д(' + str(lt) + ') : ' + country.text + '\n')
	f.close()
	i += 1
wd.quit()

