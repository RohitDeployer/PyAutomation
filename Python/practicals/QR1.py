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

# HTML code for redirection
html_code = f"""
<html>
  <head>
    <title>Redirecting...</title>
    <script>
      window.location.href = "{combined_urls}";
    </script>
  </head>
  <body>
    If you are not redirected, <a href="{combined_urls}">click here</a>.
  </body>
</html>
"""

# Generate QR code for the HTML code
qr = pyqrcode.create(html_code)

# Save the SVG file
qr.svg("combined_qr1.svg", scale=8)

print(f"QR code for combined URLs saved as combined_qr1.svg")