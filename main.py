from typing import Union
from fastapi import FastAPI
from search_engine import build_inverted_index, search, add_document

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "this is a simple search engine"}

@app.get("items/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None):
    return {"item_id": item_id, "q":q }

@app.get("/search")
def search_endpoint(query: str = None):
    if query is None:
        return {"error": "query is required"}
    else:
        # build or load your index here
        inverted_index = build_inverted_index()  
        return {"results": search(inverted_index, query)}

@app.post("/add_document")
def add_document_route(document:str):
    results = add_document(document)
    return {"results": results}
