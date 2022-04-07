import mysql.connector
import logging
import os
mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='#Sonawane@21',
                               database='gymdb')
mycursor = mydb.cursor()


class Verify(object):
    def __init__(self):
        self.trainer_cached_stamp = 0
        self.owner_cached_stamp = 0
        self.trainer_file = 'logs/trainer.log'
        self.owner_file = 'logs/owner.log'

    def verify_trainer(self):
        get_unverifiedtrainer = "select trainerid from trainer where verified = 0"

    def verify_owner(self):
        stamp = os.stat(self.owner_file).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            print("yes")


v = Verify()
v.verify_trainer()
v.verify_owner()
v.write()