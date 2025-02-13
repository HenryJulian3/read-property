# read-property

Este proyecto es una utilidad para leer propiedades de objetos en JavaScript de manera segura y eficiente, incluso cuando las propiedades están profundamente anidadas.

## 🚀 Características

- Accede a propiedades de objetos anidados utilizando una cadena de ruta.
- Devuelve el valor de la propiedad si existe.
- Devuelve `undefined` si la propiedad no existe o si el argumento proporcionado no es un objeto.

## 📦 Instalación

1. Clona el repositorio:

   ```sh
   git clone https://github.com/HenryJulian3/read-property.git
   cd read-property
   ```

2. Instala las dependencias:

   ```sh
   npm install
   ```

## 🛠 Uso

1. Importa la función en tu proyecto:

   ```javascript
   const readProperty = require('read-property');
   ```

2. Utiliza la función para leer una propiedad anidada:

   ```javascript
   const obj = {
     n: {
       p: {
         m: true
       }
     }
   };

   const value = readProperty('n.p.m', obj);
   console.log(value); // true
   ```

## 📋 Notas

- Si intentas leer una propiedad que no existe, la función devolverá `undefined`.
- Si el argumento proporcionado no es un objeto, la función también devolverá `undefined`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT.
