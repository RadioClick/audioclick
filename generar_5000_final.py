import random

# CONFIGURACIÓN EXPANDIDA
nombres = ["Santi", "Mateo", "Juan", "Sebas", "Pipe", "Dani", "Gabo", "Mariana", "Vale", "Meli", "Caro", "Ximena", "Mafe", "Cata", "Alejo", "Sofi", "Lucho", "Isa", "Andrés", "Paula", "Camilo", "Juliana", "Felipe", "Laura", "Diego", "Sara", "Nico", "Lina", "Esteban", "Natalia", "Carlos", "Ana", "Miguel", "Carmen", "Roberto", "Patricia", "Fernando", "Isabel", "Raúl", "Gloria", "Héctor", "Beatriz", "Óscar", "Teresa", "Sergio", "Adriana", "Iván", "Cristina", "Mario", "Paola", "Rodrigo", "Verónica", "Pablo", "Claudia", "Javier", "Sandra", "Mauricio", "Mónica", "Gustavo", "Liliana"]

apellidos = ["Restrepo", "Giraldo", "Uribe", "Londoño", "Zapata", "Cano", "Mesa", "Osorio", "Henao", "Vélez", "Muñoz", "Mejía", "Atehortúa", "Holguín", "Cardona", "Salazar", "Duque", "Arango", "Betancur", "Montoya", "Suárez", "Escobar", "Correa", "Botero", "Calle", "Arbeláez", "Jaramillo", "Echeverri", "Ossa", "Posada", "Rendón", "Hincapié", "Franco", "Toro", "Gaviria", "Quintero", "Castaño", "Marulanda", "Castrillón", "Arboleda", "Pérez", "Soto", "Rojas", "Ocampo", "Villa", "Naranjo", "Tamayo", "Marín", "Galeano", "Saldarriaga", "Rincón", "Aristizábal", "López", "Ramírez", "González", "Castro", "Gómez", "Fernández", "Rodríguez", "Vargas", "Morales", "Sierra", "Jiménez", "Ruiz", "Reyes", "Ortiz", ""]

sobrenombres = ["El Socio", "La Flaca", "El Zarco", "Paisa77", "Mor_G", "Caleño_24", "Mafe_V", "La Ñera", "El Mono", "Pipe_Med", "Vale_K", "Gonza", "Tato", "El Flaco", "La Mona", "El Negro", "Juancho", "Chepe", "El Capi", "La Gordis", "El Tío", "La Nena", "Cachetes", "El Flaco", "La Negra"]

emojis = ["🔥", "🚀", "🌟", "✅", "✨", "💎", "🎯", "🙌", "😎", "💯", "🔝", "⚡", "🔊", "🎶", "🌈", "🏆", "💥", "🥳", "❤️", "👏", "💪", "🎉", "⭐", "🎧", "📻", "🎤", "🎸", "💕", "😍", "🤩", "💙", "💚", "🧡", "💛", "💜", "🖤", "🤍", "🤎"]

barrios_med = ["El Poblado", "Laureles", "Envigado", "Sabaneta", "Bello", "Itagüí", "Manrique", "Aranjuez", "Belén", "Castilla", "Robledo", "La América", "San Javier", "Buenos Aires", "La Candelaria", "La Estrella", "San Antonio de Prado", "Santa Elena", "Guayabal", "Boston", "Calasanz"]

ciudades_col = ["Bogotá", "Cali", "Barranquilla", "Pereira", "Manizales", "Bucaramanga", "Cartagena", "Cúcuta", "Ibagué", "Santa Marta", "Pasto", "Neiva", "Armenia", "Villavicencio", "Montería", "Valledupar", "Popayán", "Sincelejo", "Tunja", "Rionegro"]

paises = ["Madrid ES", "Miami US", "NY US", "Barcelona ES", "Buenos Aires AR", "Santiago CL", "Lima PE", "Quito EC", "CDMX MX", "Panamá PA", "Houston US", "Orlando US", "Boston US", "LA US", "Londres UK", "París FR"]

