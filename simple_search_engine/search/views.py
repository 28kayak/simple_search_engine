# STEP 4: 
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from search.models import Document
from search.inverted_index import InvertedIndex
import json

index = InvertedIndex()

@csrf_exempt
def add_document(request):
    if request.method == "POST": 
        data = json.loads(request.body)
        doc_id = data.get("doc_id")
        content = data.get("content")
    
    # Save Data to DB
    Document.objects.create(doc_id=doc_id, content=content)
    # Add document to inverted index
    index.add_document(doc_id, content)

    return JsonResponse({"Document: document added successfully"})

def search(request):
    pass

def save_index(request):
    pass

def load_index(request):
    pass
