from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

local_path = './models/ggml-mpt-7b-chat.bin' 
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

template = """Question: {question}

Answer: Let's think step by step.

"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = GPT4All(model=local_path, callback_manager=callback_manager, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
print("Welcome to the State of the Union chatbot! Type 'exit' to stop.")
while True:
    question = input("\n Enter your question: ")
    llm_chain.run(question)
