import hashlib
import itertools

salt = ".-.s3gur1lab:-)" # Salt entregado

hashes = [
    "d46f28fd97ca6fe5aaab0f907227b12c",
    "c201f766abb974a2fce3093cbbdb42b7",
    "fee054093f9d3735142f5da1abb30681",
    "ea6f893319cc05683c828770bea3ce07"
] # Hashes entregados

letras = "abcdefghijklmnopqrstuvwxyz"
contrasenas_encontradas = []
combinaciones = [''.join(p) for p in itertools.product(letras, repeat=4)]



# Calcular el hash MD5 para cada combinación con el salt y comparar con los hashes dados
for contrasena in combinaciones:
    contrasena_con_salt = contrasena + salt
    hash_md5 = hashlib.md5(contrasena_con_salt.encode()).hexdigest()
    if hash_md5 in hashes:
        contrasenas_encontradas.append((contrasena, hash_md5))

print("Contraseñas encontradas:")
for contrasena, hash_encontrado in contrasenas_encontradas:
    print(f"Contraseña: {contrasena}, Hash: {hash_encontrado}")