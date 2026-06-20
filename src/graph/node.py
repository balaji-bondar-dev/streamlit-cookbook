
from src.graph.state import TravelState
from src.tools.flight_tool import search_flight
from src.tools.tavily_tool import tavily_search

def flight_agent(state:TravelState):
    print(">>> flight_agent called...")
    query = state["user_query"]
    flight_data = search_flight(query)
    return{
        "flight_results" : flight_data,
        "messages" : [AIMessage(content="Flight results fetched...")],
        "llm_calls" : state.get("llm_calls",0) + 1
    }     

def hotel_agent(state:TravelState):
    print(">>> hotel_agent called...")
    query = f"Best hotels for {state["user_query"]}"
    hotel_results = tavily_search(query) 
    return{
        "hotel_results" : hotel_results,
        "messages" : [AIMessage(content="Hotel information fetched...")],
        "llm_calls" : state.get("llm_calls",0) + 1
    }    

def itinerary_agent(state:TravelState):
    print(">>> itinerary_agent called...")
    prompt = f"""
    Create a travel Itinerary.
    User Query:
    {state["user_query"]}
    
    Flight Results:
    {state["flight_results"]}

    Hotel Results:
    {state["hotel_results"]}
    """
    response = llm.invoke([
        SystemMessage(
                content="You are an expert travel planner"  
        ),    
        HumanMessage(content=prompt)
    ])
    return{
        "itinerary" : response.content,
        "messages" : [response],
        "llm_calls" : state.get("llm_calls",0) + 1
    }    


def final_agent(state:TravelState):
    print(">>> final_agent called...")
    final_prompt = f"""
    Generate final travel plan with daywise details.
    
    Flight Results:
    {state["flight_results"]}

    Hotel Results:
    {state["hotel_results"]}
    
    Itinerary Results:
    {state["itinerary"]}
    """
    response = llm.invoke([HumanMessage(content=final_prompt)])
    return{
        "messages" : [response],
        "llm_calls" : state.get("llm_calls",0) + 1
    }    
