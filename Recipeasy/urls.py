from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken.views import ObtainAuthToken
from views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^obtain-auth-token$', ObtainAuthToken.as_view()),
    url(r'^get-user-info$', GetUserInfo.as_view()),
    url(r'^register-user$', UserRegistration.as_view()),

    url(r'^recipes$', RecipeList.as_view()),
    url(r'^my-recipes$', MyRecipeList.as_view()),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view()),
    url(r'^create-recipe$', CreateRecipe.as_view()),

    url(r'^ingredients$', IngredientList.as_view()),
    url(r'^ingredients/(?P<pk>[0-9]+)$', IngredientDetail.as_view()),
    url(r'^create-ingredient$', CreateIngredient.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]
