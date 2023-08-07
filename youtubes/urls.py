from django.urls import path
from.views import VideoList , VideoDetail , CommentList , CommentDetail
app_name = 'youtubes'
urlpatterns=[
    path('', VideoList.as_view() , name='video_list'),
    path('<int:pk>/', VideoDetail.as_view() , name='video_detail'),
    path('comment/', CommentList.as_view() , name='comment_list'),
    path('comment/<int:pk>', CommentDetail.as_view() , name='comment_detail'),
]