# Instalacion



```bash
# Crear un contenedor de docker con MongoDB
docker run --name mongodb-local -d -p 27017:27017 mongo:latest

# crear el entorno de trabajo
python -m venv env

# Activar el entorno de trabajo
./env/Scripts/activate

# Instalar la librerias
pip install -r requirements.txt

#Ejecutar
python index.py

```

## Modelo Entidad-Relación

### Factura
- **InvoiceNo**: Number - Número único de la factura.
- **StockCode**: String - Código de stock del producto.
- **Description**: String - Descripción del producto.
- **Quantity**: Number - Cantidad del producto.
- **InvoiceDate**: DateTime - Fecha y hora de la factura.
- **UnitPrice**: Number - Precio unitario del producto.
- **Country**: String - País de la compra.

### Cliente
- **CustomerID**: String - Identificador único del cliente.
- **Name**: String - Nombre del cliente.
- **Email**: String - Correo electrónico del cliente.
- **Phone**: String - Número de teléfono del cliente.

### Relaciones
- Cada `Factura` está asociada a un único `Cliente` a través del campo `Customer`.