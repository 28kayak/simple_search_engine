from django.db import models

# Create your models here.
# Step2: define the document model
class Document(models.Model): 
    # unique identifies for each document
    doc_id = models.CharField(max_length=255, unique=True)
    # the text content of the document to be indexed
    content = models.TextField()

    def __str__(self):
        return f"Document: {self.doc_id}"
    