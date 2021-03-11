import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = stopwords.words('english') + ['and']
URL_LIST = ['https://www.gutenberg.org/files/25830/25830-h/25830-h.htm']

RANDOM_SENTENCES = [
    "The swirled lollipop had issues with the pop rock candy.",
    "There aren't enough towels in the world to stop the sewage flowing from his mouth.",
    "The group quickly understood that toxic waste was the most effective barrier to use against the zombies.",
    "Swim at your own risk was taken as a challenge for the group of Kansas City college students.",
    "She works two jobs to make ends meet; at least, that was her reason for not having time to join us, jobs."
]
