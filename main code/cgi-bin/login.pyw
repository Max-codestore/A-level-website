import cgi, cgitb, os,re,sqlite3
import text_file_manger as tfm
form = cgi.FieldStorage()
#Below these 9 veriables are what tells the site to display which page
create_account = form.getvalue('create_account')
username = form.getvalue('username')
password = form.getvalue('password')
test = form.getvalue('test')
verify = form.getvalue('verify')
approve = form.getvalue('approve')
remove = form.getvalue('remove')
sign_in = form.getvalue('sign_in')
conferm_remove = form.getvalue('conferm_remove')
#these lines print the basic outline for all html pages the site is made off
print("content-type:text/html\n\n")
print("<html>")
print("<head>")
print('<link type="text/css" rel="stylesheet" href="../style.css">')
print('<link rel="shortcut icon" href="../faviconit/favicon.ico">')
print('<link rel="icon" sizes="16x16 32x32 64x64" href="../faviconit/favicon.ico">')
print('<link rel="icon" type="image/png" sizes="196x196" href="../faviconit/favicon-192.png">')
print('<link rel="icon" type="image/png" sizes="160x160" href="../faviconit/favicon-160.png">')
print('<link rel="icon" type="image/png" sizes="96x96" href="../faviconit/favicon-96.png">')
print('<link rel="icon" type="image/png" sizes="64x64" href="../faviconit/favicon-64.png">')
print('<link rel="icon" type="image/png" sizes="32x32" href="../faviconit/favicon-32.png">')
print('<link rel="icon" type="image/png" sizes="16x16" href="../faviconit/favicon-16.png">')
print('<link rel="apple-touch-icon" href="../faviconit/favicon-57.png">')
print('<link rel="apple-touch-icon" sizes="114x114" href="../faviconit/favicon-114.png">')
print('<link rel="apple-touch-icon" sizes="72x72" href="../faviconit/favicon-72.png">')
print('<link rel="apple-touch-icon" sizes="144x144" href="../faviconit/favicon-144.png">')
print('<link rel="apple-touch-icon" sizes="60x60" href="../faviconit/favicon-60.png">')
print('<link rel="apple-touch-icon" sizes="120x120" href="../faviconit/favicon-120.png">')
print('<link rel="apple-touch-icon" sizes="76x76" href="../faviconit/favicon-76.png">')
print('<link rel="apple-touch-icon" sizes="152x152" href="../faviconit/favicon-152.png">')
print('<link rel="apple-touch-icon" sizes="180x180" href="../faviconit/favicon-180.png">')
print('<meta name="msapplication-TileColor" content="#FFFFFF">')
print('<meta name="msapplication-TileImage" content="../faviconit/favicon-144.png">')
print('<meta name="msapplication-config" content="../faviconit/browserconfig.xml">')
print("<title>MKlearn sign in</title>")
print("</head>")
print("<body bgcolor='FFEEFF'>")



