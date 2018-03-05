

#쿼리 셋만들때 sql 에 필드 추가하는 코드
'''
Post.objects
Post.objects.all()
from django.db import connection
Post?? 
'''
#추가하는 구체적내용
# Post.objects.create(author='명한민',title='텍스트제목',content='텍스트내용',status='d')

'''
for post in Post.objects.all():
    print(post) ->str(post) ->post.__str()을 결국 실행시킨거임


데이터 쿼리셋에 다가가는 코드임 특히 저 filter함수 를 통해 데이터를 받을 수 있음


import random
for i in range(1000):
        status = random.choice(['d','p','w'])
        Post.objects.create(author='명한민',title='제목#{}'.format(i),content='테스트 내용',status=status)

Post.object.all().count()

qs1 = Post.object.filter(title__icontains='1',title__endswith='3')
print(qs1) 딱 print하는 부분에서db에 직접적으로 연결됨


이 코드는 sql 즉 db에 어떤 항목이 있고 변화했는지 알아보기 위한 코드임
from django.db import connection
connection.queries[-1]

오늘 setup 한 목록
django == 1.10.5
django-debug-toolbar
django-extensions
ipython[notebook]


'''