from aiogram.fsm.state import State, StatesGroup


class OrderStates(StatesGroup):
    select_services = State()
    enter_address = State()
    enter_contact = State()

class MainMenuStates(StatesGroup):
    main_menu = State()
    about = State()
    contacts = State()