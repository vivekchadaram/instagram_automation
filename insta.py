#--ARLEEV--

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random



class Bot():

    links = []
    links_1=[]

    def __init__(self):
        self.login(input("Enter Username : "),input("Enter Password : "))

        self.Follow_Suggestions()
        self.Follow_User()
        self.Follow_Tags()
        self.Unfollow_User()
        self.Unfollow_tags()
        self.Unfollow_Username()             
        self.like_by_tags(input("Enter Tag Name : "))
        self.like_by_username(input("Enter Username : "))
        link=input("Enter link : ")
        self.sharing_a_post(link,1)
        print(self.commenting_users_feed(input("Enter Username : ")))
        print(self.comment_your_feed(3))
        print(self.comment_using_tags(input("Enter tagname : "),3))
        



    def login(self,username,pwd):

        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_ip=self.driver.find_element_by_xpath("//input[@name='username']")
        username_ip.send_keys(username)
        pass_ip=self.driver.find_element_by_xpath("//input[@name='password']")
        pass_ip.send_keys(pwd)
        login_button=self.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
        y1=input("Y/N ? ")
        if y1 == "Y":
            info_allow_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button")
            info_allow_button.click()
        else:
            info_notnow_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
            info_notnow_button.click()
        y2=input("Y/N ? ")
        if y2 == "Y":
            notif_allow_button=self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
            notif_allow_button.click()
        else:
            notif_notnow_button=self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            notif_notnow_button.click()
    
    def Follow_Suggestions(self):
        sleep(8)
        self.driver.get("https://www.instagram.com/explore/people/")
        sleep(7)
        Follow_lst= self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")
        sleep(5)
        n=int(input("Enter no.of followers you want to follow: "))
        for i in range(n):
            Follow_lst[i].click()
    
    def Follow_User(self):
        User_inp= input("Enter Username you want to Follow : ")
        self.driver.get("https://www.instagram.com/"+User_inp+"/")
        sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
    
    def Follow_Tags(self):
        tag=input("enter a tag you want to follow: ")
        sleep(5)
        Search_tags= self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        sleep(2)
        Search_tags.send_keys('#'+tag)
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(10)
        self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
    
    def Unfollow_User(self):
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click()
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div").click()
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        sleep(8)
        Unfollow_lst= self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")
        u= int(input("Enter no.of followers you want to unfollow: "))
        for i in range(u):
            Unfollow_lst[i].click()
            sleep(5)
            Confirm =input("Y/N ? ")
            sleep(5)
            if Confirm == "Y":      
                Confirm_button=self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")
                Confirm_button.click()
            else:
                DontConfirm_button=self.driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
                DontConfirm_button.click()

    def Unfollow_tags(self):
        n=int(input("Enter the number of tags you want to unfollow : ")) 
        for i in range(n):
            tag=input("Enter Tag Name : ")
            search_box=self.driver.find_element_by_xpath("//input[@placeholder='Search']")
            search_box.send_keys("#"+tag)
            sleep(5)
            self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
            sleep(5)
            try:
                x=self.driver.find_element_by_xpath("//button[contains(text(),'Following')]")
                x.click()
            except:
                print(tag," Not Following")
            
                    
    def Unfollow_Username(self):
        User_inp_= input("Enter Username you want to Unfollow : ")
        self.driver.get("https://www.instagram.com/"+User_inp_+"/")
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button").click() 
        Confirm =input("Y/N ? ")
        sleep(5)
        if Confirm == "Y":      
            Confirm_button=self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")
            Confirm_button.click()
        else:
            DontConfirm_button=self.driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
            DontConfirm_button.click() 

    
    def like_by_tags(self,tag):
        search_box=self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box.send_keys("#"+tag)
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        links=self.driver.find_elements_by_tag_name("a")
        
        def condition(link):
            return ".com/p/" in link.get_attribute("href")
        valid_links = list(filter(condition,links))

        for i in range(3):
            link=valid_links[i].get_attribute("href")
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)

            #liking
            self.driver.find_element_by_css_selector("#react-root > section > main > div > div.ltEKP > article > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button").click()
            sleep(3)
    

    def like_by_username(self,user_name):
        search_box1=self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box1.send_keys("@"+user_name)
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        links_1=self.driver.find_elements_by_tag_name("a")
        
        def condition(link):
            return ".com/p/" in link.get_attribute("href")
        valid_links = list(filter(condition,links_1))

        for i in range(3):
            link=valid_links[i].get_attribute("href")
            if link not in self.links_1:
                self.links_1.append(link)
        
        for link in self.links_1:
            self.driver.get(link)
            sleep(3)

            #liking
            self.driver.find_element_by_css_selector("#react-root > section > main > div > div.ltEKP > article > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.ltpMr.Slqrh > span.fr66n > button").click()
            sleep(3)


    def sharing_a_post(self,link,n):
        self.driver.get(link)
        sleep(4)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[3]/button").click()
        sleep(4)
        list_select=self.driver.find_elements_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[2]/div/div[3]/button")
        i=0
        j=0
        while i<n and i<len(list_select):
            list_select[i].click()
            i+=1
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[4]/button").click()

        
    def commenting_users_feed(self,user,n=3):
        comments=["WOW","cool","Amazing man!"]
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(user))
        sleep(4)
        self.driver.get("https://www.instagram.com/"+user+"/")
        sleep(4)
        links=self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return ".com/p/" in link.get_attribute("href")
        valid_links=list(filter(condition,links))
        sleep(4)
        links_hrefs = [link.get_attribute('href') for link in valid_links]
        i=0
        while i<n and i<len(links_hrefs):
            self.driver.get(links_hrefs[i])
            sleep(4)
            self.driver.find_element_by_class_name("RxpZH").click()
            sleep(10)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(random.choice(comments))
            sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
            i+=1
        return "Done commenting "+user+" feed"
    
    
    def comment_your_feed(self,n):
        self.driver.get("https://www.instagram.com/")
        comments=["WOW","cool","Amazing man!"]
        sleep(4)
        links=self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return ".com/p/" in link.get_attribute("href") and "/liked_by/" not in link.get_attribute("href")
        valid_links=list(filter(condition,links))
        sleep(4)
        links_hrefs = list(set([link.get_attribute('href') for link in valid_links]))
        print(links_hrefs)
        i=0
        while i<n and i< len(links_hrefs):
            try:
                self.driver.get(links_hrefs[i])
                sleep(4)
                self.driver.find_element_by_class_name("RxpZH").click()
                sleep(4)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(random.choice(comments))
                sleep(4)
                self.driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
                i+=1
            except:
                continue
        return "Done commenting feed"
    
    def comment_using_tags(self,tag,n):
        comments=["WOW","cool","Amazing man!"]
        self.driver.get("https://www.instagram.com/explore/tags/"+tag+"/")
        sleep(2)
        links=self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return ".com/p/" in link.get_attribute("href")
        valid_links=list(filter(condition,links))
        sleep(2)
        links_hrefs = [link.get_attribute('href') for link in valid_links]
        for i in range(n):
            self.driver.get(links_hrefs[i])
            sleep(2)
            self.driver.find_element_by_class_name("X7cDz").click()
            sleep(2)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(random.choice(comments))
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Post')]").click()
        return "Done commenting "+tag
    
    
    


    


        
def main():
    my_bot=Bot()

if __name__=="__main__":
    main()
