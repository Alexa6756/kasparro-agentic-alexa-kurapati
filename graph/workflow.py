from langgraph.graph import StateGraph, END
from graph.state import AgentState
from agents.parser_agent import parser_node
from agents.question_agent import question_node
from agents.writer_agent import writer_node

def route(state: AgentState):
    if state["parsed_product"] is None:
        return "parser"
    if state["questions"] is None:
        return "question_agent"
    return "writer"

def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("parser", parser_node)
    graph.add_node("question_agent", question_node)  
    graph.add_node("writer", writer_node)

    graph.set_entry_point("parser")

    graph.add_conditional_edges("parser", route)
    graph.add_conditional_edges("question_agent", route)
    graph.add_edge("writer", END)

    return graph.compile()
