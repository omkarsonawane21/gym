from flask import Flask, request, flash, jsonify, Response
import mysql.connector
mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='#Sonawane@21',
                               database='gymdb')
mycursor = mydb.cursor()
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    msg = {
        'status': 404,
        'message': 'Not Found ' + request.url,
    }
    resp = jsonify(msg)
    resp.status_code = 404
    return resp


@app.route('/admin')
def admin_send():
    try:
        mycursor.execute("SELECT * FROM admin")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)

@app.route('/register', methods = ['POST'])
def register():
    try:
        if request.method == 'POST':
            print(request)

            val = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                val.append(x[i])

            loginid = 0
            mycursor.execute("select * from id_numbers")
            myresult = mycursor.fetchall()
            user = myresult[0][0]
            trainer = myresult[0][1]
            owner = myresult[0][2]

            if val[i] == "User":   # last value is type
                val.pop()
                val.append(user)            # replace the type field with loginid
                val.append("/profile/user")
                sql = "update id_numbers set userid = %s where userid = %s"
                value = (str(user + 1), str(user))
                mycursor.execute(sql, value)

            elif val[i] == "Trainer":
                logging.basicConfig(filename="logs/trainer.log", format='%(asctime)s %(message)s', filemode='a')
                logger = logging.getLogger()
                logger.setLevel(logging.INFO)
                logger.info(str(trainer))

                val.pop()
                val.append(str(trainer))
                val.append("/profile/trainer")
                sql = "update id_numbers set trainerid = %s where trainerid = %s"
                value = (str(trainer + 1), str(trainer))
                mycursor.execute(sql, value)

            elif val[i] == "Owner":
                logging.basicConfig(filename="logs/owner.log", format='%(asctime)s %(message)s', filemode='a')
                logger = logging.getLogger()
                logger.setLevel(logging.INFO)
                logger.info(str(owner))

                val.pop()
                val.apeend(str(owner))
                val.append("/profile/owner")
                sql = "update id_numbers set ownerid = %s where ownerid = %s"
                value = (str(owner + 1), str(owner))
                mycursor.execute(sql, value)

            mydb.commit()
            # val.append("0")      # initially the gymid is null

            print(val)
            sql = "insert into login(uname, password, name, mobile, email, aadhar, loginid, profile) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()


            return Response(status=200)
    except Exception as e:
        print(e)


@app.route('/login')
def login_send():
    try:
        mycursor.execute("SELECT uname, password, loginid FROM login")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/gym')
def gym_send():
    try:
        mycursor.execute("SELECT * from gym")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/trainer')
def trainer_send():
    try:
        mycursor.execute("SELECT * from trainer")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/diet')
def diet_send():
    try:
        mycursor.execute("SELECT * from diet")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/training')
def training_send():
    try:
        mycursor.execute("SELECT * from training")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


@app.route('/ad')
def ad_send():
    try:
        mycursor.execute("SELECT * from ad")
        myresult = mycursor.fetchall()
        resp = jsonify(myresult)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(host="10.100.109.85", port=5000)