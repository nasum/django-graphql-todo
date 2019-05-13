import graphene
from graphene_django import DjangoObjectType
from todo.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()

class CreateTodo(graphene.Mutation):
    class Arguments:
        description = graphene.String()
        done = graphene.Boolean()

    todo = graphene.Field(lambda :TodoType)

    def mutate(self, info, description, done):
        todo = Todo.objects.create(description=description, done=done)
        return CreateTodo(todo=todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()