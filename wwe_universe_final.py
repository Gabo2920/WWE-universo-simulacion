import json
import os
from datetime import datetime

class WWEUniverse:
    def __init__(self):
        self.archivo = "wwe_datos.json"
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.datos = json.load(f)
            if "luchadores" not in self.datos:
                self.datos["luchadores"] = []
            if "campeonatos" not in self.datos:
                self.datos["campeonatos"] = self.crear_campeonatos()
            print("\n✓ Datos cargados del archivo")
        else:
            self.datos = {}
            self.datos["luchadores"] = []
            self.datos["campeonatos"] = self.crear_campeonatos()
            print("\n✓ Nueva base de datos creada")
            
    def crear_campeonatos(self):
        campeonatos = {}
        campeonatos["RAW"] = [
            {"nombre": "Campeonato Mundial", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Intercontinental (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Intercontinental (M)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato en Parejas (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Mundial de Mujeres", "campeon": None, "dias": 0},
            {"nombre": "Money in the Bank (H)", "campeon": None, "dias": 0}
        ]
        campeonatos["SmackDown"] = [
            {"nombre": "Campeonato WWE", "campeon": None, "dias": 0},
            {"nombre": "Campeonato WWE Femenino", "campeon": None, "dias": 0},
            {"nombre": "Campeonato en Parejas (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato de Estados Unidos (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato de Estados Unidos (M)", "campeon": None, "dias": 0},
            {"nombre": "Money in the Bank (M)", "campeon": None, "dias": 0}
        ]
        campeonatos["Compartido RAW/SD"] = [
            {"nombre": "Campeonato en Parejas Femenino", "campeon": None, "dias": 0}
        ]
        campeonatos["NXT"] = [
            {"nombre": "Campeonato NXT", "campeon": None, "dias": 0},
            {"nombre": "Campeonato NXT Femenino", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Norteamericano (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Norteamericano (M)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato en Parejas (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Speed (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Speed (M)", "campeon": None, "dias": 0}
        ]
        campeonatos["AAA"] = [
            {"nombre": "Mega Campeonato", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Latinoamericano", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Mundial en Parejas (H)", "campeon": None, "dias": 0},
            {"nombre": "Campeonato Mundial Peso Crucero", "campeon": None, "dias": 0},
            {"nombre": "Reina de Reinas", "campeon": None, "dias": 0}
        ]
        return campeonatos
    def guardar_datos(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("🎮 WWE 2K26 - UNIVERSE MODE")
            print("-"*50)
            print("1. 📺 Gestionar Marcas")
            print("2. 👤 Gestionar Luchadores")
            print("3. 🏆 Gestionar Campeonatos")
            print("4. 🎲 Draft Aleatorio")
            print("5. 💾 Guardar y Salir")
            print("="*50)

            opcion = input("\nElige una opción: ")

            if opcion == "1":
                self.menu_marcas()
            elif opcion == "2":
                self.menu_luchadores()
            elif opcion == "3":
                self.menu_campeonatos()
            elif opcion == "4":
                self.draft_aleatorio()
            elif opcion == "5":
                self.guardar_datos()
                print("\n👋 ¡Datos guardados! chabela jeje.\n")
                break
            else:
                print("\n❌ Opcion inválida")

    def menu_luchadores(self):
        while True:
            print("\n" + "="*50)
            print("👤 GESTIÓN DE LUCHADORES")
            print("="*50)
            print("1. Ver todos los luchadores")
            print("2. Agregar nuevo luchador")
            print("3. Ver detalles de un luchador")
            print("4. Cambiar luchador de marca")
            print("5. Eliminar luchador")
            print("6. Volver al menú principal")
            print("="*50)

            opcion = input("\nElige una opción: ")

            if opcion == "1":
                self.ver_todos_luchadores()
            elif opcion == "2":
                self.agregar_luchador_interactivo()
            elif opcion == "3":
                self.ver_detalles_luchador()
            elif opcion == "4":
                self.cambiar_marca_interactivo()
            elif opcion == "5":
                self.eliminar_luchador()
            elif opcion == "6":
                break
            else:
                print("\n❌ Opción inválida")


    def ver_todos_luchadores(self):
        print("\n" + "="*50)
        print("📋 TODOS LOS LUCHADORES")
        print("="*50)
        
        luchadores = self.datos["luchadores"]
        
        if len(luchadores) == 0:
            print("\n❌ No hay luchadores agregados aún")
        else:
            for luchador in luchadores:
                marcas_texto = ", ".join(luchador['marcas'])
                equipo = f" ({luchador['equipo']})" if luchador['equipo'] else ""
                print(f"  • {luchador['nombre']} - {luchador['alignment']} - [{marcas_texto}]{equipo}")
        
        print(f"\n📊 Total de luchadores: {len(luchadores)}")




    def agregar_luchador_interactivo(self):
        print("\n" + "="*50)
        print("➕ AGREGAR NUEVO LUCHADOR")
        print("="*50)

        nombre = input("\n📝 Nombre del luchador: ")

        print("\n📺 ¿En qué marcas luchará? (puedes elegir varias)")
        print("1. NXT")
        print("2. RAW")
        print("3. SmackDown")
        print("4. AAA")
        
        marcas_elegidas = input("\nEscribe los números separados por comas (ej: 1,3): ")
        
        opciones_marcas = {"1": "NXT", "2": "RAW", "3": "SmackDown", "4": "AAA"}
        marcas = []
        
        for num in marcas_elegidas.split(","):
            num = num.strip()
            if num in opciones_marcas:
                marcas.append(opciones_marcas[num])
        
        if len(marcas) == 0:
            print("❌ No elegiste ninguna marca válida")
            return

        print("\n⚔️ ¿Es Face o Heel?")
        print("1. Face")
        print("2. Heel")

        align_op = input("\nAlignment: ")
        alignment = "Face" if align_op == "1" else "Heel"

        print("\n📊 ¿En qué división está?")
        print("1. Upper Card")
        print("2. Mid Card")
        print("3. Tag Team")
        print("4. Low Card")

        division_op = input("\nDivisión: ")
        divisiones = {
            "1": "Upper Card",
            "2": "Mid Card",
            "3": "Tag Team",
            "4": "Low Card"
        }

        if division_op not in divisiones:
            print("❌ División inválida")
            return

        division = divisiones[division_op]

        equipo = input("\n👥 ¿Pertenece a un equipo? (deja vacío si no): ")
        equipo = equipo if equipo else None

        luchador = {
            "nombre": nombre,
            "marcas": marcas,
            "alignment": alignment,
            "division": division,
            "equipo": equipo,
            "campeonatos_actuales": [],
            "historial_campeonatos": []
        }
        
        self.datos["luchadores"].append(luchador)
        self.guardar_datos()

        marcas_texto = ", ".join(marcas)
        print(f"\n✅ {nombre} agregado a {marcas_texto} como {alignment}")

    def ver_detalles_luchador(self):
        nombre = input("\n📝 Nombre del luchador: ")

        for luchador in self.datos["luchadores"]:
            if luchador["nombre"].lower() == nombre.lower():
                print("\n" + "="*50)
                print(f"👤 {luchador['nombre'].upper()}")
                print('='*50)
                
                marcas_texto = ", ".join(luchador['marcas'])
                print(f"📺 Marcas: {marcas_texto}")
                print(f"⚔️  Alignment: {luchador['alignment']}")
                
                division = luchador.get('division', 'Sin división')
                print(f"📊 División: {division}")

                if luchador['equipo']:
                    print(f"👥 Equipo: {luchador['equipo']}")

                if len(luchador['campeonatos_actuales']) > 0:
                    print(f"\n🏆 Campeonatos actuales:")
                    for titulo in luchador['campeonatos_actuales']:
                        print(f"  • {titulo}")
                else:
                    print(f"\n🏆 No tiene campeonatos actualmente")

                print("="*50)
                return
        
        print(f"\n❌ No se encontró a '{nombre}'")


    def cambiar_marca_interactivo(self):
        nombre = input("\n📝 Nombre del luchador: ")

        for luchador in self.datos["luchadores"]:
            if luchador["nombre"].lower() == nombre.lower():
                marcas_actual = ", ".join(luchador['marcas'])
                print(f"\n📺 {nombre} actualmente está en: {marcas_actual}")
                print("\n¿Qué quieres hacer?")
                print("1. Agregar a otra marca")
                print("2. Quitar de una marca")
                
                opcion = input("\nOpción: ")
                
                if opcion == "1":
                    print("\n📺 ¿A qué marca agregar?")
                    print("1. NXT")
                    print("2. RAW")
                    print("3. SmackDown")
                    print("4. AAA")
                    
                    marca_op = input("\nMarca: ")
                    opciones = {"1": "NXT", "2": "RAW", "3": "SmackDown", "4": "AAA"}
                    
                    if marca_op not in opciones:
                        print("❌ Opción inválida")
                        return
                    
                    nueva_marca = opciones[marca_op]
                    
                    if nueva_marca in luchador['marcas']:
                        print(f"❌ {nombre} ya está en {nueva_marca}")
                    else:
                        luchador['marcas'].append(nueva_marca)
                        self.guardar_datos()
                        print(f"✅ {nombre} agregado a {nueva_marca}")
                
                elif opcion == "2":
                    if len(luchador['marcas']) == 1:
                        print("❌ No puedes quitar la única marca. Usa eliminar luchador.")
                        return
                    
                    print("\n📺 ¿De qué marca quitar?")
                    for i, m in enumerate(luchador['marcas'], 1):
                        print(f"{i}. {m}")
                    
                    marca_num = input("\nNúmero: ")
                    try:
                        indice = int(marca_num) - 1
                        marca_eliminada = luchador['marcas'].pop(indice)
                        self.guardar_datos()
                        print(f"✅ {nombre} removido de {marca_eliminada}")
                    except:
                        print("❌ Número inválido")
                else:
                    print("❌ Opción inválida")
                
                return
        
        print(f"\n❌ No se encontró a '{nombre}'")

    def eliminar_luchador(self):
        nombre = input("\n📝 Nombre del luchador a eliminar: ")

        for luchador in self.datos["luchadores"]:
            if luchador["nombre"].lower() == nombre.lower():
                self.datos["luchadores"].remove(luchador)
                self.guardar_datos()
                print(f"\n🗑️ {nombre} eliminado completamente del universo")
                return

        print(f"\n❌ No se encontró a '{nombre}'")

    def menu_marcas(self):
        while True:
            print("\n" + "="*50)
            print("📺  GESTIÓN DE MARCAS")
            print("="*50)
            print("1. Ver roster de NXT")
            print("2. Ver roster de RAW")
            print("3. Ver roster de SmackDown")
            print("4. Ver roster de AAA")
            print("5. Ver resumen de todas las marcas")
            print("6. Volver al menu principal")
            print("="*50)

            opcion = input("\nElige una opción:")

            if opcion == "1":
                self.ver_roster("NXT")
            elif opcion == "2":
                self.ver_roster("RAW")
            elif opcion == "3":
                self.ver_roster("SmackDown")
            elif opcion == "4":
                self.ver_roster("AAA")
            elif opcion == "5":
                self.ver_resumen_marcas()
            elif opcion == "6":
                break
            else:
                print("\n❌ Opción inválida")

    def ver_roster(self, marca):
        print("\n" + "="*50)
        print(f"📋 ROSTER DE {marca.upper()}")
        print("="*50)

        luchadores = [l for l in self.datos["luchadores"] if marca in l['marcas']]

        if len(luchadores) == 0:
            print(f"\n❌ No hay luchadores en {marca} aún")
        else:
            divisiones = {
                "Upper Card": "👑",
                "Mid Card": "🥈",
                "Tag Team": "👥",
                "Low Card": "🔹"
            }

            for division, emoji in divisiones.items():
                grupo = [l for l in luchadores if l.get('division') == division]

                if len(grupo) > 0:
                    print(f"\n{emoji} {division.upper()}:")
                    for luchador in grupo:
                        equipo = f" ({luchador['equipo']})" if luchador['equipo'] else ""
                        campeon = " 🏆" if len(luchador['campeonatos_actuales']) > 0 else ""
                        print(f"  • {luchador['nombre']} - {luchador['alignment']}{equipo}{campeon}")

        print(f"\n📊 Total: {len(luchadores)} luchadores")
        print("="*50)

    def ver_resumen_marcas(self):
        print("\n" + "="*50)
        print("📊 RESUMEN DE MARCAS")
        print("="*50)

        for marca in ["NXT", "RAW", "SmackDown", "AAA"]:
            luchadores_marca = [l for l in self.datos["luchadores"] if marca in l['marcas']]
            total = len(luchadores_marca)
            faces = sum(1 for l in luchadores_marca if l['alignment'] == 'Face')
            heels = sum(1 for l in luchadores_marca if l['alignment'] == 'Heel')
            print(f"\n📺 {marca}:")
            print(f"   Total: {total} luchadores")
            print(f"   Faces: {faces} | Heels: {heels}")

        print("\n" + "="*50)
        
    def menu_campeonatos(self):
        while True:
            print("\n" + "-"*50)
            print("🏆 GESTIÓN DE CAMPEONATOS")
            print("="*50)
            print("1. Ver todos los campeonatos")
            print("2. Asignar Campeón")
            print("3. Actualizar días de reinado")
            print("4, Vacante un campeonato")
            print("5. Volver al menú principal")
            print("="*50)
            
            opcion = input("\nElige una opción: ")
            
            if opcion == "1":
                self.ver_campeonatos()
            elif opcion == "2":
                self.asignar_campeon()
            elif opcion == "3":
                self.actualizar_dias()
            elif opcion == "4":
                self.vacar_campeonato()
            elif opcion == "5":
                break
            else:
                print("\n❌ Opción Inválida")


    def ver_campeonatos(self):
        print("\n" + "="*50)
        print("🏆 CAMPEONATOS")
        print("="*50)
        
        for marca in ["RAW", "SmackDown", "Compartido RAW/SD", "NXT", "AAA"]:
            if marca in self.datos["campeonatos"]:
                print(f"\n📺 {marca}:")
                for campeonato in self.datos["campeonatos"][marca]:
                    if campeonato["campeon"]:
                        print(f"  🏆 {campeonato['nombre']}")
                        print(f"      Campeón: {campeonato['campeon']} ({campeonato['dias']} días)")
                    else:
                        print(f"  ⚪ {campeonato['nombre']} - VACANTE")
                        
        print("\n" + "="*50)            
        

    def asignar_campeon(self):
        print("\n📺 Elige la marca:")
        print("1. RAW")
        print("2. SmackDown")
        print("3. Compartido RAW/SD")
        print("4. NXT")
        print("5. AAA")
        
        marca_op = input("\nMarca: ")
        marcas = {
            "1": "RAW",
            "2": "SmackDown",
            "3": "Compartido RAW/SD",
            "4": "NXT",
            "5": "AAA"
        }
        
        if marca_op not in marcas:
            print("❌ Marca inválida")
            return
        
        marca = marcas[marca_op]
        
        print(f"\n🏆 Campeonatos de {marca}:")
        for i, camp in enumerate(self.datos["campeonatos"][marca], 1):
            estado = f"Campeón: {camp['campeon']}" if camp['campeon'] else "VACANTE"
            print(f"{i}. {camp['nombre']} - {estado}")
        
        camp_num = input("\nNúmero del campeonato: ")
        
        try:
            índice = int(camp_num) - 1
            campeonato = self.datos["campeonatos"][marca][índice]
        except:
            print("❌ Número inválido")
            return
        
        nombre_luchador = input("\n📝 Nombre del nuevo campeón: ")
        
        dias = input("📊 Días de reinado (deja vacío para 0): ")
        dias = int(dias) if dias else 0
        
        campeonato["campeon"] = nombre_luchador
        campeonato["dias"] = dias
        
        self.guardar_datos()
        print(f"\n✅ {nombre_luchador} es el nuevo campeón de {campeonato['nombre']}")
        
        
    def actualizar_dias(self):
        print("\n📺 Elige la marca:")
        print("1. RAW")
        print("2. SmackDown")
        print("3. Compartido RAW/SD")
        print("4. NXT")
        print("5. AAA")

        marca_op = input("\nMarca: ")
        marcas = {
            "1": "RAW",
            "2": "SmackDown",
            "3": "Compartido RAW/SD",
            "4": "NXT",
            "5": "AAA"
        }

        if marca_op not in marcas:
            print("❌ Marca inválida")
            return

        marca = marcas[marca_op]

        print(f"\n🏆 Campeonatos de {marca}:")
        for i, camp in enumerate(self.datos["campeonatos"][marca], 1):
            if camp['campeon']:
                print(f"{i}. {camp['nombre']} - {camp['campeon']} ({camp['dias']} días)")

        camp_num = input("\nNúmero del campeonato: ")

        try:
            indice = int(camp_num) - 1
            campeonato = self.datos["campeonatos"][marca][indice]
        except:
            print("❌ Número inválido")
            return

        if not campeonato['campeon']:
            print("❌ Este campeonato está vacante")
            return

        nuevos_dias = input(f"\n📊 Nuevos días de reinado (actualmente {campeonato['dias']}): ")

        try:
            campeonato['dias'] = int(nuevos_dias)
            self.guardar_datos()
            print(f"✅ Actualizado: {campeonato['campeon']} ahora tiene {campeonato['dias']} días")
        except:
            print("❌ Número inválido")
            
    def vacar_campeonato(self):
        print("\n📺 Elige la marca:")
        print("1. RAW")
        print("2. SmackDown")
        print("3. Compartido RAW/SD")
        print("4. NXT")
        print("5. AAA")

        marca_op = input("\nMarca: ")
        marcas = {
            "1": "RAW",
            "2": "SmackDown",
            "3": "Compartido RAW/SD",
            "4": "NXT",
            "5": "AAA"
        }

        if marca_op not in marcas:
            print("❌ Marca inválida")
            return

        marca = marcas[marca_op]

        print(f"\n🏆 Campeonatos de {marca}:")
        for i, camp in enumerate(self.datos["campeonatos"][marca], 1):
            estado = f"{camp['campeon']} ({camp['dias']} días)" if camp['campeon'] else "VACANTE"
            print(f"{i}. {camp['nombre']} - {estado}")

        camp_num = input("\nNúmero del campeonato a vacar: ")

        try:
            indice = int(camp_num) - 1
            campeonato = self.datos["campeonatos"][marca][indice]
        except:
            print("❌ Número inválido")
            return

        campeonato['campeon'] = None
        campeonato['dias'] = 0

        self.guardar_datos()
        print(f"✅ {campeonato['nombre']} ahora está VACANTE")
        
    
    def draft_aleatorio(self):
        import random

        nombre = input("\n📝 Nombre del luchador para el draft: ")

        luchador_encontrado = None

        for luchador in self.datos["luchadores"]:
            if luchador["nombre"].lower() == nombre.lower():
                luchador_encontrado = luchador
                break

        if not luchador_encontrado:
            print(f"❌ No se encontró a '{nombre}'")
            return

        marca_destino = random.choice(["RAW", "SmackDown"])

        if marca_destino in luchador_encontrado['marcas']:
            print(f"\n🎲 {nombre} ya está en {marca_destino}, no hay cambios")
        else:
            # Quitar de todas las marcas actuales
            luchador_encontrado['marcas'] = [marca_destino]
            self.guardar_datos()
            print(f"\n🎲 ¡DRAFT! {nombre} ahora solo está en {marca_destino}")




# Iniciar el programa 
if __name__ == "__main__":
    universo = WWEUniverse()
    universo.menu_principal()


