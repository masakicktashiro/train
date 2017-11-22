import os
import subprocess
import xml.etree.ElementTree as ET

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'


def parse_nlp():
    if not os.path.exists(fname_parsed):
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2017-06-09/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,     # shellで実行
            check=True      # エラーチェックあり
        )

if __name__ == "__main__":
    parse_nlp()
    root = ET.parse(fname_parsed)
    for word in root.iter("word"):
        print(word.text)
