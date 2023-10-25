## Buscador de Contraseñas por Fuerza Bruta

Script para encontrar contraseñas mediante un ataque de fuerza bruta utilizando el algoritmo de hash MD5.

El programa genera todas las combinaciones posibles de cuatro caracteres ASCII imprimibles y aplica un salto (salt) a cada combinación para calcular el hash MD5. Luego, compara los hashes resultantes con una lista predefinida de hashes entregados para encontrar coincidencias.

## Requisitos

No se requieren bibliotecas adicionales. El módulo hashlib se utiliza para calcular los hashes MD5 y itertools para generar las combinaciones.
## Uso

- El programa generará todas las combinaciones posibles de cuatro caracteres ASCII imprimibles y calculará el hash MD5 de cada combinación con el salt proporcionado.
- Comparará los hashes resultantes con la lista predefinida de hashes entregados.
- Si se encuentra una coincidencia, mostrará la contraseña correspondiente y el hash MD5.