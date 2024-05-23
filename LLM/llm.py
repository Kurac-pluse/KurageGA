from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from llama_cpp import Llama
llm_model = Llama(model_path="./models/llama-2-7b-chat.Q5_K_M.gguf", verbose=False)

# 「aggentの一日の計画」、「何分か前の行動logすべて」、「周囲の環境」「agent固有の性格や立場」の４点をプロンプトにまとめる
def generate_prompt(agent, around, datetime):
  data = []
  data.append(agent.name)
  data.append(agent.personality)
  data.append(agent.today)
  data.append(around)
  data.append(datetime.print_en_time())
  data.append(agent.return_daily_log())

  with open("./LLM/prompt_template.txt", "r") as f:
    prompt = f.read()
  for count, i in enumerate(data):
    prompt = prompt.replace(f"!<INPUT {count}>!", str(i))
  # print(prompt)
  return prompt

def Llama_request(prompt, q):
  # ログレベルの設定
  # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=False)

  # チャンクの分割
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,  # チャンクの最大文字数
    chunk_overlap=20,  # オーバーラップの最大文字数
  )
  texts = text_splitter.split_text(prompt)

  index = FAISS.from_texts(
    texts=texts,
    embedding=HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large"),
  )
  index.save_local("storage")

  # from langchain.llms import OpenAI
  # llm = OpenAI(model = "gpt-3.5-turbo-instruct",openai_api_key = "", temperature=0, verbose=True)

  llm = LlamaCpp(
    model_path="./models/llama-2-7b-chat.Q5_K_M.gguf",
    max_tokens=300,
    stop=["System:", "User:", "Assistant:", "\n"],
    temperature=0.1,
    verbose=False,
    n_ctx=2048,
)

  qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=index.as_retriever(search_kwargs={"k": 4}),
    verbose=False,
  )

  # print("    ", q)
  return qa_chain.run(q).strip()

def llm_summary(llm_response):
  prompt = f"Summarize the word [{llm_response}]"
  summary = llm_model(
    prompt,
    temperature=0.1,
    stop = ["System:", "User:", "Assistant:", "Instruction:", "Input:", "Response:", "\n"],
    echo = False,
  )
  # print("summary : ", summary["choices"][0]["text"])
  return summary["choices"][0]["text"]




if __name__ == "__main__":
  prompt = """
  My name is agent1.

  (personality)
  Gender: Male
  Age: 22
  Occupation: College Student
  Personality: the idler
  Interests: Cooking

  (daily schedule)
  Todays my daily plan
  Today I will get up at 8:00 time and go to bed at 23:00 time.
  I will eat breakfast at 9:00 time.
  I will eat lunch at 12:00 time.
  I will eat dinner at 18:00 time.
  Furthermore,  will also be conducted today.

  (surrounding objects)
  Things within my reach.
  wall, wall, wall, wall, wall, bed, bed, wall, bed, bed, wall, bed, bed
  These things currently exist around me.

  The current time is January 1, 2024 at 8:00.

  My most recent actions are
  7:55 sleeping
  7:56 sleeping
  7:57 sleeping
  7:58 sleeping
  7:59 sleeping

  From the above information, please briefly describe in one sentence the action I should take during the next minute.
  There is only one action I should take next.
  """

  print(Llama_request(prompt))
