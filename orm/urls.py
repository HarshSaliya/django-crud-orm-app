from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('' , views.loginn , name='loginn'),
    path('signup/', views.registration , name="registration"),
    path('logout/', views.logout_view, name='logout'),


    #products

    path('product_list/' , views.product_list , name="product_list"),
    path('create_product/' , views.create_product , name="create_product"),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),

    #restaurant

    path('restaurant_list/' , views.restaurant_list , name="restaurant_list"),
    path('create_restaurnt/' , views.create_restaurnt , name="create_restaurnt"),
    path('delete_restaurnt/<int:pk>' , views.delete_restaurnt , name="delete_restaurnt"),
    path('update_restaurnt/<int:pk>' , views.update_restaurnt , name="update_restaurnt"),

    #author

    path('author_list/' , views.author_list , name="author_list"),
    path('create_author/' , views.create_author , name="create_author"),
    path('delete_author<int:pk>/' , views.delete_author , name="delete_author"),
    path('update_author<int:pk>/' , views.update_author , name="update_author"),


    #bolg
    path('blog_list/' , views.blog_list , name="blog_list"),
    path('create_blog/' , views.create_blog , name="create_blog"),
    path('update_blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),

    




]