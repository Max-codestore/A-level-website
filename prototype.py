import sqlite3, os, random, time, re
import text_file_manger as tfm
import matplotlib.pyplot as plt

print('welcome to the quiz website prototype')


class Data():#The class Data contains all the methods which deal with the creation of the data given back to teachers when they look at the results for a quiz they set
    @staticmethod
    def make_chart(sql_list:list):#This method creates the bar chart from the quiz data
        results = []
        New_Colors = []
        bars = Data.getbars(sql_list)
        for i in range(len(bars)):
            results.append(sum(bars[i]))
            if sum(bars[i]) >= int(len(bars[i])/2):
                rgb = 'g'
            else:
                rgb = 'r'
            New_Colors.append(rgb)
        questions = ['q1', 'q2', 'q3', 'q4', 'q5','q6','q7','q8','q9','q10']
        plt.bar(questions,results,color=New_Colors)
        plt.title('quiz results', fontsize=14)
        plt.xlabel('question', fontsize=14)
        plt.ylabel('score', fontsize=14)
        plt.grid(True)
        plt.savefig('data.png')
        show = input('do you want to see the graph produced')
        show.lower()
        show.replace(" ","")
        if show in ("y","yes"):
            plt.show()
        pass

    @staticmethod
    def getbars(sql_list: list):#This method forms the bars for the bar chart
        bars = [[] for _ in range(10)]
        for x, extracted in enumerate(sql_list):
            for i in range(10):
                bars[i].append(extracted[i + 2])
        return bars

    @staticmethod
    def average(sql_list: list):#This method returns the avarage score that the class got
        totals = [i[1] for i in sql_list]
        average = sum(totals) / len(totals)
        return average

    @staticmethod
    def student_scores(sql_list:list):#This method forms the table of student results
        score = [[i[0] for i in sql_list],[i[1] for i in sql_list]]
        x = 11
        y = 0
        lowest = []
        scores = []
        for i in range(len(score[1])):
            if score[1][i] <= x:
                x = score[1][i]
                lowest.insert(0,score[0][i])
                scores.insert(0,score[1][i])
            else:
                lowest.append(score[0][i])
                scores.append(score[1][i])
        order = input("which order do you want it to be it desending(D) or asending(A)? ")
        order.lower()
        order.replace(" ","")
        if order in ("a","asending","highesttolowest"):
            lowest.reverse()
            scores.reverse()
        scores.insert(0, '\n')
        table = Data.form_table(lowest)
        test = Data.form_table(scores)
        return table,scores

    @staticmethod
    def form_table(table_base: list):#This method prints out the table fecthed by the 'student_scores' method
        for i in table_base:
            x = print(i, end='|')
        return x


