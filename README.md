# Jacqueline Salinas - Pre-Entrega N° 3

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

### Datos de Muestra:
Se han incluido datos de muestra para que puedas revisar y evaluar la funcionalidad de la aplicación.

---