from tkinter import *
from tkinter import ttk as ttk

root = Tk()
root.title("Chord Transposer")

# 코드북
book1 = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
book2 = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

chord_boxes = []

chord_row = 0
n = 1

def cnumber_size(event):
    pass

def sharpflat(event):
    pass

def font_size(event):
    pass

def add_chord_box():
    pass
    
def del_chord_box():
    pass
    
def transposeup():
    pass

def transposedown():
    pass

# 명령 프레임 (코드 입력칸 추가/제거)
command_frame = Frame(root)
command_frame.pack(fill='x', padx=5, pady=5) # padx, pady = 프레임간 간격 띄우기

btn_add_file = Button(command_frame, padx=5, pady=5, width=15, text='코드 입력칸 추가', command=add_chord_box)
btn_add_file.pack(side = 'left')

btn_del_file = Button(command_frame, padx=5, pady=5, width=15, text='코드 입력칸 제거', command=del_chord_box)
btn_del_file.pack(side = 'right')

# 옵션 프레임
option_frame = LabelFrame(root, text='표시 옵션')
option_frame.pack(fill='both', padx=5, pady=5, ipady=5)

# 1. 한 줄 당 코드 수 옵션
# 한 줄 당 코드 수 레이블
lbl_cnumber = Label(option_frame, text='한 줄 당 코드 수', width=14)
lbl_cnumber.pack(side='left', fill='none', expand=True, pady=5)

# 한 줄 당 코드 수 콤보
opt_cnumber = ['4', '8']
cmb_cnumber = ttk.Combobox(option_frame, state='readonly', values=opt_cnumber, width=3, justify='center')
cmb_cnumber.current(0)
cmb_cnumber.pack(side='left', fill='none', expand=True, padx=5, pady=5)
cmb_cnumber.bind("<<ComboboxSelected>>", cnumber_size)

# 2. b / # 옵션
# b / # 옵션 레이블
lbl_sharpflat = Label(option_frame, text='♭ / # 변환', width=8)
lbl_sharpflat.pack(side='left', fill='none', expand=True, padx=5, pady=5)

# # / b 옵션 콤보
opt_sharpflat = ['♭', '#']
cmb_sharpflat = ttk.Combobox(option_frame, state='readonly', values=opt_sharpflat, width=3, justify='center')
cmb_sharpflat.current(0)
cmb_sharpflat.pack(side='left', fill='none', expand=True, padx=5, pady=5)
cmb_sharpflat.bind("<<ComboboxSelected>>", sharpflat)

# 3. 글자 크기 옵션
# 글자 크기 옵션 레이블
lbl_font = Label(option_frame, text='글자 크기', width=8)
lbl_font.pack(side='left', fill='none', expand=True, padx=5, pady=5)

# 글자 크기 옵션 콤보
opt_font = ['작게', '보통', '크게']
cmb_font = ttk.Combobox(option_frame, state='readonly', values=opt_font, width=5, justify='center')
cmb_font.current(1)
cmb_font.pack(side='left', fill='none', expand=True, padx=5, pady=5)
cmb_font.bind("<<ComboboxSelected>>", font_size)

# 코드 프레임
chord_frame = LabelFrame(root, text='코드 입력칸')
chord_frame.pack(fill='both', expand=True, padx=5, pady=5)

# 코드 프레임 초기 그리드 세팅
for i in range(4):
    chord_frame.grid_columnconfigure(i, weight=1)

# 전조 프레임
transpose_frame = LabelFrame(root, text='Transpose')
transpose_frame.pack(fill='x', padx=5, pady=5, ipady=5)

btn_transpose_up = Button(transpose_frame, padx=5, pady=5, text='UP ↑', width=15, command=transposeup)
btn_transpose_up.pack(side='left', fill='x', padx=5, pady=5)

btn_transpose_down = Button(transpose_frame, padx=5, pady=5, text='DOWN ↓', width=15, command=transposedown)
btn_transpose_down.pack(side='right', fill='x', padx=5, pady=5)

root.mainloop()