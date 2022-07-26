__all__ = ['run_crtshdb']
import psycopg2

def run_crtshdb(*args):

    TARGET = args[0]
    res = []

    def ex_subs_from_db(data,domain):
        for ex_subs in data:
            if not ex_subs[-1] in res and str(ex_subs[-1]).lower().endswith(str(domain).lower()):
                if not ex_subs[-1] == domain:
                    res.append(str(ex_subs[-1]).rstrip())


    def connect_to_db(domain):
        conn = psycopg2.connect(f"dbname=certwatch user=guest host=crt.sh")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT ci.NAME_VALUE NAME_VALUE FROM certificate_identity ci WHERE ci.NAME_TYPE = 'dNSName' AND reverse(lower(ci.NAME_VALUE)) LIKE reverse(lower('%.{domain}'));")
        ex_subs_from_db(cursor.fetchall(),domain)

    try:
        connect_to_db(TARGET)
    except Exception as err:
        return ["crtshdb",err,"ERROR"]

    return ["crtshdb",res]