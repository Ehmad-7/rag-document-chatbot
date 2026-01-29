import faiss
import numpy as np

class VectorStore:
    def __init__(self,embeddings,texts):
        self.texts=texts
        dim=embeddings.shape[1]
        self.index=faiss.IndexFlatL2(dim)
        self.index.add(embeddings.astype('float32'))

    def search(self,query_embedding,top_k=3):
        D,I=self.index.search(query_embedding.astype('float32'),top_k)
        return [self.texts[i] for i in I[0]]