import graphene
from graphene_django import DjangoObjectType
from todo.models import Todo


class Todo(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    todos = graphene.List(Todo)

    def resolve_todo(self, info, **kwargs):
        return Todo.object.all()