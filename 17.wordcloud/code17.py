# coded by Prince!
# creating wordcloud using python
# prerequisite
# pip install wordcloud

from wordcloud import WordCloud
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
		Vivamus lacinia, orci vel condimentum rutrum,
  		magna turpis dignissim purus, at condimentum 
 		diam nisi sit amet turpis. Phasellus dignissim 
 		nisl eu augue auctor hendrerit."""

wrdcloud = WordCloud(background_color="white") #many arugments are there
wrdcloud.generate(text)

wrdcloud.to_file("image.png")