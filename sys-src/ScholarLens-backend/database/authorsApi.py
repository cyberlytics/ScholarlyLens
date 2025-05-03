from scholarly import scholarly
from database.dbConnection import connect_to_mongo, close_mongo_connection
from database.models.author import Author
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException

class AuthorSearch(BaseModel):
    query: str

class AuthorUpdate(BaseModel):
    scholar_id: str

async def get_all_authors() -> List[dict]:
    try:
        authors = await Author.find_all().to_list()
        return [author.dict() for author in authors]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve authors: {str(e)}")

async def search_and_save_authors(search: AuthorSearch) -> List[dict]:
    # Example of using scholarly and storing in MongoDB
    authors_data = []
    search_query = scholarly.search_author(search.query)
    
    while True:
        try:
            author = next(search_query)
            author = scholarly.fill(author, sections=['basics', 'indices', 'counts'])
            
            # Create Author document
            author_doc = Author(
                name=author.get('name', ''),
                scholar_id=author.get('scholar_id', ''),
                picture_url=author.get('url_picture', ''),
                affiliation=author.get('affiliation', ''),
                interests=author.get('interests', []),
                citations=author.get('citedby', 0),
                h_index=author.get('hindex', 0),
                i10_index=author.get('i10index', 0),
                publications=author.get('publications', []),
                cites_per_year={str(k): v for k, v in author.get('cites_per_year', {}).items()}
            )
            
            # Save to database
            await author_doc.save()
            authors_data.append(author_doc.dict())
            
        except StopIteration:
            break
    
    return authors_data

async def update_author(update: AuthorUpdate) -> dict:
    # Find the author in the database
    author_doc = await Author.find_one({"scholar_id": update.scholar_id})
    if not author_doc:
        raise HTTPException(status_code=404, detail="Author not found")
    
    try:
        # Fetch updated data from Google Scholar
        author = scholarly.search_author_id(update.scholar_id)
        author = scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        
        # Update the author document
        author_doc.name = author.get('name', author_doc.name)
        author_doc.picture_url = author.get('url_picture', author_doc.picture_url)
        author_doc.affiliation = author.get('affiliation', author_doc.affiliation)
        author_doc.interests = author.get('interests', author_doc.interests)
        author_doc.citations = author.get('citedby', author_doc.citations)
        author_doc.h_index = author.get('hindex', author_doc.h_index)
        author_doc.i10_index = author.get('i10index', author_doc.i10_index)
        author_doc.publications = author.get('publications', author_doc.publications)
        author_doc.cites_per_year = {str(k): v for k, v in author.get('cites_per_year', {}).items()}
        
        # Save the updated document
        await author_doc.save()
        
        return {"message": "Author updated successfully", "author": author_doc.dict()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update author: {str(e)}")