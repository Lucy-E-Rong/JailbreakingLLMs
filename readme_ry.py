'''
usage: main.py [-h]
    [--attack-model {vicuna-13b-v1.5,llama-2-7b-chat-hf,gpt-3.5-turbo-1106,gpt-4-0125-preview,claude-instant-1.2,claude-2.1,gemini-pro,mixtral,vicuna-7b-v1.5}]    
    [--attack-max-n-tokens ATTACK_MAX_N_TOKENS] [--max-n-attack-attempts MAX_N_ATTACK_ATTEMPTS]
    [--target-model {vicuna-13b-v1.5,llama-2-7b-chat-hf,gpt-3.5-turbo-1106,gpt-4-0125-preview,claude-instant-1.2,claude-2.1,gemini-pro}]
    [--target-max-n-tokens TARGET_MAX_N_TOKENS] [--not-jailbreakbench] [--jailbreakbench-phase {dev,test,eval}]
    [--judge-model {gpt-3.5-turbo-1106,gpt-4-0125-preview,no-judge,jailbreakbench,gcg}] [--judge-max-n-tokens JUDGE_MAX_N_TOKENS]
    [--judge-temperature JUDGE_TEMPERATURE] [--n-streams N_STREAMS] [--keep-last-n KEEP_LAST_N] [--n-iterations N_ITERATIONS] [--goal GOAL]
    [--target-str TARGET_STR] [--evaluate-locally] [--index INDEX] [--category CATEGORY] [-v]
'''