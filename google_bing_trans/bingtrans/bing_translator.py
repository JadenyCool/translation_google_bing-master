# 通过bing翻译来检查语言
# author: Jerry Gu
# time:2021-2-14


import requests
import json


class bing_translator:
    """Bing Translation"""

    def __init__(self):
        self.url = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=AF5B9463703E4CB5BF7154DF261B2FFC&IID=translator.5024.1"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
        }

    def _request(self, data):
        response = requests.post(url=self.url, data=data, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return "network requests is failed"

    @staticmethod
    def _json_parse(res):
        """
        :param res: json text
        """
        parse = json.loads(res)
        detectedLanguage = parse[0]["detectedLanguage"]
        translations = parse[0]["translations"][0]
        return detectedLanguage, translations

    def translator(self, text, to='en'):
        """
         :param text: The source text(s) to be translated.
         :type text: UTF-8 :class:`str`; :class:`unicode`;

         :param to:  You can use 99 language in target and source,details view LANGUAGES.
                    Target language: like 'en'、'zh'、'th'...
        """
        data = {
            "fromLang": "auto-detect",
            "text": "{}".format(text),
            "to": "{}".format(to)
        }

        res = self._request(data=data)
        _, translations = self._json_parse(res)
        return translations["text"]

    def detect(self, text):
        """
        :param text: The source text(s) to be translated.
        @return: en, ja, and so on
        """
        if text is None:
            pass
        data = {
            "fromLang": "auto-detect",
            "text": "{}".format(text),
            "to": "en"
        }
        res = self._request(data)
        detect_language, _ = self._json_parse(res)
        return detect_language["language"]


if __name__ == '__main__':
    bing_translator().translator("你好", 'en')
