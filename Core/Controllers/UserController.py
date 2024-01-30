import Core


def login(email, password):
    cursor = Core.cursor() # db manager
    sql = "SELECT * FROM `users` WHERE `email`='{}' AND `password`='{}'".format(str(email), str(password))

    cursor.execute(sql)

    data = cursor.fetchone()

    return data
