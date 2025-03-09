import re
import string 

index = {}
def preprocess_text(text):
    """
    lowercases and remove punctuation from text.
    """
    test = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def build_inverted_index(documents):
    inverted_index = {}
    for doc_id, text in enumerate(documents):
        words = preprocess_text(text).split()
        for word in set(words):
            if word not in inverted_index:
                # create a new dictionary entry for the word
                inverted_index[word] = []
            # append the document id to the list of document ids for the word
            inverted_index[word].append(doc_id)
    print("inverted_index", inverted_index)
    return inverted_index

def add_document(document):
    print("document", document)
    index = build_inverted_index(document)
    return index
def search(inverted_index, query):
    words = preprocess_text(query).split()
    doc_scores = {}
    
    for word in words: 
        if word in inverted_index:
            for doc_id in inverted_index[word]:
                if doc_id not in doc_scores:
                    doc_scores[doc_id] = 0
                doc_scores[doc_id] += 1
        
    #todo: normalize the scores
    
    ranked_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
    #print("ranked_docs", ranked_docs)
    return ranked_docs

if __name__ == "__main__":
    docs = [
        "The cat in the hat",
        "The cat and the dog",  
        "The hat",
        "The hope and the cat",
        "The cat and the dog and the hat",
    ]
    index = build_inverted_index(docs)
    results = search(index, "cat and hat")

    print("Results",results)
    

    
    