from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboa.prof_keyboards import make_row_keyboard

avalabel_firm_names = ['Mitsubishi', 'Otis', 'МЭЛ']
avalabel_mitsu_model = ['Elenesa3', 'Elenesa 2', 'Lehy', 'Hope']

router=Router()
class ChoiseFirmName(StatesGroup):
    choise_firm_name = State()
    choise_mitsu_model_name = State()

# Хэндлер на команду /lifts
@router.message(Command('lifts'))
async def cmd_lifts(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}, выбери производителя', reply_markup=make_row_keyboard(avalabel_firm_names))
    await state.set_state(ChoiseFirmName.choise_firm_name)

# Хэндлер на выбор Фирмы лифта
@router.message(ChoiseFirmName.choise_firm_name, F.text.in_(avalabel_firm_names) )
async def firm_choise(message: types.Message, state: FSMContext):
    await state.update_data(firm_choise=message.text.lower())
    await message.answer(f'Спасибо за выбор, выбери модель ,', reply_markup=make_row_keyboard(avalabel_mitsu_model))
    await state.set_state(ChoiseFirmName.choise_mitsu_model_name)

# Хэндлер на выбор профессии repeed
@router.message(ChoiseFirmName.choise_firm_name)
async def firm_choise_incorect(message: types.Message):

    await message.answer(f'Я не знаю такой фирмы', reply_markup=make_row_keyboard(avalabel_firm_names))

# Хэндлер на выбор уровня
@router.message(ChoiseFirmName.choise_mitsu_model_name, F.text.in_(avalabel_mitsu_model) )
async def mitsu_model_choise(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Производитель: {user_data.get("firm_choise")}. Вы выбрали модель {message.text.lower()}.  ',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

# Хэндлер на выбор профессии repeed
@router.message(ChoiseFirmName.choise_mitsu_model_name )
async def grade_choise_incorect(message: types.Message):

    await message.answer(f'Я не знаю такой модели', reply_markup=make_row_keyboard(avalabel_mitsu_model))



# Хэндлер на инфо
#@router.message(F.text.lower() == 'инфо')
#async def cmd_info(message: types.Message):
 #   name = message.chat.first_name
  #  await message.answer(f'Инфо', reply_markup=kb1)

# Хэндлер на команду /stop
#@router.message(Command('stop'))
#async def cmd_stop(message: types.Message):
  #  name = message.chat.first_name
   # await message.answer(f'Пока, {name}')