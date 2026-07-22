from PIL import Image
import matplotlib.pyplot as plt
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image load
img = Image.open("sample.jpg")

# Image show
plt.imshow(img)
plt.axis("off")
plt.savefig("sample.jpg")
print("image close ho gyi h")

# Image details
print("----- Image Details -----")
print("Width :", img.width)
print("Height:", img.height)
print("Format:", img.format)
print("Mode  :", img.mode)

# OCR
text = pytesseract.image_to_string(img)

print("\n----- Recognized Text -----")
print(text)
