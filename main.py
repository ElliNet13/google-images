import requests
from bs4 import BeautifulSoup
import os
import sys

def fetch_image_urls(query, num_images):
    url = f"https://www.google.com/search?q={query}&tbm=isch"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_urls = []
    for img in soup.find_all('img'):
        image_url = img.get('src')
        if image_url and image_url.startswith('http'):
            image_urls.append(image_url)

    return image_urls[:num_images]

def download_images(image_urls, query):
    # Create a directory to save images
    if not os.path.exists(query):
        os.makedirs(query)

    # Download images
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            i = i + 1
            with open(os.path.join(query, f"image_{i}.jpg"), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image_{i}.jpg")
        except Exception as e:
            print(f"Error downloading image_{i}: {e}")

# Define your search query and number of images to download
query = input("Search Google images for: ")
try:
 num_images = int(input("Number of images: "))
except ValueError:
  print("Invalid input. Please enter a valid number.")
  sys.exit(1)

# Fetch image URLs
image_urls = fetch_image_urls(query, num_images)

# Download images
download_images(image_urls, query)