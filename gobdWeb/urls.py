"""delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from django.contrib.auth import views as deliver_views
import accountinfo
from main import views, apis
from main.views import *



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^celery/', views.celery_task_checker, name='celery_task_checker'),

    url(r'^api_auth_token/', views.get_auth_token, name='gblapi'),

    url(r'^store/signin/', auth_views.LoginView.as_view(),{'template_name':'store/signin.html'}, name="store-signin" ),
    url(r'^store/signout', auth_views.LogoutView.as_view(),{'next_page': '/store/signin'}, name="store-signout"),
    url(r'^store/signup', views.store_signup, name="store-signup"),
    url(r'^store/sign-up', views.auth_signup, name="auth-store-signup"),
    url(r'^store/$', views.store_home, name='store_home'),


    url(r'^store/accounts/$', views.store_account, name="store_account"),
    url(r'^store/tasks/$', views.store_tasks, name="store_tasks"),
    url(r'^store/tasks/details/(?P<pk>\d+)/', views.TaskDetails.as_view(), name="task_details"),
    url(r'^store/create_task/$', views.create_task, name="create_task"),
    url(r'^api/store/cancel_task/$', apis.store_manager_cancel_task),

    url(r'^api/store/task/notification/(?P<last_request_time>.+)/$', apis.store_task_notification),

    url(r'^deliver/signin/', auth_views.LoginView.as_view(),{'template_name':'deliver/signin.html'}, name="delivery_boy-signin" ),
    url(r'^deliver/signout', auth_views.LogoutView.as_view(),{'next_page': '/deliver/signin'}, name="delivery_boy-signout"),
    url(r'^deliver/signup', views.delivery_boy_signup, name="delivery_boy-signup"),
    url(r'^deliver/$', views.delivery_boy_home, name='delivery_boy_home'),

    url(r'^deliver/accounts/$', views.delivery_boy_account, name='delivery_boy_account'),
    url(r'^deliver/tasks/$', views.deliver_tasks, name="deliver_tasks"),
    #APIs for Deliver boy


    url(r'^api/deliver/task/ready/$', apis.delivery_boy_ready_new_tasks),
    url(r'^api/deliver/task/accept/$', apis.delivery_boy_accept_task),
    url(r'^api/deliver/task/latest/$', apis.delivery_boy_get_latest_task),
    url(r'^api/deliver/task/complete/$', apis.delivery_boy_complete_task),
    url(r'^api/deliver/task/reject/$', apis.delivery_boy_reject_task),
    url(r'^api/deliver/task/completed_tasks/$', apis.get_deliver_boy_completed_tasks),

    url(r'^accounts/',include('accountinfo.urls')),

    #report url
    # url(r'^generate_tc/$', views.GenerateTc, name='generate_tc'),
    # url(r'^generar_pdf/$', views.generar_pdf, name='pdf'),
    # url('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    url('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    url(r'^$', views.roothome, name="home"),
    url(r'^services/', views.services, name='services'),
    url(r'^whygobd/', views.whygobd, name='whygobd'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^contact/', views.contact, name='contact'),
    # url(r'^djga/', include('google_analytics.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = handler404
handler500 = handler500

