from dydx3 import Client
from dydx3 import private_key_to_public_key_pair_hex
from dydx3.constants import *
from web3 import Web3

ETHEREUM_ADDRESS = ''  # your ethereum address
ETHEREUM_SECRET = ''  # your ethereum secret key
COUNTRY = ''  # your country
AffiliateLink = ''  # if you have

WEB_PROVIDER_URL = 'http://localhost:8545'
client = Client(
        network_id=NETWORK_ID_ROPSTEN,
        host=API_HOST_ROPSTEN,
        web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
        default_ethereum_address=ETHEREUM_ADDRESS,
        eth_private_key=ETHEREUM_SECRET
        )

stark_private_key = client.onboarding.derive_stark_key()
client.stark_private_key = stark_private_key
public_x, public_y = private_key_to_public_key_pair_hex(stark_private_key)
print('Your private stark key', stark_private_key)
print('Your public stark key: X', public_x)
print('Your public stark key: Y', public_y)

onboarding_information = client.onboarding.create_user(
        stark_public_key=public_x,
        stark_public_key_y_coordinate=public_y,
        ethereum_address=ETHEREUM_ADDRESS,
        referred_by_affiliate_link=AffiliateLink,
        country=COUNTRY,
        )

print(onboarding_information)
