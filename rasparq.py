#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

target_url = "https://digitarq.adbja.arquivos.pt/viewer?id=1083738"

def main():
    browser=webdriver.Firefox()
    browser.get(target_url)
    element=browser.find_element(By.ID,"ViewerControl1_TreeViewFiles")
#    element.send_keys("typing")

    link_txt = []
    for e in element.find_elements_by_class_name('TreeNode'):
        print(e.text)
        if e.text.endswith('.tif') or e.text.endswith('.TIF'):
            print('    .tif')
            if e.text not in link_txt:
                link_txt.append(e.text)
                print('    added to list')
            else:
                print('    already on list')
        else:
            print('    not .tif')

    print(len(link_txt))
    
    for a in link_txt:
        print(a)
        lnk = browser.find_element_by_xpath("//*[text()='{}']".format(a))
        print(lnk)
        lnk.click()
        time.sleep(5)
        dl_button = browser.find_element(By.ID, "ViewerControl1_HyperLinkDownload")
        dl_button.click()
        

    browser.close()

if __name__ == '__main__':
	main()
