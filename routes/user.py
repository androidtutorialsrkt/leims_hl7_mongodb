from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity                     #for getting single & list of user, use this line
from bson import ObjectId


user = APIRouter() 



@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())   


@user.post('/')
async def create_users(user:User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find()) 


@user.put('/{id}')
async def update_user(id,user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)})) 

@user.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)})) 


@user.get('/{id}') 
async def find_one_user(id):
  return userEntity(conn.local.user.find_one({"_id":ObjectId(id)})) 



 
