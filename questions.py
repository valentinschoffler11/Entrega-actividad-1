import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

score = 0.0

# Se combinan las tres listas en una sola lista de tuplas (pregunta, respuestas e indice correcto)
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, answer_options, correct_answers_index in questions_to_ask:
    # Se muestra en pantalla la pregunta
    print (question)

    # Se muestra las respuestas posibles
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        
        # Se verifica que la respuesta sea valida
        if user_answer.isdigit():
            user_answer = int (user_answer) - 1
            if user_answer < 0 or user_answer >= len(answer_options):
                print ("Respuesta no válida")
                sys.exit(1)
        else:
            print("Respuesta no valida")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index:
            print("¡Correcto!")
            score += 1.0
            break
        else:
            score -= 0.5

    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_answers_index])
            
    # Se imprime un blanco al final de la pregunta
    print()

print (f"Puntuacion: {score}")