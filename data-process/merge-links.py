import common
import json

def join(lst):
    print(type(lst))
    return json.loads("".join(lst))
link_vi = join(common.read_file("./js/link.vi"))
link_en = join(common.read_file("./js/link.en"))
link_ja = join(common.read_file("./js/link.ja"))
result = []
for i in range(0, len(link_vi)):
    vi = link_vi[i]
    en = link_en[i]
    ja = link_ja[i]
    dic = {
        "vi": vi,
        "en": en,
        "ja": ja,
    }
    result.append(dic)
link = json.dumps(result, indent=4)
common.write_file("link.txt", link)
