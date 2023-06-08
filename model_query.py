from langchain import PromptTemplate, LLMChain

# from langchain.document_loaders import CSVLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings import LlamaCppEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores.faiss import FAISS


class setup:
    # Setup
    def __init__(self):
        self.gpt4all_path = "./models/gpt4all-converted.bin"
        self.llama_path = "./models/ggml-model-q4_0.bin"

        self.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        self.loader = TextLoader("./textGita/gita ch2.txt")
        self.embeddings = LlamaCppEmbeddings(model_path=self.llama_path)
        self.llm = GPT4All(
            model=self.gpt4all_path,
            callback_manager=self.callback_manager,
            verbose=True,
            n_ctx=2024,
        )
        # # Create Index
        # docs = loader.load()
        # chunks = self.split_chunks(docs)
        # index = self.create_index(chunks)
        # index.save_local("bhagvad_gita_index")
        self.index = FAISS.load_local("./embedding", self.embeddings)

    # Split text
    def split_chunks(self, sources):
        print("Splitting documents into chunks...")
        chunks = []
        splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=32)
        for chunk in splitter.split_documents(sources):
            chunks.append(chunk)
        return chunks

    def create_index(self, chunks):
        print("Creating index...")
        texts = [doc.page_content for doc in chunks]
        metadatas = [doc.metadata for doc in chunks]

        search_index = FAISS.from_texts(texts, self.embeddings, metadatas=metadatas)

        return search_index

    def similarity_search(self, query, index):
        print("Searching for similar documents...")
        matched_docs = index.similarity_search(query, k=4)
        sources = []
        for doc in matched_docs:
            sources.append(
                {
                    "page_content": doc.page_content,
                    "metadata": doc.metadata,
                }
            )

        return matched_docs, sources

    def ask(self, question):
        matched_docs, sources = self.similarity_search(question, self.index)
        template = """
        Please use the following context to answer questions.
        Context: {context}
        ---
        Question: {question}
        Answer: From the context, the following can be said."""
        context = "\n".join([doc.page_content for doc in matched_docs])
        print("askdjf;lakjsdf;lkjas;lkdfj;laksjdf;ajdsf")
        prompt = PromptTemplate(
            template=template, input_variables=["context", "question"]
        ).partial(context=context)
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        sol = str(llm_chain.run(question))
        return sol
