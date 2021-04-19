from environs import Env


# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMIN_ID")  # Тут у нас будет список из админов
URL_menu = env.str("URL_menu")
PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")


