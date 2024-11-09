# YouTube Playlist Scraper

A Python script that extracts titles and video counts from YouTube playlists, using Selenium and BeautifulSoup. This script is ideal for users looking to gather data from multiple playlists without using the YouTube API.

## Features

- Extracts playlist titles
- Extracts video count for each playlist
- Simple to customize and use for personal or academic projects

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/) for handling JavaScript-rendered content
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for HTML parsing

## Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/viru023/youtube-playlist-scraper.git


2. Open the script and update the playlist_url variable to your desired YouTube playlist page URL. Example:

   ```python
    playlist_url = 'https://www.youtube.com/@username/playlists'


3. Run the script to see the playlist titles and video counts in your terminal.

## Example Output

```bash

Copy code
Playlist 1: Art and Culture by Neeraj Rao Sir - 6 videos
Playlist 2: Security for UPSC by Jatin Sir - 8 videos
...

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
