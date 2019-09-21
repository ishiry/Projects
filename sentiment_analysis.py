#modules
import re
import PyPDF2
from argparse import ArgumentParser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

#get cmd argument
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
args = parser.parse_args()

#function to get sentiment
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score['compound']

#read file
pdfFileObj = open(args, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#create text file for mom and dad summary
mom_txt = open(r"mom_sentiment.txt","w+")
dad_txt = open(r"dad_sentiment.txt","w+")

#string for mom
mom_string = ['mom', 'she', 'her']

for i in range(0, pdfReader.getNumPages()):
    PageObj = pdfReader.getPage(i)
    Text = PageObj.extractText().lower()
    textitem = re.split(r'(\d+/\d+/\d+(, ))', Text)
    for nouns in mom_string:
        for items2 in textitem:
            if re.search(nouns,items2):
                mom_txt.write("\nPattern Found on Page: " + str(i))
                mom_txt.write('\n================================')
                mom_txt.write('\n------MESSAGE ----------------\n')
                mom_txt.write(items2)
                mom_txt.write('\n------SENTIMENT RATING -------\n')
                mom_txt.write('Sentiment rating' + str(sentiment_analyzer_scores(items2)))
                mom_txt.write('\n\n')
mom_txt.close()


#string for dad
dad_string = ['dad','him']

for i in range(0, pdfReader.getNumPages()):
    PageObj = pdfReader.getPage(i)
    Text = PageObj.extractText().lower()
    textitem = re.split(r'(\d+/\d+/\d+(, ))', Text)
    for nouns in dad_string:
        for items2 in textitem:
            if re.search(nouns,items2):
                dad_txt.write("\nPattern Found on Page: " + str(i))
                dad_txt.write('\n================================')
                dad_txt.write('\n------MESSAGE ----------------\n')
                dad_txt.write(items2)
                dad_txt.write('\n------SENTIMENT RATING -------\n')
                dad_txt.write('Sentiment rating' + str(sentiment_analyzer_scores(items2)))
                dad_txt.write('\n\n')
dad_txt.close()
