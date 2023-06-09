import logging

from aiogram.utils import executor
from config import dp
from handlers import client, extra, callback, fsmAdminMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm(dp)
# fsm_anketa.register_handlers_fsm(dp)
extra. register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)