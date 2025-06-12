import requests
import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import pprint
import cv2 as cv


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
vid = os.path.join(SCRIPT_DIR, "..", "videos", "1.mp4")



cap = cv.VideoCapture(vid)
if not cap.isOpened():
    print("Error: Could not open video")
else:
    print("Video opened")

frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
print(frames)
frameBreak = frames // 10
framesToGet = [i * frameBreak for i in range(1,11)]
print(framesToGet)


selected_frames = []
i = 0
j = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Not ret")
        break

    if j < len(framesToGet) and i == framesToGet[j]:
        rgbFrame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        pilImage = Image.fromarray(rgbFrame)
        selected_frames.append(pilImage)
        j += 1
    i += 1

cap.release()


# if ret:
#     imagePath = 'frame.jpg'
#     cv.imwrite(imagePath, frame)
#     # cv.imshow("First frame: ", frame)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()
# else:
#     print("Could not read the fram")




# print("Current working directory:", os.getcwd())
# if not os.path.exists(img1):
#     raise FileNotFoundError(f"Image not found at path: {img1}")

# if not os.path.exists(img2):
#     raise FileNotFoundError(f"Image not found at path: {img2}")


# # imagePaths = [img1, img2]

# # for path in imagePaths:
# #     raw = Image.open(path).convert('RGB')
# #     input = processor(raw, return_tensors="pt")
# #     out = model.generate(**input)
# #     print(processor.decode(out[0], skip_special_tokens=True))

# rawImg1 = Image.open(img1).convert('RGB')
# # rawImg2 = Image.open(img2).convert('RGB')

# inputs = processor(rawImg1, return_tensors="pt")
# pprint.pprint(inputs)
# out = model.generate(**inputs)
# print()
# print(out)
# # print(processor.decode(out[0], skip_special_tokens=True))


tempContext = []

for f in selected_frames:
    inputs = processor(f, return_tensors="pt")
    out = model.generate(**inputs)
    tempContext.append(processor.decode(out[0], skip_special_tokens=True))


textSet = set()
mainContext = []
for t in tempContext:
    if t not in textSet:
        textSet.add(t)
        mainContext.append(t)

pprint.pprint(mainContext)



