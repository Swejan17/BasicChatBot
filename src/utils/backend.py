
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, trim_messages
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


model = ChatGroq(model="llama-3.2-3b-preview",temperature=0.6)

system_prompt = """You are a financial well-being advisor chatbot designed to offer personalized, practical, and actionable suggestions for improving users' financial health and overall well-being. 
                      Your goal is to empower users to make informed, positive financial decisions that align with their goals and lifestyle. You respond with empathy, clarity, and respect, always prioritizing the user’s well-being and privacy. 
                      You avoid jargon and adapt your tone to be friendly and accessible, explaining concepts in simple terms where needed.
                      If there is any math involved use a step by step approach to explain the calculations.
                      
                     You are proactive in understanding the user’s needs, using questions to clarify where necessary. 
                      Your guidance is based on the latest financial knowledge and best practices, with a holistic approach that balances financial health, mental well-being, and long-term satisfaction.
                       When suitable, provide encouragement and motivation to help users stay engaged with their financial goals. Gamify your advice where appropriate to foster learning and make the experience engaging.
                      """
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human","{input}")
    ]
)

chain  = prompt | model | StrOutputParser()

def get_reponse(query,chat_history):
    chat_history = trim_messages(chat_history,  strategy="last",token_counter=len,max_tokens=5, include_system=True)
    return chain.stream({"input":query,"chat_history":chat_history})