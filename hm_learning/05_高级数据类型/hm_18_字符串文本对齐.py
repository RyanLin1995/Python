# 假设: 以下内容是从网络上抓取的
# 要求: 顺序并且居中对齐输出以下内容
poem = ["\t\n   登鹳雀楼",
        "王之涣\t",
        "白日依山尽",
        "黄河入海流   ",
        "欲穷千里目\r",
        "    更上一层楼"]

for poem_str in poem:
    # 先使用strip方法去掉字符串空白字符
    # 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, "　"))
