import gdown

# URL file Google Drive
url = "https://drive.google.com/uc?id=1LVNQzCqUn_8rFLv0f00Td9vFOIdwcPlJ"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win11.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")