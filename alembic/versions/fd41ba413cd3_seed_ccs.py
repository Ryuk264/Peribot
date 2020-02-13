"""create media table

Revision ID: fd41ba413cd3
Revises: 
Create Date: 2019-12-31 11:41:08.262130

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'fd41ba413cd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    data_upgrades()


def data_upgrades():
    custom_commands = sa.table(
        'custom_commands',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('server_id', sa.Integer(), nullable=False),
        sa.Column('command', sa.String(), nullable=False),
        sa.Column('result', sa.String(), nullable=False),
        sa.Column('added_by_user_id', sa.Integer(), nullable=False)
    )
    op.bulk_insert(custom_commands, [
        {'server_id': 515370084538253333, 'command': '()w()', 'result': 'NO ()w()',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': '0w0', 'result': 'NO 0w0',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'bestship',
         'result': 'https://cdn.discordapp.com/attachments/515371251343294464/625185343074729994/21bc0b23-8239-42d0-bc0d-1ecc005a1692.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'bluekira',
         'result': 'My name is Blue Pearl. I\'m 19 years old. My house is in the southern section of New England, where all the postcard towns are, and I am not married. I work as an employee for a plumbing supply store, and I get home every day by 11 PM at the latest. I don\'t smoke, but I tried an edible once.\n\nI\'m in bed by 2 AM, and make sure I get at least four hours of sleep, no matter what. After eating whatever I have on me and browsing Discord and Reddit before going to bed, I usually have no problems sleeping until morning. I was told there were no issues at my last check-up.\n\nI\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, rather spending my nights looking at Blue Pearl photos, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I would probably get my ass handed to me.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'breath',
         'result': 'https://media.discordapp.net/attachments/564316750313685002/624350327206051840/relax.gif',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'cookies',
         'result': 'https://cdn.discordapp.com/attachments/515383034552385541/623691494284591105/20190909_224957.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'cpindex',
         'result': 'https://docs.google.com/document/d/1n0Q9DOLuwNAni7obdIZJBWmCBuellvkvqyPE5c1wLe4/edit?usp=sharing',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'creeper', 'result': 'Aww man',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'dab',
         'result': '<:dabphire:591755399435255831> <:peridab:609835898758234131>',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'ding', 'result': 'Dong',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'doyou',
         'result': 'remember the 21st night of september?\nlove was changing the mind of pretenders\nwhile chasing the clouds away\nOur hearts were ringing\nin the key that our souls were singing.\nas we danced in the night,\nremember - how the stars stole the night away, yeah yeah yeah.\nHey hey hey,\nba de ya - say do you remember\nba de ya - dancing in september\nba de ya - never was a cloudy day\nBa duda, ba duda, ba duda, badu\nba duda, badu, ba duda, badu\nba duda, badu, ba duda\nMy thoughts are with you\nholding hands with your heart to see you\nonly blue talk and love,\nremember - how we knew love was here to stay\nNow december found the love that we shared in september.\nonly blue talk and love,\nremember - the true love we share today\n\nhey hey hey\nba de ya - say do you remember\nba de ya - dancing in september\nba de ya - never was a cloudy day... there was a\nba de ya - say do you remember\nba de ya - dancing in september\nba de ya - golden dreams were shiny days\nNow our bell was ringing, aha\nour souls were singing.\ndo you remember every cloudy day - yau\nThere was a\nba de ya - say do you remember\nba de ya - dancing in september\nba de ya - never was a cloudy day... there was a\nba de ya - say do you remember\nba de ya - dancing in september\nba de ya - golden dreams were shiny days\nBa de ya de ya de ya\nba de ya de ya de ya\nba de ya de ya de ya - de ya... x2',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'e0wsd', 'result': 'e3rwfusd',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'emeraldtime',
         'result': 'ONLY 2 MINUTES AND 30 GOD DAMN SECONDS OF SCREEN TIME FOR ANGRERY GREEN GEM GIRL??????? whAT THE FUCK',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'hitormiss',
         'result': 'https://www.youtube.com/watch?v=Xn8rJN48Sck',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'kirapasta',
         'result': 'My name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'kiwapasta',
         'result': 'My name is yoshikage kiwa. I\'m 33 yeaws owd. My house is in the nowtheast section of mowioh, whewe aww the viwwas awe, and i am not mawwied. I wowk as an empwoyee fow kame yu depawtment stowes, and i get home evewy day by 8 pm at the watest. I don\'t smoke, but i occasionawwy dwink. I\'m in bed by 11 pm, and make suwe i get eight houws of sweep, no mattew what. Aftew having a gwass of wawm miwk and doing about twenty minutes of stwetches befowe going to bed, i usuawwy have no pwobwems sweeping untiw mowning, just wike a baby. I wake up without any fatigue ow stwess in the mowning. I was towd thewe wewe no issues at my wast check-up. What i\'m twying to expwain is that i\'m a pewson who wishes to wive a vewy quiet wife. I take cawe not to twoubwe mysewf with any enemies, wike winning and wosing, that wouwd cause me to wose sweep at night. That is how i deaw with society, and i know that is what bwings me happiness. Awthough, if i wewe to fight i wouwdn\'t wose to anyone.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'legendofperidot',
         'result': 'https://cdn.discordapp.com/attachments/515371174558040077/621916957804986369/tempFileForShare_20190912-235547.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'lemons',
         'result': 'When life gives you lemons, don\'t make lemonade. Make life take the lemons back Get mad I don\'t want your damn lemons What the hell am I supposed to do with these? Demand to see life\'s manager Make life rue the day it thought it could give Cave Johnson lemons Do you know who I am? I\'m the man who\'s gonna burn your house down With the lemons I\'m gonna get my engineers to invent a combustible lemon that burns your house down',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'lynnlshoodie',
         'result': 'Super secret ash hoodie I keep underneath my bed. Smells like strawberry and teenage boy. Keeps me warm when the world is cold. I wish Lynnl was here.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'may1',
         'result': 'this is a test I hope you enjoy all the custom commands that I\'m going to add',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'mayrant',
         'result': '1\nYou know what, I\'m sick and tired of all of these misogynist jokes about the testicles. What about ovaries? You never hear anyone say \"I have ovaries of steel.\" This genuinely makes me angry. This bias shows the fault in our culture. \nEveryday I hear people say \"do it no balls\" when someone is going to do something epic. But I never hear that about women. I feel distraught every time I hear it.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'meh',
         'result': 'https://cdn.discordapp.com/attachments/515371174558040077/623908076344311849/image0.png',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'minecraftgood',
         'result': '\"M-m... M\"\n\nNo one was paying attention in the crossroads of New York as I was giving my speech.\n\n\"M-m-mine...\"\n\nHowever, one person was intrigued in what I was saying.\n\n\"M-m-m-minecraft...\"\n\nThen it was just a domino effect, ten more people are watching.\n\n\"Minecraft...\"\n\nA hundred were now watching, this had caught the attention of even the busy drivers in rush hour. Their faces in anticipation, some were even scared. Others were complaining that this isn\'t the real deal.\n\n\"MINECRAFT...\"\n\nBut they all suddenly started cheering, shaking, praying. When they heard my tone, my pitch, my timbre.... they all knew what was going to come next. They realized... that salvation of the human race has finally come.\n\n\"Minecraft good Fortnite bad\"\n\nAnd then the silence broke\n\n\"OOOIOIIUUUUUGHHHhJJHHHHHWAASEAAAa//::\"\n\nThousands of people fell to their knees, yelling orgasmically. People starting crying tears of joy, others were running and thanking God, News reporters were already on the scene, broadcasting the entire thing nationwide and consequently the entire world. Hundreds of people came out of their cars, buses, taxis, stores, and subway stations hooting and hollering. It was a miracle unfolding.\n\nI started to say the next sentence relayed to me by our Lord and Savior.\n\n\"M-m-mi... Mine...\"\n\nAlready some people fainted at just the mere sound of my voice. Even more people came. Some were jumping from planes thousands of feet in the air, others ran or swam miles to here in mere seconds. I think I even spotted a few famous people.\n\n\"MINE...\"\n\nNearly a million people were here now. There\'s now Europeans, Canadians, Mexicans, Latin Americans, West Coasters, Africans, and even several Asians and one Australian. They were screaming hysterically, bringing gifts for me, taking pictures and videos. Fireworks and confetti everywhere, helicopters, and even Donald Trump was here with his family bowing down to me',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'mobile',
         'result': 'you ...\n\nyes you,\nyou thought we wouldn\'t realize didn\'t you ?\nYOU\'RE A MOBILE USER\nyou really thought your comment was going to go unnoticed but I saw that \"R\" at the beginning of this reddit link,\nyou stupid, how you could confuse r /something with R /something, there is only one possible explanation...\nYOU ARE A MOBILE USER WHAT A LOSER YOU ARE A STUPID NOOOOORMIE\nmeanwhile me an intellectual am using a computer, I am clearly a superior being for using a computer, after all I can play amazing games on the computer WHILE YOU PLAY NORMIE GAMES ON YOUR NORMIE MOBILE PHONE',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'modteam',
         'result': 'The best of the misfits and a group of awesome people who do their best on this server.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'mysoberass',
         'result': 'My sober-ass s/o picking up a yellow 5lb weight: \"why is this banana so heavy\" \nhttps://discordapp.com/channels/515370084538253333/515371174558040077/615019963367030784',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'nowo', 'result': 'No OwO',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'peribot', 'result': 'https://bit.ly/peribot',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'pingndp',
         'result': '<@188085837454376971> get pinged lmao', 'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'plsdontdelete',
         'result': 'haha get fricked you didnt say anything about editing',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'pong', 'result': 'PING',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'promote',
         'result': '<@412203055820439553> has been promoted to the leader bot of the server',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'qwq', 'result': 'NO QwQ',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'refuse', 'result': 'YOU CANT REFUSE MY LOVE',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'roast4harrassmentfemale',
         'result': 'Alright, someone messing with you. You are strong. Give this shithead what he needs. now this might not work for every scenario but it\'s a pretty good roast.\n`Bro, look at you mr. Cheese stick. With your fake Jordans. You never going to get a girl if you keep harassing people just to make your pepperoni face look better towards your peers. Because you\'re not honey. You can only dream that your dick was as big as your clout instead of smaller than your bank account. Bro, come back to me when you have more balls than a dog. Mr. Cheese stick, picking on women makes you less of a man than me.`',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'sourmilksea',
         'result': '`Get out of sour milk sea\nYou don''t belong there\nGet back to where you should be\nFind out what\'s going on there`\n\"Oh wait... This isn\'t milk...\"',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'stevonnierant',
         'result': 'You know what? I\'m sick and tired of all of these jokes about Lapidot. What about Stevonnie? You never hear anyone say \"I what an episode about Steven and Connie\'s relationship.\" This genuinely makes me angry. This bias shows the fault in our fandom. \nEveryday I hear people say \"I hope Lapidot is in here\" when someone is going to go watch the movie. But I never hear that about Stevonnie. I feel distraught every time I hear about it.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'thisisfine',
         'result': 'https://media.discordapp.net/attachments/550913395633684480/617893774458355713/gf18tthxf8g31.png?width=576&height=517',
         'added_by_user_id': 204792579881959424},

        {'server_id': 515370084538253333, 'command': 'trumoo',
         'result': 'Hey man you shouldn\'t do any of that TruMoo. That stuff will mess you up. My brother, he was a TruMoo dealer. 10 years at 19 y/o. Nah man you\'re too good for that TruMoo. That stuff, it does wacky things to your brain man. You are too good for TruMoo. TruMoo is like my ex, man.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'uwu', 'result': 'I\'ll allow it... for now.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'wander', 'result': 'She\'s wanderful',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'water',
         'result': 'Dominate the room, do what i do, get one of those 15L water cooler bottles and bring it to class slung over one shoulder, slam that motherfucker on the ground in the aisle.\n\nEvery time you feel a little thirsty stand up, lift the bottle to your mouth with both arms, make sure you spill plenty of water over yourself and the floor every time you do, also, let out a deep, loud, exhalation of satisfaction after every sip, then finish the routine by slamming the bottle on the ground again before loudly saying, \"pfew, I needed that, I was getting a bit THIRSTY\" yell thirsty as loud as you can.\n\nWhen class finishes, pick up the bottle in such a way that the remainder pours out as you leave the room.',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'we', 'result': 'ARE THE CRYSTAL GEMS',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'wet',
         'result': 'Rain and taking a shower makes me really wet',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'ya', 'result': 'YEET',
         'added_by_user_id': 204792579881959424},
        {'server_id': 515370084538253333, 'command': 'yiffnessgram',
         'result': 'The YiffnessGramtm sweat_dropsFurry Test is a multistage knot capacity test that progressively gets more difficult wearyok_handpoint_leftas it continues. The 200 heart_eyes_catpound bara furry test will kissbegin in 30eyes nyas. kissing_catscream_catraised_handsLine up at the cage doors. The breeding blue_heartpurple_heartsweat_dropsspeed starts slowlysweat_dropsweary, but gets fasterfirefire each minute after you hear this signal.heart_eyes_cat [nyaa~<33] tongueA single nya should be completed each time you hear this sound. [prrrr~]blue_heartblue_heart Remember to yiffsweat_dropssweat_drops in a fursuit, and yiff eyeseyestonguelipsas long as possiblecatrevolving_hearts',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'dance',
         'result': 'https://cdn.discordapp.com/attachments/486899116299911178/531194184930033664/jo0mmmyjwk821.gif',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'ya', 'result': 'YEET',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'ding',
         'result': 'https://cdn.discordapp.com/attachments/486899116299911178/528726993764876316/image0.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'eyy',
         'result': 'https://cdn.discordapp.com/attachments/486899116299911178/622599499176738835/SinfulDeterminedKrill-small.gif',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'gimme',
         'result': 'https://cdn.discordapp.com/attachments/457235693282918401/619959710191190027/Gimme_Gimme.gif',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'ginsu',
         'result': 'Ginsu48 starts making out with their image in a mirror... strage one this Ginsu48 is...',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'hot',
         'result': 'https://imgur.com/cpGwCdE\nhttps://imgur.com/cUbWo5Y\nhttps://cdn.discordapp.com/attachments/344493023008391170/463437743444328469/yeh.png\nhttps://imgur.com/Mwyi2i5\nhttps://cdn.discordapp.com/attachments/398536233388736545/534557130318151680/1vqxbhyy.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'lewd',
         'result': 'https://cdn.discordapp.com/attachments/486899116299911178/532729697889681419/image0.png',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'nice',
         'result': 'https://gfycat.com/forthrightsmoothgemsbok', 'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'no',
         'result': 'https://media.tenor.com/images/3b6dec9eb39f815d9130196d27263c94/tenor.gif',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'pout',
         'result': 'https://cdn.discordapp.com/attachments/517546603473797141/613511906518499338/FB_IMG_1566318281422.jpg',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'salute',
         'result': 'https://66.media.tumblr.com/tumblr_m8bb1k3ftA1qlh1s6o1_250.gifv',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'slap',
         'result': 'https://giphy.com/gifs/toradora-taiga-aisaka-a7HKjDb3UJ0kM',
         'added_by_user_id': 204792579881959424},
        {'server_id': 448695150135345152, 'command': 'truelove',
         'result': 'https://giphy.com/gifs/toradora-taiga-aisaka-JRrlhZpVjMZA4',
         'added_by_user_id': 204792579881959424}
    ])


def downgrade():
    pass