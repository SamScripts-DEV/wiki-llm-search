import requests
from app.config import WIKIJS_API_URL, WIKIJS_API_TOKEN
from itertools import combinations

if not WIKIJS_API_URL:
    raise ValueError("WIKIJS_API_URL no está definida en el entorno o .env")
if not WIKIJS_API_TOKEN:
    raise ValueError("WIKIJS_API_TOKEN no está definida en el entorno o .env")

def search_wikijs(keywords: str):
    headers = {
        "Authorization": f"Bearer {WIKIJS_API_TOKEN}",
        "Content-Type": "application/json"
    }
    graphql_query = {
        "query": """
        query SearchPages($query: String!) {
          pages {
            search(query: $query) {
              results {
                id
                title
                description
                path
                locale
              }
              suggestions
              totalHits
            }
          }
        }
        """,
        "variables": {"query": keywords}
    }
    response = requests.post(WIKIJS_API_URL, json=graphql_query, headers=headers, verify=False)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    response.raise_for_status()
    data = response.json()
    search_data = data.get("data", {}).get("pages", {}).get("search", {})
    results = search_data.get("results", [])
    suggestions = search_data.get("suggestions", [])
    return results, suggestions


def smart_search_wikijs(keywords: str, min_words: int = 2):
    words = keywords.split()

    queries = [" ".join(words)]
    for i in range(len(words)-1, min_words-1, -1):
        for combo in combinations(words, i):
            q = " ".join(combo)
            if q not in queries:
                queries.append(q)

    for q in queries:
        print(f"Probando búsqueda con: {q}")
        results, _ = search_wikijs(q)
        if results:
            return q, results
    return None, []