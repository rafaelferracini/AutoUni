"""
    Criar um link simbolico à pasta D:/University/current_course apontando para a disciplina ativa no momento a partir de 
    uma integração com google docs
"""
import os
import ctypes
import datetime

courses = []

# Checa a permissão de admin (necessario para criação do link simbolico)
def IsAdm():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("No admin")
        import sys
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
        return 
    print("already adm")
    return

# Obtem o semestre atual a partir das datas do calendario academico. Futuramente integrar com o calendario para obter os dados automaticamente
def get_semester(today):
    # List of semesters [(start, end)]
    semesters = [(datetime.date(2023, 3, 6), datetime.date(2023, 7, 12)),
                 (datetime.date(2023, 8, 7), datetime.date(2023, 12, 16)),
                 (datetime.date(2024, 3, 4), datetime.date(2024, 7, 6)),
                 (datetime.date(2024, 8, 5), datetime.date(2024, 12, 7))
                 ]
    for sem in semesters:
        if sem[0] < today and today < sem[1]:
            index = semesters.index(sem)
            if index % 2 == 0:
                return 1
            return 2

# Cria o diretorio correspondente ao atual semestre. Futuramente integrar com o sistema da UFSC para também criar os diretórios das disciplinas
def directory(year, sem):
    if not os.path.exists(f"D:/University/{year}.{sem}"):
        os.makedirs(f"D:/University/{year}.{sem}")
    
# Atualiza os cursos do atual semestre a partir das pastas do semestre correspondente
def att_courses(year, sem):
    for dir in os.listdir(f"D:/University/{year}.{sem}"): # Automatizar processo de identificação de semestre
        courses.append(dir)

# Exibe um menu para selecionar o curso atual que estará utilizando. Futuramente automatizar a seleção a partir da integração com Google Calendar 
def choose_course():
    print("-----------------------------")
    for course in courses:
        print(f"[{courses.index(course)}] {course}") 
    print("[9] Exit")
    print("-----------------------------")
    current_course = int(input("Selectione o curso atual: "))  
    if current_course == 9:
        exit()
    return current_course

# Cria o link simbolico para o curso atual
def create_sym(current_course, year, sem):
    if os.path.exists("C:/Users/rafae/current_course"):
        os.unlink("C:/Users/rafae/current_course")

    os.symlink(f"D:/University/{year}.{sem}/{courses[current_course]}", "C:/Users/rafae/current_course")

def main():
    IsAdm()
    today = datetime.date.today()

    semester = get_semester(today)
    year = today.year
    
    att_courses(year, semester)
    while True:
        course = choose_course()
        create_sym(course, year, semester)

if  __name__ == '__main__':
    main()
    

