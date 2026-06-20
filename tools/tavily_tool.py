from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

query="london 5 days plan hotel booking"

def tavily_search(query):
    print(">>> Tavily Search Processing...")
    # Execute the search query with parameters
    response = client.search(query=query,max_results=5)

    # # 1. Accessing metadata & generated summaries
    # print(f"Query: {response.get('query')}")
    # print(f"Search Time: {response.get('response_time')}s")
    # print(f"AI Summary Answer: {response.get('answer')}\n")

    # # 2. Processing individual search results
    # print("--- Individual Web Results ---")
    # for result in response.get("results", []):
    #     print(f"Title: {result.get('title')}")
    #     print(f"URL: {result.get('url')}")
    #     print(f"Score: {result.get('score')}") # Relevancy rating
    #     print(f"Snippet: {result.get('content')}")
    #     print("-" * 40)

    tavily_results = []

    for result in response.get("results", []):
        title = {result.get('title')}
        URL = {result.get('url')}
        Score = {result.get('score')}
        content = {result.get('content')}
        
        tavily_results.append(
            f"""
            Title : {title}
            URL : {URL}
            Score : {Score}
            Content : {content}
            """
        )

    print(tavily_results)
    return "\n".join(tavily_results)