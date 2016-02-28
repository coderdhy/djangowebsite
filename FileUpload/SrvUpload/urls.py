from django.conf.urls import url

urlpatterns = [
    url(r'(?i)^$', 'SrvUpload.views.upload', name='upload'),
]
