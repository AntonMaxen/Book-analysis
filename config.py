import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = stopwords.words('english') + ['and']
URL_LIST = ['https://www.gutenberg.org/files/25830/25830-h/25830-h.htm',
            'https://www.gutenberg.org/files/84/84-h/84-h.htm',
            'https://www.gutenberg.org/files/32069/32069-h/32069-h.htm',
            'https://www.gutenberg.org/files/19362/19362-h/19362-h.htm',
            'https://www.gutenberg.org/files/64783/64783-h/64783-h.htm',
            'https://www.gutenberg.org/files/64791/64791-h/64791-h.htm',
            'https://www.gutenberg.org/files/64790/64790-h/64790-h.htm',
            'https://www.gutenberg.org/files/2610/2610-h/2610-h.htm',
            'https://www.gutenberg.org/files/32300/32300-h/32300-h.htm',
            'https://www.gutenberg.org/files/83/83-h/83-h.htm'
            ]

book_of_interest = 'https://www.gutenberg.org/files/103/103-h/103-h.htm'

RANDOM_SENTENCES = [
    "The swirled lollipop had issues with the pop rock candy.",
    "There aren't enough towels in the world to stop the sewage flowing from his mouth.",
    "The group quickly understood that toxic waste was the most effective barrier to use against the zombies.",
    "Swim at your own risk was taken as a challenge for the group of Kansas City college students.",
    "She works two jobs to make ends meet; at least, that was her reason for not having time to join us, jobs."
]


query = "The swirled lollipop had issues with the pop rock candy."


data_set = [
    "I enjoy reading about Machine Learning and Machine Learning is my PhD subject",
    "I would enjoy a walk in the park",
    "I was reading in the library"
]

"""

x: ['a', 'b', 'c', 'd']
---
1: ['a', 'b']
2: ['a', 'b', 'c']
3: ['b', 'd', 'e']
---
total_vocab = ['a', 'b', 'c', 'd', 'e']

x: [1, , 1, ,1 , 1 , 0]

1: [1, 1 ,0 ,0 ,0]
2: [1, 1, 1, 0, 0]
3: [0, 1, 0, 1, 1]
"""
