from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from database.models.author import Author


# MongoDB connection details
MONGO_DETAILS = "mongodb+srv://app:ObwlSqbY8Dma5W5r@cluster0.6cecc96.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "ScholarlyLens"

# Create a function to get the database connection
def get_database():
    client = AsyncIOMotorClient(MONGO_DETAILS)
    return client[DATABASE_NAME]

# Functions to be used for startup and shutdown events
async def connect_to_mongo(app):
    app.mongodb_client = AsyncIOMotorClient(MONGO_DETAILS)
    app.mongodb = app.mongodb_client[DATABASE_NAME]
    
    # Initialize Beanie
    await init_beanie(
        database=app.mongodb,
        document_models=[
            Author
        ]
    )
    print("Connected to MongoDB and initialized Beanie!")

async def close_mongo_connection(app):
    app.mongodb_client.close()
    print("Closed MongoDB connection")