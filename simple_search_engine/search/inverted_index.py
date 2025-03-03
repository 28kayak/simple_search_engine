from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class InvertedIndex:
    def __init__(self):
        self.documents = {} # Map document ID to content 
        self.index = {} # Map word to list of document ID 
        self.tfidf_vectorizer = TfidfVectorizer()
    
    def add_document(self, doc_id, content):
        "Add document to the index"
        self.documents[doc_id] = content
        words = content.split()
        for word in words:
            if word not in self.index: 
                self.index[word] = []
            if doc_id not in self.index:
                self.index[word].append(doc_id)
    
    def build_tfidf(self):
        "Build TF-IDF matrix for a document"
        corpus = list(self.documents.values())
        return self.tfidf_vectorizer.fit_transform(corpus)
    
    def search(self, query):
        "search the index for the most"
        query = self.tfidf_vectorizer.transform([query])
        document_tfidf = self.build_tfidf()
        similarity = cosine_similarity(query, document_tfidf)
        return similarity
