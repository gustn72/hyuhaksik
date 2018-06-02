#!/usr/bin/env python

import urllib.request
import bs4 as bs
import json, os , re
# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

site_dic={'Stu':'http://www.hanyang.ac.kr/web/www/-248',
        'Staff':'http://www.hanyang.ac.kr/web/www/-249',
        'LoveRoom':'http://www.hanyang.ac.kr/web/www/-250',
        'NewStaff':'http://www.hanyang.ac.kr/web/www/-251',
        'NewStu':'http://www.hanyang.ac.kr/web/www/-252',
        'Dorm1':'http://www.hanyang.ac.kr/web/www/-1-',
        'Dorm2':'http://www.hanyang.ac.kr/web/www/-2-',
        'HangwonPark':'http://www.hanyang.ac.kr/web/www/-253'
}

def MakeSoup(cafeteria_name):
    source = urllib.request.urlopen(site_dic[cafeteria_name])
    soup = bs.BeautifulSoup(source,'lxml')
    return soup

def MakeCrawl():
    Modify = re.compile('[\t\n\r\f\v]')
    for cafeteria_name in site_dic:
        soup = MakeSoup(cafeteria_name)
        menulist = soup.find_all('h3')
        temp = []

        CafeInfo = soup.body.find('pre')
        CafeInfoStr = Modify.sub('',CafeInfo.text)
        for menus in menulist:
            # result = hangul.sub('', s) #한글만 선택
            s = Modify.sub('',menus.text) #메뉴를 가져온다음 공백을 없앰
            temp.append(s)

        with open(os.path.join(BASE_DIR, cafeteria_name +'.json'), 'w+') as json_file:
            if cafeteria_name in ('Dorm1','Dorm2'):
                if len(temp)==4:
                    temp[1] = '[아침] ' + temp[1]
                    temp[2] = '[점심] ' + temp[2]
                    temp[3] = '[저녁] ' + temp[3]
                elif len(temp)==3: #토요일에는 아침식사 없음
                    temp[1] = '[점심] ' + temp[1]
                    temp[2] = '[저녁] ' + temp[2]
            temp[0]=CafeInfoStr # 0에는 식당 이름이 들어있어서 없앰
            json.dump(temp, json_file)
            print(cafeteria_name +'is Writed')
#식당위치
#tab = soup.body.find('div',class_='tab-content')


# try:
#     in_box = soup.body.find_all('div',class_='in-box')
# #메뉴
#     menus=in_box[1].find_all('h3')
#     for menu in menus:
#         data.append(menu.text)
#     with open(os.path.join(BASE_DIR, '학생식당.json'), 'w+') as json_file:
#         json.dump(data, json_file)
#         print('씀')
# except:
#     pass
#
#
# #공통찬
# try:
#     CommonDish = in_box[2]
# except:
#     pass
#def RemoveEng:

if __name__== '__main__':
    MakeCrawl()
    # for cafeteria_name in site_dic:
    #     soup = MakeSoup(cafeteria_name)
    #     pricelist = soup.find_all('p',class_="price")
    #     menulist = soup.find_all('h3')
    #     Modify = re.compile('[\t\n\r\f\v]')
    #     del menulist[0]
    #     print(cafeteria_name,len(menulist),len(pricelist))
    #     for i in range(0,len(menulist)):
    #         menus = menulist[i]
    #         prices = pricelist[i]
    #         s = Modify.sub('',menus.text)
    #         print(s,prices.text)
