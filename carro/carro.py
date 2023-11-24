class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]= {}
        self.carro = carro
    
    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id" : producto.id,
                "nombreProducto": producto.nombreProducto,
                "cantidad": 1,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] +1
                    break
        self.save()
        
        
    def save(self):
        self.session["carro"] = self.carro
        self.session.modified = True
        
        
    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()
    
    def decrement(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] -1
                    if value["cantidad"]<1:
                        self.remove(producto)    
                    else:
                        self.save()
                    break
                else:
                    print("El Producto no existe en el carrito")
                    
                    
    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True