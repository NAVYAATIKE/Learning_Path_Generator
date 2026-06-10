from prompt import learning_path_prompt, parser
from model import llm
from langfuse import Langfuse

chain = learning_path_prompt | llm | parser

from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()

def generate_learning_path(skill):

    response = chain.invoke(
        {
            "skill": skill
        },
        config={"callbacks": [langfuse_handler]}
        )

    return response



