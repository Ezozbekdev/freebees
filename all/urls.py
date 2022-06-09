from django.urls import path
from .views import about, main, profile, ContactViews, BlogViews, Blog_detail

urlpatterns = [
    path('', main, name='main'),
    path('aboutus/', about, name='about'),
    path('portfolio/', profile, name='protfolio'),
    path('contact/', ContactViews, name='contact'),
    path('blog/', BlogViews, name='blog'),
    path('blog<int:id>/', BlogViews, name='blog-detail'),
]
