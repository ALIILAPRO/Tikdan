from requests   import post, get
from pathlib    import Path
from os         import mkdir
import json

def API_TIKTOK(url):
	try:
		api = "https://api.tikmate.app/api/lookup"
		body = {"url": url}
		headers = {
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'User-Agent': 'okhttp/3.12.1'
				}
		req  = post(api, body, headers).json()
		return req
	except Exception as error:
		print(error)

Path('./TikTok').mkdir(parents=True, exist_ok=True)
url           = input("Enter tiktok url: ")
result        = API_TIKTOK(url)
print("start download ...")
tkn           = result["token"]
id_v          = result["id"]
author        = result["author_id"]
author_name   = result["author_name"]
create_time   = result["create_time"]
comment_count = result["comment_count"]
like_count    = result["like_count"]
share_count   = result["share_count"]
url_dl        = f"https://tikmate.app/download/{tkn}/{id_v}.mp4"
FILE_NAME     = '{}-{}.mp4'.format(author, id_v)
FILE_PATH     = '{}/{}'.format('./TikTok',FILE_NAME)
mp4_data      = get(url_dl).content
with open(FILE_PATH, 'wb') as handler:
	handler.write(mp4_data)
print("finish.")