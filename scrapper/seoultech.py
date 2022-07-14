import requests as req
import bs4 as bs


class SeoulTech():
    def __init__(self):
        self.url = 'https://www.seoultech.ac.kr/service/info/matters/'
        self.res = req.get(self.url)
        self.soup = bs.BeautifulSoup(self.res.text, 'html.parser')

    def get_title(self):
        title = self.soup.select('#hcms_content > div.wrap_list > table > tbody > tr:nth-child(1) > td.tit.dn2 > a')
        return (title[0].text).strip()
        
    def save_title_of_announcement(self):
        title = self.get_title()
        with open('./logs/seoultech_info_matters.log', 'w') as f:
            f.writelines(title)
                
    def check_title_of_announcement(self):
        with open('./logs/seoultech_info_matters.log', 'r') as f:
            saved_title = f.read()
        if saved_title == self.get_title():
            print('No new announcement')
            return False
        else:
            self.save_title_of_announcement()
            print(f'New announcement : {self.get_title()}')
            return True
    