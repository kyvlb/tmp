from environs import Env


# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMIN_ID")  # Тут у нас будет список из админов
URL_RED = env.str("URL_RED")
URL_BLUE= env.str("URL_BLUE")

