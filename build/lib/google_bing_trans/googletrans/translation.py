# author Jerry Gu
# version : 0.0.1
import logging
from urllib.parse import quote

import json
import random
import requests

from google_bing_trans.googletrans.constants import LANGUAGES, DEFAULT_SERVICE_URLS


class Google_translator(object):

    def __init__(self, service_url=None):
        self.prefix = "https://"
        if self._check_service_url(service_url) is True:
            self.baseUrl = self.prefix + service_url
        else:
            self.baseUrl = self.prefix + 'translate.google.cn'
        self.Headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        self.url = self.baseUrl.strip() + "/_/TranslateWebserverUi/data/batchexecute"

    @staticmethod
    def _check_service_url(service_url):
        if service_url in DEFAULT_SERVICE_URLS:
            return True
        else:
            return False

    def _get_cookie(self):
        """get Cookie information"""
        res = requests.get(url=self.baseUrl, headers=self.Headers)
        cookie = res.cookies
        return cookie

    def _request_data(self, text, dest='auto', src='auto'):
        GOOGLE_TTS_RPC = ["MkEWBc"]
        parameter = [[text.strip(), dest, src, True], [1]]
        escaped_parameter = json.dumps(parameter, separators=(',', ':'))
        rpc = [[[random.choice(GOOGLE_TTS_RPC), escaped_parameter, None, "generic"]]]
        espaced_rpc = json.dumps(rpc, separators=(',', ':'))
        freq_initial = "f.req={}&".format(quote(espaced_rpc))
        freq = freq_initial
        return freq

    def _send_requests(self, data):
        cookie = self._get_cookie()
        try:
            res = requests.post(self.url, data=data, headers=self.Headers, cookies=cookie, timeout=10)
            if res.status_code == 200:
                return res
            # except requests.exceptions.Timeout
            # or ConnectionRefusedError
            # or requests.ConnectionError or requests.exceptions.SSLError
            else:
                self._send_requests(data=data)
        except requests.exceptions or ConnectionResetError:
            import time
            time.sleep(1)
            self._send_requests(data=data)

    def detect(self, text):
        text = str(text)
        if len(text) >= 5000:
            return "Warning: Can only detect less than 5000 characters"
        if len(text) == 0:
            return ""
        data = self._request_data(text)
        res = self._send_requests(data)
        if res is not None:
            try:
                for line in res.iter_lines():
                    decoded_line = line.decode('utf-8')
                    if "MkEWBc" in decoded_line:
                        try:
                            response = (decoded_line + ']')
                            response = json.loads(response)
                            response = list(response)
                            response = json.loads(response[0][2])
                            response = list(response)
                            detect_lang = response[0][2]
                        except Exception:
                            raise Exception
                        return [detect_lang, LANGUAGES[detect_lang.lower()]]
                res.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logging.log(e)
            except requests.exceptions.RequestException as e:
                logging.log(e)

    def translate(self, text, dest='auto', src='auto'):
        """Translate text from source language to destination language

          :param text: The source text(s) to be translated. Batch translation is supported via sequence input.
          :type text: UTF-8 :class:`str`; :class:`unicode`; string sequence (list, tuple, iterator, generator)

          :param dest: The language to translate the source text into.
                       The value should be one of the language codes listed in :const:`google_bing_trans.LANGUAGES`
                       or one of the language names listed in :const:`google_bing_trans.LANGCODES`.
          :param dest: :class:`str`; :class:`unicode`

          :param src: The language of the source text.
                      The value should be one of the language codes listed in :const:`google_bing_trans.LANGUAGES`
                      or one of the language names listed in :const:`google_bing_trans.LANGCODES`.
                      If a language is not specified,
                      the system will attempt to identify the source language automatically.
          :param src: :class:`str`; :class:`unicode`

          :rtype: Translated
          :rtype: :class:`list` (when a list is passed)

          Basic usage:
              from google_bing_trans import Translator
              translator = Translator()
              translator.translate('안녕하세요.')
              <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
              translator.translate('안녕하세요.', dest='ja')
              <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
               translator.translate('veritas lux mea', src='la')
              <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

          Advanced usage:
              translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
              for translation in translations:
              print(translation.origin, ' -> ', translation.text)
              The quick brown fox  ->  빠른 갈색 여우
              jumps over  ->  이상 점프
              the lazy dog  ->  게으른 개
          """
        text = str(text)
        if len(text) >= 5000:
            return "Warning: Can only detect less than 5000 characters"
        if len(text) == 0:
            return ""

        dest = dest.lower().split('_', 1)[0]
        src = src.lower().split('_', 1)[0]

        if dest in LANGUAGES:
            dest_language = LANGUAGES[dest]
        else:
            dest = 'auto'

        if src in LANGUAGES:
            src_language = LANGUAGES[src]
        else:
            src = 'auto'

        data = self._request_data(text, src, dest)
        res = self._send_requests(data)

        if res is not None:
            try:
                for line in res.iter_lines():
                    decoded_line = line.decode('utf-8')
                    if "MkEWBc" in decoded_line:
                        try:
                            response = (decoded_line + ']')
                            response = json.loads(response)
                            response = list(response)
                            response = json.loads(response[0][2])
                            response_ = list(response)
                            response = response_[1][0]
                            if len(response) == 1:
                                if len(response[0]) > 5:
                                    sentences = response[0][5]
                                else:
                                    sentences = response[0][0]
                                tran_text = ""
                                for sentence in sentences:
                                    sentence = sentence[0]
                                    tran_text += sentence.strip() + ' '
                                return tran_text
                            elif len(response) == 2:
                                sentences = []
                                for i in response:
                                    sentences.append(i[0])
                                return sentences
                        except Exception as e:
                            raise e
                        res.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise e