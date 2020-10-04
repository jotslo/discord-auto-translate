# set the following variable to True to declare that you have modified the config
i_have_read_config = False

# replace with the private token of your bot, do not share this with anyone
bot_token = "###########################################################"

# choose the translation service that translations will be fetched from
# supported services: "google", "yandex", "microsoft"
translation_service = "yandex"

# enter the api key associated with your chosen translation service
api_key = "######################################################"

# choose whether channels must be whitelisted for auto-translate to run there
channel_whitelisting_enabled = True

# ids of channels that auto translate will run in
# ignored if channel whitelisting is disabled
whitelisted_channels = [
    00000000000000000,
    00000000000000000
]

# blacklisted channels ids
# if whitelisting is disabled, the bot will ignore channels with these ids
blacklisted_channels = [
    00000000000000000,
    00000000000000000
]
