from django.conf.urls import url

urlpatterns = [
    url(r'(?i)^$', 'UIUpload.views.uiaddfile', name='upload'),
]
