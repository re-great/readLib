import sqlite3


conn = sqlite3.connect('BookUsers.db')
curr = conn.cursor()

with conn:
    curr.execute("CREATE TABLE IF NOT EXISTS Userinfo (UserID text Primary key , Userpass text NOT NULL , UserEmail NOT NULL)")
    curr.execute("CREATE TABLE IF NOT EXISTS ResetPass (Email text Primary key , OTP text NOT NULL)")


# DATABASE DETAILS

def user_details(uid):
    with conn:
        curr.execute("SELECT * FROM Userinfo WHERE UserID = :uid" , {'uid' : uid})
        return curr.fetchone()

def user_check_mail(mail):
    with conn:
        curr.execute("SELECT * FROM Userinfo WHERE UserEmail = :mail" , {'mail' : mail})
        return curr.fetchone()

def insert_user(uid , mail , p):
    with conn:
        curr.execute("INSERT INTO Userinfo VALUES (:uid , :pass , :mail)",{'uid' : uid , 'mail' : mail , 'pass' : p})
        conn.commit()




def update_otp(mail , otp):
    with conn:
        curr.execute("DELETE FROM ResetPass WHERE Email = :email" , {'email' : mail})
        curr.execute("INSERT INTO ResetPass VAlUES (:email , :otp)" , {'email' : mail , 'otp' : otp})
        print(otp , mail , 'successfully updated')

def reset_details(email):
    curr.execute("SELECT * FROM ResetPass WHERE Email = :email" , {'email' : email})
    #print('returned' , curr.fetchone(),'\n\n')
    return curr.fetchone()


def set_pass(uid , mail , password):
    with conn:
        curr.execute("DELETE FROM ResetPass WHERE Email = :email" , {'email' : mail})
        curr.execute("UPDATE Userinfo SET Userpass = :pass WHERE UserID = :uid " , {'pass' : password , 'uid' : uid})
        print('Successfully updated password')


curr.execute("select * from userinfo")
conn.commit()
print(curr.fetchall())