from serializers import UserSerializer, RecipeSerializer, NestedRecipeSerializer, IngredientSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from models import Recipe, Ingredient


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer


class GetUserInfo(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RecipeList(generics.ListAPIView):
    pagination_class = pagination.PageNumberPagination
    serializer_class = NestedRecipeSerializer
    queryset = Recipe.objects.all()


class MyRecipeList(generics.ListAPIView):
    pagination_class = pagination.PageNumberPagination
    serializer_class = NestedRecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class CreateRecipe(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer


class IngredientList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
    queryset = Recipe.objects.all()


class CreateIngredient(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
