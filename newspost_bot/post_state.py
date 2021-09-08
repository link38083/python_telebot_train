from aiogram.dispatcher.filters.state import StatesGroup, State

class Post(StatesGroup):
    title = State()
    text = State()
    pic = State()
    time = State()
