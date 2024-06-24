#Leer el excel INVENTARIO_TALLA.xlsx e imprimir el contenido de la hoja de calculo "hoja 1"
import openpyxl
import utils

#Cargar el archivo excel
archivo = openpyxl.load_workbook('./VENTAS.xlsx')
hoja = archivo['OnlineRetail']

listaFilas = list(hoja.iter_rows())

listaObjetosFormateada = []
#Recorrer las filas de la hoja de calculo
for fila in listaFilas[1:len(listaFilas)]:
    #InvoiceNo	StockCode	Description	Quantity	InvoiceDate	UnitPrice	Country	CustomerID
    objetoCeldas = {
        "InvoiceNo": fila[0].value,
        "StockCode": fila[1].value,
        "Description": fila[2].value,
        "Quantity": fila[3].value,
        "InvoiceDate": fila[4].value,
        "UnitPrice": fila[5].value if type(fila[5].value) != str else utils.formatNumber(fila[5].value),
        "Country": fila[6].value,
        "Customer": utils.customer(fila[7:11])
    }
    listaObjetosFormateada.append(objetoCeldas)

utils.save_in_db(listaObjetosFormateada)