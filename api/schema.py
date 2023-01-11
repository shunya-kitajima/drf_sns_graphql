from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphql_relay import from_global_id
from django.contrib.auth.models import User
from .models import Profile


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            "username": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)


class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = {
            "user_prof__username": ["icontains"],
        }
        interfaces = (relay.Node,)

