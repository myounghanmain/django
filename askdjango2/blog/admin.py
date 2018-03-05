from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
from .models import Comment , Post

# Register your models here.

#장식자 코드 안의 post부분을 커스터마이징한부분
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','status','created_at','updated_at']
    
    actions = ['make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    
    content_size.short_description = '내용 글자수'

    def make_published(self,request,queryset):
        updated_count = queryset.update(status = 'p')
        self.message_user(request , '{}건의 포스팅을 published상태로 변경'.format(updated_count))


#admin.site.register(Post,PostAdmin)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register()