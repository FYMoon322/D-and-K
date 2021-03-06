from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.png'), name='favicon'),
    path('', views.news_form),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.Logout.as_view()),
    path('register/', views.register),
    path('homepage/<int:user_id>', views.homepage),
    path('access_denied/', views.access_denied),
    path('api/user', views.UserApi.as_view()),
    path('api/likes', views.LikeApiView.as_view()),
    path('api/likes/<str:unique_parameter>', views.LikeApiView.as_view()),
    path('api/comments', views.CommentaryAPI.as_view()),
    path('api/comments/<int:post_id>/<int:user_id>', views.CommentaryListAPI.as_view()),
    path('api/comments/<int:pk>', views.CommentaryAPI.as_view()),
    path('api/news/<int:news_id>', views.NewsAPI.as_view()),
    path('api/reposts', views.RepostListAPI.as_view()),
    path('api/reposts/<int:pk>', views.RepostAPI.as_view()),
    path('api/findpost/<int:repost_id>', views.FindPost.as_view()),
    path('origin/<int:repost_id>', views.repost_origin),
    path('show_post/<int:post_id>', views.show_post),
    path('api/search_user/<str:request_api>', views.SearchUserAPI.as_view()),
    path('api/users_relationship/<int:user1_id>/<int:user2_id>', views.UsersRelationship.as_view()),
    path('api/friends/<int:user1_id>/<int:user2_id>', views.FriendsAPI.as_view()),
    path('api/friends', views.FriendsAPI.as_view()),
    path('api/friends/<int:user_id>', views.FriendsAPI.as_view()),
    path('api/friends_requests', views.FriendsRequestAPI.as_view()),
    path('api/friends_requests/<int:user1_id>/<int:user2_id>', views.FriendsRequestAPI.as_view()),
    path('api/subscriber/<int:user1_id>/<int:user2_id>', views.SubscriberAPI.as_view()),
    path('api/subscriber', views.SubscriberAPI.as_view()),
    path('friends/<int:user_id>', views.show_friends),
    path('find_user/', views.find_user),
    path('messages/', views.chats),
    path('messages/<int:chat_id>', views.show_chat),
    path('api/chats/<int:uid1>/<int:uid2>', views.ChatsAPI.as_view()),
    path('api/status', views.StatusAPI.as_view()),
    path('groups/<int:group_id>', views.show_group),
    path('api/community/<int:pk>', views.CommunityApi.as_view()),
    path('api/community', views.CommunityApi.as_view()),
    path('api/user_community/<int:community_pk>/<int:user_pk>', views.UserCommunityStatus.as_view()),
    path('api/user_community/<int:community_pk>/<int:user_pk>/<int:status>', views.UserCommunityStatus.as_view()),
    path('api/user_community', views.UserCommunityStatus.as_view()),
    path('show_members/<int:group_id>/', views.show_members),
    path('api/community_post/<int:news_id>', views.CommunityPostAPI.as_view()),
    path('user_groups/<int:user_id>/', views.users_groups),
    path('create_group/', views.create_group)
]
