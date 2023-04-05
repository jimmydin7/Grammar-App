from flask import render_template, request, redirect
import re
from textblob import TextBlob


class Index:

    def index(self):
        @self.app.route('/about', methods=['GET'])
        def about():
            return render_template('user/about.html')

        @self.app.route('/', methods=['GET', 'POST'])
        def index():

            # Layer 1 - Text Processing
            txt = request.form.get('txt')

            if txt != None:
                key = request.cookies.get('key')
                if key != None and self.user_handler.get(key) != None:  # This will be None if the user is not logged in.

                    # Lower the txt
                    txt.lower()

                    # Layer 2 - Corrected commonly mispelled words with re

                    # Define a dictionary of common misspelled words and their correct spellings

                    common_misspelled_words = {
                        'its': "it's",
                        'theyr': 'their',
                        'thier': 'their',
                        'there': 'their',
                        'theyre': "they're",
                        'wont': "won't",
                        'cant': "can't",
                        'shouldnt': "shouldn't",
                        'wouldnt': "wouldn't",
                        'couldnt': "couldn't",
                        'didnt': "didn't",
                        'doesnt': "doesn't",
                        'dont': "don't",
                        'youre': "you're",
                        'youll': "you'll",
                        'youd': "you'd",
                        'hes': "he's",
                        'shes': "she's",
                        'weve': "we've",
                        'theyve': "they've",
                        'ive': "I've",
                        'id': "I'd",
                        'thats': "that's",
                        'whats': "what's",
                        'heres': "here's",
                        'theres': "there's"
                    }

                    # Check for mistakes in common mispelled words
                    for misspelled, corrected in common_misspelled_words.items():
                        txt = re.sub(r'\b({})\b'.format(misspelled), corrected, txt)

                    # Layer 3 - Long forms of words
                    short_long_forms = {
                        "ai": 'Artificial Intelligence',
                        "chatgpt": 'ChatGPT',
                        "google": 'Google',
                        "wiki": 'Wikipedia'
                    }

                    for short, long in short_long_forms.items():
                        txt = re.sub(r'\b({})\b'.format(short), long, txt)

                    # Layer 4 - Parse with gingerit for final and accurate result
                    txt = self.ai.parser.parse(txt)['result']
                    return render_template('index.html', txt=txt, user=self.user_handler.get(request.cookies.get('key')))
                else:
                    return redirect('/signup')
            else:
                return render_template('index.html', txt=txt, user=self.user_handler.get(request.cookies.get('key')))






