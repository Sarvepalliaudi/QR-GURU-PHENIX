import qrcode

# Your link or text 
data = "https://www.linkedin.com/in/audi-siva-bhanuvardhan-sarvepalli-4598a8289/"

# Create QR code object
qr = qrcode.make(data)

# Save the QR code as an image
qr.save("my_qr.png")

print("QR code generated and saved as my_qr.png")
 

