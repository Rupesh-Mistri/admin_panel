

from django.urls import path
from admin_sample.views import (index, user_login, user_dashboard, seller_login, seller_dashboard,user_signup,seller_signup,seller_logout,user_logout,
                                user_order_list
                                )

urlpatterns = [
    path('',index,name="index"),
    path('user_login',user_login,name="user_login"),
    path('user_dashboard',user_dashboard,name="user_dashboard"),
    path('seller_login',seller_login,name="seller_login"),
    path('seller_dashboard',seller_dashboard,name="seller_dashboard"),
    path('user_signup',user_signup,name="user_signup"),
    path('seller_signup',seller_signup,name="seller_signup"),
    path('seller_logout',seller_logout,name="seller_logout"),
    path('user_logout',user_logout,name="user_logout"),
    path('user_order_list',user_order_list,name="user_order_list"),
]