class Quiz():#The class quiz deals with all the elements which are needed for the quiz system to work

    def __init__(self):#This method creates both the databases and other key values the site needs
        if not os.path.isfile('used_ids.db'):
            conn = sqlite3.connect('used_ids.db')
            print('creating table...')
            self.used_ids = conn.cursor()
            self.used_ids.execute("""CREATE TABLE quiz_ids_in_use 
                   (quiz INTEGER PRIMARY KEY AUTOINCREMENT,
                   quizid  UNIQUE,
                   teacher TEXT,
                   quiz_type TEXT
                   )""")
            conn.commit()
            conn.close()
        self.used_commit = sqlite3.connect('used_ids.db')
        self.used_ids = self.used_commit.cursor()

        if not os.path.isfile('quiz.db'):
            conn = sqlite3.connect('quiz.db')
            print('creating table ...')
            self.db = conn.cursor()
            self.db.execute("""CREATE TABLE quiz 
                   (quizids INTEGER PRIMARY KEY AUTOINCREMENT,
                   quizid TEXT,
                   teacher TEXT,
                   student_name TEXT,
                   total_score INTERGER,
                   q1 INTERGER,
                   q2 INTERGER,
                   q3 INTERGER,
                   q4 INTERGER,
                   q5 INTERGER,
                   q6 INTERGER,
                   q7 INTERGER,
                   q8 INTERGER,
                   q9 INTERGER,
                   q10 INTERGER)""")
            conn.commit()
            conn.close()
        self.conn = sqlite3.connect('quiz.db')
        self.db = self.conn.cursor()

    def quiz_id(self, quiz_type: int, username: str):#This is the method which controls the genaration of the quiz codes
        code = ''
        print('gerating code')
        caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(code) != 6:
            x = random.randint(1, 3)
            if x == 1:
                code += random.choice(caps)
            if x == 2:
                code += random.choice(lowercase)
            elif x == 3:
                code += random.choice(numbers)
        try:
            if len(code) >= 7:
                Q.quiz_id(quiz_type, username)
            self.used_ids.execute(
                "INSERT INTO quiz_ids_in_use(quizid,quiz_type,teacher) VALUES ('{0}',\'{1}',\'{2}')".format(code,
                                                                                                            quiz_type,
                                                                                                            username))
            self.used_commit.commit()
            return code
        except:
            print('ID which was genrated was already in use..regenarting one')
            Q.quiz_id(quiz_type, username)
    @staticmethod
    def set(username: str):#This method controls the type of quiz which the user is attempting to set
        quiz_number = input("which quiz do you want to set: 1:countries locations, 2:WW2 history  or 3:")
        if quiz_number == '1':
            print('you have set quiz 1')
            x = Q.quiz_id(1, username)
            print('the code for that quiz is {0}'.format(x))
        elif quiz_number == '2':
            print('you have set quiz 2')
            x = Q.quiz_id(2, username)
            print('the code for that quiz is {0}'.format(x))
        elif quiz_number == '3':
            print('you have set quiz 3')
            x = Q.quiz_id(3, username)
            print('the code for that quiz is {0}'.format(x))

    def debug_table(self, sql: str, table: str):#This method is used to print SQL tables mainly for debugging uses
        if table == 'id_use':
            self.used_ids.execute(sql)
            all_rows = self.used_ids.fetchall()
            print('this is the SQl table you wanted')
            for row in all_rows:
                for i in row:
                    print(i, end='|')
                print()
            print()
        else:
            self.db.execute(sql)
            all_rows = self.db.fetchall()
            print('this is the SQL table you wanted')
            for row in all_rows:
                for i in row:
                    print(i, end='|')
                print()
            print()
    @staticmethod
    def results(username: str):#This is the method responsable for returning the results of the quiz to the teacher by calling the methods inside class "Data"
        sql = ("SELECT quizid FROM quiz WHERE teacher = '{0}'".format(username))
        codes = Q.debug_table(sql, '')
        quizid = input('what quiz code was your quiz assigned (this is case sensitive) or press enter to return to home ')
        if quizid == '':
            return
        x = 0
        sql = ("SELECT student_name,total_score,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM quiz WHERE quizid = '{0}' AND teacher = '{1}' ".format(quizid, username))

        f = (Q.retrive_data_SQL(sql, '', True))
        if f is None:
            return
        x = Data.average(f)
        z = Data.make_chart(f)
        b = Data.student_scores(f)
        print('\n the avarge score {0}'.format(x))

    def do_quiz(self):#This is the method which allows a student to do the quiz
        quiz_number = None
        while quiz_number is None:
            code = input('what code is the quiz you are doing given')
            sql = ("SELECT quiz_type FROM quiz_ids_in_use WHERE quizid = '{0}'".format(code))
            quiz_number = Q.retrive_data_SQL(sql, 'id_use', False)
            if quiz_number is None:
                print('code wasnt reginised sorry :(')
                retry = input('do you want to re-enter a code type y or yes to re-enter a code')
                retry.lower()
                if not (retry == 'yes' or retry == 'y'):
                    return
        sql = ("SELECT teacher FROM quiz_ids_in_use WHERE quizid = '{0}'".format(code))
        teacher = Q.retrive_data_SQL(sql, 'id_use', False)
        if quiz_number == '1':  # note:quiz number is a string
            name = input('What is your name?')
            namecheck = re.findall(r'[\s]', name)
            while namecheck != []:
                print("sorry but your name can't contain spaces")
                name = input('What is your name?')
                namecheck = re.findall(r'[\s]', name)
            q1 = input('Which continent is Spain in?')
            q1 = q1.lower()
            q1 = q1.replace(" ", "")
            if q1 == 'europe':
                q1 = 1
            else:
                q1 = 0
            q2 = input('Which continent is Japan in?')
            q2 = q2.lower()
            q2 = q2.replace(" ", "")
            if q2 == 'asia':
                q2 = 1
            else:
                q2 = 0
            q3 = input('Which continent is Madagascar in?')
            q3 = q3.lower()
            q3 = q3.replace(" ", "")
            if q3 == 'africa':
                q3 = 1
            else:
                q3 = 0
            q4 = input('Which continent is Bolivia in?')
            q4 = q4.lower()
            q4 = q4.replace(" ", "")
            if q4 == 'southamerica':
                q4 = 1
            else:
                q4 = 0
            q5 = input('Which continent is Canada in?')
            q5 = q5.lower()
            q5 = q5.replace(" ", "")
            if q5 == 'northamerica':
                q5 = 1
            else:
                q5 = 0
            q6 = input('Which continent is New Zealand in?')
            q6 = q6.lower()
            q6 = q6.replace(" ", "")
            if q6 == 'australasia' or q6 == 'oceania':
                q6 = 1
            else:
                q6 = 0
            q7 = input('Which continent is the Falkland Islands in?')
            q7 = q7.lower()
            q7 = q7.replace(" ", "")
            if q7 == 'southamerica':
                q7 = 1
            else:
                q7 = 0
            q8 = input('Which continent is Belarus in?')
            q8 = q8.lower()
            q8 = q8.replace(" ", "")
            if q8 == 'europe':
                q8 = 1
            else:
                q8 = 0
            q9 = input('Which continent is Croatia in?')
            q9 = q9.lower()
            q9 = q9.replace(" ", "")
            if q9 == 'europe':
                q9 = 1
            else:
                q9 = 0
            q10 = input('Which continent is Vietnam in?')
            q10 = q10.lower()
            q10 = q10.replace(" ", "")
            if q10 == 'asia':
                q10 = 1
            else:
                q10 = 0
            total = q1 + q3 + q2 + q4 + q5 + q6 + q7 + q8 + q9 + q10
            print(f"you got {total} out of 10")
            self.db.execute(
                "INSERT INTO quiz(quizid,teacher,student_name,total_score,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10) VALUES ('{0}',\'{1}',\'{2}',\'{3}',\'{4}',\'{5}',\'{6}',\'{7}',\'{8}',\'{9}',\'{10}',\'{11}',\'{12}',\'{13}')".format(
                    code, teacher, name, total, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))
            self.conn.commit()
            H.attempt()

    def retrive_data_SQL(self, sql: str, table: str, muti: bool):#This is the method which allows the retreval of data from databases for manipulation needed to produce the student results
        """
        the functuion which is needed to get sql quires into usale veriables
        :param sql: the sl quire itself
        :param table: if your using the id_use table or not
        :param muti: if you want to just pull one or mutiple bits of data
        :return: the sql quirey you asked in a useable state
        """
        if table == 'id_use' and muti == False:
            get_1 = self.used_ids.execute(sql).fetchall()
            if get_1 == []:
                return None
            get_2 = get_1[0]
            get_3 = get_2[0]
            return get_3

        if table == '' and muti == False:
            get_1 = self.db.execute(sql).fetchall()
            if get_1 == []:
                return None
            get_2 = get_1[0]
            get_3 = get_2[0]
            return get_3

        if muti == True and table == 'id_use':
            get_1 = self.used_ids.execute(sql).fetchall()
            if get_1 == []:
                return None
            for get_2 in range(len(get_1)):
                get_3 = []
                get_3.append()
                get_3 = get_3[0]
                return get_3

        if muti == True and table == '':
            get_1 = self.db.execute(sql).fetchall()
            if get_1 == []:
                return None
            for get_2 in range(len(get_1)):
                get_3 = []
                get_3.append(get_1)
                get_3 = get_3[0]
                return get_3
        else:
            return Exception.with_traceback()

    def delete_quiz(self, username: str):#This is the method which allows teachers to delete a quiz
        which_quiz = input("what is the code of the quiz you want to delete?")
        sql = "DELETE FROM quiz WHERE quizid = '{0}' AND teacher = '{1}'".format(which_quiz, username)
        self.db.execute(sql)
        sql = "DELETE FROM quiz_ids_in_use WHERE quizid = '{0}' AND teacher = '{1}'".format(which_quiz, username)
        self.used_ids.execute(sql)


