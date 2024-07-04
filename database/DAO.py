from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                        from neighbor n
                        where n.state1 < n.state2"""

        cursor.execute(query)

        for row in cursor:
            result.append((idMap[row["state1"]], idMap[row["state2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getWeights(year, diff):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.state as s1, s2.state as s2
                    from sighting s, sighting s2
                    where year(s.`datetime`)=%s and year(s2.`datetime`)=%s and s.state!=s2.state and datediff(s.`datetime`,s2.`datetime`)<%s """

        cursor.execute(query, (year, year, diff,))

        for row in cursor:
            result.append((row["s1"], row["s2"]))

        cursor.close()
        conn.close()
        return result