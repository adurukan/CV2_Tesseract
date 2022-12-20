import cv2
import pytesseract
import sys

arg_path = sys.argv[1]

img_cv = cv2.imread(arg_path)

img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# print(pytesseract.get_languages(config=""))
with open(arg_path.split(".")[0] + ".txt", "w") as f:
    f.write(pytesseract.image_to_string(img_rgb, lang="eng"))
    f.close()
