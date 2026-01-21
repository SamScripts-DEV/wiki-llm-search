from fastapi import FastAPI
from app.schemas import SearchRequest, SearchResponse, RelatedPage
from app.services.llm import extract_keywords
from app.services.wikijs import search_wikijs, smart_search_wikijs
from app.config import BASE_WIKI_URL

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Microservicio LLM para WIKI.js"}

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    # 1. Extrae palabras clave de la pregunta
    keywords = extract_keywords(request.query)
    # 2. Búsqueda inteligente en Wiki.js
    query_usada, results = smart_search_wikijs(keywords, min_words=2)
    if results:
        related_pages = [
            RelatedPage(
                title=page["title"],
                url=BASE_WIKI_URL + page["path"],
                excerpt=page.get("description", "")
            ) for page in results
        ]
        return {
            "summary": "He encontrado estos artículos relacionados con lo que buscas:",
            "related_pages": related_pages,
            "files": []
        }
    else:
        # Si no hay resultados, busca sugerencias
        _, suggestions = search_wikijs(keywords)
        if suggestions:
            return {
                "summary": "No se encontraron resultados exactos. Intenta buscar usando estas palabras sugeridas: " + ", ".join(suggestions),
                "related_pages": [],
                "files": []
            }
        else:
            return {
                "summary": "No se encontraron resultados ni sugerencias. Intenta reformular tu pregunta.",
                "related_pages": [],
                "files": []
            }