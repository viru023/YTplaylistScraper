from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the YouTube playlists page
playlist_url = 'https://www.youtube.com/@Way2ias/playlists'
driver.get(playlist_url)

# Wait for the page to fully load
time.sleep(3)

# Parse page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract playlist titles and video counts
playlists = []
for h3 in soup.find_all('h3', class_='yt-lockup-metadata-view-model-wiz__heading-reset'):
    # Extract the title from the <h3> tag
    title_span = h3.find('span', class_='yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap')
    title = title_span.get_text().strip() if title_span else "Unknown Title"
    
    # Find the next div with the video count
    video_count_div = h3.find_next('div', class_='badge-shape-wiz__text')
    video_count = video_count_div.get_text().strip() if video_count_div else "Unknown Count"
    
    playlists.append({'title': title, 'video_count': video_count})

# Print playlist titles and video counts
for i, playlist in enumerate(playlists, 1):
    print(f"Playlist {i}: {playlist['title']} - {playlist['video_count']}")
