from fastapi import FastAPI
from database.dbConnection import connect_to_mongo, close_mongo_connection
from database.authorsApi import search_and_save_authors, get_all_authors, AuthorSearch


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

@app.post("/postAuthors")
async def search_authors(search: AuthorSearch):
    authors = await search_and_save_authors(search)
    return {"authors": authors}

#@app.put("/updateAuthors")
#async def update_author_endpoint(update: AuthorUpdate):
#    return await update_author(update)