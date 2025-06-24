from uuid import UUID
from fastapi import FastAPI
from database.dbConnection import connect_to_mongo, close_mongo_connection
from database.authorsApi import search_and_save_authors, get_all_authors, AuthorSearch, get_author_by_id, get_all_institutes, get_institut_by_id


app = FastAPI()

# Register database connection events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo(app)

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection(app)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/getAuthors")
async def get_authors():
    authors = await get_all_authors()
    return {"authors": authors}

@app.get("/getAuthorById/{author_id}")
async def read_author(author_id: UUID):
    return await get_author_by_id(author_id)

@app.get("/getInstitutes")
async def get_institutes():
    return await get_all_institutes();

@app.get("/getInstitutById/{institut_id}")
async def read_institut(institut_id: UUID):
    return await get_institut_by_id(institut_id)

@app.post("/postAuthors")
async def search_authors(search: AuthorSearch):
    authors = await search_and_save_authors(search)
    return {"authors": authors}

#@app.put("/updateAuthors")
#async def update_author_endpoint(update: AuthorUpdate):
#    return await update_author(update)