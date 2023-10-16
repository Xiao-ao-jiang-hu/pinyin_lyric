import json

with open('step16_result.jsonl', 'r', encoding="utf-8") as f:
    cnt=0
    for line in f:
        data = json.loads(line)
        # print(data , "\n\n\n")
        print(data["no_punctuation_lyric"])
        cnt+=1
        if(cnt > 3):
            break