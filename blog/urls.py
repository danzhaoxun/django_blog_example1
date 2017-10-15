
import blog.views
from django.conf.urls import url,include


urlpatterns = [
    url(r'^$',blog.views.archive),
    url(r'^create/',blog.views.create_blogpost)
]