class Home:#This is a class which controls the signing into the system

    def __init__(self):#This is a method sorts out a few key vales and makes sure critical accounts exist
        self.logged_in = False
        if not os.path.isfile("verified.txt"):
            tfm.write_text_file_2d(
                [['hills', 'grey', 'davidson-smith', 'max'], ['berry', '7B3dr', 'cherry38', '424209']], 'verified.txt',
                '\n')
        self.allowed_pass_teacher = tfm.read_text_file_2D('verified.txt')
        self.user = input("are you a student or a teacher?")
        self.user = self.user.replace(" ", "")
        self.user = self.user.lower()
        self.attempt_login = False
        self.ddos = 0

    def manage_accounts(self):#This is the method which is used by admin accounts
        x = tfm.read_text_file_2D('application_teachers.txt')
        y = tfm.read_text_file_2D('verified.txt')
        print(x)
        contiune = True
        while contiune:
            if not len(x) != 0:
                contiune = False
            which_ones = int(input('which user do you want to approve?'))
            for i in range(2):
                y[i].append(x[i].pop(which_ones))  #need to extract the array from verified.txt and then append this array into it
            tfm.write_text_file_2d(x, 'application_teachers.txt', '\n')
            tfm.write_text_file_2d(y, 'verified.txt', '\n')
            another = input('do you want to verify another user?')
            another.lower()
            if another in ('n', 'no'):
                contiune = False

    def new_account(self, username: str, password: str):#This method allows any teacher to create a teacher account
        y = tfm.read_text_file_2D('application_teachers.txt')
        b = username not in list(self.allowed_pass_teacher[0])
        x = password not in list(self.allowed_pass_teacher[1])
        if b != True or x != True:
            print('sorry that username/password is unavaliable')
            return
        if y == []:
            y = [[], []]
        x = [username, password]
        for i in range(2):
            y[i].append(x[i])
        tfm.write_text_file_2d(y, 'application_teachers.txt', '\n')
        print('account application competed....waiting response')

    def home(self, username: str):#This is the method which controls the home page and allows access to other parts of the program
        """
        the homepage simulastion
        :param username:
        :return:
        """
        print("welcome to MKlearn, {0}".format(username))
        if username == 'max':
            approve = input('do you want to verifiy usernames? y or n')
            approve.lower()
            if approve in ('y', 'yes'):
                H.manage_accounts()
        task = input(
            "what do you want to do? set quiz (S) or veiw quiz results (V) or log out (L) or delete a quiz (D) ")
        task = task.lower()
        if task in ('set quiz', 's', 'q'):
            Q.set(username)
        if task in ('veiw quiz results', 'v', 'r'):
            Q.results(username)
        if task in ("delete quiz", "delete", "d"):
            Q.delete_quiz(username)
        if task in ('log out', 'l', 'logout'):
            self.attempt_login = False

    def log_in(self, username: str, password: str):#This is the method which attempts to log a user into their account
        try:
            username = username.replace(" ", "")
            password = password.replace(" ", "")
            x = self.allowed_pass_teacher[0].index(username)
            y = self.allowed_pass_teacher[1].index(password)
            if x == y:
                self.logged_in = True
                return self.logged_in
        except:
            print('login failed..password incorrect')
            return self.logged_in

    def attempt(self):#This is a method which checks if a password is valid to attempt a login
        while self.logged_in == False and self.user == 'teacher':
            username = input('what is your username? ')
            password = input('what is your password? ')
            usercheck = re.findall(r'[\s]',username)
            passcheck = re.findall(r'[\s]', password)
            if passcheck != [] or usercheck != [] or password == '' or username == '':
                print('dont use spaces/nothing in your username or password'
                      ' your password has defulted to password and your username to usernmame'
                      ' please just skip the create account if you want it to be secure')
                username = 'username'
                password='password'
            logged_in = H.log_in(username, password)
            self.attempt_login = logged_in
            self.ddos += 1
            if self.attempt_login == False:
                create_account = input('do you want to create a account with those credentals')
                create_account.lower()
                if create_account in ('yes', 'y', 'do it'):
                    H.new_account(username, password)
            if self.ddos >= 3 and self.attempt_login == False:
                print('too many missed attempts..please wait')
                time.sleep(10)
                self.ddos = 0
            while self.attempt_login == True:
                H.home(username)
        if self.user == 'student':
            retry = True
            while retry == True:
                Q.do_quiz()
                retry = input('do you want to do another quiz?')
                retry.lower()
                if retry == 'n' or retry == 'no':
                    retry = False
        else:
            self.logged_in = False
            self.user = input('are you a student or a teacher?')
            H.attempt()
Q = Quiz()
H = Home()
H.attempt()
