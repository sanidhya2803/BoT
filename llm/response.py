from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def llm_response(query):

    llm = ChatGroq(
        api_key = "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",
        model = "llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
Answer the following query:
Query:
{query}
""")
    
    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({"query":query})
    
    return result
    
