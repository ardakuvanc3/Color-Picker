import tkinter as tk
import pyautogui
import webcolors

def update_color():
    # Farenin bulunduğu konumu al
    x, y = pyautogui.position()
    # Ekran görüntüsü al ve fare pozisyonundaki pikselin rengini al
    screenshot = pyautogui.screenshot()
    pixel_color = screenshot.getpixel((x, y))
    # RGB'yi HEX koduna çevir
    hex_color = webcolors.rgb_to_hex(pixel_color)
    # Renk kodunu etikete ve pencerenin arka planına uygula
    color_label.config(text=hex_color, bg=hex_color)
    # Pencereyi sürekli güncellemek için fonksiyonu tekrar çağır
    root.after(100, update_color)

# Tkinter pencere oluşturma
root = tk.Tk()
root.title("Color Picker")
root.geometry("300x100")
root.attributes('-topmost', True)  # Pencereyi her zaman en üstte tut

# Renk kodunu göstermek için label oluşturma
color_label = tk.Label(root, text="Renk kodu burada", font=("Helvetica", 14))
color_label.pack(pady=20)

# Renk kodunu güncellemek için update_color fonksiyonunu çağır
update_color()

root.mainloop()
