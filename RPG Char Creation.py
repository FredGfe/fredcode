import sys
import time

# --- MÓDULO DE DATOS ---

clases_disponibles = {
    "Guerrero": {
        "descripcion": "Especialista en combate cuerpo a cuerpo, alta vitalidad.",
        "stats_base": {"fuerza": 10, "inteligencia": 3, "destreza": 5, "vida_maxima": 150}
    },
    "Mago": {
        "descripcion": "Maestro de las artes arcanas, frágil pero poderoso.",
        "stats_base": {"fuerza": 2, "inteligencia": 12, "destreza": 4, "vida_maxima": 80}
    },
    "Pícaro": {
        "descripcion": "Experto en sigilo y ataques rápidos.",
        "stats_base": {"fuerza": 5, "inteligencia": 5, "destreza": 12, "vida_maxima": 100}
    }
}

razas_disponibles = {
    "Humano": {"bono": ("fuerza", 1), "descripcion": "Versátiles y ambiciosos."},
    "Elfo": {"bono": ("destreza", 2), "descripcion": "Ágiles y longevos, conectados con la naturaleza."},
    "Enano": {"bono": ("vida_maxima", 20), "descripcion": "Tenaces y resistentes, maestros de la forja."}
}

# --- CLASES DEL SISTEMA (Lógica de Negocio/Juego) ---

class Personaje:
    """Representa un personaje único en el mundo RPG."""
    
    def __init__(self, nombre, raza, clase):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        
        # Inicializar estadísticas básicas de la clase
        base_stats = clases_disponibles[clase]["stats_base"]
        self.fuerza = base_stats["fuerza"]
        self.inteligencia = base_stats["inteligencia"]
        self.destreza = base_stats["destreza"]
        self.vida_maxima = base_stats["vida_maxima"]
        
        # Aplicar el modificador racial
        self._aplicar_bono_raza()
        self.vida_actual = self.vida_maxima

    def _aplicar_bono_raza(self):
        """Aplica el bono estático de la raza elegida (Método Privado)."""
        stat_a_mejorar, cantidad = razas_disponibles[self.raza]["bono"]
        
        # Uso de setattr para modificar el atributo dinámicamente
        valor_actual = getattr(self, stat_a_mejorar)
        setattr(self, stat_a_mejorar, valor_actual + cantidad)

    def mostrar_ficha(self):
        """Imprime una ficha formateada del personaje."""
        print("\n" + "="*30)
        print(f" FICHA DE PERSONAJE: {self.nombre.upper()} ")
        print("="*30)
        print(f"Raza:  {self.raza}")
        print(f"Clase: {self.clase}")
        print("-" * 30)
        print(f" HP:  [{self.vida_actual}/{self.vida_maxima}]")
        print(f" STR: {self.fuerza}")
        print(f" INT: {self.inteligencia}")
        print(f" DEX: {self.destreza}")
        print("="*30 + "\n")


# --- FUNCIONES DE INTERFAZ DE USUARIO (CLI) Y VALIDACIÓN ---

def imprimir_lento(texto, velocidad=0.03):
    """Efecto de escritura dramática para la consola."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def seleccionar_opcion(opciones_dict, tipo_seleccion):
    """
    Función genérica para validar la selección del usuario
    sobre un diccionario de opciones numéricas.
    """
    opciones_lista = list(opciones_dict.keys())
    
    while True:
        print(f"\n--- Selecciona tu {tipo_seleccion} ---")
        for i, opcion in enumerate(opciones_lista, 1):
            desc = opciones_dict[opcion].get("descripcion", "")
            print(f"{i}. {opcion}: {desc}")
            
        seleccion = input(f"\nIntroduce el número de {tipo_seleccion}: ")
        
        # Validación de Entrada
        if seleccion.isdigit():
            indice = int(seleccion) - 1
            if 0 <= indice < len(opciones_lista):
                return opciones_lista[indice]
        
        print("❌ Selección inválida. Por favor, inténtalo de nuevo.")


def menu_principal():
    """Flujo principal de la creación de personajes."""
    imprimir_lento("⚔️  BIENVENIDO AL CREADOR DE LEYENDAS RPG v1.0 ⚔️", 0.05)
    
    # 1. Entrada de Nombre (Validación básica)
    while True:
        nombre = input("\nIntroduce el nombre de tu héroe/heroína: ").strip()
        if len(nombre) >= 3 and nombre.replace(' ', '').isalpha():
            break
        print("❌ El nombre debe tener al menos 3 letras y no contener números o caracteres especiales.")

    # 2. Selección de Raza
    raza_elegida = seleccionar_opcion(razas_disponibles, "Raza")
    print(f"✅ Has elegido ser un {raza_elegida}.")

    # 3. Selección de Clase
    clase_elegida = seleccionar_opcion(clases_disponibles, "Clase")
    print(f"✅ Te has convertido en un {clase_elegida}.")

    # 4. Creación e Instanciación del Objeto
    imprimir_lento("\nForjando el destino de tu personaje...", 0.06)
    nuevo_heroe = Personaje(nombre, raza_elegida, clase_elegida)
    
    # 5. Resultado Final
    imprimir_lento("\n¡Tu personaje está listo para la aventura!", 0.04)
    nuevo_heroe.mostrar_ficha()


# --- PUNTO DE ENTRADA DEL SCRIPT ---
if __name__ == "__main__":
    menu_principal()