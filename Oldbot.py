import time
from keep_alive import keep_alive
import random
import os
import discord
from discord.ext import commands
keep_alive()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
jokes = [@
    "I have an inferiority complex, but it’s not a very good one.",
    "I told my doctor that I broke my arm in two places. He told me to stop going to those places.",
    "What vegetable is cool, but not that cool? Rad-ish.",
    "I was wondering why the baseball kept getting bigger and bigger, and then it hit me.",
    "Why did the employee get fired from the calendar factory? She took a day off.",
    "Worrying works! Case in point: 90% of the things I worry about never happen.",
    "My teachers told me I’d never amount to much because I procrastinate. I told them, 'Just you wait!'",
    "Why do seagulls fly over the sea? If they flew over the bay, they would be bagels.",
    "I ordered a chicken and an egg from Amazon. I’ll let you know which comes first.",
    "What do you call a magician who lost his magic? Ian.",
    "I broke my finger last week. On the other hand, I am OK.",
    "I went to the doctor with a suspicious-looking mole. He told me they all look that way and I should have left it in the garden."
    "Two men are on opposite sides of the river. The first man shouts, “How do I get to the other side of the river?” The other man yells, “You are on the other side of the river!”",
    "Why would a pig dressed in black never get bullied? Because Batman has sworn to protect Goth-ham.",
    "Every morning, I announce that I’m going running, but then I don’t. It’s a running joke.",
    "Why is a swordfish’s nose 11 inches long? Because if it were 12 inches, it would be a foot.",
    "What state is known for its small drinks? Minnesota.",
    "What do you call a line of men waiting to get haircuts? A barberqueue.",
    "I was going to tell a time-traveling joke, but you didn’t like it.",
    "I can’t take my dog to the pond anymore because the ducks keep attacking him. That’s what I get for buying a pure bread dog.",
    "my wife and i laugh about how competitive we are. but i laugh more.",
    "how did the hipster burn his mouth? he ate his pizza before it was cool.",
    'i know they say money talks, but all mine says is "goodbye."',
    "why should you never fall in love with a tennis player? because to them, love means nothing!",
    "i gave up my seat to an elderly person on the bus. and that's how i lost my job as a bus driver.",
    "how do you find will smith in the snow? look for the fresh prints.",
    "do i know any jokes about sodium? na.",
    "70% of the earth is water, and virtually none of it is carbonated. so the earth is, in fact, flat.",
    "if you have six oranges in one hand and eight bananas in another, what do you have? big hands.",
    "my wife told me to stop impersonating a flamingo. i had to put my foot down.",
    "what did zero say to eight? nice belt.",
    "what's the difference between ignorance and apathy? i don't know, and i don't care.",
    "the past, the present and the future walked into a bar. it was tense.",
    "i just found out the company that produces yardsticks won't be making them any longer.",
    "geology rocks, but geography is where it's at.",
    "what's the difference between black-eyed peas and chickpeas? black eyed peas can sing us a song. chickpeas can hummus one.",
    "what did the duck say when she bought lipstick? put it on my bill.",
    'a termite walks into a bar. he says, "so, is the bar tender here?"',
    "did you hear that larry got a new job working for old macdonald? he's the new cieio.",
    "apparently, you can't use the words “beef stew” as a password. it's just not stroganoff.",
    "what did one plate say to the other plate? dinner's on me.",
    "what did the janitor say when he jumped out of the closet? supplies!",
    "what do you call a lazy kangaroo? a pouch potato.",
    "i stayed up all night and tried to figure out where the sun was. then it dawned on me.",
    "why do bananas never get lonely? because they hang out in bunches.",
    "why did the student eat his homework? because the teacher told him it was a piece of cake.",
    "why did the doughnut go to the dentist? to get a filling.",
    "what do you call bears with no ears? b.",
    "who built king arthur's round table? sir cumference.",
    "what do you call a bear with no teeth? a gummy bear!",
    "why did the car get a flat tire? because there was a fork in the road.",
    "how many tickles does it take to make an octopus laugh? ten-tickles.",
    "how did the vikings communicate? with norse code.",
    "what do you call a fish with no eyes? a fsh.",
    "what do you call a well-dressed lion? a dandelion.",
    "what happens to a frog's car when it breaks down? it gets toad away.",
    "what kind of car does an egg drive? a yolkswagen.",
    "there were two muffins in an oven, and one said, “it's getting hot in here, isn't it?” the other muffin gasped, “aah! a talking muffin!”",
    "what was beethoven's favorite fruit? a ba-na-na-na.",
    "what do you call a female chicken staring at a pile of lettuce? a chicken caesar salad.",
    "how do trees access their email? they log in.",
    "why don’t scientists trust atoms? they make up everything.",
    "which program do jedi use to sign their files? adobe sign kenobi.",
    "what is the best way to criticize your boss? very quietly, so she cannot hear you.",
    "our computers went down at the office today, so we had to do everything manually. it took me 15 minutes to shuffle the cards for solitaire.",
    "how do folks at nasa organize a party? they planet.",
    "why don’t comedians tell unemployment jokes? none of them work.",
    "why does snoop dogg use an umbrella? fo drizzle.",
    "how many computer programmers does it take to change a light bulb? none—that’s a hardware issue.",
    "a salesperson came into an office one day and said, “this computer will cut your workload by 50%!” the office manager replied, “great, i’ll take two of them!”",
    "what do you call someone who is happy on mondays? unemployed.",
    "what do you call 12 people doing the work of one? a committee.",
    "why didn’t the terminator upgrade to windows 10? i asked him and he said, “i still love vista, baby.”",
    "to the person who stole my copy of microsoft office, i will find you. you have my word.",
    "what kind of award does the world’s top dentist get? a little plaque.",
    "to err is human. to blame it on someone else shows management potential.",
    "if it wasn’t for the last minute, nothing would get done.",
    "archaeologist: someone whose career lies in ruins.",
    "the trouble with being punctual is that nobody’s there to appreciate it.",
    "i think they picked me for my motivational skills. everyone always says they have to work twice as hard when i’m around!",
    "have you heard about the guy who stole the calendar? he got 12 months!",
    "why does the golfer wear two pairs of pants? because he’s afraid he might get a hole in one.",
    "i’m so good at sleeping that i can do it with my eyes closed!",
    "why is it impossible to starve in the desert? because of all the sand which is there.",
    "two antennas decided to get married. the ceremony was pretty boring, but the reception was great!",
    "why shouldn’t you tell secrets in a cornfield? too many ears.",
    "what does a vegan zombie like to eat? graaains.",
    "what’s the difference between a well-dressed cyclist and a scruffy guy on a tricycle? a tire.",
    "what did the buddhist ask the hot dog vendor? make me one with everything.",
    "what do you call a pigeon who can’t find his way home? a pigeon.",
    "my wife told me to take the spider out instead of killing him, so i did. we went out, had a few drinks, saw a movie. great guy.",
    "how many sailors are pirates? 3.14%.",
    "i like telling dad jokes. sometimes he even laughs.",
    "what did one frenchman say to the other? no idea, i don’t speak french.",
    "i was raised as an only child—and that got on my brother’s nerves.",
    "why don’t vampires bet on horses? they can’t handle the stakes.",
    "a man rushed into a doctor’s surgery, shouting, “help me, please! i’m shrinking!” the doctor calmly said, “now settle down a bit. you’ll just have to learn to be a little patient.”",
    "do you know where you can get chicken broth in bulk? the stock market.",
    "what’s the best part about living in switzerland? i don’t know, but the flag is a big plus.",
    "have you heard the rumor about butter? never mind, i shouldn’t be spreading it."
]
quotes = [
    "You must be the change you wish to see in the world. -Mahatma Gandhi",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
    "The only thing we have to fear is fear itself. -Franklin D. Roosevelt",
    "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that. -Martin Luther King Jr.",
    "Do one thing every day that scares you. -Eleanor Roosevelt",
    "Well done is better than well said. -Benjamin Franklin",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. -Helen Keller",
    "It is during our darkest moments that we must focus to see the light. -Aristotle",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. -Ralph Waldo Emerson",
    "Be yourself; everyone else is already taken. -Oscar Wilde",
    "If life were predictable it would cease to be life and be without flavor. -Eleanor Roosevelt",
    "In the end, it's not the years in your life that count. It's the life in your years. -Abraham Lincoln",
    "Life is a succession of lessons which must be lived to be understood. -Ralph Waldo Emerson",
    "You will face many defeats in life, but never let yourself be defeated. -Maya Angelou",
    "Never let the fear of striking out keep you from playing the game. -Babe Ruth",
    "Life is never fair, and perhaps it is a good thing for most of us that it is not. -Oscar Wilde",
    "The only impossible journey is the one you never begin. -Tony Robbins",
    "In this life we cannot do great things. We can only do small things with great love. -Mother Teresa",
    "Only a life lived for others is a life worthwhile. -Albert Einstein",
    "The purpose of our lives is to be happy. -Dalai Lama",
    "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one. -John Lennon",
    "You only live once, but if you do it right, once is enough. -Mae West",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. -Ralph Waldo Emerson",
    "Don't worry when you are not recognized, but strive to be worthy of recognition. -Abraham Lincoln",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "Life is really simple, but we insist on making it complicated. -Confucius",
    "May you live all the days of your life. -Jonathan Swift",
    "Life itself is the most wonderful fairy tale. -Hans Christian Andersen",
    "Do not let making a living prevent you from making a life. -John Wooden",
    "Go confidently in the direction of your dreams! Live the life you've imagined. -Henry David Thoreau",
    "Keep smiling, because life is a beautiful thing and there's so much to smile about. -Marilyn Monroe",
    "In the depth of winter, I finally learned that within me there lay an invincible summer. -Albert Camus",
    "In three words I can sum up everything I've learned about life: it goes on. -Robert Frost",
    "So we beat on, boats against the current, borne back ceaselessly into the past. -F. Scott Fitzgerald",
    "Life is either a daring adventure or nothing. -Helen Keller",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss",
    "Life is made of ever so many partings welded together. -Charles Dickens",
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma — which is living with the results of other people's thinking. -Steve Jobs",
    "Life is trying things to see if they work. -Ray Bradbury",
    "Many of life's failures are people who did not realize how close they were to success when they gave up. -Thomas A. Edison",
    "The secret of success is to do the common thing uncommonly well. -John D. Rockefeller Jr.",
    "I find that the harder I work, the more luck I seem to have. -Thomas Jefferson",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. -Winston S. Churchill",
    "The way to get started is to quit talking and begin doing. -Walt Disney",
    "Don't be distracted by criticism. Remember — the only taste of success some people get is to take a bite out of you. -Zig Ziglar",
    "Success usually comes to those who are too busy to be looking for it. -Henry David Thoreau",
    "Everything you can imagine is real. -Pablo Picasso",
    "If you want to make your dreams come true, the first thing you have to do is wake up. -J.M. Power",
    "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. -Colin Powell",
    "The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere. -Barack Obama",
    "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
    "It is better to fail in originality than to succeed in imitation. -Herman Melville",
    "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
    "The road to success and the road to failure are almost exactly the same. -Colin R. Davis",
    "Always remember, your focus determines your reality. -George Lucas",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    "If you really look closely, most overnight successes took a long time. -Steve Jobs",
    "To be successful, you have to be selfish, or else you never achieve. And once you get to your highest level, then you have to be unselfish. -Michael Jordan",
    "Let the future tell the truth, and evaluate each one according to his work and accomplishments. The present is theirs; the future, for which I have really worked, is mine. -Nikola Tesla",
    "Try not to become a man of success. Rather become a man of value. -Albert Einstein",
    "Don't be afraid to give up the good to go for the great. -John D. Rockefeller",
    "Leave nothing for tomorrow which can be done today. -Abraham Lincoln",
    "Success is walking from failure to failure with no loss of enthusiasm. -Winston Churchill",
    "When you undervalue what you do, the world will undervalue who you are. -Oprah Winfrey",
    "If you want to achieve excellence, you can get there today. As of this second, quit doing less-than-excellent work. -Thomas J. Watson",
    "If you genuinely want something, don't wait for it — teach yourself to be impatient. -Gurbaksh Chahal",
    "The only place where success comes before work is in the dictionary. -Vidal Sassoon",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. -Jim Rohn",
    "Before anything else, preparation is the key to success. -Alexander Graham Bell",
    "In playing ball, and in life, a person occasionally gets the opportunity to do something great. When that time comes, only two things matter: being prepared to seize the moment and having the courage to take your best swing. -Hank Aaron",
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. -Maya Angelou",
    "The question isn't who is going to let me; it's who is going to stop me. -Ayn Rand",
    "Winning isn't everything, but wanting to win is. -Vince Lombardi",
    "Whether you think you can or you think you can't, you're right. -Henry Ford",
    "You miss 100% of the shots you don't take. -Wayne Gretzky",
    "I alone cannot change the world, but I can cast a stone across the water to create many ripples. -Mother Teresa",
    "You become what you believe. -Oprah Winfrey"
    "The most difficult thing is the decision to act, the rest is merely tenacity. -Amelia Earhart",
    "How wonderful it is that nobody need wait a single moment before starting to improve the world. -Anne Frank",
    "An unexamined life is not worth living. -Socrates",
    "Everything you've ever wanted is on the other side of fear. -George Addair",
    "Dream big and dare to fail. -Norman Vaughan",
    "Courage is grace under pressure. -Ernest Hemingway",
    "It is still best to be honest and truthful; to make the most of what we have; to be happy with simple pleasures; and have courage when things go wrong. -Laura Ingalls Wilder",
    "Nothing is impossible, the word itself says, ‘I'm possible!' -Audrey Hepburn",
    "It does not matter how slowly you go as long as you do not stop. -Confucius",
    "Don't find fault, find a remedy: anyone can complain. -Henry Ford",
    "A man may die, nations may rise and fall, but an idea lives on. -John F. Kennedy",
    "I have learned over the years that when one's mind is made up, this diminishes fear. -Rosa Parks",
    "I didn't fail the test. I just found 100 ways to do it wrong. -Benjamin Franklin",
    "If you're offered a seat on a rocket ship, don't ask what seat! Just get on. -Sheryl Sandberg",
    "With great power comes great responsibility. -Stan Lee",
    "I would rather die of passion than of boredom. -Vincent van Gogh",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
    "Dreaming, after all, is a form of planning. -Gloria Steinem",
    "Whatever the mind of man can conceive and believe, it can achieve. -Napoleon Hill",
    "First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end. -Aristotle",
    "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So, throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails. Explore, Dream, Discover. -Mark Twain"
]
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('^echo'):
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.send(message.content[6:])
            return
        role_name = "bot power"
        role = discord.utils.get(message.guild.roles, name=role_name)

        if role in message.author.roles or message.author.id == 788377795620896768:
            await message.channel.send(message.content[6:])
            message_content = message.content 

        else:
            await message.channel.send("You do not have the required role to use this command or bot power role doesn't exist")
    elif message.content.startswith('^random'):
        message.content.startswith('^random')
        message_content = message.content
        ando = message_content.from keep_alive import keep_alive
import discord
from discord.ext import commands
from discord import app_commands, message
import os
import pymongo
from sympy import sympify

keep_alive()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

Db = os.environ['MONGO']
client = pymongo.MongoClient(Db)
db = client["Cluster"]
collection = db["your_collection_name"]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="echo", description="Echoes back the message")
@app_commands.describe(say="What should I say?")
async def echo(interaction: discord.Interaction, say: str):
    if isinstance(interaction.guild, discord.Guild): 
        if "bot cmds" in interaction.user.roles or interaction.user.id == 788377795620896768:
            await interaction.response.send_message(say)
        else:
            await interaction.response.send_message('missing role "bot cmds"')
    else:
        await interaction.response.send_message(say)
@bot.tree.command(name="math", description="solve a math equation")
@app_commands.describe(solve="What should I solve?")
async def math(interaction: discord.Interaction, solve: str):
    await interaction.response.send_message(sympify(solve))
Token = os.environ['TOKEN']
bot.run(Token)
