# translation_google_bing
###free Bing and Google translation API


####trans-google-bing
Version 0.0.2
A free and unlimited python API for google translate.
It's very easy to use and solve the problem that the old api which use tk value cannot be used.
This interface is for academic use only, please do not use it for commercial use.

Version 0.0.2 have fixed url translate. Ps: If your get translations for different genders, it will return a list. https://support.google.com/translate/answer/9179237?p=gendered_translations&hl=zh-Hans&visit_id=637425624803913067-1347870216&rd=1

####Installation
```pip install trans-google-bing```
####Basic Usage of Google Translation
#####Translate
```python
from google_bing_trans import Google_translator 
translator = Google_translator()
text = translator.translate('你好', dest='en')
print(text)

-> Hello
```


####Advanced Usage
#####Translate
```python
from google_bing_trans import Google_translator 
```

##### You can set the service_url according to your needs. for example: service_url= "translation.google.com"
#####  it is default "translation.google.cn" if you not to set service_url
```python 
translator = Translation(service_url = "translation.google.com")  
```
# <Translate text="hello" dest=en src=zh>  
#####  default parameter : dest=auto src=auto 
#####  For src param is not to set, because API can automatically identify the src translation language
```python
from google_bing_trans import Google_translator
translator = Google_translator()
text = translator.translate('你好', dest='en')
print(text)
-> hello
```
#####Detect
```python
from google_bing_trans import Google_translator

detector = Google_translator() 
text = detector.detect("こんにちは")
print(text)

-> ['ja', 'japanese']
```
---
####Basic Usage of Bing Translation
#####Translate
```python
from google_bing_trans import bing_translator 
translator = bing_translator()
text = translator.translator('你好', to='en')
print(text)

-> Hello
```

#####Detect
```python
from google_bing_trans import bing_translator

detector = bing_translator() 
text = detector.detect("こんにちは")
print(text)

-> 'ja'
```

Prerequisites
Python >=3.6
requests

