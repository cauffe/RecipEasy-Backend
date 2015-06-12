from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^obtain-auth-token$', obtain_jwt_token),
    url(r'^refresh-auth-token$', refresh_jwt_token),
    url(r'^verify-auth-token$', verify_jwt_token),

    url(r'^get-user-info$', GetUserInfo.as_view()),
    url(r'^register-user$', UserRegistration.as_view()),

    url(r'^recipes$', RecipeList.as_view()),
    url(r'^my-recipes$', RecipeMyList.as_view()),
    url(r'^my-favorites$', RecipeMyFavorites.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view()),
    url(r'^create-recipe$', RecipeCreate.as_view()),

    url(r'^ingredients$', IngredientListCreate.as_view()),
    url(r'^ingredients/(?P<pk>[0-9]+)$', IngredientDetail.as_view()),
    url(r'^create-ingredient$', IngredientListCreate.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]
