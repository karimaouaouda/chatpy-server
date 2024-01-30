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
                {
                    "role": "user",
                    "content": self.message}
            ]
        )

        self.ready = True

    def content(self):
        print(self.response.choices)
        return self.response.choices.pop(0).message.content