import json
# from tqdm import tqdm
# from pypinyin.contrib.tone_convert import to_finals
# from g2pM import G2pM
# g2pw = G2pM()
# lista = [i.replace("u:", "v") for i in g2pw("虐卷均旅", tone=True, char_split=False)]
# print(lista)
# print([to_finals(i) for i in lista])
# print(to_finals("nve"))

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
#     output_file = open("outputs/rythm_result1.jsonl", "w")
#     i = 0
#     for line in tqdm(f):
#         i += 1
#         if i >= 200000:
#             if(i%50000 == 0):
#                 output_file.close()
#                 output_file = open(f"outputs/rythm_result{int(i/50000)}.jsonl", "w")
#             try:
#                 data_json = json.loads(line)
#             except Exception as e:
#                 print(e)
#             lyric = data_json["processed_lyric"]
#             lyric_id = data_json["lyric_id"]
#             last_chars = [i[-1] if i != "" else "" for i in lyric]
#             pinyin = [i.replace("u:", "v") for i in g2pw(last_chars, tone=False, char_split=False)]
#             finals = [to_finals(i) for i in pinyin]
#             rythm = [(yun_mapper[i] if i in yun_mapper else -1) for i in finals]
#             output_file.write("{\"lyric_id\": " + str(lyric_id) +", \"rythm_info\": " + str(rythm) +"}\n")
            
#     output_file.close()

with open("step21_result.jsonl", "r") as file:
    for line in file:
        print([i.replace(" ", "") for i in json.loads(line)["processed_lyric"]])
        break