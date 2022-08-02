# pip install pygame
from re import L
from smtplib import SMTPNotSupportedError
from tkinter import *
from xml.sax import SAXNotSupportedException
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
root = Tk()
root.title('MP3 PLAYER')
root.geometry("500x450")

# initialize pygame mixer
pygame.mixer.init()

# GRAB SONG TIME INFO


def playtime():
    # CHECK FOR DOUBLE TIME
    if stopped:
        return
    # to get the current time in second
    # grab current song elapse time
    current_time = pygame.mixer.music.get_pos() / 1000
    # THROW UP LABEL TO GET DATA
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song pos:{int(current_time)}')
    converted_current_time = time.strftime(
        '%M:%S', time.gmtime(current_time))

    # GET CURRENTLY PLAYING SONG

    current_song = song_box.curselection()

    # GRAB THE NEXT SONG TITLE
    song = song_box.get(ACTIVE)
    # PLAY THE NEXT SONG
    song = f'C:/Users/KIIT/OneDrive/Desktop/intern/{song}'
    # LOAD SONG  WITH MUTAGEN
    song_mut = MP3(song)
    # GET SONG LENGTH
    global song_length
    song_length = song_mut.info.length
    # CONVERT TO TIME FORMAT
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    # INCREASE CURRENT TIME BY 1
    current_time += 1
    if int(my_slider.get()) == int(song_length):
        status_bar.config(
            text=f"TIME ELAPSED:{converted_song_length}")
    elif paused:
        pass

    elif int(my_slider.get()) == (int(current_time)):
        # UPDATE slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # UPDATE slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        converted_current_time = time.strftime(
            '%M:%S', time.gmtime(int(my_slider.get())))
        # OUTPUT TIME TO STATUS BAR
        status_bar.config(
            text=f"TIME ELAPSED:{converted_current_time} / {converted_song_length}")
        # move this along by one second
        next_time = int(my_slider.get())+1
        my_slider.config(value=next_time)

    # OUTPUT TIME TO STATUS BAR

    #status_bar.config(text=f"TIME ELAPSED:{converted_current_time} / {converted_song_length}")
    # UPDATE SLIDER POSITION VALUE TO CURRENT SONG POSITION
    # my_slider.config(value=int(current_time))

    # update time
    status_bar.after(1000, playtime)


# ADD SONG FUNCTION


def add_song():
    song = filedialog.askopenfilename(
        initialdir='C:/Users/KIIT/OneDrive/Desktop/intern', title="choose a song", filetypes=(("MP3 Files", "*.mp3"),))
    # to remove the file location of the song in the display
    song = song.replace("C:/Users/KIIT/OneDrive/Desktop/intern/", "")
    # to add the song in display
    song_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(
        initialdir='C:/Users/KIIT/OneDrive/Desktop/intern', title="choose a song", filetypes=(("MP3 Files", "*.mp3"),))
    # LOOPING THROUGH SONGS
    for song in songs:
        song = song.replace("C:/Users/KIIT/OneDrive/Desktop/intern/", "")
        song_box.insert(END, song)


def play():

    # SET STOPPED VARIABLE TO FALSE SO THAT THE SONNG CAN PLAY
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/KIIT/OneDrive/Desktop/intern/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # call the play function
    playtime()
    # UPDATE SLIDER TO THE POSITION
    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=0)
    current_volume = pygame.mixer.music.get_volume()
    slider_label.config(text=current_volume*100)


global stopped
stopped = False


def stop():
    # RESET SLIDER AND STATUS BAR
    status_bar.config(text='')
    my_slider.config(value=0)
    # STOP SONG FROM PLAYING
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    status_bar.config(text='')
    # SET STOP VARIABLE TO TRUE
    global stopped
    stopped = True


def next_song():
    # RESET SLIDER AND STATUS BAR
    status_bar.config(text='')
    my_slider.config(value=0)
    # GET THE CURRENT SONG TUPLE NUMBER
    next_one = song_box.curselection()
    # add the next song
    next_one = next_one[0]+1
    # GRAB THE NEXT SONG TITLE
    song = song_box.get(next_one)
    # PLAY THE NEXT SONG
    song = f'C:/Users/KIIT/OneDrive/Desktop/intern/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # TO REMOVE THE ACTIVE BAR
    song_box.selection_clear(0, END)
    # MOVE THE BAR
    song_box.activate(next_one)
    # SET THE BAR
    song_box.selection_set(next_one, last=None)


