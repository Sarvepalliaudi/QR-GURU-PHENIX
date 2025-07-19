✅ Corrected & Working Version:
python
Copy
Edit
import qrcode

# Your link or text 
data = "https://www.linkedin.com/in/audi-siva-bhanuvardhan-sarvepalli-4598a8289/"

# Create QR code object
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("my_qr.png")  # This line works because 'qr' is a PIL Image object

print("QR code generated and saved as my_qr.png")
🔍 Additional Tip:
If you want more customization like size, color, or border, you can use qrcode.QRCode:

python
Copy
Edit
import qrcode

data = "https://www.linkedin.com/in/audi-siva-bhanuvardhan-sarvepalli-4598a8289/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qr.png")

print("Customized QR code generated and saved as custom_qr.png")
Let me know if you want it in a specific color, size, or format (like SVG or PDF).








You said:
i am giving this code in git repo so please give the read me 


ChatGPT said:
Here’s a professional and clean README.md for your QR code generator GitHub repository:

🔗 QR Code Generator using Python
This project generates a QR code for any given text or URL using Python's qrcode library. In this case, the QR code links to a LinkedIn profile.

📌 Preview
It generates a QR code like this (example output):

🧑‍💻 Author
Audi Siva Bhanuvardhan Sarvepalli
🔗 LinkedIn Profile

🚀 Features
Generate QR codes from any URL or text

Save the QR code as an image (PNG)

Simple and beginner-friendly code

Easily customizable (size, colors, border, etc.)

🛠️ Requirements
Python 3.x

qrcode library

Pillow (PIL) for image saving

⚙️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
Install dependencies

bash
Copy
Edit
pip install qrcode[pil]
📄 Usage
bash
Copy
Edit
python generate_qr.py
This will generate a file named my_qr.png in the same directory, containing your QR code.

📁 File Structure
css
Copy
Edit
qr-code-generator/
│
├── generate_qr.py      # Main QR code generator script
├── my_qr.png           # Output QR code image
└── README.md           # Project information
🧩 Customize
You can change the data variable inside generate_qr.py to any text or URL you like:

python
Copy
Edit
data = "https://example.com"
To further customize the size, error correction, colors, etc., use the advanced version in the script with qrcode.QRCode().

📜 License
This project is open source and available under the MIT License.
