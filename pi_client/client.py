import socketio
import time
import board
import platform
import pygame

if platform.system() == "Linux":
    import busio
    import adafruit_mpr121

pygame.mixer.init()
sioClient = socketio.Client()
SERVER_URL = ''
mode = 'piano'


def play_sound(piano_sounds, drum_sounds):
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
    while True:
        for i in range(12):
            if mpr121[i].value:
                print('Input {} touched!'.format(i))
                global_mode = globals()['mode']
                if global_mode == "piano":
                    sound = piano_sounds[i]
                elif global_mode == "drum":
                    sound = drum_sounds[i]
                else:
                    sound = piano_sounds[i]
                sound.play()
        time.sleep(0.1)


class SoundPlayer():
    piano_sounds = []
    drum_sounds = []

    def __init__(self):
        self.piano_sounds.append(pygame.mixer.Sound("p_sound1.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound2.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound6.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound7.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound8.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound9.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound10.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound4.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound5.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound6.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("p_sound12.wav"))

        self.drum_sounds.append(pygame.mixer.Sound("g_sound1.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound2.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound3.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound4.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound5.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound6.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound7.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound8.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound9.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound10.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound11.wav"))
        self.drum_sounds.append(pygame.mixer.Sound("g_sound12.wav"))

    def start(self):
        global mode
        print(mode + ' mode is on at start!')
        play_sound(self.piano_sounds, self.drum_sounds)


# When connected to the server
@sioClient.on('connect')
def connect():
    print('connected!')
    sioClient.emit('client_type', 'pi')


# When disconnected to the server
@sioClient.event
def disconnect():
    print('disconnected from server!')


# When 'piano' message is received, play piano
@sioClient.on('piano')
def play_piano():
    print('piano mode requested!')
    global mode
    mode = 'piano'


# When 'drum' message is received, play drum
@sioClient.on('drum')
def play_drum():
    print('drum mode requested!')
    global mode
    mode = 'drum'


# Special disconnect handle automatically run when socket is disconnected
@sioClient.event()
def disconnect():
    print('Disconnected from server! Retrying connection in 2 seconds...')
    time.sleep(2)
    sioClient.connect(SERVER_URL)


# Special error handler automatically run when there is a connection error
@sioClient.event
def connect_error():
    print('Connection failed! Retrying in 2 seconds...')
    time.sleep(2)
    sioClient.connect(SERVER_URL)


soundPlayer = SoundPlayer()

sioClient.connect(SERVER_URL)

# The never-ending loop starts
soundPlayer.start()
