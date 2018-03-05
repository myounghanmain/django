from django.shortcuts import get_object_or_404,render
from .models import Post
from django.http import Http404
# Create your views here.

def post_list(request):
    qs = Post.objects.all() # 데이터베이스 접근
    
    q = request.GET.get('q','')  #q는 models.py에 있는 q이며 그걸 가져와서 내가 검색하면 그것만 보여주게 끔하는코드구현
    if q:
        qs =qs.filter(title__icontains=q)
    return render(request , 'blog/post_list.html',{
        'post_list':qs,
        'q':q,    #인자로 넘길때 사용되는 코드
    })

def post_detail(request, id):
    '''
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
        '''
    #위코드랑 동일코드임
    post = get_object_or_404(Post,id=id) 
    return render(request,'blog/post_detail.html',{
        'post':post,
})