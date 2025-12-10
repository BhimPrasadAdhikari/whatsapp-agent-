from langgraph.graph import END, START, StateGraph 
from .nodes import conversation_node
from .state import State 

def create_graph():

    graph_builder = StateGraph(State)
    graph_builder.add_node("conversation_node", conversation_node)
    graph_builder.add_edge(START, "conversation_node")
    graph_builder.add_edge("conversation_node", END)

    return graph_builder 

graph = create_graph().compile() 

