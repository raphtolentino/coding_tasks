# libraries used for this project
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# chat variables
my_bot = ChatBot(
    name="PyBot", # bot name
    read_only=True,
    logic_adapters =["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
    ) # bot ability to learn

small_talk = [
    'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m pybot. ask me a math question, please.'
]

math_talk_1 = [
    'pythagorean theorem'
    'a squared plus b squared equals c squared.'
]

math_talk_2 = [
    'law of cos'
    'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)'
]

list_trainer = ListTrainer(my_bot)

for item in(small_talk,math_talk_1,math_talk_2):
    list_trainer(item)
    
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("hi"))
print(my_bot.response("I feel amazing"))
print(my_bot.response("What is your name"))
print(my_bot.response("What is the pathagoras theory"))
print(my_bot.response("What is the law of cos"))