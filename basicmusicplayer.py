import os
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
# Music Application Title 
root.title('Python Music Player w/ Tkinter by R. John Dunn')
root.geometry("500x300")

pygame.mixer.init()

# Function to add songs to the playlist
def add_songs():
    files = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3;*.wav")])
    for file in files:
        song_name = os.path.basename(file)  # Extract the filename from the path
        songlist.insert(END, song_name)  # Insert only the filename into the playlist

# Function to play selected song
def play_song():
    song = songlist.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Function to pause the currently playing song
def pause_song():
    pygame.mixer.music.pause()

# Function to resume the paused song
def resume_song():
    pygame.mixer.music.unpause()

# Function to play the next song in the playlist
def next_song():
    next_song_index = (songlist.curselection()[0] + 1) % songlist.size()
    song = songlist.get(next_song_index)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songlist.selection_clear(0, END)
    songlist.activate(next_song_index)
    songlist.selection_set(next_song_index)

# Function to play the previous song in the playlist
def previous_song():
    previous_song_index = (songlist.curselection()[0] - 1) % songlist.size()
    song = songlist.get(previous_song_index)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songlist.selection_clear(0, END)
    songlist.activate(previous_song_index)
    songlist.selection_set(previous_song_index)

# GUI Components
songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()

play_button = Button(control_frame, text="Play", command=play_song)
pause_button = Button(control_frame, text="Pause", command=pause_song)
next_button = Button(control_frame, text="Next", command=next_song)
previous_button = Button(control_frame, text="Previous", command=previous_song)

play_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
next_button.grid(row=0, column=3, padx=10)
previous_button.grid(row=0, column=4, padx=10)

add_songs_button = Button(root, text="Add Songs", command=add_songs)
add_songs_button.pack()

root.mainloop()
