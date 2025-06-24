from scholarly import scholarly, ProxyGenerator
from database.dbConnection import connect_to_mongo, close_mongo_connection
from database.models.author import Author
from database.models.institut import Institut
from database.models.publication import Publication
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException
import uuid
from uuid import UUID
from bson import DBRef


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

class AuthorWithoutPublications(BaseModel):
    id: uuid.UUID
    google_scholar_id: str
    name: str
    institut: Optional[InstitutData]
    interest: List[str]
    email: str
    h_index: int
    i10_index: int
    citation: int
    h_index5y: int
    i10_index5y: int
    citation5y: int
    cited_by_years: List[int]

class PublicationData(BaseModel):
    id: uuid.UUID
    content: str
    year: Optional[int]
    citation: Optional[str]
    gs_id: Optional[str]
    citation_count: Optional[int]
    cited_by_url: Optional[str]
    cites_id: List[str]

class AuthorFull(BaseModel):
    id: uuid.UUID
    google_scholar_id: str
    name: str
    institut: Optional[InstitutData]
    publications: List[PublicationData]
    interest: List[str]
    email: str
    h_index: int
    i10_index: int
    citation: int
    h_index5y: int
    i10_index5y: int
    citation5y: int
    cited_by_years: List[int]

async def get_all_authors() -> List[AuthorWithoutPublications]:
    try:
        # Step 1: Load all authors (with publications) as full Beanie documents
        authors_data = await Author.find_all().to_list()

        result = []
        for author in authors_data:
            # Step 2: Remove publications manually
            author.publications = []
            print(author.institut)
            # Step 3: Dereference institut (if present and is DBRef)
            institut_data = None
            if author.institut is not None:
                institut_data = await author.institut.fetch()
                print(institut_data)


            # Step 4: Build response model
            model_instance = AuthorWithoutPublications(
                id=author.id,
                google_scholar_id=author.google_scholar_id,
                name=author.name,
                institut=InstitutData(
                    name=institut_data.name,
                    domain=institut_data.domain,
                    webpage=institut_data.webpage,
                    country=institut_data.country,
                    country_code=institut_data.country_code
                ) if institut_data else None,
                interest=author.interest or [],
                email=author.email or "",
                h_index=author.h_index or 0,
                i10_index=author.i10_index or 0,
                citation=author.citation or 0,
                h_index5y=author.h_index5y or 0,
                i10_index5y=author.i10_index5y or 0,
                citation5y=author.citation5y or 0,
                cited_by_years=author.cited_by_years or []
            )

            result.append(model_instance)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve authors: {str(e)}")


async def get_author_by_id(author_id: UUID) -> AuthorFull:
    try:
        # Get the author document
        author = await Author.get(author_id)

        if not author:
            raise HTTPException(status_code=404, detail="Author not found")

        # Fetch linked institut
        institut_data = None
        if author.institut is not None:
            institut = await author.institut.fetch()
            institut_data = InstitutData(
                name=institut.name,
                domain=institut.domain,
                webpage=institut.webpage,
                country=institut.country,
                country_code=institut.country_code
            )

        # Fetch linked publications
        publications = []
        for pub_link in author.publications:
            publication = await pub_link.fetch()
            if publication:
                publications.append(PublicationData(
                    id=publication.id,
                    content=publication.content,
                    year=publication.year,
                    citation=publication.citation,
                    gs_id=publication.gs_id,
                    citation_count=publication.citation_count,
                    cited_by_url=publication.cited_by_url,
                    cites_id=publication.cites_id
                ))

        # Return response
        return AuthorFull(
            id=author.id,
            google_scholar_id=author.google_scholar_id,
            name=author.name,
            institut=institut_data,
            publications=publications,
            interest=author.interest or [],
            email=author.email or "",
            h_index=author.h_index,
            i10_index=author.i10_index,
            citation=author.citation,
            h_index5y=author.h_index5y,
            i10_index5y=author.i10_index5y,
            citation5y=author.citation5y,
            cited_by_years=author.cited_by_years or []
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve author: {str(e)}")
    

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

async def get_all_institutes() -> List[Institut]:
    try:
        institutes = await Institut.find_all().to_list()
        return institutes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve institutes: {str(e)}")
    

async def get_institut_by_id(institut_id: UUID) -> dict:
    try:
        institut = await Institut.get(institut_id, fetch_links=True)
        if not institut:
            raise HTTPException(status_code=404, detail="Institut not found")

        # Fetch and serialize each author
        authors_data = []
        for author in institut.authors:
            authors_data.append({
                "id": author.id,
                "name": author.name,
                "google_scholar_id": author.google_scholar_id,
                "email": author.email,
                "interest": author.interest,
                "h_index": author.h_index,
                "i10_index": author.i10_index,
                "citation": author.citation,
                "h_index5y": author.h_index5y,
                "i10_index5y": author.i10_index5y,
                "citation5y": author.citation5y,
                "cited_by_years": author.cited_by_years,
            })

        # Return institut with authors included
        return {
            "id": institut.id,
            "name": institut.name,
            "domain": institut.domain,
            "webpage": institut.webpage,
            "country": institut.country,
            "country_code": institut.country_code,
            "province": institut.province,
            "authors": authors_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve institut: {str(e)}")