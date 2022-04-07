import mysql.connector      # database connected
mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='#Sonawane@21', database='gymdb')
mycursor = mydb.cursor()    # use of cursor for execution

mycursor.execute("SELECT gymid from gym")
myresult = mycursor.fetchall()
last_gymid_entry = myresult[len(myresult) - 1][0]
print(type(last_gymid_entry))
'''
# admin
mycursor.execute("CREATE TABLE admin(name VARCHAR(20) primary key, password VARCHAR(15) not null, "
                 "role VARCHAR(15))")

owner = "Omkar Sonawane"
opass = "o"
sale = "Rushikesh Sanap"
spass = "r"
dboy1 = "Ronnie Coleman"
dpass1 = "c"
dboy2 = "Jay Cutler"
dpass2 = "j"
type1 = "Super admin"
type2 = "Admin"
type3 = "Verifier"
type4 = "Maintainer"

sql = "INSERT INTO admin (name, password, role) VALUES (%s, %s, %s)"
val = [(owner, opass, type1), (sale, spass, type2), (dboy1, dpass1, type3), (dboy2, dpass2, type4)]
mycursor.executemany(sql, val)
mydb.commit()

# to store previos id numbers
# user -    1000000000
# trainer - 3000000000
# owner -   4000000000
mycursor.execute("create table id_numbers(userid int unsigned, trainerid int unsigned, "
                 "ownerid int unsigned)")

sql = "insert into id_numbers (userid, trainerid, ownerid) values (%s, %s, %s)"
val = ("1000000000", "3000000000", "4000000000")
mycursor.execute(sql, val)
mydb.commit()

# gym - 100000
mycursor.execute("create table gym(gymid int unsigned primary key auto_increment, gym_name varchar(30) not null, "
                 "address varchar(100), photo varchar(100))")

# login - set id appropriately on basis of who is registering i.e trainer, owner or user
# while signing in for first time ask for trainer, owner or user
mycursor.execute("create table login(uname varchar(15) unique not null, password varchar(15) not null, "
                 "loginid int unsigned primary key, name varchar(30) not null, mobile varchar(12) "
                 "unique not null, email varchar(30) unique not null, aadhar varchar(15) unique not "
                 "null, profile varchar(100), gymid int unsigned, foreign key(gymid) references gym(gymid))")

# server - stores ip address of each individual id of all along with active status of that id
mycursor.execute("CREATE TABLE server(serverid int unsigned PRIMARY KEY, foreign key(serverid) references login("
                 "loginid) on "
                 "delete "
                 "cascade , ip VARCHAR(50), status tinyint)")

# trainer
mycursor.execute("create table trainer(trainerid int unsigned primary key, foreign key(trainerid) references login("
                 "loginid) on delete"
                 " cascade, verified boolean, certificate varchar(100), "
                 "info varchar(200), photos varchar(100))")

# chat
mycursor.execute("create table chat(senderid int unsigned not null, foreign key(senderid) references login(loginid), "
                 "recvid int "
                 "unsigned not null, foreign key(recvid) references login(loginid), msg varchar(500), "
                 "timeofmsg timestamp,"
                 " status tinyint, check (senderid <> recvid))")

# diet
mycursor.execute("create table diet(meal1 varchar(100), meal2 varchar(100), meal3 varchar(100), meal4 varchar(100), "
                 "meal5 varchar(100), meal6 varchar(100), time1 time, time2 time, time3 time, time4 time, time5 time, "
                 "time6 time, tid int unsigned, foreign key(tid) references trainer(trainerid), "
                 "userid int unsigned, foreign key(userid) references login(loginid), supplement varchar(30))")

# training
mycursor.execute("create table training(exercise varchar(50) not null, weight smallint unsigned, rep tinyint unsigned, "
                 "no_of_set tinyint unsigned, break tinyint unsigned, info varchar(100), "
                 "tid int unsigned, foreign key(tid) references trainer(trainerid), userid int unsigned, foreign key("
                 "userid) "
                 "references login(loginid))")

# ad
mycursor.execute("create table ad(ad_id int unsigned primary key auto_increment, product varchar(50) not null, "
                 "info varchar(200), price float, grp tinyint unsigned, photo varchar(100))")
'''