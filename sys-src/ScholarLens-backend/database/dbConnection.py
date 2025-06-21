from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from database.models.author import Author
from database.models.publication import Publication
from database.models.institut import Institut
from pydantic import BaseModel

Author.model_rebuild()
Institut.model_rebuild()
Publication.model_rebuild()

# MongoDB connection details
MONGO_DETAILS = "mongodb+srv://app:ObwlSqbY8Dma5W5r@cluster0.6cecc96.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&ssl=true&tlsAllowInvalidCertificates=true"
DATABASE_NAME = "ScholarlyLens"

# Create a function to get the database connection
def get_database():
    client = AsyncIOMotorClient(MONGO_DETAILS)
    return client[DATABASE_NAME]

# Functions to be used for startup and shutdown events
async def connect_to_mongo(app):
    try:
        app.mongodb_client = AsyncIOMotorClient(MONGO_DETAILS, uuidRepresentation="standard")
        app.mongodb = app.mongodb_client[DATABASE_NAME]

        
        # Initialize Beanie with all document models
        await init_beanie(
            database=app.mongodb,
            document_models=[
                Institut,
                Publication,
                Author
            ]
        )

        print("Connected to MongoDB and initialized Beanie!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {str(e)}")
        raise

async def close_mongo_connection(app):
    app.mongodb_client.close()
    print("Closed MongoDB connection")