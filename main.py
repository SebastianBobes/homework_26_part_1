import csv

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl



if __name__ == '__main__':

    df = pd.read_csv("nba.csv")

    pd.set_option("display.max_rows", 500)
    pd.set_option("display.width", 1000)
    pd.set_option("display.max_columns", 10)


    MENU = """
    1.Arata mi toti jucatorii a caror nume contine un substring citit de la tastatura.
    2.Arata mi  toti jucatorii de la o echipa, nume / pozitie/ salariu.
    3.Arata mi toti jucatorii care vin de la un anumit colegiu citit de la tastatura.
    4.Arata mi toti jucatorii care nu au mers la colegiu si completati Nan cu High School/ Abroad.
    5.Sorteaza mi jucatorii dupa salariu (de la cel mai mare la cel mai mic.)
    6.Converteste coloana Number sa nu mai fie float ci int. """
while True:
    user_pick = int(input(MENU))

    match user_pick:
        case 1:
            user_string = input("Dati un substring: ")
            my_filter = df.loc[(df["Name"].str.contains(user_string, case=False, na=False))]
            print(my_filter)



        case 2:
            team = input("Dati o echipa:")
            filter_by_team = df.loc[df.Team == team]
            print(filter_by_team)
            name = input("Dati un nume:")
            filter_by_name = df.loc[df.Name == name]
            print(filter_by_name)
            position = input("Dati o pozitie:")
            filter_by_position = df.loc[df.Position == position]
            print(filter_by_position)
            salary = float(input("Dati un salariu"))
            filter_by_salary = df.loc[df.Salary == salary]
            print("Jucatorii care au salariul introdus sunt:")
            print(filter_by_salary)
        case 3:
            college = input("Dati un colegiu:")
            filter_by_college = df.loc[df.College == college]
            print("Jucatorii care vin de la colegiul citit sunt: ")
            print(filter_by_college)
        case 4:
            players_without_college = df.loc[df.College.isnull()]
            print(players_without_college)
            df.fillna({"College":"High School/ Abroad"}, inplace=True)
            print(df)
        case 5:
            sorted_by_salary = df.sort_values(["Salary"] ,ascending = False)
            print(sorted_by_salary)
        case 6:
            df.fillna({"Number": 0} ,inplace=True)
            df['Number']= df['Number'].astype(int, errors='ignore')
            print(df)
        case 7:
            df['WeightKG'] = df["Weight"]*0.45359237
            df['Height']=df['Height'].str.replace('-','.')
            df['Height'] = df["Height"].astype(float, errors='ignore')
            df['HeightM'] = df["Height"]*0.3048
            print(df)
            my_list = ['Height', 'Weight']
            df = df.drop(my_list, axis=1)
            print(df)

            ax = df.plot.bar(x="Age", y="Salary", rot=0)
            plt.show()

            excel_writer = pd.ExcelWriter("NBA.xlsx")
            df.to_excel(excel_writer,
                        sheet_name="N-B-A")
            excel_writer.close()
        case _:
            exit()
