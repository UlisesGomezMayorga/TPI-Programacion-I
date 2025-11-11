import csv
import os
def normalizarnom(nombre:str) -> str:
	return " ".join(nombre.split()).casefold()
def cargarpaises(nombre_archivo:str) -> list:
	lista = []
	if not os.path.isfile(nombre_archivo):
		return lista
	with open(nombre_archivo, mode="r", encoding="utf-8", newline="") as f:
		lector = csv.DictReader(f)
		for fila in lector:
			nombre = fila.get("nombre","").strip()
			poblacion = fila.get("poblacion","").strip()
			superficie = fila.get("superficie","").strip()
			continente = fila.get("continente","").strip()
			if nombre == "" or poblacion == "" or superficie == "" or continente == "":
				continue
			if not poblacion.isdigit() or not superficie.isdigit():
				continue
			pais = {
				"nombre":nombre,
				"poblacion":int(poblacion),
				"superficie":int(superficie),
				"continente":continente,
			}
			lista.append(pais)
	return lista
def guardarpaises(nombre_archivo:str, lista_paises:list) -> None:
	with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as f:
		campos = ["nombre", "poblacion", "superficie", "continente"]
		escritor = csv.DictWriter(f, fieldnames=campos)
		escritor.writeheader()
		for pais in lista_paises:
			escritor.writerow({
				"nombre":pais["nombre"],
				"poblacion":str(pais["poblacion"]),
				"superficie":str(pais["superficie"]),
				"continente":pais["continente"],
			})
   
def pedirentero(mensaje:str, minimo:int = 0) -> int:
	while True:
		valor = input(mensaje).strip()
		if valor.isdigit():
			n = int(valor)
			if n >= minimo:
				return n
			else:
				print(f"tenes que ingresar un número mayor o igual a {minimo}")
		else:
			print("ingresa un número entero sin decimales")
def buscarpais(lista_paises:list, termino:str) -> list:
	term_norm = normalizarnom(termino)
	resultados = []
	for pais in lista_paises:
		if term_norm in normalizarnom(pais["nombre"]):
			resultados.append(pais)
	return resultados

def agregarpais(lista_paises:list) -> bool:
	nombre = input("nombre del país:").strip()
	if nombre == "":
		print("El nombre no puede estar vacío")
		return False
	nuevo_norm = normalizarnom(nombre)
	for pais in lista_paises:
		if normalizarnom(pais["nombre"]) == nuevo_norm:
			print("el pais ya existe en la lista")
			return False
	poblacion = pedirentero("población (entero >= 0):", 0)
	superficie = pedirentero("Superficie (km2, entero >= 0):", 0)
	continente = input("Continente:").strip()
	if continente == "":
		print("el continente no puede estar vacío")
		return False
	pais = {
		"nombre":nombre,
		"poblacion":poblacion,
		"superficie":superficie,
		"continente":continente,
	}
	lista_paises.append(pais)
	print(f"País '{nombre}' agregado correctamente")
	return True

def actualizarpais(lista_paises:list) -> bool:
	termino = input("ingrese nombre (o parte) del país a actualizar:").strip()
	if termino == "":
		print("búsqueda vacía")
		return False
	resultados = buscarpais(lista_paises, termino)
	if len(resultados) == 0:
		print("no se encontraron países con ese término")
		return False
	if len(resultados) > 1:
		print("Se encontraron varios países:")
		for i, p in enumerate(resultados, start=1):
			print(f"{i}. {p['nombre']} (población:{p['poblacion']}, Superficie:{p['superficie']})")
		sel = input("Seleccione el número del país a actualizar (o ENTER para cancelar):").strip()
		if not sel.isdigit():
			print("Operación cancelada")
			return False
		idx = int(sel) - 1
		if idx < 0 or idx >= len(resultados):
			print("Selección inválida")
			return False
		pais_seleccionado = resultados[idx]
	else:
		pais_seleccionado = resultados[0]
	referencia = None
	for p in lista_paises:
		if normalizarnom(p["nombre"]) == normalizarnom(pais_seleccionado["nombre"]):
			referencia = p
			break
	if referencia is None:
		print("error:país no encontrado")
		return False
	print(f"Actualizando '{referencia['nombre']}'.valores actuales:población={referencia['poblacion']},superficie={referencia['superficie']}")
	nueva_pob = pedirentero("Nueva población (enteros >= 0):", 0)
	nueva_sup = pedirentero("Nueva superficie (km2, entero >= 0):", 0)
	referencia["poblacion"] = nueva_pob
	referencia["superficie"] = nueva_sup
	print(f"'{referencia['nombre']}' actualizado correctamente")
	return True

def mostrarmenu() -> None:
	print("\n---Menú de Gestión de Países--")
	print("1.agregar un país")
	print("2.actualizar población/superficie de un país")
	print("3.Buscar país por nombre")
	print("4.Filtrar países")
	print("5.ordenar países")
	print("6.mostrar estadísticas")
	print("7.mmostrar todos los países")
	print("8.Guardar y salir")
	print("0.salir sin guardar")
def buscarpaisinteractivo(lista_paises:list) -> None:
	termino = input("ingrese nombre o parte del nombre a buscar:").strip()
	if termino == "":
		print("búsqueda vacía")
		return
	resultados = buscarpais(lista_paises, termino)
	if not resultados:
		print("no se encontraron coincidencias")
		return
	print(f"Se encontraron {len(resultados)} país(es):")
	for p in resultados:
		print(f"- {p['nombre']}:población={p['poblacion']}, Superficie={p['superficie']}, Continente={p['continente']}")
