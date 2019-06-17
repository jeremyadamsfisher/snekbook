from PIL import Image
from pathlib import Path


def main():
    images_orig = Path("curated_downloads").glob("*")
    images_new_dir = Path("thumbs")
    images_new_dir.mkdir(exist_ok=True)
    for img_fp in images_orig:
        for im_type, size in [("norm", (250, 250)), ("thumb", (50, 50))]:
            with Image.open(img_fp) as im:
                main_dim = min(im.size)
                im.convert("RGB")
                im_cropped = im.crop((0, 0, main_dim, main_dim))
                im_cropped.thumbnail(size, Image.ANTIALIAS)
                thumb_path = images_new_dir / f"{im_type}_{img_fp.stem}.jpg"
                im_cropped.save(str(thumb_path), "JPEG", quality=80)


if __name__ == "__main__":
    main()
