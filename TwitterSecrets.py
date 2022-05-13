CONSUMER_KEY = "GviHro8BFbnOwOJqF4SN1vkaW"
CONSUMER_SECRET = "1zIRxMuvb2wPmgj2ZdJFldtwVVc2ZxmsQOzo2MfH00xmK7xoRY"

ACCESS_TOKEN = "1170682735825842176-eyAX74a3TcNEwHbUBRb55rjgoXC9zT"
ACCESS_SECRET = "7oO02Z9XeK4iabLIUyjzqmkDPgHzmXCNZTaa6UN1B5c8L"

class TwitterSecrets:
	def __init__(self):
		self.CONSUMER_KEY = CONSUMER_KEY
		self.CONSUMER_SECRET = CONSUMER_SECRET
		self.ACCESS_TOKEN = ACCESS_TOKEN
		self.ACCESS_SECRET = ACCESS_SECRET

		for key, secret in self.__dict__.items():
			assert secret != "", f"Please provide a valid secret for: {key}"

twitter_secrets = TwitterSecrets()
