import xml.etree.ElementTree as ET
import pydot_ng as pydot
import nlp44
fname_parsed="nlp.txt.xml"


def nlp57():
    root=ET.parse(fname_parsed)
    i=0
    for deps in root.iterfind(
        './document/sentences/sentence/dependencies' + \
        '[@type="collapsed-dependencies"]'):
        root_ls = []
        dis_ls = []
        i+=1
        for dep in deps.iter("dep"):
            if dep.get("type") != "punct":
                root_ls.append(
                    (dep.find("./governor").get("idx"),
                    dep.find("./governor").text))
                dis_ls.append(
                    (dep.find("./dependent").get("idx"),
                    dep.find("./dependent").text))

        yield (root_ls, dis_ls)

if __name__ == "__main__":
    sen_num=0
    for root_ls,dis_ls in zip(
        [i[0] for i in nlp57()],
        [i[1] for i in nlp57()]):
        sen_num+=1
        print(sen_num)
        print([(i, p) for i, p in zip(root_ls, dis_ls)])
        graph = nlp44.graph_from_edges_ex([
            (i, p) for i, p in zip(root_ls, dis_ls)],directed=True)
        graph.write_png("sen_num{}.png".format(sen_num))
