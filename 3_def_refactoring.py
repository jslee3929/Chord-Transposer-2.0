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
    # 줄 별 그리드 세팅
    global cns
    cns = event.widget.get()
    for i in range(int(cns)):
        chord_frame.grid_columnconfigure(i, weight=1)
        chord_frame.grid_columnconfigure(i+int(cns), weight=0)

def sharpflat(event):
    sf = event.widget.get()
    for chord in chord_boxes:    
        o_chord = globals()['{}'.format(chord)].get()
        
        # No Chord
        if not o_chord:
            continue

        # Slash Index
        if o_chord.find('/') == -1:
            slash_index = None
        else:
            slash_index = o_chord.find('/')

        # Slash Chord
        if slash_index != None:
            slash_chord = o_chord[slash_index+1:]
        
        # Chord Root
        if len(o_chord) == 1:
            chord_root = o_chord
        elif o_chord[1] == '#' or o_chord[1] == 'b':
            chord_root = o_chord[:2]
        else:
            chord_root = o_chord[0]

        # Tension
        if slash_index is None:
            tension = o_chord[o_chord.index(chord_root[-1])+1:]
        else:
            tension = o_chord[o_chord.index(chord_root[-1])+1:slash_index]
        
        # Check #/b
        if sf == opt_sharpflat[0]: # b
            if len(chord_root) == 1:
                pass
            elif chord_root[1] == '#':
                chord_root = book2[book1.index(chord_root)]
            elif chord_root[1] == 'b':
                pass

            if slash_chord is None:
                pass
            if len(slash_chord) == 1:
                pass
            elif slash_chord[1] == '#':
                slash_chord = book2[book1.index(slash_chord)]
            elif slash_chord[1] == 'b':
                pass
        
        elif sf == opt_sharpflat[1]:
            if len(chord_root) == 1:
                pass
            elif chord_root[1] == 'b':
                chord_root = book1[book2.index(chord_root)]
            elif chord_root[1] == '#':
                pass

            if slash_chord is None:
                pass
            elif len(slash_chord) == 1:
                pass
            elif slash_chord[1] == 'b':
                slash_chord = book1[book2.index(slash_chord)]
            elif slash_chord[1] == '#':
                pass

        # Convert Chord #/b
        if len(tension) == 0:
            convert_chord = chord_root
        else:
            convert_chord = '{0}{1}'.format(chord_root, tension)
        
        if slash_index == None:
            convert_chord = convert_chord
        else:
            convert_chord = '{0}{1}/{2}'.format(chord_root, tension, slash_chord)
        
        globals()['{}'.format(chord)].delete(0, END)
        globals()['{}'.format(chord)].insert(0, (convert_chord))

def font_size(event):
    fs = event.widget.get()
    if fs == '작게':
        for chord in chord_boxes:
            globals()['{}'.format(chord)].configure(font='TkDefaultFont 9 bold')
    elif fs == '보통':
        for chord in chord_boxes:
            globals()['{}'.format(chord)].configure(font='TkDefaultFont 12 bold')
    elif fs == '크게':
        for chord in chord_boxes:
            globals()['{}'.format(chord)].configure(font='TkDefaultFont 14 bold')

def add_chord_box():
    global chord_row, n
    
    # Add Chord Box
    for x in range(int(cmb_cnumber.get())):
        
        # Font Size Setting
        fs = cmb_font.get()
        if fs == '작게':
            fs = 9
        elif fs == '보통':
            fs = 12
        elif fs == '크게':
            fs = 14
        
        globals()['chord{}'.format(n)] = Entry(chord_frame, width=10, justify='center')
        globals()['chord{}'.format(n)].grid(row=chord_row, column=x, sticky=W+E, padx=(2, 2), pady=(2, 2))
        globals()['chord{}'.format(n)].configure(font='TkDefaultFont {} bold'.format(fs))
        chord_boxes.append('chord{}'.format(n))
        n += 1
    chord_row += 1

def del_chord_box():
    global n
    for i in range(int(cmb_cnumber.get())):
        if n <= 1:
            break
        n -= 1
        globals()['chord{}'.format(n)].destroy()
        chord_boxes.pop()
    
