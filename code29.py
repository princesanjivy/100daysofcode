# @princesanjivy
# translate text to any language
# using Google translate API

from googletrans import Translator

trans = Translator()
translated = trans.translate(text="python programming language",
				src="en",		#the source text language, 'en' for english
				dest="ta")		#the language to translate the source text, 'ta' for tamil
#refer googletrans.LANGCODES

print(translated.text)

# OUTPUT
# 'பைதான் நிரலாக்க மொழி'