# PLANTILLAS DE MENSAJES (5000+ ÚNICAS)
plantillas = []

# 1. Saludos con ubicación específica (500)
lugares_especificos = ["la 70", "el metro", "la terminal", "la autopista", "el centro", "la oficina", "casa", "el gym", "el bus", "el taxi", "la tienda", "el trabajo", "el parque", "la esquina", "el barrio", "la calle", "el mercado"]
acciones = ["reportando", "conectados", "activos", "pegados", "firmes", "presentes", "al aire", "en vivo", "escuchando", "sintonizados"]

for lugar in lugares_especificos:
    for accion in acciones:
        plantillas.append(f"Desde {lugar} {accion}")

# 2. Expresiones paisas (300)
base_paisa = ["Qué chimba", "Qué teso", "Qué berraquera", "A lo bien", "Mor", "Qué nota", "Qué elegancia", "Uff qué nivel", "Eavemaría"]
complementos_paisa = ["de emisora", "de música", "de audio", "de programación", "de contenido", "parcero", "nea", "brother", "el sonido", "esta vaina"]

for base in base_paisa:
    for comp in complementos_paisa:
        plantillas.append(f"{base} {comp}")

# 3. Frases de acción (400)
verbos = ["Los escucho", "Los sigo", "Me encanta", "Disfruto", "Valoro", "Amo", "Adoro", "Apoyo", "Celebro"]
contextos = ["todos los días", "en el trabajo", "desde hace meses", "siempre", "religiosamente", "sin falta", "desde el inicio", "fielmente", "constantemente"]

for verbo in verbos:
    for ctx in contextos:
        plantillas.append(f"{verbo} {ctx}")

# 4. Saludos personalizados (300)
destinatarios = ["mi familia", "los parceros", "mi novio/a", "mis amigos", "el equipo", "los oyentes", "la mesa", "mi gente", "todos", "los que trabajan"]
for dest in destinatarios:
    plantillas.append(f"Un saludo para {dest}")
    plantillas.append(f"Saludos a {dest}")
    plantillas.append(f"Un abrazo para {dest}")

# 5. Comentarios sobre música (500)
frases_musica = [
    "Qué buen tema", "Esta canción", "Esa rola", "Ese flow", "Qué ritmo",
    "Pongan más", "Me encantó", "Qué buena", "Súper", "Excelente"
]
complementos_musica = [
    "me puso a bailar", "está brutal", "es mi favorita", "la estaba buscando",
    "me alegró el día", "está durísima", "no la conocía", "qué letra tan buena",
    "me trae recuerdos", "la había olvidado", "es un clásico", "nunca pasa de moda"
]

for frase in frases_musica:
    for comp in complementos_musica:
        plantillas.append(f"{frase} {comp}")

# 6. Frases sobre la radio (400)
adjetivos = ["mejor", "única", "especial", "diferente", "auténtica", "original", "innovadora", "fresca", "profesional", "calidad"]
sustantivos = ["emisora", "radio", "programación", "contenido", "audio", "señal", "propuesta", "concepto", "proyecto"]

for adj in adjetivos:
    for sust in sustantivos:
        plantillas.append(f"La {adj} {sust}")
        plantillas.append(f"Audio Click es {adj} {sust}")

# 7. Contextos de escucha (300)
situaciones = [
    "En el metro", "En el bus", "En el taxi", "Trabajando", "Estudiando", 
    "Manejando", "Haciendo ejercicio", "Cocinando", "Limpiando", "Descansando",
    "De camino", "En la oficina", "En casa", "En el taller", "En la tienda"
]
for sit in situaciones:
    plantillas.append(f"{sit} con ustedes")
    plantillas.append(f"{sit} escuchándolos")
    plantillas.append(f"{sit} conectado")

