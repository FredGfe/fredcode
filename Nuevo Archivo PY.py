import os
import tkinter as tk
from tkinter import messagebox

# Optional dependency for resizing raster images
use_pillow = True
try:
    from PIL import Image, ImageTk
except ImportError:
    use_pillow = False

chars = [
    {
        "name": "Linne",
        "role": "Striker",
        "description": "Fast melee attacker with dashes.",
        "image": "images/linne.png",
    },
    {
        "name": "Hyde",
        "role": "Tank",
        "description": "Heavy armor and crowd control.",
        "image": "images/hyde.png",
    },
    {
        "name": "Byakuya",
        "role": "Support",
        "description": "Healer/buffer with ranged skills.",
        "image": "images/byakuya.png",
    },
    {
        "name": "Wagner",
        "role": "Mage",
        "description": "High burst damage with spells.",
        "image": "images/wagner.png",
    },
]

class CharacterSelectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Select")
        self.root.geometry("560x420")
        self.selected = None
        self.image_cache = {}

        self.title_label = tk.Label(root, text="Select Your Character", font=("Segoe UI", 16, "bold"))
        self.title_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=5)

        # placeholder image in case real asset is unavailable
        self.placeholder_photo = tk.PhotoImage(width=220, height=220)
        self.placeholder_photo.put("#dddddd", to=(0, 0, 220, 220))
        self.placeholder_photo.put("#888888", to=(1, 1, 218, 218))

        self.portrait_label = tk.Label(root, text="No character selected", width=220, height=220, relief="sunken", bg="#ffffff", compound="center", image=self.placeholder_photo)
        self.portrait_label.image = self.placeholder_photo
        self.portrait_label.pack(pady=5)

        self.info_text = tk.Text(root, width=64, height=4, state="disabled", bg="#f8f8f8")
        self.info_text.pack(padx=10, pady=5)

        self.confirm_button = tk.Button(root, text="Confirm Selection", command=self.confirm_selection, state="disabled")
        self.confirm_button.pack(pady=8)

        self.build_character_buttons()

    def load_character_image(self, image_path):
        if image_path in self.image_cache:
            return self.image_cache[image_path]

        full_path = os.path.abspath(image_path)
        img = None

        if os.path.exists(full_path):
            if use_pillow:
                try:
                    pil_img = Image.open(full_path)
                    pil_img = pil_img.convert("RGBA")

                    max_w, max_h = 220, 220
                    orig_w, orig_h = pil_img.size
                    scale = min(max_w / orig_w, max_h / orig_h)
                    scaled_w = max(1, int(orig_w * scale))
                    scaled_h = max(1, int(orig_h * scale))

                    resized = pil_img.resize((scaled_w, scaled_h), Image.LANCZOS)

                    canvas = Image.new("RGBA", (max_w, max_h), (220, 220, 220, 255))
                    offset_x = (max_w - scaled_w) // 2
                    offset_y = (max_h - scaled_h) // 2
                    canvas.paste(resized, (offset_x, offset_y), resized)

                    img = ImageTk.PhotoImage(canvas)
                except Exception:
                    img = None
            else:
                try:
                    img = tk.PhotoImage(file=full_path)
                except Exception:
                    img = None

        self.image_cache[image_path] = img
        return img

    def build_character_buttons(self):
        for i, char in enumerate(chars):
            btn = tk.Button(
                self.buttons_frame,
                text=f"{char['name']} ({char['role']})",
                width=16,
                relief="raised",
                command=lambda c=char: self.select_character(c),
            )
            btn.grid(row=0, column=i, padx=4)

    def select_character(self, char):
        self.selected = char
        img = self.load_character_image(char.get("image", ""))

        if img is not None:
            self.portrait_label.configure(image=img, text="")
            self.portrait_label.image = img
        else:
            self.portrait_label.configure(image=self.placeholder_photo, text=f"{char['name']}\nportrait missing", font=("Segoe UI", 10), compound="center")
            self.portrait_label.image = self.placeholder_photo

        self.info_text.configure(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"Name: {char['name']}\n")
        self.info_text.insert(tk.END, f"Role: {char['role']}\n")
        self.info_text.insert(tk.END, f"Description: {char['description']}\n")
        self.info_text.configure(state="disabled")
        self.confirm_button.configure(state="normal")

    def confirm_selection(self):
        if not self.selected:
            messagebox.showwarning("No selection", "Please select a character first.")
            return
        messagebox.showinfo("Character Confirmed", f"You selected: {self.selected['name']} ({self.selected['role']})")


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSelectApp(root)
    root.mainloop()

