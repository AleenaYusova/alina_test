import mysql.connector
from mysql.connector import errorcode


# class SQLStatementsBank:
#     """ Запрос на выборку последнего неподтвержденного экашена Подписания договора у клиента """
#     password_recovery_for_customer_first_part = """ SELECT ar.`hash` FROM mb_action_requests AS ar
#         WHERE (ar.`action` = 'password.recovery' AND
#                   ar.`confirmed_at` is NULL AND
#                   ar.`params` LIKE '%customerLogin":"""
#     password_recovery_for_customer_second_part = """%') ORDER BY ar.`id` DESC LIMIT 1;"""
#
#     """ Запрос на выборку последнего неподтвержденного экашена предоставление доступа """
#     action_requests_for_customer_first_part = """ SELECT ar.`hash` FROM mb_action_requests AS ar
#         WHERE (ar.`action` = 'contract.sign.confirmation' AND
#                   ar.`confirmed_at` is NULL AND
#                   ar.`params` LIKE '%customerLogin":"""
#     action_requests_for_customer_second_part = """%') ORDER BY ar.`id` DESC LIMIT 1;"""
#
#     # """ Запрос на выборку последнего неподтвержденного экшена Подписания договора: """
#     # sql_statement = """ SELECT hash FROM mb_action_requests ar WHERE ar.action = 'contract.sign.confirmation'
#     #                     AND ar.confirmed_at is NULL ORDER BY ar.id DESC LIMIT 1;"""
#

class Query:
    @staticmethod
    def query(customer_email):
        cnx = None
        try:
            cnx = mysql.connector.connect(user='bizportal',
                                          password='bizportal',
                                          host='172.16.102.110',
                                          database='bizportal_test')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        """ Запрос на выборку последнего неподтвержденного экашена Подписания договора у клиента """
        sql_statement = "SELECT ar.`hash` FROM mb_action_requests AS ar \
            WHERE (ar.`params` LIKE '%" + customer_email + "%') LIMIT 1 "
        print(sql_statement)

        cursor = cnx.cursor()
        print(cursor)
        result = cursor.execute(sql_statement)
        print(result)
        row = cursor.fetchone()
        # row = cursor.fetchall()
        print(row)
        row = str(row[0])
        newstring = row
        print(newstring)
        cnx.close()
        newstring = newstring.replace("bytearray(b'", "")
        newstring = newstring.replace("')", "")
        print(newstring)
        return newstring
