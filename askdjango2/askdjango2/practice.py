

#----- zero-----
'''
blog/0001
blog/0002
blog/0003
blog/0004
blog/0005   <--- 00006 마이그레이션만 수행 : python manage.py migrate blog 0006 (backward)
blog/0006
blog/0007   <--- 0007 취소 : python manage.py migrate blog (forward)

모든 migrate 순차적으로 취소 할라면 : <--- python manage.py migrate blog zero

python manage.py migrate blog '''

