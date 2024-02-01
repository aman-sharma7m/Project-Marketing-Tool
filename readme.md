# Project-Marketing-Tool

A gen-ai tool to generate tweet, sales copy and product description based on the nature of the age group. Also, you can decide the word limit. It'll generate the following.

## Installation & create environment

Clone the project

```bash
  git clone link_to_copy
```

Go to the project directory

```bash
  cd proj_dir
```

Create the enviroment

```bash
  conda create --prefix ./lang_env
  conda activate {path}/lang_env
  python -m ipykernel install --user --name=lang_env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Provide openai and huggingface api keys

```
create a .env file and store your keys in this format.

OPENAI_API_KEY="key_goes_here"
HUGGINGFACEHUB_API_TOKEN="key_goes_here"
```

Start the server

```bash
  streamlit run app.py
```

## Code Explanation

Code is divided into 3 sections:

0. dotenv load help to call the keys that we defined

1. The frontend part which is build on the streamlit app. we take all the user inputs regarding query, what has to be generate, for what audience it should be build and word_limit.

2. All the info taken by user is passed to function called llm_response which build the prompt template using fewshotprompttemplate. then passed to the llm to generate the response. as examples are added acc to the age-group, you can change it to get more precise response.

3. Display the results back to the streamlit app.

libraries used:

```
import streamlit as st
from langchain import PromptTemplate,FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv
from langchain.llms import OpenAI,HuggingFaceHub
```
