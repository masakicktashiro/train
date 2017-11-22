import xml.etree.ElementTree as ET
fname_parsed = "nlp.txt.xml"


def nlp56():
    root = ET.parse(fname_parsed)
    core_ls = []
    core_dic = {}
    for i in root.iter("coreference"):
        core = i.findtext(
            "./mention[@representative='true']/text")
        for t in i.iterfind("./mention"):
            start_num = int(t.findtext("start"))
            sen_num = int(t.findtext("sentence"))
            end_num = int(t.findtext("end"))
            core_dic[
                str(sen_num) + "_" + str(start_num)] = [core,end_num]
            core_ls.append([sen_num, start_num, end_num])
    return core_ls, core_dic

if __name__  == "__main__":
    core_ls,core_dic = nlp56()
    root = ET.parse(fname_parsed)
    for i in root.iterfind(
        "./document/sentences/sentence"):
        sen_num = int(i.get("id"))
        org_test=0
        for t in i.iterfind("./tokens/token"):
            start_num = int(t.get("id"))
            if (sen_num, start_num) in (
                (i[0],i[1]) for i in core_ls):
                org_test =core_dic[
                    str(sen_num) + "_" + str(start_num)][1] - start_num
                print(
                    "[" + \
                    core_dic[str(sen_num) + "_" + str(start_num)][0] + \
                    "]",
                    "(",end="")
                print(t.findtext("word"),end=" ")
            elif org_test > 0:
                print(t.findtext("word"),end=" ")
                org_test -= 1
                if org_test == 0:
                    print(")",end=" ")
            else:
                print(t.findtext("word"),end=" ")
        print()                
