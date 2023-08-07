# Tikdan

tikdan is a Python package that provides functionality for exporting video information from TikTok URLs using the TikMate API.

## Installation

You can install tikdan using `pip`:

```sh
pip install tikdan
```

## Usage

```python
from tikdan import Tikdan

tiktok_api = Tikdan.Api()
url = input("Enter TikTok URL: ")
video_info = tiktok_api.export_video_info(url)
print(video_info)
```

### License

This project is licensed under the [GNU General Public License v3.0](https://github.com/ALIILAPRO/Tikdan/blob/main/LICENSE).