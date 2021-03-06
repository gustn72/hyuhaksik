from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from hyuhaksik.models import Menu
from urllib.request import urlopen
import json, datetime,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))




def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['학생식당', '교직원식당','사랑방', '신교직원식당', '신학생식당', '제1 생활관', '제2 생활관', '행원파크']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")
    site_dic={'학생식당':'http://www.hanyang.ac.kr/web/www/-248',
            '교직원식당':'http://www.hanyang.ac.kr/web/www/-249',
            '사랑방':'http://www.hanyang.ac.kr/web/www/-250',
            '신교직원식당':'http://www.hanyang.ac.kr/web/www/-251',
            '신학생식당':'http://www.hanyang.ac.kr/web/www/-252',
            '제1 생활관':'http://www.hanyang.ac.kr/web/www/-1-',
            '제2 생활관':'http://www.hanyang.ac.kr/web/www/-2-',
            '행원파크':'http://www.hanyang.ac.kr/web/www/-253'
    }
    try:
        MenuList = getdata(cafeteria_name)
    except:
        MenuList=''

    return JsonResponse({
            'message': {
                'text': today_date + '의 ' + cafeteria_name + ' 메뉴입니다.\n\n' + MenuList,
                'message_button': {
                'label': cafeteria_name + ' 홈페이지',
                'url':site_dic[cafeteria_name]
                }

            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['학생식당', '교직원식당','사랑방', '신교직원식당', '신학생식당', '제1 생활관', '제2 생활관', '행원파크']
            }

        })

def getdata(cafeteria_name):
    try:
        with open(os.path.join(BASE_DIR, cafeteria_name + '.json'), 'r+') as f:
            jdata = json.load(f)
            menus="\n\n".join(jdata)
    except:
        pass
    return menus
