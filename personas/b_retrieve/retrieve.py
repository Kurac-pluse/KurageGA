from LLM.llm import *
import re

def get_retrieve(first_agent, around, second_agent, datetime, destination):

    # agentの近くに他のagentがいるか、またはすでに会話が始まっているかの判定
    if(need_conversation(first_agent, second_agent)):
        llm_response = get_conversation(first_agent, second_agent)
        return llm_response

    # 「aggentの一日の計画」、「何分か前の行動logすべて」、「周囲の環境」「agent固有の性格や立場」の４点をプロンプトにまとめる
    prompt = generate_prompt(first_agent, around, datetime)
    # print("||----------||")
    # print(prompt)
    # print("^^----------^^")
    #10分前の行動と現在時刻から今行うべき行動を出力する
    log_txt = first_agent.curr_log[-1].contents
    # if "" in log_txt:
    #     log_txt = log_txt.replace("", "")
    if "I am" in log_txt:
        log_txt = log_txt.split("I am")[1]
    if "I" in log_txt:
        log_txt = log_txt.replace("I", "")
    if "." in log_txt:
        log_txt = log_txt.replace(".", "")
    if "currently" in log_txt:
        log_txt = log_txt.replace("currently", "")
    if "my" in log_txt:
        log_txt = log_txt.replace("my", "your")
    log_txt = log_txt.strip()
    q = f"""You are agent1. You were "{log_txt}" ten minutes ago at {first_agent.curr_log[-1].time}; Think about the flow, what are you doing now at {datetime.print_hour_minute()}?"""
# What are you doing {datetime.print_hour_minute()}?
# Please output according to the following writing style.
# {first_agent.return_curr_log(3)}{datetime.print_hour_minute()} 

    llm_response = Llama_request(prompt, q)
    while True:
        if len(llm_response) <= 50:
            break
        llm_response = llm_summary(llm_response)
    count = 0
    while True:
        # print("||----------||")
        # print(q)
        # print("^^----------^^")
        # llm_response = Llama_request(prompt, q)
        if llm_response != "" and re.search("I don't know", llm_response) == None:
            break
        if count == 10:
            llm_response = first_agent.curr_log[-1].contents
            print(f"non-passage : {llm_response}")
            break
        count += 1
        # print(str(count)+" :"+llm_response+":")
        llm_response = Llama_request(prompt, q)
        # print("non-passage")
    # llm_responseをlogに追加

    first_agent.set_mylog(llm_response, datetime)
    return llm_response

def need_conversation(first_agent, second_agent):
    return False

def get_conversation(agent1, agent2):
    prompt = " "
    llm_response = Llama_request(prompt)
    return llm_response

