class TextNormalization:
    def __init__(self,data):
        self.data = data
        self.start()
    def start(self):
        print('''
            1)converting strings to lowercase
            2)removing punctuations
            3)removing special characters
            4)handling emoji
            5)removing extra spaces
            6)expanding words and abbrevations
            7)correcting words
            ''')
    def lower_case(self,data):
        data = data.lower()
        return data
    def punctuations(self):
        ch = self.data
        import string
        punctuations = string.punctuation
        for ch in punctuations:
            chrs = ch.replace(ch," ")
        self.data = chrs
    def special_characters(self):
        chars = self.data
        for ch in chars:
            if not ch.isalnum() and not ord(ch)==32:
                chars = chars.replace(ch," ")
        self.data = chars
    def handling_emoji(self):

obj = TextNormalization()