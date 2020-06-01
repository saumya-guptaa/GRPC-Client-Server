import googletrans

from googletrans import Translator
translator=Translator()

def google_trans(x):
    y=translator.translate(x)
    return y