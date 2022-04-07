import io
import traceback
import base64
import mysql.connector
from PIL import Image
from flask import Flask, request, jsonify

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


@app.route('/getimage', methods=['POST'])
def getimage():
    try:
        if request.method == 'POST':
            x = request.get_json()
    #     X[0] will be the image in string

            decodeit = open('C:/gym_server/gym/profile/user/hello_level.png', 'wb')
            decodeit.write(base64.b64decode(x[0]))
            decodeit.close()

            resp = jsonify(1)
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)


@app.route('/register', methods=['POST'])
def register():
    try:
        if request.method == 'POST':
            print(request)

            val = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                val.append(x[i])

            mycursor.execute("select * from id_numbers")
            myresult = mycursor.fetchall()
            user = myresult[0][0]
            trainer = myresult[0][1]
            owner = myresult[0][2]

            print(val[i])
            if val[i] == "User":   # last value is type
                val.pop()
                val.append(str(user))            # replace the type field with loginid
                val.append("/profile/user/" + str(user))
                sql = "update id_numbers set userid = %s where userid = %s"
                value = (str(user + 1), str(user))

            elif val[i] == "Trainer":
                val.pop()
                val.append(str(trainer))

                # also add trainer in trainer table
                traineradd = "insert into trainer(trainerid) values(%s)"
                mycursor.execute(traineradd, str(trainer))
                mydb.commit()

                val.append("/profile/trainer/" + str(trainer))
                sql = "update id_numbers set trainerid = %s where trainerid = %s"
                value = (str(trainer + 1), str(trainer))

            elif val[i] == "Gym Owner":
                val.pop()
                val.append(str(owner))
                val.append("/profile/owner/" + str(owner))
                sql = "update id_numbers set ownerid = %s where ownerid = %s"
                value = (str(owner + 1), str(owner))

            mycursor.execute(sql, value)
            mydb.commit()

            print(val)
            sql = "insert into login(uname, password, name, mobile, aadhar, email, loginid, profile) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()

            # return Response(status=200, response=jsonify([1]))
            resp = jsonify([1])
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)
        # writing the below lines is useless why?
        # resp = jsonify(0)
        # resp.status_code = 200
        # return resp


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


@app.route('/creategym', methods=['POST'])
def creategym():
    try:
        if request.method == 'POST':
            val = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                val.append(x[i])
            # will have only gym name and address, id gets set auto increment
            print(val[i])

            mycursor.execute("SELECT gymid from gym")
            myresult = mycursor.fetchall()
            last_gymid_entry = myresult[len(myresult) - 1][0] + 1

            val.append("/profile/gymphotos/" + str(last_gymid_entry))

            sql = "insert into gym(gym_name, address, photo) values(%s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()

            resp = jsonify([1])
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


@app.route('/updateuserprofile', methods=['POST'])
def updateuserprofile():
    try:
        if request.method == 'POST':
            attributes = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                attributes.append(x[i])

            gymname = list()
            gymname.append(attributes[2])

            get_gymid = "select gymid from gym where gymname = %s"
            mycursor.execute(get_gymid, gymname)
            gymid = mycursor.fetchall()[0][0]

            attributes.pop(2)       # remove gymname
            attributes.insert(2, gymid) # insert gymid in that place
            # last index will automatically will be loginid

            # mobile, email, nameofgym, loginid    try to send loginid also
            sql = "update login set mobile = %s, email = %s, gymid = %s where loginid = %s"
            mycursor.execute(sql, attributes)
            mydb.commit()
    except Exception as e:
        traceback.print_stack(e)


@app.route('/updatetrainerprofile', methods=['POST'])
def updatetrainerprofile():
    try:
        if request.method == 'POST':
            attributes = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                attributes.append(x[i])

            get_gymid = "select gymid from gym where gymname = %s"
            mycursor.execute(get_gymid, attributes[2])
            gymid = mycursor.fetchall()

            attributes.pop(2)       # remove gymname
            attributes.insert(2, gymid) # insert gymid in that place

            trainerinfo = attributes.pop(3)
            # last index will automatically will be loginid

            # mobile, email, nameofgym, info, loginid    try to send loginid also
            sql = "update login set mobile = %s, email = %s, gymid = %s where loginid = %s"
            mycursor.execute(sql, attributes)
            mydb.commit()

            sql = "update trainer set info = %s where trainerid = %s"
            val = [trainerinfo, attributes[3]]
            mycursor.execute(sql, val)
            mydb.commit()
    except Exception as e:
        traceback.print_stack(e)


@app.route('/updateownerprofile', methods=['POST'])
def updateownerprofile():
    try:
        if request.method == 'POST':
            attributes = list()
            x = request.get_json()

            i = 0
            for i in range(len(x)):
                attributes.append(x[i])

            get_gymid = "select gymid from gym where gymname = %s"
            mycursor.execute(get_gymid, attributes[2])
            gymid = mycursor.fetchall()

            attributes.pop(2)       # remove gymname
            attributes.insert(2, gymid) # insert gymid in that place
            # last index will automatically will be loginid

            # mobile, email, nameofgym, loginid    try to send loginid also
            sql = "update login set mobile = %s, email = %s, gymid = %s where loginid = %s"
            mycursor.execute(sql, attributes)
            mydb.commit()
    except Exception as e:
        traceback.print_stack(e)


@app.route('/senduserprofilepic', methods=['POST'])
def senduserprofilepic():
    try:
        if request.method == 'POST':
            attributes = list()
            x = request.get_json()

            print(x)
            i = 0
            for i in range(len(x)):
                attributes.append(x[i])

        image_path = 'C:/gym_server/gym/profile/user/' + attributes[0] + '/' + attributes[0] + '.jpg'
        pil_img = Image.open(image_path, mode='r') # reads the PIL image
        byte_arr = io.BytesIO()
        pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
        encoded_img = base64.encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64

        resp = jsonify(encoded_img)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)