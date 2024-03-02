import pathlib
import requests
import json

if (pathlib.Path(__file__).parents[1] / "config.json").exists():
    with open(pathlib.Path(__file__).parents[1] / "config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        if not config["Words"]:
            print("Word Upgrader has been disabled")
            exit(0)

PATH = pathlib.Path(__file__).parents[1] / "README.md"
word = requests.get("https://v1.hitokoto.cn/", verify=False).json()

with open(PATH, mode="r", encoding="utf-8") as f:
    README = f.readlines()
    author = word['from_who'] if word['from_who'] != None else "佚名"
    README[README.index("```\n")+1] = word["hitokoto"] + f" --{author}" + "\n"
    with open(PATH, "w+", encoding="utf-8") as w:
        w.writelines(README)
    print("Replaced with: " ,word["hitokoto"] + f" --{author}" + "\n")