from app.services.wikijs import smart_search_wikijs

if __name__ == "__main__":
    keywords = "zabbix agente caído monitoreo"
    print("Buscando en Wiki.js con combinaciones inteligentes de:", keywords)
    base_url = "https://172.32.1.54/"
    query_usada, results = smart_search_wikijs(keywords, min_words=2)
    if results:
        print(f"\nResultados usando: '{query_usada}'\n")
        for r in results:
            url = base_url + r['path']
            print(f"- {r['title']}: {url}")
            print(f"  {r['description']}\n")
    else:
        print("No se encontraron resultados con ninguna combinación.")