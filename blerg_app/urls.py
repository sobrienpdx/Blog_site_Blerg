from django.urls import path
from . import views

app_name = 'blerg_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
	path('search_blerg/', views.search_blerg, name='search_blerg'),
	path('detail/<int:pk>', views.comment, name='comment'),
	path('<title>/', views.visit_blerg, name='visit_blerg'),#the <title> variable is what gets passed into the views.whatever when you call it. You can put as many variables as you want there (i.e.'<title>/<variable>') as long as there are arguements in the view to recieve the information. The way to access the HTML code is by having the view call it, not by this page. The variables that come through here can be grabbed directly from the nav bar or from input in the html forms


]