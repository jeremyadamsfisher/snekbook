import argparse
import csv
import subprocess
import webbrowser
import json
from PIL import Image
from pathlib import Path
from google_images_download import google_images_download


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("snake_db_fp", type=Path)
    return parser.parse_args().__dict__

def main(snake_db_fp: Path):
    sneks_already_encountered = []
    sneks_skipped = []
    sneks_already_encountered_fp = Path("sneks_encountered.json")
    if sneks_already_encountered_fp.exists():
        with sneks_already_encountered_fp.open() as f:
            j = json.load(f)
            sneks_already_encountered = j["encountered"]
            sneks_skipped = j["skipped"]
    with snake_db_fp.open() as f:
        snake_download_dir = Path.cwd() / "curated_downloads"
        snake_download_dir.mkdir(exist_ok=True)
        for snake in csv.DictReader(f):
            if snake["index"] in sneks_already_encountered or snake["index"] in sneks_skipped:
                continue
            else:
                try:
                    response = google_images_download.googleimagesdownload()
                    downloads = list(response.download({
                        "keywords": f"{snake['genus']} {snake['species']} {snake['common_name']}",
                        "limit": 4,
                    })[0].values())[0]
                    images = [Image.open(fp) for fp in downloads]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.show()
                    chosen_snake_idx = None
                    while True:
                        try:
                            chosen_snake_idx = int(input(f"Which snake do you choose? (Select: {list(range(1, len(images) + 1))}) ")) - 1
                            chosen_snake_fp = Path(downloads.pop(chosen_snake_idx))
                        except ValueError:
                            raise NameError  # skip
                        except IndexError:
                            pass  # invalid input
                        else:
                            break
                    chosen_snake_fp.replace(snake_download_dir / f"{snake['index']}{chosen_snake_fp.suffix.lower()}")
                    sneks_already_encountered.append(snake["index"])
                    for other_download in downloads:
                        Path(other_download).unlink()
                except NameError:
                    sneks_skipped.append(snake["index"])
            subprocess.check_call('''osascript -e \'quit app "Preview"\'''', shell=True)
            with sneks_already_encountered_fp.open("wt") as f:
                json.dump({
                    "encountered": sneks_already_encountered,
                    "skipped": sneks_skipped, 
                }, f)


if __name__ == "__main__":
    main(**cli())