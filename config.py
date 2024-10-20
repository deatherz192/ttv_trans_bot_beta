######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
Twitch_Channel          = ''

Trans_Username          = ''
Trans_OAUTH             = 'oauth:'

#######################################################
# OPTIONAL CONFIGS ####################################
Trans_TextColor         = 'HotPink'
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

lang_TransToHome        = 'ru'
lang_HomeToOther        = 'ru'

Show_ByName             = True
Show_ByLang             = True

Ignore_Lang             = ["tt", "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-CN", "zh-TW", "co",
                "hr", "cs", "da", "nl", "eo", "et", "tl", "fi", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha",
                "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky",
                "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa",
                "pl", "pt", "ma", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "su", "sw",
                "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]
Ignore_Users            = ['Nightbot']
Ignore_Line             = ['http', '.com', '.ru' '⣿', '░', '▓']
Delete_Words            = ['+', '-']

# Any emvironment, set it to `True`, then text will be read by TTS voice!
# TTS_In:User Input Text, TTS_Out:Bot Output Text
TTS_In                  = False
TTS_Out                 = False
TTS_Kind                = "gTTS" # You can choice "CeVIO" if you want to use CeVIO as TTS.
# CeVIO_Cast            = "さとうささら" # When you are using CeVIO, you must set voice cast name.
TTS_TextMaxLength = 0
TTS_MessageForOmitting = ''

# if you make TTS for only few lang, please add langID in the list
# for example, ['ja'] means Japanese only, ['ko','en'] means Korean and English are TTS!
ReadOnlyTheseLang       = []

# Select the translate engine ('deepl' or 'google')
Translator              = 'deepl'

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = 'https://script.google.com/macros/s/AKfycbyAlFZooSCW7MpzRCmnX4HueuTeS4nVg7gWMG8yPINrZDl89VSSe-UblitZ4AMhYU9F/exec'

# Enter the suffix of the Google Translate URL you normally use.
# Example: translate.google.co.jp -> 'co.jp'
#          translate.google.com   -> 'com'
GoogleTranslate_suffix  = 'com'

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = True
