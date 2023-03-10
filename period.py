"""
    get the current perioed (year and semester)
    futurament tentar integrar com calendario academico
"""

import datetime

# Colocar a data de inicio dos semestres em variaveis e checar se hoje esta entre 
# essas datas para obter o semestre atual
start_20231 = datetime.date(2023, 3, 6)
end_20231 = datetime.date(2023, 7, 12)

start_20232 = datetime.date(2023, 8, 7)
end_20232 = datetime.date(2023, 12, 16)

start_20241 = datetime.date(2024, 3, 4)
end_20241 = datetime.date(2024, 7, 6)

start_20242 = datetime.date(2024, 8, 5)
end_20242 = datetime.date(2024, 12, 7)


# No futuro, automatizar para ele buscar essa informação direto no calendário academico

def get_semester():
    today = datetime.date.today()
    if start_20231 < today and today < end_20231:
        print("Estamos em 2023.1")
    
def main():
    year = datetime.date.today().year
    print(year)
    get_semester()

if __name__ == "__main__":
    main()
