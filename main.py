from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

import jwt

payload = {
    'user_id': 1,
    'user_name': 'Rick Grimes',
    'user_email': 'rickgrimes@gmail.com',
    'message': "We're The Ones Who Live"
}

secret = serialization.load_pem_private_key(
    open('jwt-key', 'rb').read(),
    password=None,
    backend=default_backend()
)


# PARTE 1 -- Generar un JWT firmado
encoded_jwt = jwt.encode(payload, secret, algorithm='RS256')

print("JWT Generado:\n", encoded_jwt)



# PARTE 2 -- Verificar el JWT
print("\nExtraccion de la informacion del JWT:")

public = serialization.load_pem_public_key(
    open('jwt-key.pub', 'rb').read(),
    backend=default_backend()
)


try:
    decoded_payload = jwt.decode(encoded_jwt, public, algorithms=['RS256'])
    print(decoded_payload)
except jwt.ExpiredSignatureError:
    print("El token ha expirado")
except jwt.InvalidTokenError:
    print("El token no es valido")



