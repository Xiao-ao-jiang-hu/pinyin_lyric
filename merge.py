import json
from tqdm import tqdm
# from pypinyin.contrib.tone_convert import to_finals
# from g2pM import G2pM

# g2pw = G2pM()

# origin_set = set()
# with open("step21_result.jsonl", "r") as fin:
#     for line in tqdm(fin):
#         origin_set.add(json.loads(line)["lyric_id"])

# with open("outputs/rythm.jsonl", "r") as fin:
#     for line in tqdm(fin):
#         origin_set.remove(json.loads(line)["lyric_id"])

# yun_mapper = {'a': 0, 'ia': 0, 'ua': 0, 
#               'o': 1, 'uo': 1, 
#               'e': 2, 'ie': 2, 've': 2, 
#               'i': 3, 
#               'u': 4, 
#               'v': 5, 
#               'ai': 6, 'uai': 6, 
#               'ei': 7, 'uei': 7, 'ui': 7,
#               'ao': 8, 'iao': 8, 
#               'ou': 9, 'iou': 9, 'iu': 9,
#               'an': 10, 'ian': 10, 'uan': 10, 'van': 10, 
#               'en': 11, 'in': 11, 'uen': 11, 'vn': 11, 'un': 11,
#               'ang': 12, 'iang': 12, 'uang': 12,
#               'eng': 13, 'ing': 13, 'ueng': 13,
#               'ong': 14, 'iong': 14,
#               'er': 15}
# with open("step21_result.jsonl", "r") as f:
#     output_file = open("outputs/rythm_result_add.jsonl", "w")
#     for line in tqdm(f):
#         try:
#             data_json = json.loads(line)
#         except Exception as e:
#             print(e)
#         if(data_json["lyric_id"] in origin_set):
#             lyric = data_json["processed_lyric"]
#             lyric_id = data_json["lyric_id"]
#             last_chars = [i[-1] if i != "" else "" for i in lyric]
#             pinyin = [i.replace("u:", "v") for i in g2pw(last_chars, tone=False, char_split=False)]
#             finals = [to_finals(i) for i in pinyin]
#             rythm = [(yun_mapper[i] if i in yun_mapper else -1) for i in finals]
#             output_file.write("{\"lyric_id\": " + str(lyric_id) +", \"rythm_info\": " + str(rythm) +"}\n")
            
#     output_file.close()
        
# print(origin_set)

# import os
# files = os.listdir("outputs")
# print(files)

# with open('rythm.jsonl', 'w') as merged_file:
#     # 遍历每个文件，读取内容后写入到新建的合并文件中
#     for name in files:
#         file_path = os.path.join("outputs", name)
#         with open(file_path, 'r') as current_file:
#             content = current_file.read()
#             merged_file.write(content)

file_dict = {}
with open("step21_result.jsonl", "r") as fin:
    for line in tqdm(fin):
        json_dict = json.loads(line)
        file_dict[json_dict["lyric_id"]] = json_dict
        
with open("rythm.jsonl", "r") as fin:
    for line in tqdm(fin):
        json_dict = json.loads(line)
        file_dict[json_dict["lyric_id"]]["rhyme_info"] = json_dict["rythm_info"]

with open("step22_result.jsonl", "w") as file:
    for key, value in file_dict.items():
        file.write(str(value)+"\n")
