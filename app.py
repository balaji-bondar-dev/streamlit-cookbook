'''
# pip install langgraph langchain langchain-openai langchain-groq langchain-community langchain-tavily psycopg[binary] psycopg_pool python-dotenv tavily-python pip install requests streamlit

# install PostgresSql and create database
CREATE DATABASE langgraph_memory;  ( or open pgadmin4 and create database there )
'''
# LangGraph Multi-Agent Travel Booking System with Long-Term Memory

# main.py

import os
from typing import TypedDict, Annotated
import operator

#import psycopg
from langgraph.graph import StateGraph, START, END
#from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import (
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from langchain_groq import ChatGroq

#from tools.tavily_tool import tavily_search
#from tools.flight_tool import search_flights
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)




# # import sys
# import os
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated
# import operator

# # from langgraph.graph import StateGraph,START,END
# from langchain.messages import AnyMessage,HumanMessage,SystemMessage,AIMessage
# from langchain_groq import ChatGroq
# # from langgraph.checkpoint.postgres import PostgresSaver
# # import psycopg

# from tools.flight_tool import search_flight
# from tools.tavily_tool import tavily_search

# load_dotenv()

# # if len(sys.argv) > 1:
# #     print(f"Received input parameter: {sys.argv[1]}")

llm = ChatGroq(
    model="llama-3.1-8b-instant", #llama-3.1-8b-instant,openai/gpt-oss-120b,openai/gpt-oss-20b
    temperature=0.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

#print(llm.invoke("What is the capital of France?"))
messages = [
    SystemMessage(content="You are a helpful assistant.Answer in one sentence."),
    HumanMessage(content="What is the captial of france"),
]
response = llm.invoke(messages)
# print("❯❯❯❯Final response ")
print({response.type})
print({response.content})

# # class TravelState(TypedDict):
# #     messages: Annotated[list[AnyMessage], operator.add]
# #     user_query: str
# #     flight_results: str
# #     hotel_results: str
# #     itinerary: str
# #     llm_calls: int

# # def flight_agent(state:TravelState):
# #     print(">>> flight_agent called...")
# #     query = state["user_query"]
# #     flight_data = search_flight(query)
# #     return{
# #         "flight_results" : flight_data,
# #         "messages" : [AIMessage(content="Flight results fetched...")],
# #         "llm_calls" : state.get("llm_calls",0) + 1
# #     }     

# # def hotel_agent(state:TravelState):
# #     print(">>> hotel_agent called...")
# #     query = f"Best hotels for {state["user_query"]}"
# #     hotel_results = tavily_search(query) 
# #     return{
# #         "hotel_results" : hotel_results,
# #         "messages" : [AIMessage(content="Hotel information fetched...")],
# #         "llm_calls" : state.get("llm_calls",0) + 1
# #     }    

# # def itinerary_agent(state:TravelState):
# #     print(">>> itinerary_agent called...")
# #     prompt = f"""
# #     Create a travel Itinerary.
# #     User Query:
# #     {state["user_query"]}
    
# #     Flight Results:
# #     {state["flight_results"]}

# #     Hotel Results:
# #     {state["hotel_results"]}
# #     """
# #     response = llm.invoke([
# #         SystemMessage(
# #                 content="You are an expert travel planner"  
# #         ),    
# #         HumanMessage(content=prompt)
# #     ])
# #     return{
# #         "itinerary" : response.content,
# #         "messages" : [response],
# #         "llm_calls" : state.get("llm_calls",0) + 1
# #     }    


# # def final_agent(state:TravelState):
# #     print(">>> final_agent called...")
# #     final_prompt = f"""
# #     Generate final travel plan with daywise details.
    
# #     Flight Results:
# #     {state["flight_results"]}

# #     Hotel Results:
# #     {state["hotel_results"]}
    
# #     Itinerary Results:
# #     {state["itinerary"]}
# #     """
# #     response = llm.invoke([HumanMessage(content=final_prompt)])
# #     return{
# #         "messages" : [response],
# #         "llm_calls" : state.get("llm_calls",0) + 1
# #     }    

# # builder = StateGraph(TravelState)
# # builder.add_node("flight_agent",flight_agent)
# # builder.add_node("hotel_agent",hotel_agent)
# # builder.add_node("itinerary_agent",itinerary_agent)
# # builder.add_node("final_agent",final_agent)

# # builder.add_edge(START,"flight_agent")



# # builder.add_edge("flight_agent","hotel_agent")
# # builder.add_edge("hotel_agent","itinerary_agent")
# # builder.add_edge("itinerary_agent","final_agent")
# # builder.add_edge("final_agent",END)

# # # DATABASE_URL = os.getenv("DATABASE_URL")

# # # _conn = psycopg.connect(DATABASE_URL)
# # # checkpointer = PostgresSaver(_conn)
# # # checkpointer.setup()

# # graph = builder.compile()
# # user_input = "plan a 2 days japan trip including flights,hotels and sightseeing"
# # #user_input = input("Enter Travel Request: ")

# # config = {"configurable": {"thread_id": "1000"}}

# # final_result = graph.invoke(
# #     {
# #         "messages": [HumanMessage(content=user_input)],
# #         "user_query": user_input,
# #         "flight_results": "",
# #         "hotel_results": "",
# #         "itinerary": "",
# #         "llm_calls": 0
# #     },
# #     config=config
# # )

# # print(">>> final_result")

# # for each_message in final_result["messages"]:
# #     print(each_message.content)
