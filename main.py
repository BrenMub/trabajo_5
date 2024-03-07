from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs homework 5",
    version="0.0.1"
)

list_users = [["zam", "be"]]

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

    list_users.append([username, email])
    print("prueba")
    return {
            "username": username,
            'email': email,
            "id": str(uuid.uuid4()),
            "message": "The user was created successfully",
            "status": 200
            }







