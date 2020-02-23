
from django.contrib import admin
from django.urls import  include, path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("ai_image/",include("ai_image.urls"))
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEIDA_URL,document_root=settings.MEDIA_ROOT)
