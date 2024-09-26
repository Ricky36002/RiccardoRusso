
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAwc9uIwmdNbFUMB797+C73/QATMflxFfljonKo6QKmZJ0U2zq\nbYJCOug+eghb3Lehf97Ik+gjHUZbc3sy1WztDFreiRIVx8Z6jfo1IlH1Pcn3/4PB\nr3cU7JDNMUNV4VaVn75QJVveUIJ5YptN7oZGUZkI4AShPv5hIpSygLF1UJYZ2xK6\nUeGGnIkVdtECIBeCRHnKrcv0XgIL5fvMcsqRupTSmo/oBc8rajJ/QjGx/If8nIfN\nn1PmKsv5s/GeThFe5iOLPX3PMr19bdUlNCjhFfjx9DURZgmkiXxjK3xMdYLKqUKQ\npx3TJkaEwF04zzCedytc9iaXxE98s+bqMXPkIQIDAQABAoIBAC4mrP1e7ra4cWm8\nF5AlnddojSG7gDVPEPTuTvjEuVl0jIrJJtHI8OiCIU6B6w4WFDkU3gKKhsIT3PcU\n4Tf9Zj1I7jEJw3H9C3X/nON9TL7X91w7DcYwvyTOHm6asDqmmZ6efQtIYxoc17bp\ncJdaFiicHobp01Pi01KewhrvJxZ3HS4vwT75aF544Q9caK1eQeVZ990QyCQjVL5w\nRqrPPThHopxvYt7xxqX+9IyJdt32EzA+zwDobzhQZ0Ji1h5OxQqy5VBuFgMFVVRR\nWefwSNOlr0uw/kt3kjK9U3ivGoOK0tm+u05owMhMqJqku8VI4DbobbvQDUfpBrR4\nEJgrkzkCgYEAyNvzdNe5QoAcE9Y1q1Tozt6TVxrFGW0phkqmpeRn4fSHvx+xw766\nPqhY6WPc8o2qtNCKMHUCoKhExW3eCQ/we8wvypOC9wl3HLxdVqotoejqRvtJdObW\nhIRYzD1enOKz83g2dxRrez7kUuaCdHSpBtCAnjwDMhuaPSicVpxKvAMCgYEA9wQX\n9uxRav2IeWexnW7HsjDJVLfLOTcxz35x562vjhZ7ZPk+aVU2GazLNOWMbrwtWH2l\nPeVU6T3mc9etJgFSJHairx9xJHRI1SJZSrIaNHLuAi+bO3GNx144YuWLLc7CRMse\nt7A5CHVrCb0G/DmlQknXx500iaZfpG/JIcSp8AsCgYEAuW/fd3sGTa/qvCGi0PgG\nK57vlpZfa5cNpC7dZgDWK5TPkpMXUimO1vQjie2pecFy3ZY+TnhooZxYSZGiUOmH\nUzPy12qSmbICZuQ8pBtfH8DiMgAjFCtd12A8fusVo2/lRR0x44RVqqYos6SewhdG\nScVLSUsMhEFZh6crlwaaNLMCgYAcYpkKY++bNtU29kZ/y9ogzOBl3tT4lzIfIO2f\n7OKOlmDJoqacXhFgc+3J/1La6r7fO1kAuti+EMHpr/ASvPYegI+DRj6vLLmt3Euc\nfMjsHATjtWrGMu9S6K3cF3qd4fOLCjhWbWawZSXOsa0a0Nj/vBKSuqrt4nN9Juda\n/Ql2LwKBgQC/27ND0WqgE2GI8sD/II1BTgGqGP+ATUeKZbZ5ZONO00He2MTs3PIV\nQD1iu6hzbj2UGzl+ZyCQcIZyu0AxOpdR3QB4Fip3KCtgKVNCUR1xGonQdwaIqLhc\nOnMAuDNUOsx3+FIIAGLEzNX8jgMlU8Q8IxOt9vcQr7jxHuO7KRrVXA==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwc9uIwmdNbFUMB797+C7\n3/QATMflxFfljonKo6QKmZJ0U2zqbYJCOug+eghb3Lehf97Ik+gjHUZbc3sy1Wzt\nDFreiRIVx8Z6jfo1IlH1Pcn3/4PBr3cU7JDNMUNV4VaVn75QJVveUIJ5YptN7oZG\nUZkI4AShPv5hIpSygLF1UJYZ2xK6UeGGnIkVdtECIBeCRHnKrcv0XgIL5fvMcsqR\nupTSmo/oBc8rajJ/QjGx/If8nIfNn1PmKsv5s/GeThFe5iOLPX3PMr19bdUlNCjh\nFfjx9DURZgmkiXxjK3xMdYLKqUKQpx3TJkaEwF04zzCedytc9iaXxE98s+bqMXPk\nIQIDAQAB\n-----END PUBLIC KEY-----"
sPubGioele= "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqhHBI8P5uzFToYd7tgtt\nT0WajjRK+WNnDsyZuw4KEm6RW9AzQod5Qu9tHH1+5QW7vwpXkwhDtoDhp7t5d0mW\nrVLn29uqkiFxIFW7d5W/ixARdT/e8aji4poNLwGiE7o2PKhfLRulP2854TkeyGFW\ny5bACKSQOQOVVgCt7n6mHwILS2351CycnIF0ngeKFN/okKgZKzIk5ThqfjQp49JS\nmHehqRxs9GfdLJGRR9rDUPF0odm98EBk/zqtUbAeyt2XZNHxlgaNYBSJqFa7wny1\nnZalwhsU5MPagPHkw/upTg4qQLFTdePpOBuwFkw3RHMgmFWytxWrP5Jmky26WKfU\neQIDAQAB\n-----END PUBLIC KEY-----"
# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key = RSA.import_key(sPubGioele)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# # Example usage
message = "devo fare la Cacca!"
encrypted_message = encrypt_message(message, public_key)

# print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)
# encrypted_message = "N+0mODRS66ihma14IYaxAyvW+vx8pUdfmgG4nH5ac/2Wp4/P4HRdFa96GGuSSKHdo4p+cx5svRZgxLApcrwhHPVoFD47r2/aL/ax8cQKl4BAGp6xtW3nlj2wonINdjNwuvKjmdVmRIG0YoS262y1J19OZFq93GkpRBaxdBSiNE2HZrFXhdZbfSKcpDHMPB4p8BpMmotZ6ZOLhG0b+C+y1rfkJjpI3xSMtlA0+YliiQbOjt2BrCn8GDHg1AjWdhhi6db6dhpqVRFq1HuazZ5spN3d3+ZcdfOT4o+rLTwe315qEoteLV/5GY+4saHEdEcTUHf4Zmmc2twAcktEGL9wUA=="
# decrypted_message = decrypt_message(encrypted_message, key_pair)
# print("Decrypted Message:", decrypted_message)

