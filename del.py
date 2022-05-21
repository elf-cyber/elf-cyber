from telethon import TelegramClient
from colorama import init,Fore
init()

api_id,api_hash = 16676203,'41c37be4581fe2b679ab7d9df0c79e7f'
Tar = '@SignalCryptoCurrency_ir'
Token = '1404309723:AAG3qa8j69BcjDrgkNDvJvxSmsSMLGxamRU'
unknown = TelegramClient('dell',api_id,api_hash).start(bot_token=Token)

async def main():
    users = list()
    me = await unknown.get_me()
    async for x in unknown.iter_participants(entity=Tar):
        users.append(x.id)
    users.remove(int(me.id))
    for x in users:
        try:
            await unknown.kick_participant(Tar, int(x))
            print(Fore.LIGHTMAGENTA_EX+'[+]',Fore.LIGHTYELLOW_EX+str(x),Fore.LIGHTCYAN_EX+'Banned')
        except:
            continue
with unknown:
    unknown.loop.run_until_complete(main())
