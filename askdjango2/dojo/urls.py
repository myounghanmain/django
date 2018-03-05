from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    #(?P ) : 이 영역의 문자열에 정규표현식을 적용해서
    #\d+ : \d+ 패턴에 부합된다면
    # <x> : x 라는 변수명으로 인자를 넘기겠다.
    # 뷰의 인자로 넘겨받은 값들은 모두 문자열 타입입니다.
    url(r'^sum/(?P<x>\d+)/$',views.mysum),
   # 숫자가 하나가 나오는케이스임 ?P<x>
    url(r"^sum/(?P<numbers>[\d/]+)/$",views.mysum),
    #                      숫자를 존나 받아서 마지막에 /친거임
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),
    url(r'^list1/$',views.post_list1),
    url(r'^list2/$',views.post_list2),
    url(r'^list3/$',views.post_list3),
    url(r'^excel/$',views.excel_downloads),

    url(r'^cbv/list1/$',views_cbv.post_list1),
    url(r'^cbv/list2/$',views_cbv.post_list2),
    #url(r'^cbv/list3/$',views_cbv.post_list3),
    #url(r'^cbv/excel/$',views_cbv.excel_downloads),
]