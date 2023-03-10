"""
    Criar um link simbolico à pasta D:/University/current_course apontando para a disciplina ativa no momento a partir de 
    uma integração com google docs
"""
import os
import ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
    print("No admin")
    import sys
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
else:
    print("admin")

courses = []

for dir in os.listdir("D:/University/2023.1"): # Automatizar processo de identificação de semestre
    courses.append(dir)

while True:
    print("-----------------------------")
    for course in courses:
        print(f"[{courses.index(course)}] {course}") # Automatizar criação de pastas para o curso a partir da matricula 
    print("-----------------------------")
    current_course = int(input("Selectione o curso atual: "))  # Automatizar processo de curso a partir de integração com Google Calendar
    if current_course == 9:
        exit()
    
    if os.path.exists("C:/Users/rafae/current_course"):
        os.unlink("C:/Users/rafae/current_course")

    os.symlink(f"D:/University/2023.1/{courses[current_course]}", "C:/Users/rafae/current_course")

    os.system("cls")
