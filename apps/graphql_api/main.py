
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry


# --------------------------------------------------
# 1. Create FastAPI Application
# --------------------------------------------------

app = FastAPI(
    title="API Exploration Lab - GraphQL",
    description="GraphQL User Management API",
    version="1.0.0"
)


# --------------------------------------------------
# 2. Define User GraphQL Type
# --------------------------------------------------

@strawberry.type
class User:
    id: int
    name: str
    email: str


# --------------------------------------------------
# 3. Sample User Data
# --------------------------------------------------

users_data = [
    User(id=1, name="Deepu", email="deepu@example.com"),
    User(id=2, name="Rahul", email="rahul@example.com"),
    User(id=3, name="Kiran", email="kiran@example.com")
]


# --------------------------------------------------
# 4. Define GraphQL Query Operations
# --------------------------------------------------

@strawberry.type
class Query:

    # Get all users
    @strawberry.field
    def users(self) -> list[User]:
        return users_data

    # Get user by ID
    @strawberry.field
    def user(self, id: int) -> User | None:
        for user in users_data:
            if user.id == id:
                return user

        return None

    # Hello query
    @strawberry.field
    def hello(self) -> str:
        return "Hello! GraphQL is working."


# --------------------------------------------------
# 5. Define GraphQL Mutation Operations
# --------------------------------------------------

@strawberry.type
class Mutation:

    # Create user
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:

        new_id = max(
            (user.id for user in users_data),
            default=0
        ) + 1

        new_user = User(
            id=new_id,
            name=name,
            email=email
        )

        users_data.append(new_user)

        return new_user

    # Update user
    @strawberry.mutation
    def update_user(
        self,
        id: int,
        name: str | None = None,
        email: str | None = None
    ) -> User | None:

        for user in users_data:
            if user.id == id:

                if name is not None:
                    user.name = name

                if email is not None:
                    user.email = email

                return user

        return None

    # Delete user
    @strawberry.mutation
    def delete_user(self, id: int) -> bool:

        for index, user in enumerate(users_data):
            if user.id == id:
                users_data.pop(index)
                return True

        return False


# --------------------------------------------------
# 6. Create GraphQL Schema
# --------------------------------------------------

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)


# --------------------------------------------------
# 7. Create GraphQL Router
# --------------------------------------------------

graphql_app = GraphQLRouter(schema)


# --------------------------------------------------
# 8. Register GraphQL Endpoint
# --------------------------------------------------

app.include_router(
    graphql_app,
    prefix="/graphql"
)


# --------------------------------------------------
# 9. Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to GraphQL API Exploration Lab"
    }
