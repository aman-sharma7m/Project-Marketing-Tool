import streamlit as st
from langchain import PromptTemplate,FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv
from langchain.llms import OpenAI,HuggingFaceHub
import warnings
warnings.filterwarnings('ignore')

#loading keys
load_dotenv()




#initial web_page 
st.set_page_config(page_title='Marketting Tool')
st.header('Hi How can i help you?')

# get_text query
query=st.text_area('Enter Text:',height=275)
#get text_type
text_type=st.selectbox('Please select the text type:',('Write a sales copy','create a tweet','write a product description'))
#get_user_fit
user_type=st.selectbox('Please Select action performed:',('Kid','Adult','Senior Citizen'))
#get_age group
word_limit=st.slider('words limit',5,200,5)
#select model
model=st.selectbox('Please select the model:',('GPT','HUG'))
#submit button
submit=st.button('Generate')


def llm_response(query,text_type,user_type,word_limit,model):
  #working on the prompt 

  #examples
  if user_type=='Kid':
    examples=[
      {
        'query':'what is a mobile?',
        'answer':'Mobile is a magical device, like a mini-enchanted playground.'
      },
      {
        'query':'what are your dreams?',
        'answer':'my dreams are to visit colourful adventures,become superhero'
      }
    ]
  elif user_type=='Adult':
    examples=[
      {
        'query':'what is a mobile?',
        'answer':'mobile is a working device. to ease out your daily task.'
      },
      {
        'query':'what are your dreams?',
        'answer':'Dream to become successful and help others'
      }
    ]
  elif user_type=='Senior Citizen':
    examples=[
      {
        'query':'what is a mobile?',
        'answer':'mobile is a device to call your relatives.'
      },
      {
        'query':'what are your dreams?',
        'answer':'dream to enjoy my remaining life before death.'
      }
    ]

  #example template
  example_template='''
    Question: {query}
    Response: {answer}
  '''

  example_prompt=PromptTemplate(
    input_variables=['query','answer'],
    template=example_template
  )

  example_selector=LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=2000
  )

  prefix='''
  you are a {user_type} and {text_type} \n
  in {word_limit} words. \n
  Here are some examples to understand the nature:
  '''

  sufix='''
  Question: {user_input} \n
  Response:
  '''

  final_prompt=FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=sufix,
    input_variables=['user_input','user_type','text_type','word_limit']
  )

  final_p=final_prompt.format(user_input=query,
                                          user_type=user_type,
                                          text_type=text_type,
                                          word_limit=str(word_limit)
                                          )
  if model=='GPT':
    open_llm=OpenAI(model='gpt-3.5-turbo-instruct')
    response=open_llm(final_p)
  else:
    hug_llm=HuggingFaceHub(repo_id='google/flan-t5-xxl')
    response=hug_llm(final_p)
  return final_p,response


if submit:
  out_prompt,response=llm_response(query,text_type,user_type,word_limit,model)
  st.write('Your text:',query)
  st.write('Your selected text-type:',text_type)
  st.write('your selected type:',user_type)
  st.write('Your selected word-limit:',str(word_limit))
  st.write('Your final prompt:',out_prompt)
  st.subheader('Respose:',response)
  st.write(response)
