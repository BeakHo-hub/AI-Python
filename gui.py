import tkinter as tk
from PIL import Image, ImageTk

class DekuImageViewer:
    def __init__(self, root, image_files):
        self.root = root
        self.root.title("미도리야 이미지 뷰어")

        self.image_files = image_files
        self.tk_images = [None] * len(image_files)
        self.current_image_index = -1

        # 초기 이미지 선택 버튼 프레임
        self.select_frame = tk.Frame(root)
        self.select_frame.pack(pady=10)

        self.image_buttons = []
        for i, filename in enumerate(self.image_files):
            button = tk.Button(self.select_frame, text=f"미도리야 {i+1}", command=lambda idx=i: self.show_selected_image(idx))
            button.pack(side=tk.LEFT, padx=5)
            self.image_buttons.append(button)

        # 이미지 표시 레이블
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # 이동 버튼 프레임 (처음에는 숨김)
        self.navigation_frame = tk.Frame(root)
        self.navigation_buttons = []
        for i in range(len(image_files) - 1):
            button = tk.Button(self.navigation_frame, text="", command=lambda idx=i: self.show_other_image(idx))
            self.navigation_buttons.append(button)

        self.load_tk_images()

    def load_tk_images(self):
        for i, filename in enumerate(self.image_files):
            try:
                img = Image.open(filename)
                self.tk_images[i] = ImageTk.PhotoImage(img)
            except FileNotFoundError:
                tk.messagebox.showerror("오류", f"이미지 파일 '{filename}'을 찾을 수 없습니다.")
                self.tk_images[i] = None
            except Exception as e:
                tk.messagebox.showerror("오류", f"이미지 로딩 오류: {e}")
                self.tk_images[i] = None

    def show_selected_image(self, index):
        if 0 <= index < len(self.tk_images) and self.tk_images[index]:
            self.current_image_index = index
            self.image_label.config(image=self.tk_images[index])
            self.image_label.image = self.tk_images[index] # 이미지 객체 유지
            self.update_navigation_buttons()
            self.navigation_frame.pack(pady=5) # 이동 버튼 프레임 표시
        else:
            tk.messagebox.showerror("오류", "이미지를 표시할 수 없습니다.")

    def update_navigation_buttons(self):
        other_images_indices = [i for i in range(len(self.image_files)) if i != self.current_image_index]
        for i, idx in enumerate(other_images_indices):
            if 0 <= idx < len(self.image_files):
                button_text = f"미도리야 {idx + 1}"
                command = lambda target_idx=idx: self.show_selected_image(target_idx)
                if i < len(self.navigation_buttons):
                    self.navigation_buttons[i].config(text=button_text, command=command)
            else:
                if i < len(self.navigation_buttons):
                    self.navigation_buttons[i].config(text="", command=None)

        # 필요한 만큼 이동 버튼 프레임에 버튼 배치
        for button in self.navigation_buttons:
            button.pack(side=tk.LEFT, padx=5)

    def show_other_image(self, nav_index):
        other_images_indices = [i for i in range(len(self.image_files)) if i != self.current_image_index]
        if 0 <= nav_index < len(other_images_indices):
            self.show_selected_image(other_images_indices[nav_index])

if __name__ == "__main__":
    root = tk.Tk()
    image_files = ["deku1.png", "deku2.jpg", "deku3.png", "deku4.jpg", "deku5.png"] # 실제 파일명으로 변경
    app = DekuImageViewer(root, image_files)
    root.mainloop()