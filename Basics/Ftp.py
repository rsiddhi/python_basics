from ftplib import FTP

# Connect to FTP server
ftp = FTP("ftp.dlptest.com")  # public test FTP server
ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")  # test credentials

# Show files
ftp.retrlines("LIST")

# Download a file
with open("downloaded_file.txt", "wb") as f:
    ftp.retrbinary("RETR test.txt", f.write)

ftp.quit()
