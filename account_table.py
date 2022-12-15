import sys
import ibm_db
import datetime

def main(dict):

    # ACCOUNT_TABLE テーブルにselect文を発行する
    if dict["action"] == "select":
        ssldsn = "DATABASE=BLUDB;HOSTNAME=***.databases.appdomain.cloud;PORT=32459;PROTOCOL=TCPIP;UID=***;PWD=***;Security=SSL"
        db_conn = ibm_db.connect(ssldsn,"","")
        sql = "SELECT * FROM ACCOUNT_DATA WHERE ID = ?"
        db_stmt = ibm_db.prepare(db_conn,sql)
        id = dict["id"]
        ibm_db.bind_param(db_stmt,1,id)
        ibm_db.execute(db_stmt)
        rows = ibm_db.fetch_tuple(db_stmt)
        ibm_db.close(db_conn)


        return {'result':
            {
                "id": rows[0],
                "name": rows[1],
                "age": rows[2],
                "sex": rows[3],
                "tel": rows[4],
                "address": rows[5],
                "pizza": rows[6],
                "size": rows[7],
                "drink": rows[8],
                "side": rows[9],
                "member": rows[10],
                "flag": rows[11]
            }
        }

