from pypinyin import pinyin
from pypinyin import Style
from collections import Counter
from pprint import pprint
from pypinyin.contrib.tone_convert import to_finals
from g2pM import G2pM
import os
import json
from pprint import pprint
from tqdm import tqdm, trange

GPU_ID = '7'
os.environ['CUDA_VISIBLE_DEVICES'] = GPU_ID

# g2pw = G2PWConverter(
#             model_dir='G2PWModel_v2/',
#             style='pinyin',
#             model_source=None,
#             num_workers=10,
#             batch_size=4096,
#             enable_non_tradional_chinese=True,
#             turnoff_tqdm=False
#         )

g2pw = G2pM()

tongyun = Counter()
pingze = Counter()
yun_mapper = {'a': 0, 'ia': 0, 'ua': 0, 
              'o': 1, 'uo': 1, 
              'e': 2, 'ie': 2, 've': 2, 
              'i': 3, 
              'u': 4, 
              'v': 5, 
              'ai': 6, 'uai': 6, 
              'ei': 7, 'uei': 7, 'ui': 7,
              'ao': 8, 'iao': 8, 
              'ou': 9, 'iou': 9, 'iu': 9,
              'an': 10, 'ian': 10, 'uan': 10, 'van': 10, 
              'en': 11, 'in': 11, 'uen': 11, 'vn': 11, 'un': 11,
              'ang': 12, 'iang': 12, 'uang': 12,
              'eng': 13, 'ing': 13, 'ueng': 13,
              'ong': 14, 'iong': 14,
              'er': 15}
def map_pinyin_to_ans(tone):
    if tone is None:
        return (-1, -1)
    
    yun = to_finals(tone)
    if yun not in yun_mapper:
        # print(tone)
        return (-1, -1)
    yun = yun_mapper[yun]

    diao = tone[-1]
    if diao == '5':
        diao = 2
    elif diao == '3' or diao == '4':
        diao = 1
    elif diao == '1' or diao == '2':
        diao = 0
    return yun, diao

def tone_detect(sentence_list):
    # print(sentence_list)
    all_res = []
    for sentence in tqdm(sentence_list):
        # print(sentence)
        if sentence != "":
            all_res.append(g2pw(sentence, tone=True, char_split=False))
        else:
            all_res.append([""])
    final_res = []
    # print(all_res)
    for res, sentence in zip(all_res, sentence_list):
        if not res or res[-1] is None:
            y, d = map_pinyin_to_ans(None)
        else:
            y, d = map_pinyin_to_ans(res[-1])
        
        
        tongyun[y] += 1
        pingze[d] += 1
        final_res.append([sentence, y])

    return final_res


song_list = []
song_len = []
song_id = []
with open('step16_result.jsonl', 'r', encoding="utf-8") as f:
    cnt = 0
    for line in tqdm(f):
        cnt += 1
        
        # if cnt > 10:
        #     break
        # print(data["generation_string"])
        if cnt > 470000:
            lyric_dict = json.loads(line)
            sentence_list = lyric_dict["no_punctuation_lyric"]
            song_list += sentence_list
            song_len.append(len(sentence_list))
            song_id.append(lyric_dict['lyric_id'])
            cnt+=1
print("computing")
final_res = tone_detect(song_list)
st = 0
print("writing into file"+f'outputs/lyric_test_res{48}.txt')
with open(f'outputs/lyric_test_res{48}.jsonl', 'w') as fout:
    for l in trange(len(song_len)):
        cur_song = final_res[st:st+song_len[l]]
        cur_song_str = json.dumps(cur_song, ensure_ascii=False)
        fout.write("{\"id\":"+str(song_id[l])+", \"lyric\":"+cur_song_str+'}\n') 
        st += song_len[l]
song_list = []
song_len = []
song_id = [] 
            