def transposeup():
    for chord in chord_boxes:
        o_chord = globals()['{}'.format(chord)].get()

        # No Chord
        if not o_chord:
            continue

        # Slash Index
        if o_chord.find('/') == -1:
            slash_index = None
        else:
            slash_index = o_chord.find('/')

        # Slash Chord
        if slash_index != None:
            slash_chord = o_chord[slash_index+1:]
        
        # Chord Root
        if len(o_chord) == 1:
            chord_root = o_chord
        elif o_chord[1] == '#' or o_chord[1] == 'b':
            chord_root = o_chord[:2]
        else:
            chord_root = o_chord[0]

        # Tension
        if slash_index is None:
            tension = o_chord[o_chord.index(chord_root[-1])+1:]
        else:
            tension = o_chord[o_chord.index(chord_root[-1])+1:slash_index]
        
        # Transpose Chord Root
        if len(chord_root) == 1:
            tp_up_root = book2[book2.index(chord_root) + 1]
        elif chord_root[1] == '#':
            tp_up_root = book1[book1.index(chord_root) + 1]
        elif chord_root[1] == 'b':
            tp_up_root = book2[book2.index(chord_root) + 1]
        else:
            tp_up_root = book2[book2.index(chord_root) + 1]

        # Transpose Slash Chord
        if slash_index == None:
            tp_up_slash = None
        elif len(slash_chord) == 1:
            tp_up_slash = book2[book2.index(slash_chord) + 1]
        elif slash_chord[1] == '#':
            tp_up_slash = book1[book1.index(slash_chord) + 1]
        elif slash_chord[1] == 'b':
            tp_up_slash = book2[book2.index(slash_chord) + 1]
        else:
            tp_up_slash = book2[book2.index(slash_chord) + 1]

        # Convert Chord #/♭
        if cmb_sharpflat.get() == opt_sharpflat[0]: # b
            if len(tp_up_root) == 1:
                pass
            elif tp_up_root[1] == '#':
                tp_up_root = book2[book1.index(tp_up_root)]
            elif tp_up_root[1] == 'b':
                pass

            if tp_up_slash is None:
                pass
            elif len(tp_up_slash) == 1:
                pass
            elif tp_up_slash[1] == '#':
                tp_up_slash = book2[book1.index(tp_up_slash)]
            elif tp_up_slash[1] == 'b':
                pass
        
        elif cmb_sharpflat.get() == opt_sharpflat[1]:
            if len(tp_up_root) == 1:
                pass
            elif tp_up_root[1] == 'b':
                tp_up_root = book1[book2.index(tp_up_root)]
            elif tp_up_root[1] == '#':
                pass

            if tp_up_slash is None:
                pass
            elif len(tp_up_slash) == 1:
                pass
            elif tp_up_slash[1] == 'b':
                tp_up_slash = book1[book2.index(tp_up_slash)]
            elif tp_up_slash[1] == '#':
                pass

        # Transpose Chord
        if len(tension) == 0:
            tp_up_chord = tp_up_root
        else:
            tp_up_chord = '{0}{1}'.format(tp_up_root, tension)
        
        if slash_index == None:
            tp_up_chord = tp_up_chord
        else:
            tp_up_chord = '{0}{1}/{2}'.format(tp_up_root, tension, tp_up_slash)
        
        globals()['{}'.format(chord)].delete(0, END)
        globals()['{}'.format(chord)].insert(0, (tp_up_chord))

def transposedown():
    for chord in chord_boxes:
        o_chord = globals()['{}'.format(chord)].get()

        # No Chord
        if not o_chord:
            continue

        # Slash Index
        if o_chord.find('/') == -1:
            slash_index = None
        else:
            slash_index = o_chord.find('/')

        # Slash Chord
        if slash_index != None:
            slash_chord = o_chord[slash_index+1:]
        
        # Chord Root
        if len(o_chord) == 1:
            chord_root = o_chord
        elif o_chord[1] == '#' or o_chord[1] == 'b':
            chord_root = o_chord[:2]
        else:
            chord_root = o_chord[0]

        # Tension
        if slash_index is None:
            tension = o_chord[o_chord.index(chord_root[-1])+1:]
        else:
            tension = o_chord[o_chord.index(chord_root[-1])+1:slash_index]
        
        # Transpose Chord Root
        if len(chord_root) == 1:
            tp_down_root = book2[book2.index(chord_root) - 1]
        elif chord_root[1] == '#':
            tp_down_root = book1[book1.index(chord_root) - 1]
        elif chord_root[1] == 'b':
            tp_down_root = book2[book2.index(chord_root) - 1]
        else:
            tp_down_root = book2[book2.index(chord_root) - 1]

        # Transpose Slash Chord
        if slash_index == None:
            tp_down_slash = None
        elif len(slash_chord) == 1:
            tp_down_slash = book2[book2.index(slash_chord) - 1]
        elif slash_chord[1] == '#':
            tp_down_slash = book1[book1.index(slash_chord) - 1]
        elif slash_chord[1] == 'b':
            tp_down_slash = book2[book2.index(slash_chord) - 1]
        else:
            tp_down_slash = book2[book2.index(slash_chord) - 1]

        # Convert Chord #/♭
        if cmb_sharpflat.get() == opt_sharpflat[0]: # b
            if len(tp_down_root) == 1:
                pass
            elif tp_down_root[1] == '#':
                tp_down_root = book2[book1.index(tp_down_root)]
            elif tp_down_root[1] == 'b':
                pass

            if tp_down_slash is None:
                pass
            if len(tp_down_slash) == 1:
                pass
            elif tp_down_slash[1] == '#':
                tp_down_slash = book2[book1.index(tp_down_slash)]
            elif tp_down_slash[1] == 'b':
                pass
        
        elif cmb_sharpflat.get() == opt_sharpflat[1]:
            if len(tp_down_root) == 1:
                pass
            elif tp_down_root[1] == 'b':
                tp_down_root = book1[book2.index(tp_down_root)]
            elif tp_down_root[1] == '#':
                pass

            if tp_down_slash is None:
                pass
            elif len(tp_down_slash) == 1:
                pass
            elif tp_down_slash[1] == 'b':
                tp_down_slash = book1[book2.index(tp_down_slash)]
            elif tp_down_slash[1] == '#':
                pass

        # Transpose Chord
        if len(tension) == 0:
            tp_down_chord = tp_down_root
        else:
            tp_down_chord = '{0}{1}'.format(tp_down_root, tension)
        
        if slash_index == None:
            tp_down_chord = tp_down_chord
        else:
            tp_down_chord = '{0}{1}/{2}'.format(tp_down_root, tension, tp_down_slash)

        globals()['{}'.format(chord)].delete(0, END)
        globals()['{}'.format(chord)].insert(0, (tp_down_chord))

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