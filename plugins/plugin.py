from slackbot.bot import respond_to


@respond_to('進捗は？')
def mention_func(message):
    message.reply('悪し．．．')
    message.react('sunglasses')
