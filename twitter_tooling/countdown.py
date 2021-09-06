import sys, time

linea_limpia = "\r                              "

def countdown(seg=3):
    while seg >= 0:
        time.sleep(1)
        sys.stdout.write(linea_limpia)
        sys.stdout.flush()
        
        if seg > 1:
            sys.stdout.write("\r---> Esperando " + str(seg) + " segundos...")
        elif seg > 0:
            sys.stdout.write("\r---> Esperando " + str(seg) + " segundo...")
        else:
            sys.stdout.write("\r--- Espera completada ---\n")
        
        seg -= 1