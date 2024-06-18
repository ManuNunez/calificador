import pandas as pd
import os

def registrar_alumno(nombre, grado, grupo, aciertos):

    alumno = {
        'Nombre': nombre,
        'Grado': grado,
        'Grupo': grupo,
        'Aciertos': aciertos
    }
    if not os.path.exists('data'):
        os.makedirs('data')
    file_path = os.path.join('data', 'alumnos.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = df.append(alumno, ignore_index=True)
    else:
        df = pd.DataFrame([alumno])
    df.to_csv(file_path, index=False)
    print(f'Alumno {nombre} registrado exitosamente.')
