from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("about/", hello.views.about, name="about"),
    path("accomplished-events/", hello.views.recent, name="Accomplished_Events"),
    path("support/", hello.views.support, name="support"),
    path("contact/", hello.views.contact, name="contact"),
    
    path("admin/", admin.site.urls),
]
