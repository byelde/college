na10 = 0
num = 765
num = str(num)[::-1]
bi=8
bf=16

db = '0123456789abcdefghijklmnopqrstuvwxyz'

for idx_digito, digito in enumerate(num):
    for idx_db, db_digito in enumerate(db):
        if digito == db_digito:
            na10 += ((int(bi)**idx_digito)*int(idx_db))

nabf = ''

while True:
         
        if na10 < bf:
            for idx_db, db_digito in enumerate(db):
                  if str(na10) == str(idx_db):
                       nabf += db_digito
                       break
            break

        
        for idx_db, db_digito in enumerate(db):
            if idx_db == na10%bf:
                nabf += str(db_digito)
                na10 = na10//bf
                break


