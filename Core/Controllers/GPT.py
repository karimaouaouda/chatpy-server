from openai import OpenAI

API_KEY = "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"


class GPT:
    def __init__(self, **kwargs):
        self.message = "hello"

        self.client = OpenAI(api_key=API_KEY)

        self.message = kwargs['message']

        self.response = None

        self.ready = False

        self.send()

    def send(self):
        self.response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an assistant psychotherapist, skilled in dealing with people according to their psychological state."},
                {"role": "user", "content": self.message}
            ]
        )

        self.ready = True

    def content(self):
        print(self.response.choices)
        return self.response.choices.pop(0).message.content
