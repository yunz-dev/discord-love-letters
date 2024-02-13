from dotenv import load_dotenv
import requests
import os


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    data = {
  "content": "Hey, welcome to <:discohook:736648398081622016> **Discohook**! The easiest way to personalise your Discord server.\n\nThere's more info below, but you don't have to read it. If you're ready press **Clear All** in the top of the editor to get started.\n\nDiscohook has a [support server](https://discohook.app/discord), if you need help feel free to join in and ask questions, suggest features, or just chat with the community.\n\nWe also have [complementary bot](https://discohook.app/bot) that may help out, featuring reaction roles and other utilities.\n_ _",
  "embeds": [
    {
      "title": "What's this about?",
      "description": "Discohook is a free tool that allows you to personalise your server to make your server stand out from the crowd. The main way it does this is using [webhooks](https://support.discord.com/hc/en-us/articles/228383668), which allows services like Discohook to send any messages with embeds to your server.\n\nTo get started with sending messages, you need a webhook URL, you can get one via the \"Integrations\" tab in your server's settings. If you're having issues creating a webhook, [the bot](https://discohook.app/bot) can help you create one for you.\n\nKeep in mind that Discohook can't do automation yet, it only sends messages when you tell it to. If you are looking for an automatic feed or custom commands this isn't the right tool for you.",
      "color": 5814783,
      "fields": [
        {
          "name": "wdsadsa",
          "value": "dsadsadsadsadsa"
        }
      ],
      "author": {
        "name": "yunz"
      },
      "image": {
        "url": "https://cdn.discordapp.com/attachments/286436855296032768/1206916849980411925/4KzczqD.jpg?ex=65ddbfe8&is=65cb4ae8&hm=63786d60ea7ef8d3406562e97555b2698190ef36835fab282cdd4b342c8e2f40&"
      }
    }
  ],
  "attachments": []
} 
    response = requests.post(token, json=data)

    if response.status_code == 204:
        print("yay")
    else:
        print("nay")


if __name__ == "__main__":
    main()
