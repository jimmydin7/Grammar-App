import json
from gingerit.gingerit import GingerIt
import re
from textblob import TextBlob

class Ai:
    def __init__(self, app):
        self.app = app
        self.parser = GingerIt()

        file = open('scripts/ai/temp_storage.json')
        self.storage = json.load(file)
        file.close()
    
    def layers1_3(self, txt):
        # Layer 1
        # Lower the txt
        txt.lower()

        # Layer 2 - Corrected commonly mispelled words with re

        # Define a dictionary of common misspelled words and their correct spellings
        # Check for mistakes in common mispelled words

        # common_misspelled_words = self.app.handler.db.data['ai-storage']['common-misspelled-words']
        common_misspelled_words = self.storage['common-misspelled-words']

        for misspelled, corrected in common_misspelled_words.items():
            txt = re.sub(r'\b({})\b'.format(misspelled), corrected, txt)


        # Layer 3 - Long forms of words

        # short_long_forms = self.app.handler.db.data['ai-storage']['short-long-forms']
        short_long_forms = self.storage['short-long-forms']

        for short, long in short_long_forms.items():
            txt = re.sub(r'\b({})\b'.format(short), long, txt)
        return txt
    
    def layer4(self, txt):
        # Layer 4 - Parse with gingerit for final and accurate result
        return self.parser.parse(txt)['result']