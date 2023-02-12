import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image


# create GUI window
window = tk.Tk()
window.title("QR code Generator")
window.geometry("500x500")

# label to display instructions
label = tk.Label(text="Enter the URL or TEXT:", font=("helvetica",15))
label.pack()

# entry widget to take input from user
entry = tk.Entry(font=("Helvetica", 15), width=30)
entry.pack()

# button to generate QR code
def generate_qr_code():
    # get the URL from entry widget
    url = entry.get()
    # create QR code object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # add data to QR code object
    qr.add_data(url)
    qr.make(fit=True)
    # convert QR code object to image
    img = qr.make_image(fill_color="black", back_color="white")
    # convert image to PhotoImage object
    img = ImageTk.PhotoImage(img.convert("RGB"))
    # display QR code in label
    qr_code_label = tk.Label(image=img)
    qr_code_label.image = img
    qr_code_label.pack()
    # button to save QR code image

def save_image():
    # get the URL from entry widget
    url = entry.get()
    # create QR code object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # add data to QR code object
    qr.add_data(url)
    qr.make(fit=True)
    # convert QR code object to image
    img = qr.make_image(fill_color="black", back_color="white")
    # open file dialog to select location to save image
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    # save image to selected location
    img.save(file_path)
    # open file dialog to select location to save image
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    # save image to selected location
    img.save(file_path)


# create generate button
generate_button = tk.Button(text="Generate QR code", command=generate_qr_code)
generate_button.pack()

# create save button
save_button = tk.Button(text="Save QR code", command=save_image, font=("Helvetica", 15))
save_button.pack()

# run the GUI window
window.mainloop()
