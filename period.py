"""
    get the current perioed (year and semester)
    futurament tentar integrar com calendario academico
"""

import datetime

def main():
    year = datetime.date.today().year
    print(year)

if __name__ == "__main__":
    main()
