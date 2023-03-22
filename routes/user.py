from fastapi import APIRouter
from models.user import User ,Movie ,Upadte_Movie
from config.db import conn 
from schemas.user import serializeDict, serializeList,userEntity1
from bson import ObjectId
user = APIRouter() 

@user.get('/')
async def find_all_users():
    return serializeList(conn.local.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

@user.put('/{id}')
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))

#   Retrieve all the records of movies and shows in database
@user.get('/apigetdata')
async def get_all_records():
    return serializeList(conn.Database.netflix.find())

#	Display the movie and show’s detail using title
@user.get('/api/{title}')
async def search_record_by_title(title):
    return serializeDict(conn.Database.netflix.find_one({"title":title}))

#  Insert the new movie and show
@user.post('/api')
async def insert_record(movie: Movie):
    conn.Database.netflix.insert_one(dict(movie))
    return serializeList(conn.Database.netflix.find({"title":movie.title}))

#   Update the record using title. (By update only title, description and imdb score)
@user.put('/api/{title}')
async def update_record_by_title(title,update_movie: Upadte_Movie):
    conn.Database.netflix.find_one_and_update({"title":title},{
        "$set":dict(update_movie)
    })
    return serializeDict(conn.Database.netflix.find_one({"title":title}))

#   Delete the record using title
@user.delete('/api/{title}')
async def delete_record_by_title(title):
    return serializeDict(conn.Database.netflix.find_one_and_delete({"title":title}))