def prev_song():
    # RESET SLIDER AND STATUS BAR
    status_bar.config(text='')
    my_slider.config(value=0)
    # GET CURRENT SONG TUPLE NUMBER
    next_one = song_box.curselection()
    # add the next song
    next_one = next_one[0]-1
    # GRAB THE NEXT SONG TITLE
    song = song_box.get(next_one)
    # PLAY THE NEXT SONG
    song = f'C:/Users/KIIT/OneDrive/Desktop/intern/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # TO REMOVE THE ACTIVE BAR
    song_box.selection_clear(0, END)
    # MOVE THE BAR
    song_box.activate(next_one)
    # SET THE BAR
    song_box.selection_set(next_one, last=None)


def delete_song():
    stop()
    song_box.delete(ANCHOR)  # HIGHLIGHTED SING IS ANCHOR
    pygame.mixer.music.stop()

# DELETE ALL SONGS


def delete_all_songs():
    stop()

    song_box.delete(0, END)
    pygame.mixer.music.stop()


# CREATE GLOBAL PAUSE VARIABLE
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # TO UNPAUSE
        pygame.mixer.music.unpause()
        paused = False
    else:
        # TO PAUSE
        pygame.mixer.music.pause()
        paused = True
# CREATE SLIDER FUNSTION


def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} / {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'C:/Users/KIIT/OneDrive/Desktop/intern/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

# function for volume


def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    # GER CURRENT VOLUME
    current_volume = pygame.mixer.music.get_volume()
    slider_label.config(text=current_volume * 100)


# CREATE FRAME
#master_frame = Frame(root)
# master_frame.pack()

# To create playlist box
song_box = Listbox(root, bg="black", fg="red", width=500,
                   selectbackground="red", selectforeground="white")
song_box.pack(pady=20)

# DESIGN  CONTOL BUTTONS AND LOCATE THE BUTTONS
forward_button_img = PhotoImage(
    file='C:/Users/KIIT/OneDrive/Pictures/for.png', )

back_button_img = PhotoImage(
    file='C:/Users/KIIT/OneDrive/Pictures/backj.png')
play_button_img = PhotoImage(
    file='C:/Users/KIIT/OneDrive/Pictures/imageplay.png')
pause_button_img = PhotoImage(
    file='C:/Users/KIIT/OneDrive/Pictures/pause1.png')
stop_button_img = PhotoImage(file='C:/Users/KIIT/OneDrive/Pictures/stopj.png')
# CREATE FRAME
controls_frame = Frame(root)
controls_frame.pack()


# CREATE CONTROL BUTTONS
forward_button = Button(
    controls_frame, image=forward_button_img, borderwidth=0, command=next_song)
back_button = Button(controls_frame, image=back_button_img,
                     borderwidth=0, command=prev_song)
play_button = Button(controls_frame, image=play_button_img,
                     borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_button_img,
                      borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_button_img,
                     borderwidth=0, command=stop)

forward_button.grid(row=0, column=0, padx=10)
back_button.grid(row=0, column=1, padx=0)
play_button.grid(row=0, column=2, padx=0)
pause_button.grid(row=0, column=3, padx=0)
stop_button.grid(row=0, column=4, padx=70)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add new songs
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(
    label="ADD ONE SONG TO THE PLAYLIST", command=add_song)
# CREATE PLAYLIST
add_song_menu.add_command(
    label="ADD MANY SONGS TO THE PLAYLIST", command=add_many_songs)

# DELETE SONGS
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="REMOVE SONGS", menu=remove_song_menu)
remove_song_menu.add_command(
    label="DELETE A  SONG FROM THE PLAYLIST", command=delete_song)
remove_song_menu.add_command(
    label="DELETE A  SONG FROM THE PLAYLIST", command=delete_all_songs)
# CREATE STATUS BAR
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# CREATE MUSIC SLIDER
my_slider = ttk.Scale(root, from_=0, to=100,
                      orient=HORIZONTAL, value=0, command=slide, length=1000)

my_slider.pack(pady=0)  # to push it down
# CREATE VOLUME FRAME
volume_frame = LabelFrame(root, text="Volume")
volume_frame.pack(pady=0)
# CREATE VOLUME SLIDER
volume_slider = ttk.Scale(volume_frame, from_=0, to=1,
                          orient=VERTICAL, value=1, command=volume, length=100)

volume_slider.pack(pady=0)
# CREATE TEMPORARY SLIDER LABEL
slider_label = Label(root, text="0")
slider_label.pack(pady=0)


root.mainloop()
