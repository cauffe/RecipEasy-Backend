from models import Recipe, Ingredient
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserRegistrationSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name',)


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe


class NestedRecipeSerializer(ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
