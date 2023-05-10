import requests
from bs4 import BeautifulSoup
import pyperclip
import webbrowser

url = input("Enter in the URL for the article you want to summarise: ")

# Scraping the text of the article.
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

main_text = ""
for p in soup.find_all("p"):
    main_text += p.get_text()

# Formatting the question and copying it to dashboard.
output = 'Can you make a summary of the following article: "{}"'.format(main_text)
print(output)
pyperclip.copy(output)

# Open ChatGPT.
url = "https://chat.openai.com/"
webbrowser.open_new(url)
print("\nOpening ChatGPT site...")