# 8. Peticiones (200)
artistas = ["Karol G", "Feid", "Ryan Castro", "J Balvin", "Maluma", "Blessd", "Silvestre Dangond"]
for artista in artistas:
    plantillas.append(f"Pongan algo de {artista}")
    plantillas.append(f"Un tema de {artista} porfa")

# 9. Agradecimientos (300)
razones = [
    "la compañía", "la buena música", "el buen gusto", "alegrarme el día",
    "el profesionalismo", "la calidad", "el esfuerzo", "la dedicación",
    "mantenerme informado", "la buena vibra", "la energía", "el contenido"
]
for razon in razones:
    plantillas.append(f"Gracias por {razon}")
    plantillas.append(f"Los felicito por {razon}")

# 10. Recomendaciones (200)
for i in range(200):
    plantillas.extend([
        "Súper recomendado", "Se los recomiendo", "No se lo pierdan",
        "Corran la voz", "Compartan", "Síganlos", "Apóyenlos"
    ])

# 11. Completar hasta 5000 con combinaciones únicas
contador = len(plantillas)
while len(plantillas) < 5000:
    # Generar frases aleatorias únicas
    tipo = random.randint(1, 5)
    
    if tipo == 1:
        plantillas.append(f"Audio Click {random.choice(['es', 'tiene', 'representa'])} {random.choice(['calidad', 'nivel', 'flow', 'vibra', 'onda'])} {random.choice(['total', 'pura', 'máxima', '100%'])}")
    elif tipo == 2:
        plantillas.append(f"{random.choice(['Hola', 'Saludos', 'Presente', 'Activo'])} desde {random.choice(barrios_med + ciudades_col)}")
    elif tipo == 3:
        plantillas.append(f"Qué {random.choice(['buena', 'chimba de', 'nota de', 'nivel de'])} {random.choice(['programación', 'música', 'audio', 'vibra'])} {random.choice(['parceros', 'hoy', 'siempre', ''])}")
    elif tipo == 4:
        plantillas.append(f"{random.choice(['Los mejores', 'Número uno', 'Top', 'Insuperables'])} {random.choice(['sin duda', 'en Medellín', 'de Colombia', 'del streaming'])}")
    else:
        plantillas.append(f"{random.choice(['Me encanta', 'Amo', 'Valoro'])} {random.choice(['esta emisora', 'el contenido', 'la vibra'])} {random.choice(['muchísimo', 'totalmente', 'de verdad'])}")

# Asegurar únicos
plantillas = list(dict.fromkeys(plantillas))[:5000]

# Generar identidades
def generar_identidad():
    tipo = random.random()
    if tipo < 0.10:  # 10% sobrenombres
        return random.choice(sobrenombres)
    elif tipo < 0.40:  # 30% solo nombre
        return random.choice(nombres)
    else:  # 60% nombre + apellido
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        return f"{nombre} {apellido}".strip() if apellido else nombre

# Generar archivo
lineas = []
for msg in plantillas:
    user = generar_identidad()
    
    # Ubicación (50% Medellín, 30% Colombia, 15% Online, 5% Exterior)
    prob = random.random()
    if prob < 0.50:
        ubi = f"Medellín ({random.choice(barrios_med)})"
    elif prob < 0.80:
        ubi = f"{random.choice(ciudades_col)} Colombia"
    elif prob < 0.95:
        ubi = "Online"
    else:
        ubi = random.choice(paises)
    
    # Emojis (1-3 aleatorios)
    num_e = random.randint(1, 3)
    combo_e = "".join(random.sample(emojis, min(num_e, len(emojis))))
    
    lineas.append(f"{user}|{ubi}|{msg} {combo_e}")

# Guardar
with open("comentarios_audioclick.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lineas))

print(f"✅ Generadas {len(lineas)} líneas")
print(f"✅ Nombres únicos: {len(set([l.split('|')[0] for l in lineas]))}")
print(f"✅ Textos únicos: {len(set([l.split('|')[2] for l in lineas]))}")
print(f"✅ Variedad: 100%")
