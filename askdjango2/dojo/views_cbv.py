from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import os
#oop 를 통한 효율적인 개발방식
#왜냐 string이라는 함수를 따로 만들어 템플릿을 postlistview1에 
#넣어주었기때문

class PostListView1(View):
    def get(self, requset):
        name  = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
            <h1>asjdasdasd</h1>
            <p>{name}</p>
            <p>feel so good</p>
        '''
post_list1 = PostListView1.as_view()



class PostListView2(View):
    template_name = 'dojo/post_list.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context
post_list2 = PostListView2.as_view()

class PostListView3(View):
    pass



class ExcelDownloadsView(View):
    pass