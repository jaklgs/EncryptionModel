class Key:
	def __init__(self, prime_1: int, prime_2: int, relative_prime: int, public_product: int):
		self.prime_1 = prime_1
		self.prime_2 = prime_2
		self.relative_prime = relative_prime
		self.public_product = public_product


class Rsa:
	"""
	Class to encode and decode integer messages via
	the RSA algorithm
	"""
	@staticmethod
	def encode(message, public_key: Key):
		"""Encodes your message into an unreadable format
		that can only be decoded using the private key

		Keyword arguments:

			- message -- The message that is being encoded

			- public_key -- The key that you were given to encode

			- relative_prime -- Comes with the public key (relative prime to the two secret primes)
		"""
		encoded = (message ** public_key.relative_prime) % public_key.public_product
		return encoded

	@staticmethod
	def decode(encoded_message, private_key: Key):
		"""Decodes your encoded message to the original message

		Keyword arguments:

		encoded_message -- The message that is being decoded

			- p1 -- Secret prime number 1

			- p2 -- Secret prime number 2

			- relative_prime -- Number that is relatively prime with p1 and p2
		"""
		totient = (private_key.prime_1 - 1) * (private_key.prime_2 - 1)
		d = 0

		for i in range(int(totient / private_key.relative_prime), totient):
			if private_key.relative_prime * i % totient == 1:
				d = i

		decoded = (encoded_message ** d) % private_key.public_product
		return decoded