def filtrar_por_continente(lista_paises:list) -> None:
	cont = input("ingrese continente a filtrar:").strip()
	if cont == "":
		print("Continente vacío")
		return
	cont_norm = cont.casefold()
	encontrados = [p for p in lista_paises if p["continente"].casefold() == cont_norm]
	if not encontrados:
		print("no se encontraron países para ese continente")
		return
	for p in encontrados:
		print(f"- {p['nombre']}:población={p['poblacion']}, Superficie={p['superficie']}")
def filtrarporrangop(lista_paises:list) -> None:
	print("ingrese rango de población:")
	minimo = pedirentero("Mínimo (>=0):", 0)
	maximo = pedirentero("Máximo (>= mínimo):", minimo)
	encontrados = [p for p in lista_paises if p["poblacion"] >= minimo and p["poblacion"] <= maximo]
	if not encontrados:
		print("no se encontraron países en ese rango")
		return
	for p in encontrados:
		print(f"- {p['nombre']}:población={p['poblacion']}")
def filtrarporrangos(lista_paises:list) -> None:
	print("ingrese rango de superficie (km2):")
	minimo = pedirentero("Mínimo (>=0):", 0)
	maximo = pedirentero("Máximo (>= mínimo):", minimo)
	encontrados = [p for p in lista_paises if p["superficie"] >= minimo and p["superficie"] <= maximo]
	if not encontrados:
		print("no se encontraron países en ese rango")
		return
	for p in encontrados:
		print(f"- {p['nombre']}:Superficie={p['superficie']}")
def ordenar_paises(lista_paises:list) -> None:
	print("Ordenar por:\n1. nombre\n2. población\n3. Superficie")
	opcion = input("Elegi opción:").strip()
	if opcion not in ("1", "2", "3"):
		print("Opción inválida")
		return
	orden = input("Orden ascendente? (s/n):").strip().lower()
	asc = (orden == "s" or orden == "si")
	if opcion == "1":
		lista_ordenada = sorted(lista_paises, key=lambda x:x["nombre"].casefold(), reverse=not asc)
	elif opcion == "2":
		lista_ordenada = sorted(lista_paises, key=lambda x:x["poblacion"], reverse=not asc)
	else:
		lista_ordenada = sorted(lista_paises, key=lambda x:x["superficie"], reverse=not asc)
	for p in lista_ordenada:
		print(f"- {p['nombre']}:población={p['poblacion']}, Superficie={p['superficie']}, Continente={p['continente']}")
def mostrar_estadisticas(lista_paises:list) -> None:
	if not lista_paises:
		print("no hay países cargados")
		return
	mayor = lista_paises[0]
	menor = lista_paises[0]
	suma_pob = 0
	suma_sup = 0
	por_cont = {}
	for p in lista_paises:
		if p["poblacion"] > mayor["poblacion"]:
			mayor = p
		if p["poblacion"] < menor["poblacion"]:
			menor = p
		suma_pob += p["poblacion"]
		suma_sup += p["superficie"]
		clave = p["continente"]
		if clave in por_cont:
			por_cont[clave] += 1
		else:
			por_cont[clave] = 1
	promedio_pob = suma_pob // len(lista_paises)
	promedio_sup = suma_sup // len(lista_paises)
	print(f"País con mayor población:{mayor['nombre']} ({mayor['poblacion']})")
	print(f"País con menor población:{menor['nombre']} ({menor['poblacion']})")
	print(f"Promedio de población:{promedio_pob}")
	print(f"Promedio de superficie:{promedio_sup} km2")
	print("Cantidad de países por continente:")
	for cont, cantidad in por_cont.items():
		print(f"- {cont}:{cantidad}")
def mostrar_todos(lista_paises:list) -> None:
	if not lista_paises:
		print("no hay países para mostrar")
		return
	for p in lista_paises:
		print(f".{p['nombre']}:poblacion={p['poblacion']},superficie={p['superficie']},continente={p['continente']}")
def menuprincipal(nombre_archivo:str = "paises.csv") -> None:
	lista = cargarpaises(nombre_archivo)
	modificado = False
	while True:
		mostrarmenu()
		opcion = input("Elegi una opción:").strip()
		match opcion:
			case "1":
				cambiado = agregarpais(lista)
				if cambiado:
					guardarpaises(nombre_archivo, lista)
					modificado = True
			case "2":
				cambiado = actualizarpais(lista)
				if cambiado:
					guardarpaises(nombre_archivo, lista)
					modificado = True
			case "3":
				buscarpaisinteractivo(lista)
			case "4":
				print("Filtrar por:1.Continente\n2Rango de población\n3.rango de superficie")
				sub = input("Elegí").strip()
				if sub == "1":
					filtrar_por_continente(lista)
				elif sub == "2":
					filtrarporrangop(lista)
				elif sub == "3":
					filtrarporrangos(lista)
				else:
					print("opción invalida")
			case "5":
				ordenar_paises(lista)
			case "6":
				mostrar_estadisticas(lista)
			case "7":
				mostrar_todos(lista)
			case "8":
				guardarpaises(nombre_archivo, lista)
				print("saliendo y guardando")
				break
			case "0":
				if modificado:
					confirmar = input("Hay cambios sin guardar. ¿Salir sin guardar? (s/n):").strip().lower()
					if confirmar == "s" or confirmar == "si":
						print("saliendo sin guardar")
						break
				else:
					print("saliendo")
					break
			case _:
				print("Opción incorrecta")
if __name__=="__main__":
	menuprincipal()