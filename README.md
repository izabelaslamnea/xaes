# XAES — Cifrado y descifrado de archivos

## Descripción

XAES es una herramienta desarrollada en Python que permite cifrar y descifrar datos utilizando el algoritmo de cifrado simétrico AES-128 en modo CBC.

El programa lee los datos desde la entrada estándar y escribe el resultado en la salida estándar, lo que permite utilizarlo desde la terminal y combinarlo con otros comandos.

## Tecnologías utilizadas

- **Python 3**
- **AES-128-CBC** para el cifrado simétrico
- **PBKDF2 con SHA-256** para la derivación de claves
- **PyCryptodome** para las operaciones criptográficas

## Requisitos

- Python 3
- Biblioteca PyCryptodome

Instala la dependencia con:

```bash
python -m pip install pycryptodome
```

## Uso

El programa recibe una opción para indicar si se desea cifrar (`-e`) o descifrar (`-d`), seguida de una contraseña.

### Cifrar un archivo

```bash
python xaes.py -e "mi_contraseña" < archivo.txt > archivo.enc
```

### Descifrar un archivo

```bash
python xaes.py -d "mi_contraseña" < archivo.enc > archivo_recuperado.txt
```

Sustituye los nombres de los archivos por los que quieras utilizar. Para recuperar los datos correctamente, debes utilizar la misma contraseña empleada durante el cifrado.

## Funcionamiento

1. Se genera una sal aleatoria.
2. Se deriva una clave AES de 128 bits y un vector de inicialización a partir de la contraseña y la sal.
3. Los datos se cifran mediante AES en modo CBC, aplicando el relleno necesario.
4. El resultado incluye una cabecera y la sal para permitir la derivación de la clave durante el descifrado.

## Consideraciones de seguridad

Este proyecto tiene fines educativos. AES-CBC no proporciona autenticación ni garantiza por sí solo la integridad de los datos. Para proteger información sensible en aplicaciones reales, se recomienda utilizar un esquema de cifrado autenticado, como AES-GCM, y gestionar las contraseñas de forma segura.

## Autoría

Proyecto académico desarrollado en Python.
