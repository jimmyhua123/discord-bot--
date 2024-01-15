import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_links = ['https://discord.com/api/webhooks/1182667255704727613/u88eF8S1ihBHOg4XJ7YUexHpIXws_waiCFubAQt9CQkZCt3YyJjBHivM5xRhIA6dkeji']

def send_discord_message():
    role_id = '593854125356220417'  # 請將這裡替換為您想要標記的身份組ID
    image_url = 'https://i.imgur.com/GDpLBJQ.jpeg'  # 直接圖片URL
    description = f'這裡是消息的描述。 <@&{role_id}>'  # 消息描述，包含標記身份組

    embed = DiscordEmbed()
    embed.set_image(url=image_url)  # 設置圖片
    embed.description = description
    embed.color = 16077457  # 可以根據需要更改顏色

    for link in webhook_links:
        webhook = DiscordWebhook(url=link, content=f'<@&{role_id}>')  # 在消息內容中添加標記身份組
        webhook.add_embed(embed)
        webhook.execute()
        print("消息已發送。")

if __name__ == '__main__':
    send_discord_message()
