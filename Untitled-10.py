#najmenej 10 symbolov
#aspon 1 cislo
#aspon 1 velke a 1 male pismeno
#ASCII

def checkio(password):
    if len(password)>=10:
        status=False
        for i in password:
            if i.isdigit():
                status = True
        if status:
            status1=False
            for i in password:
                if i.isupper():
                    status1=True
            if status1:
                status2=False
                for i in password:
                    if i.islower():
                        status2=True
                if status2:
                    status3=True
                    for i in password:
                        if not(i.isascii()):
                            status3=False
                    if status3:
                        return True
                    else:
                        return False
                else:
                        return False
            else:
                    return False
        else:
            return False
    else:
        return False
print(checkio("Jozomamamôu6"))
pass

def checkio2(password):
    status_digit = False
    status_lower = False
    status_upper = False
    status_ascii = True
    for i in password:
        if i.isdigit():
            status_digit = True
        if i.islower():
            status_lower = True
        if i.isupper():
            status_upper = True
        if not(i.isascii()):
            status_ascii = False
    return status_digit and status_upper and status_lower and status_ascii
print(checkio2("abcDefsff99"))
pass

def wrapik():
    wrap="abcefghijklmnopqrstuvwxyz"