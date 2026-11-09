
from concurrent import futures
import grpc
from threading import Lock

from apps.grpc_api.proto import user_pb2
from apps.grpc_api.proto import user_pb2_grpc


# --------------------------------------------------
# 1. Create User Service Implementation
# --------------------------------------------------

class UserService(user_pb2_grpc.UserServiceServicer):

    def __init__(self):

        # In-memory user storage
        self.users = {
            1: {
                "id": 1,
                "name": "Deepu",
                "email": "deepu@example.com"
            },
            2: {
                "id": 2,
                "name": "Rahul",
                "email": "rahul@example.com"
            },
            3: {
                "id": 3,
                "name": "Kiran",
                "email": "kiran@example.com"
            }
        }

        self.next_id = 4

        # Protect shared data from concurrent modifications
        self.lock = Lock()

    # --------------------------------------------------
    # 2. Get All Users
    # --------------------------------------------------

    def GetUsers(self, request, context):

        with self.lock:

            users = [
                user_pb2.UserResponse(
                    id=user["id"],
                    name=user["name"],
                    email=user["email"]
                )
                for user in self.users.values()
            ]

        return user_pb2.UserListResponse(users=users)

    # --------------------------------------------------
    # 3. Get User By ID
    # --------------------------------------------------

    def GetUser(self, request, context):

        if request.id <= 0:
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "User ID must be greater than zero"
            )

        with self.lock:

            user = self.users.get(request.id)

            if user is None:
                context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    "User not found"
                )

            return user_pb2.UserResponse(
                id=user["id"],
                name=user["name"],
                email=user["email"]
            )

    # --------------------------------------------------
    # 4. Create User
    # --------------------------------------------------

    def CreateUser(self, request, context):

        name = request.name.strip()
        email = request.email.strip()

        if not name or not email:
            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Name and email are required"
            )

        with self.lock:

            for user in self.users.values():

                if user["email"].lower() == email.lower():

                    context.abort(
                        grpc.StatusCode.ALREADY_EXISTS,
                        "Email already exists"
                    )

            new_user = {
                "id": self.next_id,
                "name": name,
                "email": email
            }

            self.users[self.next_id] = new_user

            self.next_id += 1

            return user_pb2.UserResponse(
                id=new_user["id"],
                name=new_user["name"],
                email=new_user["email"]
            )

    # --------------------------------------------------
    # 5. Update User
    # --------------------------------------------------

    def UpdateUser(self, request, context):

        name = request.name.strip()
        email = request.email.strip()

        if request.id <= 0 or not name or not email:

            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "Valid ID, name and email are required"
            )

        with self.lock:

            user = self.users.get(request.id)

            if user is None:

                context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    "User not found"
                )

            for other_id, other_user in self.users.items():

                if (
                    other_id != request.id
                    and other_user["email"].lower() == email.lower()
                ):

                    context.abort(
                        grpc.StatusCode.ALREADY_EXISTS,
                        "Email already exists"
                    )

            user["name"] = name
            user["email"] = email

            return user_pb2.UserResponse(
                id=user["id"],
                name=user["name"],
                email=user["email"]
            )

    # --------------------------------------------------
    # 6. Delete User
    # --------------------------------------------------

    def DeleteUser(self, request, context):

        if request.id <= 0:

            context.abort(
                grpc.StatusCode.INVALID_ARGUMENT,
                "User ID must be greater than zero"
            )

        with self.lock:

            if request.id not in self.users:

                context.abort(
                    grpc.StatusCode.NOT_FOUND,
                    "User not found"
                )

            del self.users[request.id]

        return user_pb2.DeleteUserResponse(
            success=True,
            message="User deleted successfully"
        )


# --------------------------------------------------
# 7. Start gRPC Server
# --------------------------------------------------

def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    user_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(),
        server
    )

    port = server.add_insecure_port("127.0.0.1:50051")

    if port == 0:
        raise RuntimeError("Could not bind to gRPC port 50051")

    server.start()

    print("gRPC server started successfully")
    print("Server address: localhost:50051")
    print("Waiting for client requests...")

    try:
        server.wait_for_termination()

    except KeyboardInterrupt:
        print("Shutting down gRPC server...")
        server.stop(grace=5).wait()


if __name__ == "__main__":
    serve()
