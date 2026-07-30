import easyocr
import cv2

reader = easyocr.Reader(['en', 'hi'])

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    processed_path = image_path.replace(".", "_processed.")

    cv2.imwrite(processed_path, gray)

    return processed_path

def extract_text(image_path):

    processed_image = preprocess_image(image_path)

    result = reader.readtext(processed_image)

    text = ""
    confidence = []

    for item in result:
        text += item[1] + "\n"
        confidence.append(round(item[2] * 100, 2))

    avg_confidence = 0

    if confidence:
        avg_confidence = round(sum(confidence) / len(confidence), 2)

    return text, avg_confidence

    return text