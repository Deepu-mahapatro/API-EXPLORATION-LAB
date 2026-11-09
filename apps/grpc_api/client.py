
import grpc

from apps.grpc_api.proto import user_pb2
from apps.grpc_api.proto import user_pb2_grpc


# --------------------------------------------------
# 1. Connect to gRPC Server
# --------------------------------------------------

def main():

    channel = grpc.insecure_channel("localhost:50051")

    stub = user_pb2_grpc.UserServiceStub(channel)

    print("\nConnected to gRPC server")

    try:

        # --------------------------------------------------
        # 2. Get All Users
        # --------------------------------------------------

        print("\n========== GET ALL USERS ==========")

        response = stub.GetUsers(
            user_pb2.Empty()
        )

        for user in response.users:

            print(
                f"ID: {user.id}, "
                f"Name: {user.name}, "
                f"Email: {user.email}"
            )

        # --------------------------------------------------
        # 3. Get User By ID
        # --------------------------------------------------

        print("\n========== GET USER ==========")

        user = stub.GetUser(
            user_pb2.GetUserRequest(id=1)
        )

        print(user)

        # --------------------------------------------------
        # 4. Create User
        # --------------------------------------------------

        print("\n========== CREATE USER ==========")

        created_user = stub.CreateUser(
            user_pb2.CreateUserRequest(
                name="Asha",
                email="asha@example.com"
            )
        )

        print("Created user:")
        print(created_user)

        new_id = created_user.id

        # --------------------------------------------------
        # 5. Update User
        # --------------------------------------------------

        print("\n========== UPDATE USER ==========")

        updated_user = stub.UpdateUser(
            user_pb2.UpdateUserRequest(
                id=new_id,
                name="Asha Updated",
                email="asha.updated@example.com"
            )
        )

        print("Updated user:")
        print(updated_user)

        # --------------------------------------------------
        # 6. Delete User
        # --------------------------------------------------

        print("\n========== DELETE USER ==========")

        deleted_user = stub.DeleteUser(
            user_pb2.DeleteUserRequest(id=new_id)
        )

        print(deleted_user.message)

        # --------------------------------------------------
        # 7. Verify Deletion
        # --------------------------------------------------

        print("\n========== VERIFY DELETION ==========")

        try:

            stub.GetUser(
                user_pb2.GetUserRequest(id=new_id)
            )

        except grpc.RpcError as error:

            print("Expected error:", error.code().name)
            print("Details:", error.details())

        # --------------------------------------------------
        # 8. Get All Users Again
        # --------------------------------------------------

        print("\n========== FINAL USER LIST ==========")

        final_response = stub.GetUsers(
            user_pb2.Empty()
        )

        for user in final_response.users:
            print(user)

    except grpc.RpcError as error:

        print("\n gRPC request failed")
        print("Status:", error.code().name)
        print("Details:", error.details())

    finally:

        channel.close()

        print("\nClient connection closed")


# --------------------------------------------------
# 9. Execute Client
# --------------------------------------------------

if __name__ == "__main__":
    main()
