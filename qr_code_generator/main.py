import qrcode

def generate_qr_code():
    data = input("Enter the data to encode in the QR code: ")
    output_file = input("Enter the output file name (e.g., qrcode.png): ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved to {output_file}")

# Run the function
generate_qr_code()

