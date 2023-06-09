import requests
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Get the text data from a website
url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url)
text_data = response.text

# Clean the text data
cleaned_data = re.sub(r'\[[0-9]*\]', ' ', text_data)  # Remove citations
cleaned_data = re.sub(r'\s+', ' ', cleaned_data)  # Remove extra spaces
cleaned_data = re.sub('[^a-zA-Z]', ' ', cleaned_data)  # Remove non-alphabetic characters
cleaned_data = cleaned_data.lower()  # Convert to lowercase
cleaned_data = cleaned_data.split()  # Split into individual words

# Remove stopwords
stopwords_set = set(stopwords.words('english'))
cleaned_data = [word for word in cleaned_data if word not in stopwords_set]

# Lemmatize words
lemmatizer = WordNetLemmatizer()
cleaned_data = [lemmatizer.lemmatize(word) for word in cleaned_data]

# Count the word frequency
word_count = {}
for word in cleaned_data:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

# Build the word cloud
wordcloud = WordCloud().generate_from_frequencies(word_count)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
