from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
import chromadb
from chromadb.config import Settings as ChromaSettings
from langchain.llms import AzureOpenAI
import openai  # for calling the OpenAI API

import openai_config
import chroma_config

chroma_settings=ChromaSettings(chroma_client_auth_provider="chromadb.auth.token.TokenAuthClientProvider",chroma_client_auth_credentials=chroma_config.CHROMA_TOKEN)
chroma_client=chromadb.HttpClient(host=chroma_config.CHROMA_HOST, port=chroma_config.CHROMA_PORT, settings=chroma_settings)
embeddings = OpenAIEmbeddings(deployment="policeembedding")

def get_policies():
    return [c.name[14:].capitalize().replace('-', ' ') for c in chroma_client.list_collections()]

def answer_query(query, collection_name):
    db=Chroma(client=chroma_client, client_settings=chroma_settings, collection_name=collection_name, embedding_function=embeddings)
    chat = ChatOpenAI(deployment_id="policechat", temperature=0)
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=db.as_retriever(),
        chain_type_kwargs={"verbose": False}
    )
    result = chain({"question": query}, return_only_outputs=True)
    return result

