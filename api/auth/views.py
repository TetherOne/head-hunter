# from fastapi import APIRouter, Form, HTTPException, Depends
# from starlette import status
#
# from api.auth import utils
# from api.auth.schemas import UserSchema
# from core.models import db_helper, User
#
# router = APIRouter()
#
#
#
# def validate_auth_user(
#     username: str = Form(),
#     password: str = Form(),
#     email: str = Form(),
# ):
#
#
#
#
# @router.post("/login")
# def auth_user(
#     user: UserSchema = Depends(validate_auth_user),
# ):
#     jwt_payload = {
#         "sub": user.id,
#         "username": user.username,
#         "email": user.email,
#     }
#     token = utils.encode_jwt(jwt_payload)
#     return {
#         "access_token": token,
#         "token_type": "bearer",
#     }
