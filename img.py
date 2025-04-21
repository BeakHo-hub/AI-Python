from PIL import Image

# 이미지 열기
img = Image.open("your_image.jpg")

# 이미지 크기 확인
print(f"이미지 크기: {img.size}")

# 이미지 형식 확인
print(f"이미지 형식: {img.format}")

# 이미지 회전
rotated_img = img.rotate(90)

# 이미지 크기 조정
resized_img = img.resize((200, 150))

# 이미지 자르기 (좌상단 (50, 50)에서 가로 100, 세로 80 픽셀 영역)
cropped_img = img.crop((50, 50, 150, 130))

# 이미지 저장
rotated_img.save("rotated_image.jpg")
resized_img.save("resized_image.png")
cropped_img.save("cropped_image.bmp")

# 이미지 표시 (Jupyter Notebook 환경 등에서)
img.show()
rotated_img.show()
resized_img.show()
cropped_img.show()