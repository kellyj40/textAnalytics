hurricane <- Corpus (DirSource('Desktop/TextAnalyticsWebsite/textAnalytics/TextAnalytics/Tutorials/tutorial4/temp2/'))
inspect(hurricane)
wordcloud(hurricane, scale=c(5,0.5), max.words=100, random.order=FALSE, rot.per=0.35, use.r.layout=FALSE, colors=brewer.pal(8, 'Dark2'))