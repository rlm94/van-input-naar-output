VIP_VR = 0.37
ENTRANCE = 7.45
valENTRANCE = int(input("Hoeveel toegangsticket wilt u: "))
valVIP_VR = int(input("Hoeveel minuten wilt u gebruik maken van de VIP-VR GameSeat: "))
myOrder = "Dit geweldige dagje-uit met {} mensen in de Speelhal met {} minuten VR kost je maar {} euro"
TOTAL = valENTRANCE*ENTRANCE+valVIP_VR*VIP_VR

print(myOrder.format(valENTRANCE, valVIP_VR, TOTAL))

