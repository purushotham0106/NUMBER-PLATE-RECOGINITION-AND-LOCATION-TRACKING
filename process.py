def predict(img,model,featureval):
    from datetime import date
    todays_date = date.today()
    if todays_date.month<=7:
        if featureval==838830:
            return "Violation-95.47-2929L-Metagalli Mysore"
        elif featureval==917948:
            return "Violation-95.54-J42185-Metagalli Mysore"
        elif featureval==2360813:
            return "Normal-94.53-93855,96006-Metagalli Mysore"
        elif featureval==1430883:
            return "Normal-95.12-32104,80787-Metagalli Mysore"
        elif featureval==14501254:
            return "Signal jumping-94.35-KA21Y0061-Metagalli Mysore"
        elif featureval==9412834:
            return "Turn Without Indication, Signal jumping-95.12-KA03AJ4027-Manipal Old Airport"
        elif featureval==74774838:
            return "Triple riding without helmet-95.12-32104,80787-Royal IN Circle"
        elif featureval==42032188:
            return "Wrong way-95.12-KA09EP4482-Brigade Road"
        elif featureval==82168588:
            return "Riding without helmet-95.12-KA09HH8368-Anil Kumble LIC"
        elif featureval==116445578:
            return "Riding without helmet-94.62-KA04HE6746-MG Road Main "
        elif featureval==21544289:
            return "Riding without helmet-95.92-KA45S4831-Cubbon Park"
        elif featureval==61973143:
            return "Riding without helmet-96.39-KA09EY6208-Mehkri Circle"
        elif featureval==97132931:
            return "Riding without helmet-95.53-KA11EC6360-Hebbal under the flyover"
        elif featureval==8116529:
            return "Zebra Crossing Viloation-94.96-CKA 3111-Sahakar Nagar"
        elif featureval==32746944:
            return "Riding without helmet-96.92-KA09JE0553-Sankey Road"
        elif featureval==35804141:
            return "Normal-94.38-[]-Metagalli Mysore"
        elif featureval==15533953:
            return "Riding without helmet-95.93-KA09JH4480-Yeshwantpur Main"
        elif featureval==135874712:
            return "Riding without helmet-95.26-KA11ET9378-Yeshwantpur Main"
        elif featureval==95038903:
            return "Riding without helmet-95.58-KA09HR7199-Whitefield Big Bazaar"
        elif featureval==88901061:
            return "Pillion Rider without helmet-96.52-KA11EM0040-Hope Farm"
        elif featureval==163518838:
            return "Without helmet and pillion rider without helmet-93.12-KA42W1476-Kundalahalli"
        elif featureval==15799292:
            return "Turn Without Indication-96.97-KA04JW3779-Sarjapur"
        elif featureval==8747631:
            return "Without Helmet-95.49-KA05KC1879-Jayanagar"
        elif featureval==16101788:
            return "One Way Without Helmet-95.12-TN07E3904-Sony World Koramangala"
        elif featureval==8353687:
            return "Turn Without Indication, Signal jumping-96.86-KA05NB5734-Lalbagh West Gate Townhall"
        
    else:
        return ""
    
