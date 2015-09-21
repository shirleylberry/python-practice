import webapp2
import cgi
import string

form = """
    <form method = "post">
        Enter some text to Rot13:
        <br>
        <label> Month
            <input type = "text" name = "text" value = "%(text)s">
        </label>
        <div style = "color: red">%(error)s</div>
        <input type = "submit">
    </form>
"""

class Rot13Handler(webapp2.RequestHandler):
    def write_form(self, error = "", text = ""):
        self.response.out.write(form % {"error": error,
                                        "text" : cgi.escape(text, quote = True),})

    def rot13(self, orig_text):
        new_text = ""
        alphabet = list(string.ascii_lowercase)
        orig_text.lower()
        for letter in orig_text:
            if letter in alphabet:
                orig_index = alphabet.index(letter)
                new_index = (orig_index + 13) % 26
                new_letter = alphabet[new_index]
                new_text += new_letter
            else:
                new_text += letter
        return new_text


    def get(self):
        self.write_form(error = "", text = "")

    def post(self):
        orig_text = self.request.get('text')
        text = self.rot13(orig_text)
        self.response.out.write(text)

