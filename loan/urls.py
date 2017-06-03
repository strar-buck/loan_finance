from django.conf.urls import url
from loan.views import upload_pdf,dashboard

urlpatterns = [
    url(r'^list/$', upload_pdf, name='list'),
    url(r'^dashboard/$', dashboard, name='dashboard')
]