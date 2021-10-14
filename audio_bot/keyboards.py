from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
import vk_api
from vk_api.audio import VkAudio
import os

def two_factor():
    code = input("Code? ")
    remember_device = True
    return code, remember_device

vk_loginn = os.getenv("vk_login")
vk_password = os.getenv("vk_pass")
vk_session = vk_api.VkApi(vk_loginn, vk_password, auth_handler=two_factor)
vk_session.auth()
vkaudio = VkAudio(vk_session)

####
button_boom = KeyboardButton('BOOM', callback_data="from_boom")
button_yamusic = KeyboardButton("Яндекс.Музыка", callback_data="from_yamusic")
first_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(button_boom, button_yamusic)
####

####
button_all_songs = KeyboardButton("Общая музыка - 0", callback_data="album_0")
album_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(button_all_songs)
for album in vkaudio.get_albums():
    button_album = KeyboardButton(album.get("title")+" - "+str(album.get("id")), callback_data="album_"+str(album.get("id")))
    albums_keyboard = album_keyboard.add(button_album)
####


class DataInput(StatesGroup):
    vk_link = State()