def DB(proj_name,prog_use,proj_idea,proj_application,proj_budget,contact):
    import sqlite3
    conn = sqlite3.connect('client.db')
    print ("Opened database successfully")
    # proj_name = "moon rock"
    # prog_use = "cpp"
    # proj_idea = "to create a rover"
    # proj_application = "to build"
    # proj_budget = 2000
    # contact = 9874546513
    # conn.execute('''CREATE TABLE myclient1
    #          (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
    #          NAME           TEXT    NOT NULL,
    #          USE            TEXT    NOT NULL,
    #          IDEA           TEXT    NOT NULL ,
    #          APPLICATION    TEXT    NOT NULL,
    #          BUDGET         INT     NOT NULL,
    #          CONTACT        INT     NOT NULL);''')
    # print ("Table created successfully")
    conn.execute("INSERT INTO myclient1 (NAME,USE,IDEA,APPLICATION,BUDGET,CONTACT) VALUES (?,?,?,?,?,?)",(proj_name,prog_use,proj_idea,proj_application,proj_budget,contact));
    conn.commit()
    print("Records inserted Sucessfully")
    conn.close()
    