import mysql.connector
import logging
import os
mydb = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='#Sonawane@21',
                               database='gymdb')
mycursor = mydb.cursor()


class Verify(object):
    def __init__(self):
        self._cached_stamp = 0
        self.trainer_file = 'logs/trainer.log'
        self.owner_file = 'logs/owner.log'

    def verify_trainer(self):
        stamp = os.stat(self.trainer_file).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
    #     if file is changed , i.e new trainer has been added, verify it

    def verify_owner(self):
        stamp = os.stat(self.owner_file).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp