from telegram.client import Telegram

tg = Telegram(
    api_id=21724,
    api_hash="3e0cb5efcd52300aec5994fdfc5bdc16",
    phone="+6283836372576",  # you can pass 'bot_token' instead
    database_encryption_key=b"f7b0a677e5078fefb10df0d0f6a253aa3e98eb88dc11d5e379ff6c9da84b77ba",
    files_directory="./tdlib2/",
    device_model="Samsung SM-T713",
    application_version="0.25.1.1560",
    system_version="SDK 27",
)
a = tg.login()
print(a.WAIT_TDLIB_PARAMETERS)
# if this is the first run, library needs to preload all chats
# otherwise the message will not be sent
# result = tg.get_chats()
# result.wait()

# chat_id: int
# result = tg.send_message(268916327, Spoiler("Hello world!"))
# `tdlib` is asynchronous, so `python-telegram` always returns you an `AsyncResult` object.
# You can receive a result with the `wait` method of this object.
# result.wait()
# print(result.update)

tg.stop()  # you must call `stop` at the end of the scrit
