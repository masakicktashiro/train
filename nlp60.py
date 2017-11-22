import leveldb
import gzip
import json
import os
fname_gz = "artist.json.gz"
fname_db = "test_db"

if not os.path.exists(fname_db):
    db = leveldb.LevelDB(fname_db)


def nlp60():
    with gzip.open("../"+fname_gz,"rt",encoding="utf-8") as f:
        for line in f:
            data_json = json.loads(line)
                
            key = data_json.get("name") + "\t" + str(data_json["id"])
            if data_json.get("area") is not None:
                area = data_json.get("area")
            else:
                area = ""

            db.Put(key.encode(),area.encode())
    print("{}件登録しました。".format(len(list(db.RangeIter(include_value=False)))))
if __name__ == "__main__":
    nlp60()
