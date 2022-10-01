from BotAmino import BotAmino, Parameters




print("wait...")
client = BotAmino("raaavisharma1925@gmail.com", "ravi2603")
client.prefix = "/"  # set the prefix to /
client.wait = 10  # wait 10 sec before doing a new command


def test(data: Parameters):
    return data.authorId in ["f8f2f421-59c7-4933-9cd8-0cf954f06f93","ab15c9f0-37fb-44b5-842b-bb70245c5dc8","e7a9b567-32d0-4551-8a71-96d0eb27168c","b0dbbf5a-4370-4e82-80f3-1b670cad0ac7","df4335ba-5eb3-445c-86e0-edf7dcc927f6","42305a05-67c9-4ea3-9b57-f01e5f26cd01", "c6cc9187-e796-4ff9-8376-18c0663aa079"]


@client.command("ping", test) # "ping" the command and test the function, if test is True the command will be executed, else it will not
def ping(data: Parameters):
    data.subClient.send_message(data.chatId, message="pong!")


@client.command("pong") # "pong" the command, the test function is not necessary
def pong(data: Parameters):
    if data.subClient.is_in_staff(data.authorId): # will execute the command if the user is in the amino's staff (learder/curator)
        data.subClient.send_message(data.chatId, message="ping!")


@client.answer("hey")
def hello(data: Parameters):
    data.subClient.send_message(data.chatId, message="Hey! Hey!")


@client.on_member_join_chat()
def say_hello(data: Parameters):
    data.subClient.send_message(data.chatId, f"welcome here {data.author}!")


@client.on_member_leave_chat(["chatId"]) # the chatId is not necessary, put one if you want a specified chat only
def say_goodbye(data: Parameters):
    data.subClient.send_message(data.chatId, f"See you soon {data.author}!")


client.launch()
print("ready")