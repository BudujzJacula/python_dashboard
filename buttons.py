import tkinter as tk

root = tk.Tk()

root.geometry("1024x600")
root.title("OBD2 Dashboard")

label = tk.Label(root, text="Hello, World!", font=("Helvetica", 36))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=('Arial', 16), height=3)
textbox.pack(padx=20, pady=20)

button = tk.Button(root, text="Click me!", font=('Arial', 16))
button.pack(padx=20, pady=20)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn_1 = tk.Button(button_frame, text="1", font=('Arial', 18))
btn_1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn_2 = tk.Button(button_frame, text="2", font=('Arial', 18))
btn_2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn_3 = tk.Button(button_frame, text="3", font=('Arial', 18))
btn_3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn_4 = tk.Button(button_frame, text="4", font=('Arial', 18))
btn_4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn_5 = tk.Button(button_frame, text="5", font=('Arial', 18))
btn_5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn_6 = tk.Button(button_frame, text="6", font=('Arial', 18))
btn_6.grid(row=1, column=2, sticky=tk.W + tk.E)

button_frame.pack(fill='x')

another_btn = tk.Button(root, text="Another button", font=('Arial', 18))
another_btn.place(x=400, y=400, height=100, width=200)


root.mainloop()