from django.conf.urls import url
from loan.views import upload_pdf

urlpatterns = [
    url(r'^list/$', upload_pdf, name='list')
]