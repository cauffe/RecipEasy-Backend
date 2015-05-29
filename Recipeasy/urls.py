from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from views import GetUserInfo, UserRegistration


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^obtain-auth-token/', obtain_auth_token),
    url(r'^get-user-info/', GetUserInfo.as_view()),
    url(r'^register-user/', UserRegistration.as_view()),
]
