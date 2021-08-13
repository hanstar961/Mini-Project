# import socketio
# import time
# import board
# import platform
# import pygame
#
# if platform.system() == "Linux":
#     import busio
#     import adafruit_mpr121
#
# pygame.mixer.init()
# piano_sounds = list()
# guitar_sounds = list()
#
# mode = 'piano'
#
# piano_sounds.append(pygame.mixer.Sound("sound1.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound2.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound3.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound4.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound5.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound6.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound7.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound8.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound9.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound10.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound11.wav"))
# piano_sounds.append(pygame.mixer.Sound("sound12.wav"))
#
# sioClient = socketio.Client()
# server_url = 'http://127.0.0.1:3000'
#
#
# @sioClient.on('connect')
# def connect():
#     print('connected!')
#     sioClient.emit('client_type', 'pi')
#
#
# @sioClient.event
# def disconnect():
#     print('disconnected from server!')
#
#
# @sioClient.on('piano')
# def change_mode_piano(data):
#     global mode
#     mode = "piano"
#     print('Piano mode on!')
#     change_mode(piano_sounds, guitar_sounds)
#
#
# @sioClient.on('guitar')
# def change_mode_guitar(data):
#     global mode
#     mode = "guitar"
#     print('Guitar mode on!')
#     change_mode(piano_sounds, guitar_sounds)
#
#
# def change_mode(piano_sounds, guitar_sounds):
#     i2c = busio.I2C(board.SCL, board.SDA)
#     mpr121 = adafruit_mpr121.MPR121(i2c)
#     while True:
#         for i in range(12):
#             if mpr121[i].value:
#                 print('Input {} touched!'.format(i))
#                 global_mode = globals()['mode']
#                 if global_mode == "piano":
#                     sound = piano_sounds[i]
#                 elif global_mode == "guitar":
#                     sound = guitar_sounds[i]
#                 else:
#                     sound = piano_sounds[i]
#                 sound.play()
#         time.sleep(0.1)
#
#
# sioClient.connect(server_url)
# sioClient.wait()
