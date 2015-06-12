from serializers import *
from rest_framework import generics, pagination, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from models import Recipe, Ingredient


class UserRegistration(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data='User created', status=status.HTTP_201_CREATED)


class GetUserInfo(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RecipeListPagination(pagination.PageNumberPagination):
    page_size = 6


class RecipeList(generics.ListAPIView):
    pagination_class = RecipeListPagination
    serializer_class = NestedRecipeSerializer
    queryset = Recipe.objects.all()


class RecipeMyList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = RecipeListPagination
    serializer_class = NestedRecipeSerializer

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class RecipeCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
    queryset = Recipe.objects.all()
