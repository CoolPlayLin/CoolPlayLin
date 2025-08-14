from time import sleep, time
import requests
import random
import pathlib
import json
import os

# Setup
apis = ["https://i18.net/bing.php"]
PATH = pathlib.Path(__file__).parents[1] / "photo.png"
HISTORY_PATH = pathlib.Path(__file__).parents[1] / "assets"


def main():
    CONTINUE = True
    TIMES = 0
    if not (int(time()) % random.randint(1, 10) in [random.randint(1, 10) for each in range(random.randint(1, 8))]):
        RUN_TIMES = 1
    if (int(time()) % random.randint(1, 10) in [random.randint(1, 10) for each in range(random.randint(1, 10))]):
        Archive = True
        HISTORY = [int(pathlib.Path(each.replace("photo", "").replace(
            "-", "")).stem) for each in os.listdir(HISTORY_PATH)]
        HISTORY.sort()
        Archive_PATH = HISTORY_PATH / f"photo-{HISTORY[-1] + 1}.png"
        del HISTORY
    else:
        Archive = False
    
    url = apis[random.randint(0, len(apis)-1)]
    response = requests.get(url, verify=False)

    with open(PATH, "wb+") as f:
        f.write(response.content)
    if Archive:
        with open(Archive_PATH, "wb+") as f:
            f.write(response.content)


if __name__ == "__main__":
    if (pathlib.Path(__file__).parents[1] / "config.json").exists():
        with open(pathlib.Path(__file__).parents[1] / "config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            if not config["Image_up"]:
                print("Image Updater has been disabled")
                exit(0)
    main()
