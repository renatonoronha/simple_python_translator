from tkinter import Tk, ttk, Text, Button
from ttkthemes import ThemedTk
from translate import Translator

#JANELA TK DEFAULT
# window = Tk()

#JANELA DO TTKTHEMES
window = ThemedTk(theme='breeze')

window.title('SmiiLe Translator')

global_frame = ttk.Frame()

def translate_to(event=None):
    input_txt = input_text.get('1.0', 'end')
    src = input_combo.get()
    dest = output_combo.get()
    translation = Translator(from_lang=src, to_lang=dest).translate(input_txt)

    output_text.configure(state='normal') 
    output_text.delete('1.0', 'end')
    output_text.insert('1.0', translation)
    output_text.configure(state='disabled')


values = ['pt', 'en', 'es', 'ja']

#INPUT
input_frame = ttk.Frame(global_frame)

input_label = ttk.Label(
    input_frame,
    text='Input', 
    font=(None, 20)
)
input_combo = ttk.Combobox(
    input_frame, 
    values=values,
    font=(None, 15)
)
input_combo.set('pt')

input_label.grid(row=0, column=0, padx=10, pady=10)
input_combo.grid(row=0, column=1, padx=10, pady=10)
input_frame.pack()

input_text = Text(
    global_frame, 
    height=10, 
    width=50, 
    font=(None, 15))
input_text.pack(padx=10, fill='both', expand='yes')


#OUTPUT
output_frame = ttk.Frame(global_frame)

output_label = ttk.Label(
    output_frame,
    text='Output', 
    font=(None, 20)
)
output_combo = ttk.Combobox(
    output_frame, 
    values=values,
    font=(None, 15)
)
output_combo.set('en')

output_label.grid(row=0, column=0, padx=10, pady=10)
output_combo.grid(row=0, column=1, padx=10, pady=10)
output_frame.pack()

output_text = Text(
    global_frame,
    height=10, 
    width=50, 
    font=(None, 15),
    state='disabled'
)
output_text.pack(padx=10,pady=10, fill='both', expand='yes')


style = ttk.Style()
style.configure('TButton', font=('Arial', 15))

button = ttk.Button(
    global_frame, 
    text='Translate', 
    command=translate_to
)
button.pack(fill='both', padx=10, pady=10)

window.bind('<Return>', translate_to)
global_frame.pack()

window.mainloop()