import create_bot
import asyncio
from handlers import inline,commands
import logging


async def main():
    bot = create_bot.bot
    dp = create_bot.dp
 
    print('Bot online')
    
    dp.include_router(commands.router)
    dp.include_router(inline.router)
    #await bot.delete_webhook()
    await dp.start_polling(bot)
   
if __name__ == "__main__":
    logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('main')
    asyncio.run(main())