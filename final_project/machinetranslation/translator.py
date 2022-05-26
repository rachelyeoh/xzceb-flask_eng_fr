"""
This module contains the method to translate from one language to another
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

# Translator Instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=(VERSION),
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    "This function is to translate english to french"
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    return frenchText.get('translations')[0].get('translation')


def frenchToEnglish(frenchText):
    "This function is to translate french to english"
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))
    return englishText.get('translations')[0].get('translation')
