from os import environ
import openai

openai.api_type = "azure"
openai.api_base = "https://account.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = ""
openai.model = "text-embedding-ada-002"
openai.deployment_id="deployment_1"
openai.engine="deployment_1"
environ["OPENAI_API_TYPE"] = "azure"
environ["OPENAI_API_VERSION"] = "2023-05-15"
environ["OPENAI_API_BASE"] = "https://account.openai.azure.com/"
environ["OPENAI_API_KEY"] = ""
environ["MODEL"] = "text-embedding-ada-002"
environ["DEPLOYMENT_ID"] = "deployment_1"
