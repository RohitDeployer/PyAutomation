import pyqrcode

# List of URLs
urls = [
    "https://www.linkedin.com/in/rohit-more-87a405295/",
    "https://github.com/RohitDeployer",
    "https://hashnode.com/@RohitDeployer",
    # Add more URLs as needed
]

# Concatenate URLs with a delimiter
delimiter = ","
combined_urls = delimiter.join(urls)

# Generate QR code for the combined URLs
qr = pyqrcode.create(combined_urls)

# Save the SVG file
qr.svg("combined_qr.svg", scale=8)

print(f"QR code for combined URLs saved as combined_qr.svg")