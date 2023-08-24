
invites_before = {}
invites_after = {}

@bot.event
async def on_ready():


    target_guild_id = 0 # Айди сервера, где нужно брать все приглашения

    for guild in bot.guilds:
        if guild.id == target_guild_id:
            invites = await guild.invites()
            #заполняем наш словарь нашими приглашениями ДО того как на сервер зашел пользователь
            for invite in invites:
                invites_before[invite.code] = {}
                invites_before[invite.code]['uses'] = invite.uses
@bot.event
async def on_invite_create(invite):
    guild_id = 0 #айди сервера, тот же, который и в on_ready()
    if invite.guild.id == guild_id:
        #добавляем созданное приглшаение в словарь
        invites_before[invite.code] = {}
        invites_before[invite.code]['uses'] = invite.uses
        print(invite.code)
        print(invites_before)
@bot.event
async def on_member_join(member):
    guild_id = 0
    #проверка что событие происходит на нашем сервере
    if member.guild.id == guild_id: #айди сервера, тот же, который и в on_ready()
        print(Fore.BLUE + 'Новый пользователь в дискорд сервере', member.id)
        invites = await member.guild.invites() # берем все действительные приглашения и записываем их в invites_after
        for invite in invites: #перебираем
            #создаем для каждого кода свой словарь
            invites_after[invite.code] = {}
            invites_after[invite.code]['uses'] = invite.uses
        #перебор всех кодов из invites_after
        for invite_code in invites_after:
            data_invites_before = invites_before.get(invite_code)
            data_invites_after = invites_after.get(invite_code)
            #получаем дату и использования
            uses_before = data_invites_before['uses']
            uses_after = data_invites_after['uses']

            #сравниваем
            if uses_after > uses_before:
                invites_before[invite_code]['uses'] = uses_after
                print(Fore.CYAN + f'Пользователь присоединился по коду {invite_code}')

                #далее ваш код чтобы обработать событие
                #Текущий инвайт код в цикле invite_code / текущее кол-во использований uses_after, uses_before, invites_before[invite_code]['uses']
                # |
                # |
                # |
                # ↓
