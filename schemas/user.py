# Normal way
from bson import ObjectId

def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "password":item["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

# worst way 
def userEntity1(item) -> dict:
    return {
        {
            # "_id":str(item["_id"]),
  "id": item["id"],
  "title": item["title"],
  "description": item["description"],
  "type": item["type"],
  "release_year": item["release_year"],
  "age_certification": item["age_certification"],
  "genres": item["genres"],
  "production_countries": item["production_countries"],
  "imdb_score": item["imdb_score"]
}
    }