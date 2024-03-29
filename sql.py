import asyncio
import asyncpg
import logging


from data.config import PG_USER, PG_PASS

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)

async def create_bd():
    create_bd_command = open("create_bd.sql", "r").read()

    logging.info("Connecting to bd.")
    conn: asyncpg.Connection = await asyncpg.connect(
        user = PG_USER,
        password = PG_PASS,
    )
    await conn.execute(create_bd_command)
    logging.info("Tabled has been created.")
    await conn.close()

async def create_pool():
    return await asyncpg.create_pool(
        user=PG_USER,
        password=PG_PASS,
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_bd())

