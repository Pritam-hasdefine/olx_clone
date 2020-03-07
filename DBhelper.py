import mysql.connector


class DBhelper:
    def __init__(self):
        try:
            self._connection = mysql.connector.connect(user="root", password="",
                                                       host="127.0.0.1", database="userdb")
            self._cursor = self._connection.cursor()
            print("Connected to DB")
        except:
            print("Could not connect to database. Error code 2er43wsd")
            exit(0)

    def search(self, key1, value1, key2, value2, table):
        self._cursor.execute("""
        SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'                 
        """.format(table, key1, value1, key2, value2))



        data = self._cursor.fetchall()


        return data

    def search1(self,table,key1,type,value1):
        self._cursor.execute("""
        	    SELECT * FROM `{}` WHERE `{}` {} '{}'                 
        	    """.format(table, key1, type, value1))
        data = self._cursor.fetchall()
        return data





        print(data)
        return data

    def searchowner(self,values1):
    #SELECT * from users where users.user_id IN (SELECT proposals.juliet_id FROM `users`,`proposals` where users.user_id=proposals.romeo_id)
        self._cursor.execute("""
        SELECT * FROM users WHERE users.user_id IN (SELECT proposals.romeo_id FROM `proposals` where proposals.juliet_id LIKE '{}' )
        """.format(values1))

        data = self._cursor.fetchall()
        return data


    def dataupdate(self, insertDict,value):
        colValue = []
        dataValue = []
        for i in insertDict:
            colValue.append(i)
        for i in insertDict.values():
            dataValue.append(i)
        print(colValue,dataValue)
        for i,j in zip(colValue,dataValue):
            query = "UPDATE `userdb1` SET `{}`='{}' WHERE userdb1.user_id='{}' ".format(i,j,value)
            try:
                self._cursor.execute(query)
                self._connection.commit()
            except:
                return 0

        return 1

    def searchOne(self, key1, value1, table, type):
        self._cursor.execute("""
	    SELECT * FROM `{}` WHERE `{}` {} '{}'                 
	    """.format(table,key1,type,value1))

        data = self._cursor.fetchall()

        return data

    def insert(self, insertDict, table):
        """INSERT INTO users ('name','email','password','gender','age','city') VALUES ('NULL', 'Virat', 'virat@gmail.com','1234','Male','25','Mumbai')"""

        colValue = ""
        dataValue = ""
        for i in insertDict:
            colValue = colValue + "`" + i + "`,"
            dataValue = dataValue + "'" + insertDict[i] + "',"


        colValue = colValue[0:-1]


        dataValue = dataValue[0:-1]


        query = "INSERT INTO `{}` ({}) VALUES ({})".format(table,colValue, dataValue)


        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0

    def insertimg(self, table,img):
        """INSERT INTO users ('name','email','password','gender','age','city') VALUES ('NULL', 'Virat', 'virat@gmail.com','1234','Male','25','Mumbai')"""



        query = "INSERT INTO `{}` ({}) VALUES ({})".format(table, 'Image', img)

        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0