class Home:
    def __init__(self):
        self.logged_in = False
        created = False#this is the veriable which if the table has been created it returns true which then means the required accounts are automaticlly approved
        if not os.path.isfile('users.db'):#these lines are responsable for creating the table of users of the website
            created = True
            conn = sqlite3.connect('users.db')
            self.users = conn.cursor()
            self.users.execute("""CREATE TABLE users 
                       (user_ids INTEGER PRIMARY KEY AUTOINCREMENT,
                       allowed_username UNIQUE,
                       allowed_password UNIQUE,
                       applied_username UNIQUE,
                       applied_password UNIQUE 
                       )""")
            conn.commit()
            conn.close()
        self.users_commit = sqlite3.connect('users.db')
        self.users = self.users_commit.cursor()
        self.required_users = [['hills', 'grey', 'davidson-smith', 'max'], ['berry', '7B3dr', 'cherry38', '424209']]#this is the list of required users for the website
        if created == True:
         for i in range(len(self.required_users[0])):
             self.users.execute("INSERT INTO users(allowed_username,allowed_password) VALUES (?,?)",(self.required_users[0][i],self.required_users[1][i]))#used to put the required users in the database if needed
        self.users_commit.commit()
        self.attempt_login = True
        self.account = False

    @staticmethod
    def home(username: str):
        """
        this method creates the home page
        :param username:the username of the site user signed in
        :return:
        """
        tfm.write_text_file([username], 'logged_in.txt')#writes the logged in accounts name to a text file so the site remebers it
        print('<h1> <a href="../login.html"><img src="../images/site_logo.png" width="400" height="200"></a> </h1>')
        print('<div class="form">')
        print("welcome to MKlearn, {0}".format(username))
        print('<p> login successful </p>')
        if username == 'max':#this if statement allows the printing of the admin controls for my own account
            print('<form method = "POST" action = "login.pyw">')
            print('<input type="submit" name="approve" value="approve other users">')
            print('</form>')
            print('<br><br>')
        print('<form method = "POST" action = "login.pyw">')
        print('<input type="submit" name="remove" value="delete your own account">')
        print('</form>')
        print('<br><br>')
        print('<form method = "POST" action = "quiz.pyw">')
        print('<input type="submit" name="view" value="veiw results of a quiz you set">')
        print('<br><br>')
        print('<input type="submit" name="delete" value="delete quiz you set">')
        print('<br><br>')
        print('<input type="submit" name="set" value="set your own quiz">')
        print('<br><br>')
        print('</div>')
        print('</form>')
        print("</body>")
        print("</html>")
    def remove_accounts(self,conferm_remove:bool):
        """
        this method allows people to be able to delete their own accounts
        :param conferm_remove: this is the veriable which controls if the account has been set to be removed
        """
        username = tfm.read_text_file('logged_in.txt')[0]#this featches the username of the person currently logged on
        print('<h1> <a href="../login.html"><img src="../images/site_logo.png" width="400" height="200"></a> </h1>')
        print('<form method = "POST" action = "login.pyw">')
        print('<p> pressing this button below will comferm your will to delete your account</p>')
        print('remove account<input type="submit" name="conferm_remove">')
        if conferm_remove != None:#once the user chooses to remove their account then this script is run to do that
            sql = f"DELETE FROM users WHERE allowed_username = '{username}'"#this removed their account
            self.users.execute(sql)
            self.users_commit.commit()
            sql = f"DELETE FROM quiz WHERE teacher = '{username}'"#this removed all quizes they set
            conn = sqlite3.connect('quiz.db')
            db = conn.cursor()
            db.execute(sql)
            conn.commit()
            sql = f"DELETE FROM quiz_ids_in_use WHERE teacher = '{username}'"#this removed all results from the quizes set
            used_commit = sqlite3.connect('used_ids.db')
            used_ids = used_commit.cursor()
            used_ids.execute(sql)
            used_commit.commit()
            print('<p>account and all data conneted to it has been removed so please use the button below to remove your account </p>')
            print('<a href = "../login.html" >return home</a>')
    def retrive_data_SQL(self, sql: str, table: str, muti: bool):
        """
        this method enables data to be fetched from a sql table 
        :param sql: the SQL which is applied to the table 
        :param table: tells the method which table to apply the SQL statement to
        :param muti: Tells the method if the SQL statement requires to fetch mutiple peases of data rather then a single one 
        :return: it returns the data from the SQL table in a form which it can be used and treated as a veriable 
        """""
        if muti == False and table == 'users':
                get_1 = self.users.execute(sql).fetchall()#takes the data from the sql table
                if get_1 == []:
                    return None
                get_2 = get_1[0]#removes it from the tuple
                get_3 = get_2[0]#removed it from the list to turn it into useable values
                return get_3
        if muti == True and table == 'users':
                get_1 = self.users.execute(sql).fetchall()#extracts data from the sql table
                if get_1 == []:
                    return None
                for get_2 in range(len(get_1)):
                    get_3 = []
                    get_3.append(get_1)
                    get_3 = get_3[0]#extracts the desired data from the tuple
                    return get_3

    def debug_table(self, sql: str):
        """
        This method allows printing of a SQL table in a nice format
        :param self: the self parameter from the class
        :param sql:the SQl statement defining what needs to be printed
        :return:
        """
        self.users.execute(sql)
        all_rows = self.users.fetchall()#gets data from the SQL table
        print('the accouts are writen username|different persons username')
        for row in all_rows:
            for i in row:
                print(i, end='|')#used to print SQL table data
            print()
        print()

    def manage_accounts(self,verify: str):
        """
        this method allows for the approvel of user accounts for administrators
        :param self:the self parameter from the class
        :param verify:the username of the acount to verify
        :return:
        """
        applied = self.users.execute("SELECT applied_username FROM users").fetchall()#grabs all applied usernames only for the purpose of checking if there are any
        print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
        if len(applied) == 0:
            print('<p>there are no accounts which need to be verifyed</p>')
        if verify == None:
            H.debug_table("SELECT applied_username FROM users WHERE applied_username != '' AND applied_password !=''")#prints all applied usernames for the admin to see
            print("<p>enter the username of the account you want to approve</p>")
            print('<form method = "POST" action = "login.pyw">')
            print('teacher to be verified<input type="text" name="verify">')
            print('<br><br>')
            print('<input type="submit" name="confirm remove" value="comfirm the approal of the account with that username">')
            print('</form>')
        if verify != None:
            try:
                sql = f"SELECT applied_password FROM users WHERE applied_username = '{verify}'"#this is the SQL statement to grab the password connected to that username
                password = H.retrive_data_SQL(sql,'users', False)#this actually grabs the password connected to the username
                self.users.execute("INSERT INTO users(allowed_username, allowed_password) VALUES (?,?)",(verify,password))#puts the username and password into the allowed users section
                self.users.execute("DELETE FROM users WHERE applied_password = ? AND applied_username = ?",(password,verify))#deletes them from applied users
                self.users_commit.commit()
                applied = self.users.execute("SELECT applied_username,applied_password FROM users").fetchall()#gets all users which have applied now after the change to update the site
            except:
                print(
                    "<p>enter the username of the account you want to approve</p>")
                print('<p>ops something went wrong</p>')
                print('<form method = "POST" action = "login.pyw">')
                print('teacher to be verified<input type="text" name="verify">')
                print('<br><br>')
                print('<input type="submit" name="confirm remove">')
                print('</form>')
                return

            if len(applied) == 0:
                print('<p>there are no accounts which need to be verifyed</p>')
            H.debug_table("SELECT applied_username FROM users WHERE applied_username != '' AND applied_password !=''")
            print("<p>enter the username of the account you want to approve</p>")
            print('<p>the account was successfully verified</p>')
            print('<form method = "POST" action = "login.pyw">')
            print('teacher to be verified<input type="text" name="verify">')
            print('<br><br>')
            print('<input type="submit" name="confirm remove">')
            print('</form>')
    def log_in(self, username: str, password: str):
        """
        this method allows the website to check if the password and username provided match those within the database
        :param username:the username of the account trying to sign in
        :param password: the password of the account trying to sign in
        :return:
        """
        try:
            username = username.replace(" ", "")#removing the spaces
            password = password.replace(" ", "")
            check = self.users.execute("SELECT * FROM users where allowed_username = ? and allowed_password = ?",(username,password)).fetchall()#checks to make sure a user with the same username and password didnt exist
            if check != []:
                self.logged_in = True#one of the verification stages to sign in
                return self.logged_in
            else:
                print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
                print('<h2>Teacher login </h2>')
                print('<p> username/password was incorrect try again</p>')
                print('<br><br>')
                print('<form method = "POST" action = "login.pyw">')
                print('username <input type = "text" name = "username">')
                print('<br><br>')
                print('password <input type = "password" name = "password">')
                print('<br><br>')
                print('<input type = "submit" value = "Submit" name="sign_in">')
                print('</form>')
                print('<br><br>')
                print('<a href = "../new_account.html" > teachers who dont have a account go here </a>')
                print('<a href = "../student_home.html" > students go here </a>')
                print('</body>')
                return False
        except:
            print('<h1><img src = "../images/site_logo.png" width = "400" height = "200"></h1>')
            print('<h2>Teacher login </h2>')
            print('<p> username/password was incorrect try again</p>')
            print('<br><br>')
            print('<form method = "POST" action = "login.pyw">')
            print('username <input type = "text" name = "username">')
            print('<br><br>')
            print('password <input type = "password" name = "password">')
            print('<br><br>')
            print('<input type = "submit" value = "Submit" name="sign_in">')
            print('</form>')
            print('<br><br>')
            print('<a href = "../new_account.html" > teachers who dont have a account go here </a>')
            print('<a href = "../student_home.html" > students go here </a>')
            print('</body>')
    def new_account(self, username: str, password: str):
        """
        this method allows for new accounts to apply to be approved
        :param username:the username of the account which applied
        :param password:the password of the account which applied
        :return:
        """
        user_check_clone = self.users.execute("SELECT * FROM users where allowed_username = ?",(username,)).fetchall()#checks to make sure the username isnt dublicated
        password_check_clone =  self.users.execute("SELECT * FROM users where allowed_password = ?",(password,)).fetchall()
        usercheck = re.findall(r'[\s]', username)#checks to make sure the new username doesnt have a space in it
        passcheck = re.findall(r'[\s]', password)
        if user_check_clone == [] and password_check_clone == [] and usercheck == [] and passcheck == []:#only passes a username if those passwords arent dublicated and dont contain spaces
            try:
                self.users.execute("INSERT INTO users(applied_username, applied_password) VALUES (?,?)",(username,password))#inserts the username into the database
                self.users_commit.commit()
                print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
                print('<p>enter your username and password you want to use for you account and then wait for it to be approved </p>')
                print('account application competed....waiting response')
                print('<div class ="pyro">')
                print('<div class ="before"> </div>')
                print('<div class ="after"> </div>')
                print('</div>')
                print('<form method = "POST" action = "login.pyw">')
                print('username <input type = "text" name = "username" required>')
                print('<br><br>')
                print('password <input type = "password" name = "password" required>')
                print('<br><br>')
                print('<input type = "submit" value = "create account" name = "create_account">')
                print('</form>')
                print('<a href = "../login.html" > teacher login</a>')
            except:
                print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
                print('<p>enter your username and password you want to use for you account and then wait for it to be approved </p>')
                print('sorry that username/password is invalid')
                print('<form method = "POST" action = "login.pyw">')
                print('username <input type = "text" name = "username" required>')
                print('<br><br>')
                print('password <input type = "password" name = "password" required>')
                print('<br><br>')
                print('<input type = "submit" value = "create account" name = "create_account">')
                print('</form>')
                print('<a href = "../login.html" > teacher login</a>')
        else:
            print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
            print('<p>enter your username and password you want to use for you account and then wait for it to be approved </p>')
            print('sorry that username/password is invalid')
            print('<form method = "POST" action = "login.pyw">')
            print('username <input type = "text" name = "username" required>')
            print('<br><br>')
            print('password <input type = "password" name = "password" required>')
            print('<br><br>')
            print('<input type = "submit" value = "create account" name = "create_account">')
            print('</form>')
            print('<a href = "../login.html" > teacher login</a>')

    def attempt(self, username: str, password: str):
        """
        the method checks the username and password wont break the website then submits
        them to be checked if there is a account connected to them
        :param username: the username of the person trying to log in
        :param password: the password of the person trying to log in
        :return:
        """
        if self.logged_in == False:
            usercheck = re.findall(r'[\s]',username)
            passcheck = re.findall(r'[\s]', password)
            if usercheck != [] or passcheck != [] or password == 'password' or username == 'username':#makes sure submitted passwords dont contain spaces and are just username and password
                print('<h1><a href = "../login.html"><img src = "../images/site_logo.png" width = "400" height = "200"> </a></h1>')
                print('<h2>Teacher login </h2>')
                print('<p> username/password was incorrect try again</p>')
                print('<br><br>')
                print('<form method = "POST" action = "login.pyw">')
                print('<label for = "username">username</label> <input type = "text" name = "username" id = "username" required>')
                print('<br><br>')
                print('<label for = "password">password</label> <input type = "password" name = "password" id = "password" required>')
                print('<br><br>')
                print('<input type = "submit" value = "Submit" name="sign_in">')
                print('</form>')
                print('<br><br>')
                print('<a href = "../new_account.html"> teachers who dont have a account go here </a>')
                print('<a href = "../student_home.html"> students go here </a>')
                print('</body>')
                return None
            self.attempt_login = H.log_in(username, password)
            if self.attempt_login == True:
                H.home(username)

    @staticmethod
    def selector(username:str, password:str, create_account:bool,verify: str,approve:bool,remove:bool,conferm_remove:str,sign_in:bool):
     #this is the method which desides which method is run based on which button you pressed within the site
     if create_account != None:
         H.new_account(username, password)
     if approve != None or verify != None:
         H.manage_accounts(verify)
     if remove != None or conferm_remove != None:
         H.remove_accounts(conferm_remove)
     if sign_in != None:
         H.attempt(username,password)


H = Home()
H.selector(username, password, create_account,verify,approve,remove,conferm_remove,sign_in)
