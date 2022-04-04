from PIL import Image, ImageSequence
import pytesseract


# TODO:
# look at translation apis - gcp free tier?
# test output on non-standard pages
# setup config - file ext, lang, img loc, keys, maybe page:psm dict for any non-standard pages

LANG = "fin"

if __name__ == "__main__":
    # big multi-page tiff - just break for now
    with Image.open("./local/history.tif") as img:
        for idx, frame in enumerate(ImageSequence.Iterator(img)):
            pg = pytesseract.image_to_string(frame, lang=LANG)
            print(pg)
            if idx == 1:
                break
