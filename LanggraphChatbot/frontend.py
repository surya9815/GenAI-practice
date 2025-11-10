import streamlit as st
from backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

# chatmessage.  AND  chatinput
#  st.session_state ---> dict

CONFIG = {'configurable':{'thread_id':'thread-1'}}
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# message_history = [
#     {'role':'user', 'content': 'Hi'}
#     ]

# Load the contents
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

user_input = st.chat_input('Type here')

if user_input:
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    
    # v0.1 - Normal AI Message
    # response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]},config=CONFIG)
    # ai_message = response['messages'][-1].content
    # st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    # with st.chat_message('assistant'):
    #     st.text(ai_message)
    
    # v0.2 - Add Streaming
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    
