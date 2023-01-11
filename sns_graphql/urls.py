from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from sns_graphql.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
]
