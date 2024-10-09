# Importing the googletrans library
from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    """
    Translate the text from one language to another using the Google Translator API.
    
    Args:
        text (str): The text to translate.
        source_lang (str): The source language code (e.g., 'en' for English, 'es' for Spanish, 'fr' for French).
        target_lang (str): The target language code (e.g., 'es', 'fr', 'en').
        
    Returns:
        str: The translated text.
    """
    # Create an instance of the Translator class from googletrans
    translator = Translator()

    # Translate the given text from the source language to the target language
    translation = translator.translate(text, src=source_lang, dest=target_lang)

    # Return the translated text as a string
    return translation.text

if __name__ == '__main__':
    # Define the text to translate
    text = str(input("Please enter a text to translate"))

    # Specify the source language (English)
    source_lang = str(input("Please enter a source language 'en' for English, 'es' for Spanish, 'fr' for French"))

    # Specify the target language (Spanish)
    target_lang = str(input("Please enter a target language 'en' for English, 'es' for Spanish, 'fr' for French"))

    # Call the translate_text function to translate the text
    translated_text = translate_text(text, source_lang, target_lang)

    # Print the original and translated texts
    print(f"Original text: {text}")
    print(f"Translated text: {translated_text}")
