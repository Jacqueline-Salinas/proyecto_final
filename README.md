# Jacqueline Salinas - Proyecto Final

## Descripción del Proyecto

Este proyecto Django se compone de varias aplicaciones organizadas de la siguiente manera:

### Aplicaciones:
1. **Config**: Aplicación predeterminada de Django usada para la configuración del proyecto.
2. **Core**: Aplicación principal que contiene la estructura base y plantillas, como `base.html`.
3. **Producto**:
    - Incluye tres modelos fundamentales:
        - `Producto`: Define los productos disponibles con detalles como nombre, precio, descripción y proveedor.
        - `Proveedor`: Gestiona la información de los proveedores asociados a los productos.
        - `Stock`: Controla la cantidad disponible de cada producto.
    - Formularios para cada modelo, permitiendo el ingreso y la gestión de información de manera eficiente.
    - Implementación de un formulario de búsqueda que filtra los productos según el nombre.
    - Se requiere la instalación adicional de la librería Pillow==10.1.0 para habilitar la funcionalidad de carga de imágenes en los formularios de productos. Esto puede realizarse con el comando `pip install Pillow`.
4. **Cliente**:

    - `Registro`: Formulario para que los usuarios puedan registrarse en la plataforma.
    - `Login`: Interfaz de inicio de sesión para los usuarios existentes.
    - `Restricción`: de acceso a ciertas URL para usuarios autenticados.

### Datos de Muestra:
Se han incluido datos de muestra para que puedas revisar y evaluar la funcionalidad de la aplicación.
usuario de muestra:
admin -- clave: 123 

user -- clave: prueba123

### Uso de pagina:
Al entrar a la pagina por primera vez se veran cargados algunos productos, primero debemos hacer login con la cuenta de administrador (admin - 123) debemos apretar productos en el navbar, en esa ruta se encuentran los formularios para ingresar datos a nuestros 3 modelos y tambien esta el formulario de busqueda.

En el formulario producto debemos ingresar (ademas de nombre, precio, descripcion y proveedor) una imagen para que aparezca en nuestro home principal.
---
Como cliente solo es posible visualizar la pantalla inicial, donde se visualiza la imagen y el precio de producto. Como una funcionalidad posterior para habilitar en la pagina seria el carrito de compras y el cliente puede ir agregando los productos para posteriormente hacer la compra.

