from scholarly import scholarly, ProxyGenerator
from database.dbConnection import connect_to_mongo, close_mongo_connection
from database.models.author import Author
from database.models.institut import Institut
from database.models.publication import Publication
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException


class InstitutData(BaseModel):
    name: str
    domain: List[str] = []
    webpage: List[str] = []
    country: str = ""
    country_code: str = ""
    
class AuthorSearch(BaseModel):
    query: str
    institut: InstitutData

class AuthorUpdate(BaseModel):
    scholar_id: str

async def get_all_authors() -> List[dict]:
    try:
        authors = await Author.find_all().to_list()
        return [author.dict() for author in authors]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve authors: {str(e)}")

async def search_and_save_authors(search: AuthorSearch) -> List[dict]:
    authors_data = []
    try:
        print(f"Searching for authors with query: '{search.query}'")
        search_query = scholarly.search_author_id(search.query)
        scholarly.pprint(search_query)
        # 1. Use institut info from request
        institut_data = search.institut
        print(f"Institut data: {institut_data}")
        institut = await Institut.find_one({'name': institut_data.name})
        if not institut:
            institut = Institut(
                name=institut_data.name,
                domain=institut_data.domain,
                webpage=institut_data.webpage,
                country=institut_data.country,
                country_code=institut_data.country_code,
                authors=[]
            )
            await institut.save()
            print(f"Institut saved: {institut}")

        try:
            print("Found author:", search_query)    
            author = scholarly.fill(search_query, sections=['basics', 'indices', 'counts', 'publications'])
            print(f"Author data from scholarly: {author}")

            # 1. Create Researcher first without publications
            researcher = Author(
                google_scholar_id=author.get('scholar_id', ''),
                name=author.get('name', ''),
                institut=institut,
                publications=[],  # Start with empty publications
                interest=author.get('interests', []),
                email=author.get('email', ''),
                h_index=author.get('hindex', 0),
                i10_index=author.get('i10index', 0),
                citation=author.get('citedby', 0),
                h_index5y=author.get('hindex5y', 0),
                i10_index5y=author.get('i10index5y', 0),
                citation5y=author.get('citedby5y', 0),
                cited_by_years=[v for k, v in sorted(author.get('cites_per_year', {}).items())]
            )
            await researcher.save()

            # 2. Create Publications after researcher exists
            publications = []
            for pub in author.get('publications', []):
                publication = Publication(
                    author=researcher,
                    content=pub.get("bib", {}).get("title", ""),
                    year=int(pub.get("bib", {}).get("pub_year", 0)),
                    citation=pub.get("bib", {}).get("citation", ""),
                    gs_id=pub.get("author_pub_id", ""),
                    citation_count=pub.get("num_citations", 0),
                    cited_by_url=pub.get("citedby_url", ""),
                    cites_id=pub.get("cites_id", [])
                )
                await publication.save()
                publications.append(publication)

            # 3. Update researcher with publications
            researcher.publications = publications
            await researcher.save()

            # 4. Link researcher to institut
            institut.authors.append(researcher)
            await institut.save()

            # Convert to dict and handle the Link fields properly
            author_dict = {
                "id": str(researcher.id),
                "google_scholar_id": researcher.google_scholar_id,
                "name": researcher.name,
                "institut": {
                    "id": str(institut.id),
                    "name": institut.name
                },
                "publications": [
                    {
                        "id": str(pub.id),
                        "year": pub.year,
                        "content": pub.content
                    } for pub in publications
                ],
                "interest": researcher.interest,
                "email": researcher.email,
                "h_index": researcher.h_index,
                "i10_index": researcher.i10_index,
                "citation": researcher.citation,
                "h_index5y": researcher.h_index5y,
                "i10_index5y": researcher.i10_index5y,
                "citation5y": researcher.citation5y,
                "cited_by_years": researcher.cited_by_years
            }
            authors_data.append(author_dict)

        except StopIteration:
            raise HTTPException(status_code=404, detail="No authors found matching the search query")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to process author data: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search for authors: {str(e)}")

    return authors_data

#async def update_author(update: AuthorUpdate) -> dict:
    # Find the author in the database
    #author_doc = await Author.find_one({"scholar_id": update.scholar_id})
    #if not author_doc:
        # raise HTTPException(status_code=404, detail="Author not found")
    
    #try:
        # Fetch updated data from Google Scholar
        #author = scholarly.search_author_id(update.scholar_id)
        #author = scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        
        # Update the author document
        #author_doc.name = author.get('name', author_doc.name)
        #author_doc.picture_url = author.get('url_picture', author_doc.picture_url)
        #author_doc.affiliation = author.get('affiliation', author_doc.affiliation)
        #author_doc.interests = author.get('interests', author_doc.interests)
        #author_doc.citations = author.get('citedby', author_doc.citations)
        #author_doc.h_index = author.get('hindex', author_doc.h_index)
        #author_doc.i10_index = author.get('i10index', author_doc.i10_index)
        #author_doc.publications = author.get('publications', author_doc.publications)
        #author_doc.cites_per_year = {str(k): v for k, v in author.get('cites_per_year', {}).items()}
        
        # Save the updated document
        #   await author_doc.save()
        
    #    return {"message": "Author updated successfully", "author": author_doc.dict()}
    
    #except Exception as e:
        #raise HTTPException(status_code=500, detail=f"Failed to update author: {str(e)}")