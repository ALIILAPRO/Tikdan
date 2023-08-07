from requests import post

class Api:
    def export_video_info(self, url):
        result = self._api_tiktok(url)
        try:
            if result:
                video_info = {
                    "token": result["token"],
                    "id": result["id"],
                    "author_id": result["author_id"],
                    "author_name": result["author_name"],
                    "create_time": result["create_time"],
                    "comment_count": result["comment_count"],
                    "like_count": result["like_count"],
                    "share_count": result["share_count"],
                    "download_url": f"https://tikmate.app/download/{result['token']}/{result['id']}.mp4"
                }
                return video_info
        except KeyError:
            print("Unable to fetch TikTok details.")
        except Exception as error:
            print(error)

    def _api_tiktok(self, url):
        try:
            api = "https://api.tikmate.app/api/lookup"
            body = {"url": url}
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/3.12.1'
            }
            req = post(api, body, headers).json()
            return req
        except Exception as error:
            print(error)