import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# function to get response from my llama model 
def getLLamaResponse(input_text,no_words,blog_style):
    # llama model 
    llm = CTransformers(model ="D:\projects\llama2\models\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type = 'llama',
                        config ={'max_new_tokens':256,
                                 'temperature':0.01})
    # prompt template
    template="""Write a blog for {blog_style} for a topic"{input_text}" within {no_words} words:"""

    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],template = template)
    
    # generating response from LLM model 
    response = llm(prompt.format(blog_style = blog_style,input_text =input_text,no_words= no_words))

    print(response)

    return response

# streamlit config 
st.set_page_config(page_title="LangChain", 
                   page_icon="🤖", 
                   layout="centered", 
                   initial_sidebar_state="collapsed") 

st.header("Generate Blogs🤖 :")

# input text field 
input_text = st.text_input("Enter the blog topic: ")

# creating two more columns for additional two fields

col1 , col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("enter the number of words:")

with col2:
    blog_style = st.selectbox("Writing the blog for: ",
                              ('Researchers','Data Scientist', 'Common People'),index=0)

submit= st.button("Generate")

# getting final response 

if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))



