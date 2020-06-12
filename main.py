# discord-auto-translate by JoshSCF (joshl.io)

import config, discord, re
from modules import yandex
from discord import Webhook, RequestsWebhookAdapter

client = discord.Client()

apis = {
    "yandex": yandex
}

async def get_webhook(bot, channel, webhook_list):
    # if webhook exists, return
    for webhook in webhook_list:
        if webhook.user == bot and webhook.channel_id == channel.id:
            return webhook
    
    # otherwise, create new webhook and return
    new_webhook = await channel.create_webhook(
        name = "discord-auto-translate",
        reason = "This webhook is used to post translations on behalf of a user."
    )
    return new_webhook


async def replace_message(message, translation):
    user = message.author

    # prepare webhook, delete message and send message with the same name & pic as user
    webhook_info = await get_webhook(client.user, message.channel, await message.guild.webhooks())
    webhook = Webhook.partial(webhook_info.id, webhook_info.token, adapter=RequestsWebhookAdapter())
    await message.delete()
    webhook.send(translation, username = user.nick or user.name, avatar_url = user.avatar_url)


@client.event
async def on_message(message):
    channel_id = message.channel.id
    
    # ignore message if channel blacklisted or not whitelisted
    if config.channel_whitelisting_enabled:
        if channel_id not in config.whitelisted_channels:
            return
    else:
        if channel_id in config.blacklisted_channels:
            return

    # translate message via relevant translation module
    api_service = apis[config.translation_service]
    translation = api_service.translate(message.content, config.api_key)

    # compare translation with original, replace if different
    alnum_translation = re.sub(r"\W+", "", translation)
    alnum_message = re.sub(r"\W+", "", message.content)

    if alnum_translation != alnum_message:
        await replace_message(message, translation)


if not config.i_have_read_config:
    # user has not read config file, don't start code
    print("You must modify config.py before running!")
    input("Press enter to continue...")
    exit()

client.run(config.bot_token)