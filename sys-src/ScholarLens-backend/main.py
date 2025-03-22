from fastapi import FastAPI
from scholarly import scholarly

search_query = scholarly.search_author('oth-aw.de')  # Replace 'MIT' with your target institution

# Retrieve and print a few results
for i in range(20):  # Adjust the number of profiles you want
    try:
        author = next(search_query)
        print(f"Name: {author['name']}")
        print(f"Affiliation: {author['affiliation']}")
        print(f"Interests: {author.get('interests', [])}")
        print(f"Scholar ID: {author['scholar_id']}")
        print("-" * 40)
    except StopIteration:
        print("No more results.")
        break


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
