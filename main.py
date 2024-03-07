from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs homework 5",
    version="0.0.1"
)

list_users = [["zam", "be", "125a"]]

@app.post("/api/v1/register/")
async def register_user(username: str, email: str, password: str):
    for sublist in list_users:
        if sublist[1] == email:
            return JSONResponse(
                content="The mail has already been registered before",
                status_code=status.HTTP_409_CONFLICT
            )
        elif sublist[0] == username:
            return JSONResponse(
                content="This username already exists",
                status_code=status.HTTP_409_CONFLICT
            )

    id_user = str(uuid.uuid4())
    list_users.append([username, email, id_user])
    return {
            "username": username,
            'email': email,
            "id": id_user,
            "message": "The user was created successfully",
            "status": 200
            }

@app.get("/api/v1/user/{id}/")
async def get_user_data(id_user):
    for sublist in list_users:
        if sublist[2] == id_user:
            return {
                "username": sublist[0],
                'email': sublist[1],
                "id": id_user,
                "status": 200
            }
    return JSONResponse(
        content="This user id does not exist",
        status_code=status.HTTP_404_NOT_FOUND
    )






