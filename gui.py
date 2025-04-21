import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import os

class DekuImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("랜덤 데쿠 이미지 뷰어")

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.show_button = tk.Button(root, text="다른 데쿠 보여줘!", command=self.show_random_deku)
        self.show_button.pack(pady=5)

        self.image_paths = []
        self.load_images()
        self.current_tk_image = None

        if not self.image_paths:
            messagebox.showerror("오류", "미도리야 이미지를 찾을 수 없습니다. 이미지를 같은 폴더 또는 'images' 하위 폴더에 넣어주세요.")

    def load_images(self):
        # 현재 폴더에서 이미지 파일 찾기
        for filename in os.listdir("."):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff')):
                self.image_paths.append(filename)

        # 'images' 하위 폴더에서 이미지 파일 찾기
        if os.path.exists("images"):
            for filename in os.listdir("images"):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff')):
                    self.image_paths.append(os.path.join("images", filename))

        random.shuffle(self.image_paths) # 이미지 경로를 섞어서 처음부터 같은 이미지 나오는 것을 방지

    def show_random_deku(self):
        if self.image_paths:
            random_image_path = random.choice(self.image_paths)
            try:
                image = Image.open(random_image_path)
                self.update_image_display(image)
            except FileNotFoundError:
                messagebox.showerror("오류", f"이미지 파일 '{random_image_path}'을 찾을 수 없습니다.")
                self.image_paths.remove(random_image_path) # 찾을 수 없는 경로는 목록에서 제거
            except Exception as e:
                messagebox.showerror("오류", f"이미지 로딩 오류: {e}")
        else:
            messagebox.showinfo("알림", "표시할 미도리야 이미지가 없습니다.")

    def update_image_display(self, img):
        self.tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image # 이미지 객체 유지

if __name__ == "__main__":
    root = tk.Tk()
    app = DekuImageApp(root)
    root.mainloop()