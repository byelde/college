def voter(age):
    if age < 16 or age > 65:
        x = 'Non-voter'
    elif 16 <= age < 18:
        x = 'Optional voter'
    else:
        x = 'Mandatory voter'
    return x