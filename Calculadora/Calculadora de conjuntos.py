import tkinter as tk
from tkinter import messagebox

class Operadores:
    def __init__(self):
        self.A = set()
        self.B = set()

    def conjunto_conjunto (self):
            self.A = self.leer_conjunto("A")
            self.B = self.leer_conjunto("B")

    def leer_conjunto (self, nombre):
            valores= input(f"Ingrese los datos del conjunto {nombre} separados por comas ")
            return set(map(int, valores.split(",")))
        
    def union(self):
            resultado = set()
            for elemento in self.A: 
                resultado.add(elemento)
            for elemento in self.B:
                resultado.add(elemento)
            return resultado
        
    def interseccion(self):
            resultado = set()
            for elemento in self.A:
                if elemento in self.B:
                 resultado.add(elemento)
            return resultado
        
    def diferencia(self):
            resultado = set()
            for elemento in self.A:
                if elemento not in self.B:
                    resultado.add(elemento)
            return resultado
        
    def cont (self, conjunto, elemento):
            return elemento in conjunto 

    def dif_simetrica (self):
            res = set()
            for x in self.A:
                if not self.cont(self.B,x) and x not in res:
                    res.add(x)
            for y in self.B:
                if not self.cont(self.A,y) and y not in res:
                    res.add(y)
            return res
    
    def disyuntiva (self):
     for x in self.A:
          if self.cont (self.B,x):
               return False
     return True
    
    def prod_simetrico (self):
     res = set()
     for x in self.A:
          for y in self.B:
               par= (x,y)
               if par not in res:
                    res.add(par)
     return res
    
class LectorConjuntos:
    def leer_conjunto(self, valores_str):
        try:
            if not valores_str.strip():
                return set()
            
            numeros = [int(x.strip()) for x in valores_str.split(",") if x.strip()]
            return set(numeros)
        except ValueError:
            raise ValueError("Ingresa solo números separados por comas")

class InterfazConjuntos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Conjuntos")
        self.geometry("600x500")
        
        self.lector = LectorConjuntos()
        self.operadores = Operadores() 
        self.crear_componentes()
    
    def crear_componentes(self):
        tk.Label(self, text="CALCULADORA DE CONJUNTOS", 
                font=("Arial", 16, "bold"), fg="blue").pack(pady=15)
        
        #Conjuntos
        frame_a = tk.Frame(self)
        frame_a.pack(pady=10)
        tk.Label(frame_a, text="Conjunto A:", font=("Arial", 12, "bold")).pack()
        tk.Label(frame_a, text="Ingresa números separados por comas (ej: 1,9,20,53,411)").pack()
        self.entry_a = tk.Entry(frame_a, width=50, font=("Arial", 10))
        self.entry_a.pack(pady=5)

        frame_b = tk.Frame(self)
        frame_b.pack(pady=10)
        tk.Label(frame_b, text="Conjunto B:", font=("Arial", 12, "bold")).pack()
        tk.Label(frame_b, text="Ingresa números separados por comas (ej: 2,8,19,50,400)").pack()
        self.entry_b = tk.Entry(frame_b, width=50, font=("Arial", 10))
        self.entry_b.pack(pady=5)
        
        #Botones
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=15)
        
        botones_fila1 = [
            ("UNIÓN", self.calcular_union, "lightgreen"),
            ("INTERSECCIÓN", self.calcular_interseccion, "lightblue"),
            ("DIFERENCIA A-B", self.calcular_diferencia, "lightyellow")
        ]
        for i, (texto, comando, color) in enumerate(botones_fila1):
            tk.Button(frame_botones, text=texto, command=comando, 
                     bg=color, width=15).grid(row=0, column=i, padx=5, pady=5)
        
        botones_fila2 = [
            ("DIF. SIMÉTRICA", self.calcular_dif_simetrica, "lightcoral"),
            ("¿DISYUNTIVOS?", self.verificar_disyuntivos, "lightpink"),
            ("PROD. CARTESIANO", self.calcular_producto, "lightgray")
        ]
        for i, (texto, comando, color) in enumerate(botones_fila2):
            tk.Button(frame_botones, text=texto, command=comando, 
                     bg=color, width=15).grid(row=1, column=i, padx=5, pady=5)
        
        #Resultados
        self.frame_resultados = tk.Frame(self)
        self.frame_resultados.pack(pady=15, fill=tk.BOTH, expand=True)
        
        tk.Label(self.frame_resultados, text="RESULTADOS:", 
                font=("Arial", 12, "bold"), fg="blue").pack()
        
        self.texto_resultados = tk.Text(self.frame_resultados, height=15, width=60,
                                      font=("Consolas", 9), bg="white")
        self.texto_resultados.pack(pady=5)
    
    def obtener_conjuntos(self):
        try:
            str_a = self.entry_a.get()
            str_b = self.entry_b.get()
            
            self.operadores.A = self.lector.leer_conjunto(str_a)
            self.operadores.B = self.lector.leer_conjunto(str_b)
            return True
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False
    
    def mostrar_resultado(self, titulo, resultado):
        self.texto_resultados.delete(1.0, tk.END)
        self.texto_resultados.insert(tk.END, f"=== {titulo} ===\n\n")
        self.texto_resultados.insert(tk.END, f"Resultado: {resultado}\n\n")
        if isinstance(resultado, bool):
            self.texto_resultados.insert(tk.END, f"Respuesta: {'SÍ' if resultado else 'NO'}")
        
    def calcular_union(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.union()
            self.mostrar_resultado("Unión A y B", resultado)
    
    def calcular_interseccion(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.interseccion()
            self.mostrar_resultado("Intersección A y B", resultado)
    
    def calcular_diferencia(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.diferencia()
            self.mostrar_resultado("Diferencia A y B", resultado)
    
    def calcular_dif_simetrica(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.dif_simetrica()
            self.mostrar_resultado("Diferencia Simétrica", resultado)
    
    def verificar_disyuntivos(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.disyuntiva()
            self.mostrar_resultado("¿Son conjuntos disyuntivos?", resultado)
    
    def calcular_producto(self):
        if self.obtener_conjuntos():
            resultado = self.operadores.prod_simetrico()
            self.mostrar_resultado("Producto cartesiano A y B", resultado)

# Ejecutar la aplicación
if __name__ == "__main__":
    app = InterfazConjuntos()
    app.mainloop()