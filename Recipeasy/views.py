from serializers import UserSerializer, RecipeSerializer, IngredientSerializer, NestedRecipeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer


class GetUserInfo(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RecipeList(generics.ListAPIView):
    serializer_class = NestedRecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer


class CreateRecipe(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer


class IngredientList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer


class CreateIngredient(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = IngredientSerializer
