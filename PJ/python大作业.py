import re


def tag_count(text):
    left_tags = re.findall(r"<[^/!]*?[ >]", text)
    for i in left_tags:
        i = i[1:-1].lower()
        if i in tags:
            tags[i] += 1
        else:
            tags[i] = 1

def write(content, add_empty=False):
    if add_empty:
        out_file.write("\n")
    out_file.write(content + "\n")

def get_sub_file(merchant_path):
    true_path = folder + merchant_path[2:]
    merchant_str = open(true_path, "rt").read().replace("\n", "").replace("\r", "")
    tag_count(merchant_str)

    merchant_str = merchant_str.replace("<br>", "").strip()

    scene_name = get_value(merchant_str, "h3")[0]
    write("### " + scene_name, True)

    stage_tip = get_value(merchant_str, "i")[0]
    write("*" + stage_tip + "*", True)

    for ab in get_ab(merchant_str):
        # 演员名
        write("**" + ab[0] + "**", True)
        # 台词
        write("")
        for j in ab[1]:
            if re.match("<i>", j):
                write("*" + get_value(j, "i")[0] + "*", True)
                write("")
                continue
            write(j)


def get_value(text, tag_name = ""):
    # 解析尖括号里面的内容
    if tag_name == "":
        res = re.findall(r"[^>]*<", text)
        for i in range(len(res)):
            res[i] = res[i][:-1].strip()
        return res
    else:
        tuple_list = re.findall(
            r"<" + tag_name + r"[\s\S]*?</" + tag_name + r">", text, re.I
        )
        res_list = []
        for i in range(len(tuple_list)):
            mid_with_brackets = re.findall(r">[\s\S]*<", tuple_list[i][1:-1])[0]
            res_list.append(mid_with_brackets[1:-1].strip())
        return res_list


def get_tag_html(text):
    res_list = re.findall(r'href=".*"', text)
    return res_list[0][6:-1].strip()


def get_ab(text):
    tuple_list = re.findall(
        r"<a[^<>]*?><b>[^<>]*?</b></a>[^<>]*?<blockquote>.*?</blockquote>", text, re.I
    )

    res = []
    for i in range(len(tuple_list)):
        val = tuple_list[i]
        res.append([])
        # 0:
        res[i].append(get_value(val, "b")[0])
        bq = get_value(val, "blockquote")[0]
        # 1:
        res[i].append(get_value(bq, "[ap]"))
    return res


out_file = open("The Merchant of Venice.md", "w")

tags = {}
file_path = ""
folder = ""

file_path = input("请输入文件")
try:
    scene_list_str = open(file_path, "rt")
except FileNotFoundError:
    print("找不到文件")
    exit(0)

# 找到前缀路径
index = -1
for i in range(len(file_path)):
    if file_path[i] == "/" or file_path[i] == "\\":
        index = i
folder = file_path[: index + 1]

scene_list_str = scene_list_str.read().replace("\n", "").replace("\r", "")
tag_count(scene_list_str)
body = get_value(scene_list_str, "body")[0]

write("# " + "The Merchant of Venice", True)

p_list = get_value(body, "p")

# 解析p标签
for i in range(len(p_list)):
    p_list[i] = p_list[i].split("<br>")[0:-1]
    for j in range(len(p_list[i])):
        p_list[i][j] = p_list[i][j].strip()

for act in p_list:
    write("## " + act[0][:5], True)
    for scene in act:
        scene_name = get_value(scene)
        scene_file_path = get_tag_html(scene)
        get_sub_file(scene_file_path)

res = sorted(tags.items(), key=lambda kv: kv[1], reverse=True)[:3]
print("使用最多的三个标签:")
for i in res:
    print(i[0] + ": " + str(i[1]))

out_file.close()
