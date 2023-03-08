"""
    Criar um link simbolico à pasta D:/University/current_course apontando para a disciplina ativa no momento a partir de 
    uma integração com google docs
"""
import os
import ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
    print("Sem permissão de administrador.")
    import sys
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
else:
    print("Permissão")

courses = []

for dir in os.listdir("D:/University/semester-1"): # Automatizar processo de identificação de semestre
    courses.append(dir)

print("-----------------------------")
for course in courses:
    print(f"[{courses.index(course)}] {course}")
print("-----------------------------")
current_course = int(input("Selectione o curso atual: "))  # Automatizar processo de curso a partir de integração com Google Calendar

os.symlink(f"D:/University/semester-1/{courses[current_course]}", "D:/University/current_course")


