from .state import State 
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from .utils.chains import get_character_response_chain

async def conversation_node(state: State, config: RunnableConfig):
    chain = get_character_response_chain(state.get("summary", ""))
    response = await chain.ainvoke({
        "messages": state.get("messages", []), 
    }, config=config)

    return {"messages": response} 


