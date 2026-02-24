import requests as re


nome=input("Introduza o Primeiro Nome: ")

sobrenome=input("Introduza o Ultimo nome: ")

rmin=int(input("Introduza o Numero Minimo para começar a procurar: "))

rmax=int(input("Introduza o Numero Maximo:"))

role=input("Introduza se é Formador ou Formando: ")



print(nome,sobrenome,rmin,rmax,role)


for i in range(rmin,rmax):
    request=re.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={i}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771937426904")


    if nome and sobrenome in request.text:
        if f"Sessão como {role}" in request.text:
            print(i,"encontrado")
            break
    else:
        print("nao encontrado")