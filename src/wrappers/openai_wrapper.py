from openai import OpenAI


class OpenaiWrapper:
    """ Wrapper encapsulating OpenAi's chat completion api for testing.

    Attributes:
        client (:obj:`OpenAI`): OpenAI class object with access to APIs.

    """
    def __init__(self, key: str) -> None:
        """Sets up a new OpenAI class object allowing access to the api.

        Args:
            key (str): OpenAI api access key.

        Returns:
            None
        """
        self.client = OpenAI(api_key=key)

    def get_chat_response(self, model, messages) -> dict:
        """Generates a response from the selected OpenAI model.

        Args:
            model (str): Name of the model to be used.
            messages (list): Messages to be sent to the model prior to
                generation.

        Returns:
            The dictionary containing the response of the model.
        """
        return self.client.chat.completions.create(
            model=model,
            messages=messages)
