from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from tkinter import*
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
import Twitter as tweet

chatbot = bot = ChatBot('GOD')
bot.set_trainer(ListTrainer)
for files in os.listdir('chatterbot-corpus/chatterbot_corpus/data/english/'):
    data = open('chatterbot-corpus/chatterbot_corpus/data/english/' + files , 'r').readlines()
    bot.train(data)


class TkinterGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("the I-DO")
        self.user_name = ""
        self.configure(background="#B55C6C")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = tk.Button(self, state = 'normal', text='Get Response', foreground = '#FAB25F',command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = tk.Entry(self, state='normal', bg = '#FAB25F',foreground = 'white')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
        
        self.conversation_lbl = tk.Label(self, anchor=tk.E, text='Conversation:', background = '#FAB25F',foreground = 'white')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='normal', bg = '#212121', fg = 'white')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)


        self.conversation['state'] = 'normal'
        self.conversation.insert(tk.END, "Commands:" + "\n" + "     'tweet [input tweet]'" + "\n" + "     'play song'" + "\n" + "     'play game'" + "\n" + 
                                        "       game controls:" + "\n" + "           WASD to move" + "\n" + "           Arrow Keys to aim" + 
                                        "\n" + "           SPACE to shoot" + "\n")
        self.conversation.insert(tk.END, "\n" + "Enter your name:" + "\n")
        self.conversation['state'] = 'disabled'

    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        if self.user_name == "":
            self.user_name = user_input
            if self.user_name == "":
                self.conversation['state'] = 'normal'
                self.conversation.insert(tk.END, "Enter your name:"+ "\n")
                self.conversation['state'] = 'disabled'
            else:
                response = chatbot.get_response("Hello")

                self.conversation['state'] = 'normal'
                self.conversation.insert(
                tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
            )
                self.conversation['state'] = 'disabled'
        else:
            command = 'null'

            if user_input[0:4] == 'play':
                command = 'play'
            if user_input[0:5] == 'tweet':
                command = 'tweet'
            
            if command == 'play':
                if user_input == 'play song':
                    exec(open('rand_beat.py').read())
                elif user_input == 'play game':
                    exec(open('game_run.py').read())
            elif command == 'tweet':
                status = "From " + self.user_name + ": " + user_input[6:]
                new_tweet = tweet.Tweet(status = status)
                self.conversation['state'] = 'normal'
                self.conversation.insert(tk.END, "\n" + self.user_name + " just tweeted: " + user_input[6:] + "\n" + "Check out your tweet at: https://twitter.com/project_i_do" + "\n" + "\n")
                self.conversation['state'] = 'disabled'

            else:
                response = chatbot.get_response(user_input)

                self.conversation['state'] = 'normal'
                self.conversation.insert(
                    tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
                )
                self.conversation['state'] = 'disabled'


gui = TkinterGUI()
gui.mainloop()
