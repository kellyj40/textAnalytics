library(tm)
library(SnowballC)
library(wordcloud)

# Take in all the files from the temp directory.
hurricane <- Corpus (DirSource('Desktop/TextAnalyticsWebsite/textAnalytics/TextAnalytics/Tutorials/tutorial4/temp/'))
inspect(hurricane)
# Standard preprocessing, already done most in the python file
hurricane <- tm_map(hurricane, stripWhitespace)
hurricane <- tm_map(hurricane, tolower)
hurricane <- tm_map(hurricane, removeWords, stopwords('english'))
hurricane <- tm_map(hurricane, stemDocument)

wordcloud(hurricane, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, 'Dark2'))


