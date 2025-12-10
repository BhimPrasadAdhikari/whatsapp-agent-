from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .helper import get_chat_model
from core.prompts import SYSTEM_PROMPT

def get_character_response_chain(summary: str = ""):
    model = get_chat_model()
    system_message = SYSTEM_PROMPT

    if summary:
        system_message += f"""

        Summary of the conversation so far: {summary}
        """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    return prompt | model 