import wikipedia
from wordcloud import WordCloud, STOPWORDS

title = str(input("enter the title: "))
keyword = wikipedia.search(title)
page = wikipedia.page(keyword)
content = page.content
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color="white",
                      max_words=300,
                      stopwords=stopwords)
wordcloud.generate(content)
wordcloud.to_file("output.jpg")