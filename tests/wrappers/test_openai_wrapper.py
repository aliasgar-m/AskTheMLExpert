import os
import unittest

from src.wrappers.openai_wrapper import OpenaiWrapper


class TestOpenAiWrapper(unittest.TestCase):
    def test_response(self):
        """
        """
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            self.fail("OPENAI_API_KEY environment variable not set")

        api_wrapper = OpenaiWrapper(key=api_key)
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": "Say this is a test"}]

        response = api_wrapper.get_chat_response(model=model,
                                                 messages=messages)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
