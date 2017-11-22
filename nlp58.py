import xml.etree.ElementTree as ET
fname_parsed = "nlp.txt.xml"


def nlp58():
    root = ET.parse(fname_parsed)

    for sentence in root.iterfind("./document/sentences/sentence"):
        sent_dic = {}
        jutsu = ""
        shugo = ""
        mokuteki = ""

        for dep in sentence.iterfind(
           "dependencies[@type='collapsed-dependencies']/dep"):
                dep_type = dep.get("type")
                gov_idx = dep.find("./governor").get("idx")
                gov = dep.find("./governor").text
                if gov_idx + "_" + gov not in sent_dic.keys():
                    sent_dic[
                        gov_idx + "_" + gov] = [0, 0]
                if dep_type == "nsubj":
                    sent_dic[
                        gov_idx + "_" + gov][0] = 1
                elif dep_type == "dobj":
                    sent_dic[
                        gov_idx + "_" + gov][1] = 1
                if sent_dic[gov_idx + "_" + gov] == [1, 1]:
                    jutsu = gov_idx + "_" + gov
                #print(sent_dic)

        for dep in sentence.iterfind(
           "dependencies[@type='collapsed-dependencies']/dep"):
                dep_type = dep.get("type")
                gov_idx = dep.find("./governor").get("idx")
                gov = dep.find("./governor").text
                if gov_idx + "_" + gov == jutsu and \
                   dep_type == "nsubj":
                        shugo = dep.findtext("./dependent")
                elif gov_idx + "_" + gov == jutsu and \
                 dep_type == "dobj":
                        mokuteki = dep.findtext("./dependent")
        if len(jutsu) > 0:
            yield shugo + "\t" + jutsu.split("_")[1] + "\t" + mokuteki
        else:
            yield ""
if __name__ == "__main__":
    for i,sentence in enumerate(nlp58()):
        if len(sentence) > 0:
            print(i,sentence)
