from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import os
# Create your views here.

def mysum(request,x):
    result = sum(map(int,numbers.split("/")))
    result = sum(map(lambda s: int(s or 0),numbers.split("/")))
    return HttpResponse(result)


def hello(request ,name,age):
    return HttpResponse("안녕하세요. {}.{}살이시네요.".format(name,age))


#첫번째 방법
def post_list1(request):
    name  = 'come on!!'
    return HttpResponse('''
    <h1>aksdjango</h1>
    <p>{name}</p>
    <p>여러분의 뭐가 되어 드릴까요!! come on!!!</p>
    '''.format(name = name))


#두번째 방법
def post_list2(request):
    name = '공유'
    response = render(request, 'myapp/post_list.html', {'name': name})
    return response


#세번째 방법
def post_list3(request):
    return JsonResponse({
    'message': '안녕 파이썬!!!!!!',
    'items': ['파이썬','장고','Celery','Azure','Aws'],
    },json_dumps_params={'ensure_ascii':False})


def excel_downloads(request):
    #filepath = 'C:/Users/askdjango2/come.xlsx'
    #이게 좀더 좋은코딩이다. 밑에게 왜냐하면 base_dir이 절대 경로 즉 최상위 경로 askd
    #askdjango2 의 setting.py 를 들어가보면 base_dir에 보이는데 filepath 'C:/Users/askdjango2로 지정되어있기때문이다
    filepath = os.path.join(settings.BASE_DIR)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')#엑셀 컨텐트 타입이어서 application/vnd!~~~ 이렇게 쓰는거임
        response['Content-Dispostion'] = 'attachmen; filename = "{}"'.format(filename)
        return response