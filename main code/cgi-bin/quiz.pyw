import cgi,cgitb,sqlite3,os,re,random,data
import text_file_manger as tfm
#this is the code to retrive the user logged in
username = tfm.read_text_file('logged_in.txt')[0]
form = cgi.FieldStorage()
#these are all the form values the site needs to get
set_ = form.getvalue('set')
delete = form.getvalue('delete')
view = form.getvalue('view')
code = form.getvalue('code')
approve = form.getvalue('approve')
testing = form.getvalue('test')
quizid = form.getvalue('quizid')
q1 = form.getvalue('q1')
q2 = form.getvalue('q2')
q3 = form.getvalue('q3')
q4 = form.getvalue('q4')
q5 = form.getvalue('q5')
q6 = form.getvalue('q6')
q7 = form.getvalue('q7')
q8 = form.getvalue('q8')
q9 = form.getvalue('q9')
q10 = form.getvalue('q10')
name = form.getvalue('name')
order = form.getvalue('order')
quiz_num = form.getvalue('quiz_num')
verify_type = form.getvalue("verify_type")
confirm_remove= form.getvalue("confirm_remove")
which_quiz = form.getvalue('remove_id')
remove = form.getvalue("remove")
create_quiz = form.getvalue('create_quiz')
set_quiz = form.getvalue('set_quiz')
do_quiz = form.getvalue('do_quiz')
enter_quiz = form.getvalue('enter_quiz')
quiz_title = form.getvalue('quiz_title')
question1 = form.getvalue('question1')
question2 = form.getvalue('question2')
question3 = form.getvalue('question3')
question4 = form.getvalue('question4')
question5 = form.getvalue('question5')
question6 = form.getvalue('question6')
question7 = form.getvalue('question7')
question8 = form.getvalue('question8')
question9 = form.getvalue('question9')
question10 = form.getvalue('question10')
answer_correct1 = form.getvalue('answer_correct1')
answer_correct2 = form.getvalue('answer_correct2')
answer_correct3 = form.getvalue('answer_correct3')
answer_correct4 = form.getvalue('answer_correct4')
answer_correct5 = form.getvalue('answer_correct5')
answer_correct6 = form.getvalue('answer_correct6')
answer_correct7 = form.getvalue('answer_correct7')
answer_correct8 = form.getvalue('answer_correct8')
answer_correct9 = form.getvalue('answer_correct9')
answer_correct10 = form.getvalue('answer_correct10')
answer_incorrect1 = form.getvalue('answer_incorrect1')
answer_incorrect2 = form.getvalue('answer_incorrect2')
answer_incorrect3 = form.getvalue('answer_incorrect3')
answer_incorrect4 = form.getvalue('answer_incorrect4')
answer_incorrect5 = form.getvalue('answer_incorrect5')
answer_incorrect6 = form.getvalue('answer_incorrect6')
answer_incorrect7 = form.getvalue('answer_incorrect7')
answer_incorrect8 = form.getvalue('answer_incorrect8')
answer_incorrect9 = form.getvalue('answer_incorrect9')
answer_incorrect10 = form.getvalue('answer_incorrect10')
submit_quiz = form.getvalue('end_quiz')
preview_quiz = form.getvalue('preveiw_quiz')
remove_title = form.getvalue('remove_title')
results = form.getvalue('results')
print("content-type:text/html\n\n")
print("<html>")
print("<head>")
print('<link rel="shortcut icon" href="../faviconit/favicon.ico">')#this is the script needed to produce the websites icon on the tab
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
print('<link type="text/css" rel="stylesheet" href="../style.css">')
print("<title>Welcome {0}</title>".format(username))
print("</head>")
print("<body>")



class Quiz():
    def __init__(self):
        self.D = data.Data()
        if not os.path.isfile('used_ids.db'):#checks if the used_ids database exists, if it doesnt then this creates it
            conn = sqlite3.connect('used_ids.db')
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

        if not os.path.isfile('quiz.db'):#creates the quiz table
            conn = sqlite3.connect('quiz.db')
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
                   q10 INTERGER)
                """)
            conn.commit()
            conn.close()
        self.conn = sqlite3.connect('quiz.db')
        self.db = self.conn.cursor()

        if not os.path.isfile('custom_quiz.db'):#creates the table needed to make the custom quiz
            conn = sqlite3.connect('custom_quiz.db')
            self.custom_quiz = conn.cursor()
            self.custom_quiz.execute("""CREATE TABLE custom_quiz
                   (quiz_number INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT UNIQUE,
                   q1 TEXT,
                   q1_correct TEXT,
                   q1_incorrect TEXT,
                   q2 TEXT,
                   q2_correct TEXT,
                   q2_incorrect TEXT,
                   q3 TEXT,
                   q3_correct TEXT,
                   q3_incorrect TEXT,
                   q4 TEXT,
                   q4_correct TEXT,
                   q4_incorrect TEXT,
                   q5 TEXT,
                   q5_correct TEXT,
                   q5_incorrect TEXT,
                   q6 TEXT,
                   q6_correct TEXT,
                   q6_incorrect TEXT,
                   q7 TEXT,
                   q7_correct TEXT,
                   q7_incorrect TEXT,
                   q8 TEXT,
                   q8_correct TEXT,
                   q8_incorrect TEXT,
                   q9 TEXT,
                   q9_correct TEXT,
                   q9_incorrect TEXT,
                   q10 TEXT,
                   q10_correct TEXT,
                   q10_incorrect TEXT)
                """)
            conn.commit()
            conn.close()
        self.custom_quiz_connect = sqlite3.connect('custom_quiz.db')
        self.custom_quiz = self.custom_quiz_connect.cursor()


    def quiz_id(self, quiz_type: int, username: str):
        code = '' #this is the method which makes the code which is attached to each quiz
        print('<p>gerating code</p>')
        caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while len(code) != 6:
            x = random.randint(1, 3)#this controls if the program selects a capital letter,lowercase letter or a number for each charater of the code
            if x == 1:
                code += random.choice(caps)#selects what charater from the selected charater type to use
            if x == 2:
                code += random.choice(lowercase)
            elif x == 3:
                code += random.choice(numbers)
        try:
            if len(code) >= 7:
                Q.quiz_id(quiz_type, username)
            self.used_ids.execute("INSERT INTO quiz_ids_in_use(quizid,quiz_type,teacher) VALUES (?,?,?)",(code,quiz_type,username))#adds the code,quiz type and teacher to the in use database
            self.used_commit.commit()
            print('<p>The code for that quiz is {0}</p>'.format(code))
            return code
        except:
            print('<p>ID which was genrated was already in use..regenarting one</p>')
            Q.quiz_id(quiz_type, username)

    def set(self,preview_error:str):
        print("<p>Which quiz do you want to set from the list of already made quizzes or do you want to make your own</p>")
        sql = "SELECT title FROM custom_quiz"
        titles = Q.retrive_data_SQL(sql,'custom_quiz',True)#fetches all titles of the quizes
        sql = "SELECT quiz_number FROM custom_quiz"
        number = Q.retrive_data_SQL(sql,'custom_quiz',True)#fetches all the numbers of the quiz
        print('<p>The already made quizzes</p>')
        if preview_error != None:
            print('<p>{0}</p>'.format(preview_error))
        for i in range(len(titles)):
            print('<form method = "POST" action = "quiz.pyw">')
            print('<input type="radio" name="quiz_num" value="{0}">{1}'.format(number[i][0],titles[i][0]))#used to print all of these quizes to be selected
        print('<br><br>')
        print('<input type="submit" name="set_quiz" value="Set the selected quiz">')
        print('<input type="submit" name="create_quiz" value="Create a Quiz">')
        print('<input type="submit" name="preveiw_quiz" value="Preveiw selected">')
        print('</form>')
        print("</body>")
        print("</html>")


    def create_quiz(self,enter_quiz:str,title:str,question1:str,question2:str,question3:str,question4:str,question5:str,question6:str,question7:str,question8:str,question9:str,question10:str,answer_correct1:str,answer_correct2:str,answer_correct3:str,answer_correct4:str,answer_correct5:str,answer_correct6:str,answer_correct7:str,answer_correct8:str,answer_correct9:str,answer_correct10:str,answer_incorrect1:str,answer_incorrect2:str,answer_incorrect3:str,answer_incorrect4:str,answer_incorrect5:str,answer_incorrect6:str,answer_incorrect7:str,answer_incorrect8:str,answer_incorrect9:str,answer_incorrect10:str):
        print('<p>Welcome to the quiz creator menu</p>')
        print('<p>the question box is where you put the question,the correct answer box is where the correct answer is put'
              ' and the incorrect answer box is where the incorrect answer is put</p>')
        print('<form method = "POST" action = "quiz.pyw">')
        if enter_quiz == None:
            print('quiz title<input name="quiz_title" type="text" required>')
            print('<br><br>')
            print('question 1<input name="question1" type="text" required>'
                  'correct answer 1<input name="answer_correct1" type="text" required>'
                  'incorrect answer 1<input name="answer_incorrect1" type="text" required>'
                  '<br><br>')
            for i in range(9):#used to make the page on creating quizes
                print('question {0}<input name="question{0}" type="text">'
                      'correct answer {0}<input name="answer_correct{0}" type="text">'
                      'incorrect answer {0}<input name="answer_incorrect{0}" type="text">'
                      '<br><br>'.format(i + 2))
            print('<input type="submit" name="enter_quiz" value="Create the quiz">')
            print('<a href = "../login.html" >return home</a>')
        else:
            try:
                self.custom_quiz.execute("INSERT INTO custom_quiz(title, q1, q1_correct, q1_incorrect, q2, q2_correct, q2_incorrect, q3, q3_correct, q3_incorrect, q4, q4_correct, q4_incorrect, q5, q5_correct, q5_incorrect, q6, q6_correct, q6_incorrect, q7, q7_correct, q7_incorrect, q8, q8_correct, q8_incorrect, q9, q9_correct, q9_incorrect, q10, q10_correct, q10_incorrect) "
                                        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(title,question1,
                                                                                              answer_correct1,
                                                                                              answer_incorrect1,
                                                                                              question2,answer_correct2,
                                                                                              answer_incorrect2,
                                                                                              question3,answer_correct3,
                                                                                              answer_incorrect3,
                                                                                              question4,answer_correct4,
                                                                                              answer_incorrect4,
                                                                                              question5,answer_correct5,
                                                                                              answer_incorrect5,
                                                                                              question6,answer_correct6,
                                                                                              answer_incorrect6,
                                                                                              question7,answer_correct7,
                                                                                              answer_incorrect7,
                                                                                              question8,answer_correct8,
                                                                                              answer_incorrect8,
                                                                                              question9,answer_correct9,
                                                                                              answer_incorrect9,
                                                                                              question10,
                                                                                              answer_correct10,
                                                                                              answer_incorrect10))#adds all the needed data about a custom quiz to the database
                self.custom_quiz_connect.commit()
                print('<p>quiz created</p>')
            except:#used to remake the create custom quiz page if inserting errors
                print('<p>The title you used wasnt unique please resubmit the quiz with a different title ')
            print('question 1<input name="question1" type="text">'
                  'correct answer 1<input name="answer_correct1" type="text">'
                  'incorrect answer 1<input name="answer_incorrect1" type="text">'
                  '<br><br>')
            for i in range(9):
                print('question {0}<input name="question{0}" type="text">'
                      'correct answer {0}<input name="answer_correct{0}" type="text">'
                      'incorrect answer {0}<input name="answer_incorrect{0}" type="text">'
                      '<br><br>'.format(i + 2))
            print('<input type="submit" name="enter_quiz" value="Create the quiz">')
            print('Return to the set quiz screen<input type="submit" name="set">')
    def debug_table(self, sql: str, table: str,subtext: str):
        if table == 'id_use':#used to get data from the id in use table
            self.used_ids.execute(sql)
            all_rows = self.used_ids.fetchall()#gets sql data
            print(subtext)
            for row in all_rows:
                for i in row:
                    print(i, end='|')#prints out the table
                print()
            print()
            return None
        if table == 'custom':#used for the custom quiz table
            self.custom_quiz.execute(sql)
            all_rows = self.custom_quiz.fetchall()#gets sql data
            print(subtext)
            for row in all_rows:
                for i in row:
                    print(i, end='|')#prints out the table
                print()
            print()
            return None
        else:
            self.db.execute(sql)#used for the quiz data table
            all_rows = self.db.fetchall()#gets sql data
            print(subtext)
            for row in all_rows:
                for i in row:
                    print(i, end='|')#prints out the table
                print()
            print()
            return None


    def results(self,username: str,quizid:str,order:str,results:str):
        if quizid == None or quizid == '' and results != None:
            sql = f"SELECT quizid,quiz_type FROM quiz_ids_in_use WHERE teacher = '{username}'"
            quiz_data = Q.retrive_data_SQL(sql,'id_use',True)#used to fetch the quizid's and types of a certain teacher
            quiz_codes = []
            quiz_type = []
            quiz_titles = []
            quiz_attempts = []
            for i in range(len(quiz_data)):#all used in forming a table of codes,titles and attempt numbers
                quiz_codes.append(quiz_data[i][0])
                quiz_type.append(quiz_data[i][1])
                sql = f"SELECT title FROM custom_quiz WHERE quiz_number = '{quiz_type[i]}'"#gets the title of each quiz code
                quiz_title = Q.retrive_data_SQL(sql,'custom_quiz',False)
                if quiz_title == None:
                    quiz_title = 'this quiz has been removed'
                quiz_titles.append(quiz_title)
                sql = f"SELECT student_name FROM quiz WHERE quizid = '{quiz_codes[i]}'"#gets the names of each student
                partisapents = Q.retrive_data_SQL(sql,'',True)
                if partisapents == None:
                    partisapents = 0
                else:
                    partisapents = len(partisapents)#used to work out the number of students who attempted
                quiz_attempts.append(partisapents)
            print('<div class="floatLeft1">')
            print('<table border="3">'
                  '<caption>your quizzes</caption>'
                  '<tr>'
                  '<th>code</th>'
                  '<th>title</th>'
                  '<th>attampts</th>'
                  '</tr>')
            for i in range(len(quiz_data)):#used to print the table data
                print('<tr>'
                      '<td>{0}</td>'
                      '<td>{1}</td>'
                      '<td>{2}</td>'
                        '</tr>'.format(quiz_codes[i],quiz_titles[i],quiz_attempts[i]))
            print('</table>')
            print('</div>')
            print('<p>What quiz code was your quiz assigned (this is case sensitive)</p>')
            print('<form method="post" action="quiz.pyw">')
            print('<br><br>')
            print('<p>Please enter the code for the quiz you want to view</p>')
            print('code<input maxlength="6" name="quizid" type="text" required>')
            print('<br><br>')
            print('<p>The site will genrate a table of resuts for you.if you want it in asending order please check the circle below</p>')
            print('<br><br>')
            print('Check and submit to change the list order to desending order<input type="radio" name="order" value="asending">')
            print('<br><br>')
            print('<input type="submit" value="submit"name="results">')
            print('</form>')
            print('<br><br>')
            return None
        sql = f"SELECT student_name,total_score,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM quiz WHERE quizid = '{quizid}' AND teacher = '{username}'"
        quiz_data = (Q.retrive_data_SQL(sql, '', True))#fetches the quiz data
        if quiz_data == None or quizid == []:
            sql = f"SELECT quizid,quiz_type FROM quiz_ids_in_use WHERE teacher = '{username}'"
            quiz_data = Q.retrive_data_SQL(sql,'id_use',True)
            quiz_codes = []
            quiz_type = []
            quiz_titles = []
            quiz_attempts = []
            for i in range(len(quiz_data)):
                quiz_codes.append(quiz_data[i][0])
                quiz_type.append(quiz_data[i][1])
                sql = f"SELECT title FROM custom_quiz WHERE quiz_number = '{quiz_type[i]}'"
                quiz_title = Q.retrive_data_SQL(sql,'custom_quiz',False)
                if quiz_title == None:
                    quiz_title = 'this quiz has been removed'
                quiz_titles.append(quiz_title)
                sql = f"SELECT student_name FROM quiz WHERE quizid = '{quiz_codes[i]}'"
                partisapents = Q.retrive_data_SQL(sql,'',True)
                if partisapents == None:
                    partisapents = 0
                else:
                    partisapents = len(partisapents)
                quiz_attempts.append(partisapents)#used to remake the table assuming the selected quiz had no data
            print('<div class="floatLeft">')
            print('<table border="3">'
                  '<caption>your quizzes</caption>'
                  '<tr>'
                  '<th>code</th>'
                  '<th>title</th>'
                  '<th>attampts</th>'
                  '</tr>')
            for i in range(len(quiz_data)):
                print('<tr>'
                      '<td>{0}</td>'
                      '<td>{1}</td>'
                      '<td>{2}</td>'
                        '</tr>'.format(quiz_codes[i],quiz_titles[i],quiz_attempts[i]))
            print('</table>')
            print('<p>What quiz code was your quiz assigned (this is case sensitive)</p>')
            print('<form method="post" action="quiz.pyw">')
            print('<br><br>')
            print('<p>Sorry the code you entered has no data attached to it</p>')
            print('code<input maxlength="6" name="quizid" type="text" required>')
            print('<br><br>')
            print('<p>The site will genrate a table of resuts for you.if you want it in desending order please check the circle below</p>')
            print('<br><br>')
            print('Check and submit to change the list order to desending order<input type="radio" name="order" value="asending">')
            print('<br><br>')
            print('<input type="submit" value="submit">')
            print('</form>')
            return 
        print('<h1><img src = "../images/site_logo.png" width = "400" height = "200"></h1>')
        print('<div class="title2">')
        print(f'<p>Results of the quiz with the ID of {quizid}</p>')
        print('</div>')
        chart = self.D.make_chart(quiz_data)#makes the chart
        avarage = self.D.average(quiz_data)#works out avarage
        scores = self.D.student_scores(quiz_data,order)#makes the table
        print(f'<p> {avarage} is the class avarage score</p>')

    def do_quiz(self,code,error):
        quiz_number = None
        while quiz_number is None:
            sql = f"SELECT quiz_type FROM quiz_ids_in_use WHERE quizid = '{code}'"
            quiz_number = Q.retrive_data_SQL(sql, 'id_use', False)#used to gain the type of quiz based on the code
            if quiz_number == None and code == None:
                print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>')
                print('<p>Enter the 6 charater code from your teacher into the box below.</p>'
                      '<p>Please be aware that the code is case sensive</p>'
                      '<form method = "post" action = "quiz.pyw">'
                      '<br><br>'
                      '<p>Please enter a code</p>'
                      'code<input maxlength = "6" name = "code" type = "text">'
                      '<br><br>'
                      '<input type = "submit" value = "submit" name = "do_quiz">'
                      '</form>'
                      '<br><br>'
                      '<a href = "../login.html" > teacher login </a>')
                return None
            elif quiz_number == None and code != None:
                print('<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>'
                      '<p>Enter the 6 charater code from your teacher into the box below.</p>'
                      '<p>Please be aware that the code is case sensive</p>'
                      '<form method = "post" action = "quiz.pyw">'
                      '<br><br>'
                      '<p>This quiz doesnt exist</p>'
                      'code<input maxlength = "6" name = "code" type = "text">'
                      '<br><br>'
                      '<input type = "submit" value = "submit" name = "do_quiz">'
                      '</form>'
                      '<br><br>'
                      '<a href = "../login.html" > teacher login </a>')
                return None

        else:
            if error == True:
                tfm.write_text_file([code], 'code.txt')
                sql = f"SELECT title FROM custom_quiz where quiz_number = '{quiz_number}'"
                titles = Q.retrive_data_SQL(sql, 'custom_quiz', False)#if error occours then write the code to a text file incase
                if titles == None:
                    print(
                        '<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>'
                        '<p>Enter the 6 charater code from your teacher into the box below.</p>'
                        '<p>Please be aware that the code is case sensive</p>'
                        '<form method = "post" action = "quiz.pyw">'
                        '<br><br>'
                        '<p>The quiz attached to this code has no data or has been deleted by a admin</p>'
                        'code<input maxlength = "6" name = "code" type = "text">'
                        '<br><br>'
                        '<input type = "submit" value = "submit" name = "do_quiz">'
                        '</form>'
                        '<br><br>'
                        '<a href = "../login.html" > teacher login </a>')
                    return None
                sql = f"SELECT q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM custom_quiz where quiz_number = '{quiz_number}'"
                questions = Q.retrive_data_SQL(sql, 'custom_quiz', True)
                sql = f"SELECT q1_correct,q2_correct,q3_correct,q4_correct,q5_correct,q6_correct,q7_correct,q8_correct,q9_correct,q10_correct FROM custom_quiz where quiz_number = '{quiz_number}'"
                correct_answers = Q.retrive_data_SQL(sql, 'custom_quiz', True)
                sql = f"SELECT q1_incorrect,q2_incorrect,q3_incorrect,q4_incorrect,q5_incorrect,q6_incorrect,q7_incorrect,q8_incorrect,q9_incorrect,q10_incorrect FROM custom_quiz where quiz_number = '{quiz_number}'"#all there of these statements are used to extract all needed information for the quiz
                incorrect_answers = Q.retrive_data_SQL(sql, 'custom_quiz', True)
                print('<h1><img src = "../images/site_logo.png" width = "400" height = "200"> </h1>')
                print('<p>Welcome to the {0}</p>'.format(titles))
                print('<p>please enter a different username</p>')
                print('<form method = "POST" required action = "quiz.pyw">')
                print('<div class ="name">')
                print('Name: <input type = "text" name = "name" required>')
                print('</div>')
                question = []
                for i in range(len(questions[0])):
                    question.append(i)#automatically numbers the questions
                for i in range(len(questions[0])):
                    thrid_answer = None
                    while thrid_answer == None or thrid_answer == i:
                        thrid_answer = random.choice(question)
                    question.remove(thrid_answer)#removes the thrid answer once selected
                    print('<div class ="radio-toolbar">')
                    if questions[0][i] == None:#prevents it getting stuck
                        break
                    order = random.randint(1, 3)#used to randomise where the different answers go
                    if order == 1:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{0}<input type = "radio" name = "q{3}" value = "{0}">'
                              '{1}<input type = "radio" name = "q{3}" value = "{1}">'
                              '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],
                                                                                             incorrect_answers[0][i],
                                                                                             incorrect_answers[0][
                                                                                                 thrid_answer], i + 1))
                    elif order == 2:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                              '{0}<input type = "radio" name = "q{3}" value = "{0}">'
                              '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],
                                                                                             incorrect_answers[0][i],
                                                                                             incorrect_answers[0][
                                                                                                 thrid_answer], i + 1))
                    else:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                              '{2}<input type = "radio" name = "q{3}" value = "{2}">'
                              '{0}<input type = "radio" name = "q{3}" value = "{0}">'.format(correct_answers[0][i],
                                                                                             incorrect_answers[0][i],
                                                                                             incorrect_answers[0][
                                                                                                 thrid_answer], i + 1))
                print('</div>')
                print('<input type ="submit" value ="Submit" name="end_quiz">'
                      '</form>')
            else:#used to remake if a error occoured
                tfm.write_text_file([code],'code.txt')
                sql = f"SELECT title FROM custom_quiz where quiz_number = '{quiz_number}'"
                titles = Q.retrive_data_SQL(sql, 'custom_quiz', False)
                if titles == None:
                    print(
                        '<h1><a href = "../login.html"> <img src = "../images/site_logo.png" width = "400" height = "200"></a></h1>'
                        '<p>Enter the 6 charater code from your teacher into the box below.</p>'
                        '<p>Please be aware that the code is case sensive</p>'
                        '<form method = "post" action = "quiz.pyw">'
                        '<br><br>'
                        '<p>The quiz attached to this code has no data</p>'
                        'code<input maxlength = "6" name = "code" type = "text">'
                        '<br><br>'
                        '<input type = "submit" value = "submit" name = "do_quiz">'
                        '</form>'
                        '<br><br>'
                        '<a href = "../login.html" > teacher login </a>')
                    return None
                sql = f"SELECT q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM custom_quiz where quiz_number = '{quiz_number}'"
                questions = Q.retrive_data_SQL(sql,'custom_quiz',True)
                sql = f"SELECT q1_correct,q2_correct,q3_correct,q4_correct,q5_correct,q6_correct,q7_correct,q8_correct,q9_correct,q10_correct FROM custom_quiz where quiz_number = '{quiz_number}'"
                correct_answers = Q.retrive_data_SQL(sql,'custom_quiz',True)
                sql = f"SELECT q1_incorrect,q2_incorrect,q3_incorrect,q4_incorrect,q5_incorrect,q6_incorrect,q7_incorrect,q8_incorrect,q9_incorrect,q10_incorrect FROM custom_quiz where quiz_number = '{quiz_number}'"
                incorrect_answers = Q.retrive_data_SQL(sql,'custom_quiz', True)
                print('<h1><img src = "../images/site_logo.png" width = "400" height = "200"> </h1>')
                print('<p>Welcome to the {0}'.format(titles))
                print('<form method = "POST" required action = "quiz.pyw">')
                print('<div class ="name">')
                print('Name: <input type = "text" name = "name" required>')
                print('</div>')
                question = []
                for i in range(len(questions[0])):
                    question.append(i)
                for i in range(len(questions[0])):
                    thrid_answer = None
                    while thrid_answer == None or thrid_answer == i:
                        thrid_answer = random.choice(question)
                    question.remove(thrid_answer)
                    print('<div class ="radio-toolbar">')
                    if questions[0][i] == None:
                        break
                    order = random.randint(1,3)
                    if order == 1:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{0}<input type = "radio" name = "q{3}" value = "{0}">'
                               '{1}<input type = "radio" name = "q{3}" value = "{1}">'
                               '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],incorrect_answers[0][i],incorrect_answers[0][thrid_answer],i+1))
                    elif order == 2:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                               '{0}<input type = "radio" name = "q{3}" value = "{0}">'
                               '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],incorrect_answers[0][i],incorrect_answers[0][thrid_answer],i+1))
                    else:
                        print('<legend>{0}?</legend>'.format(questions[0][i]))
                        print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                               '{2}<input type = "radio" name = "q{3}" value = "{2}">'
                               '{0}<input type = "radio" name = "q{3}" value = "{0}">'.format(correct_answers[0][i],incorrect_answers[0][i],incorrect_answers[0][thrid_answer], i+1))
                print('</div>')
                print('<input type ="submit" value ="Submit" name="end_quiz">'
                      '</form>')

    def preveiw(self,quiz_number):
        if quiz_number == None:
            Q.set('Please select a quiz to preveiw before pressing the preview button')
            return
        sql = f"SELECT title FROM custom_quiz where quiz_number = '{quiz_number}'"#uses the same algorithm to make a demo of how a quiz would look
        titles = Q.retrive_data_SQL(sql, 'custom_quiz', False)
        sql = f"SELECT q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM custom_quiz where quiz_number = '{quiz_number}'"
        questions = Q.retrive_data_SQL(sql, 'custom_quiz', True)
        sql = f"SELECT q1_correct,q2_correct,q3_correct,q4_correct,q5_correct,q6_correct,q7_correct,q8_correct,q9_correct,q10_correct FROM custom_quiz where quiz_number = '{quiz_number}'"
        correct_answers = Q.retrive_data_SQL(sql, 'custom_quiz', True)
        sql = f"SELECT q1_incorrect,q2_incorrect,q3_incorrect,q4_incorrect,q5_incorrect,q6_incorrect,q7_incorrect,q8_incorrect,q9_incorrect,q10_incorrect FROM custom_quiz where quiz_number = '{quiz_number}'"
        incorrect_answers = Q.retrive_data_SQL(sql, 'custom_quiz', True)
        print('<h1><img src = "../images/site_logo.png" width = "400" height = "200"> </h1>')
        print('<p>Welcome to the {0}'.format(titles))
        print('<form method = "POST" required action = "quiz.pyw">')
        print('<div class ="name">')
        print('Name: <input type = "text" name = "name">')
        print('</div>')
        question = []
        for i in range(len(questions[0])):
            question.append(i)
        for i in range(len(questions[0])):
            thrid_answer = None
            while thrid_answer == None or thrid_answer == i:
                thrid_answer = random.choice(question)
            question.remove(thrid_answer)
            print('<div class ="radio-toolbar">')
            if questions[0][i] == None:
                break
            order = random.randint(1, 3)
            if order == 1:
                print('<legend>{0}?</legend>'.format(questions[0][i]))
                print('{0}<input type = "radio" name = "q{3}" value = "{0}">'
                      '{1}<input type = "radio" name = "q{3}" value = "{1}">'
                      '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],
                                                                                     incorrect_answers[0][i],
                                                                                     incorrect_answers[0][thrid_answer],
                                                                                     i + 1))
            elif order == 2:
                print('<legend>{0}?</legend>'.format(questions[0][i]))
                print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                      '{0}<input type = "radio" name = "q{3}" value = "{0}">'
                      '{2}<input type = "radio" name = "q{3}" value = "{2}">'.format(correct_answers[0][i],
                                                                                     incorrect_answers[0][i],
                                                                                     incorrect_answers[0][thrid_answer],
                                                                                     i + 1))
            else:
                print('<legend>{0}?</legend>'.format(questions[0][i]))
                print('{1}<input type = "radio" name = "q{3}" value = "{1}">'
                      '{2}<input type = "radio" name = "q{3}" value = "{2}">'
                      '{0}<input type = "radio" name = "q{3}" value = "{0}">'.format(correct_answers[0][i],
                                                                                     incorrect_answers[0][i],
                                                                                     incorrect_answers[0][thrid_answer],
                                                                                     i + 1))
        print('</div>')
        print('Return to the set quiz screen<input type="submit" name="set">'#this is the only difference to the actual quiz, a single button which sents you back to the select screen
              '</form>')

    def quiz_results(self,name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
        code = tfm.read_text_file('code.txt')[0]
        score = []
        name_check = re.findall(r'[\s]', name)#this checks the name doesnt contain space
        if name_check != []:
            Q.do_quiz(code,True)
            return None
        student_answers=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        sql = f"SELECT teacher FROM quiz_ids_in_use WHERE quizid = '{code}'"
        teacher = Q.retrive_data_SQL(sql, 'id_use', False)
        sql = f"SELECT quiz_type FROM quiz_ids_in_use WHERE quizid = '{code}'"
        quiz_number = Q.retrive_data_SQL(sql, 'id_use', False)
        sql = f"SELECT q1_correct,q2_correct,q3_correct,q4_correct,q5_correct,q6_correct,q7_correct,q8_correct,q9_correct,q10_correct FROM custom_quiz where quiz_number = '{quiz_number}'"
        correct_answers = Q.retrive_data_SQL(sql, 'custom_quiz', True)
        sql = f"SELECT q1,q2,q3,q4,q5,q6,q7,q8,q9,q10 FROM custom_quiz where quiz_number = '{quiz_number}'"
        questions = Q.retrive_data_SQL(sql, 'custom_quiz', True)
        for i in range(len(student_answers)):
            if student_answers[i] == correct_answers[0][i]:#this makes the student answers
                if student_answers[i] == None:#this stops quizes shorter then 10 questions having the students get larger scores then are possible
                    score.append(0)
                else:
                    score.append(1)
            else:
                score.append(0)
        q1 = score[0]
        q2 = score[1]
        q3 = score[2]
        q4 = score[3]
        q5 = score[4]
        q6 = score[5]
        q7 = score[6]
        q8 = score[7]
        q9 = score[8]
        q10 = score[9]#this adds the students results of each question
        lenght = 0
        for i in range(len(correct_answers[0])):
            if correct_answers[0][i] != None:
                lenght += 1
        total = sum(score)
        reward_check = 100*(total/lenght)#used to work out the percentage correct
        try:
            sql = f"SELECT student_name FROM quiz WHERE student_name = '{name}' AND quizid = '{code}'"
            check = Q.retrive_data_SQL(sql,'',False)
            if check == None:
                self.db.execute("INSERT INTO quiz(quizid,teacher,student_name,total_score,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                        code, teacher, name, total, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10))#adds the scores to the database
                self.conn.commit()
                for i in range(len(student_answers)):
                    if student_answers[i] != correct_answers[0][i]:
                        print(
                            '<p>Sorry your answer to the question of {0} was incorrect. the correct answer was {1}</p>'.format(
                                questions[0][i], correct_answers[0][i]))
                        print('<br><br>')
                print('<p> {0}/{1}'.format(total, lenght))
                if reward_check >= 80:#produced fireworks when score is over 80%
                    print('<div class ="pyro">')
                    print('<div class ="before"> </div>')
                    print('<div class ="after"> </div>')
                    print('</div>')
                print('<br><br>')
                print('<a href = "../login.html" > return to homepage </a>')
            else:
                raise Exception('name used in this quiz')
            try:
                sql = f"SELECT student_name,total_score FROM quiz WHERE quizid = '{code}' AND teacher = '{teacher}'"
                f = (Q.retrive_data_SQL(sql, '', True))
                b = self.D.student_scores(f, order, message='leaderboard')#used to produce a leaderboard
            except:
                print('<p>You are the first one to compete the quiz so there is no leaderboard</p>')
        except:
            print('<p>Opps something went wrong..chances are you used somebody elses name so please try again with a differenet name</p>')
            Q.do_quiz(code,False)




    def retrive_data_SQL(self, sql: str, table: str, muti: bool):
        """
        the functuion which is needed to get sql quires into usale veriables
        :param sql: the sl quire itself
        :param table: if your using the id_use,custom_quiz table or not
        :param muti: if you want to just pull one or mutiple bits of data
        :return: the sql quirey you asked in a useable state
        """
        if table == 'id_use' and muti == False:
            get_1 = self.used_ids.execute(sql).fetchall()#takes the data from the sql table
            if get_1 == []:
                return None
            get_2 = get_1[0]#removes it from the tuple
            get_3 = get_2[0]#removed it from the list to turn it into useable values
            return get_3

        if table == '' and muti == False:
            get_1 = self.db.execute(sql).fetchall()#takes the data from the sql table
            if get_1 == []:
                return None
            get_2 = get_1[0]#removes it from the tuple
            get_3 = get_2[0]#removed it from the list to turn it into useable values
            return get_3

        if muti == True and table == 'id_use':
            get_1 = self.used_ids.execute(sql).fetchall()
            if get_1 == []:
                return None
            for get_2 in range(len(get_1)):
                get_3 = []
                get_3.append(get_1)
                get_3 = get_3[0]#extracts the desired data from the tuple
                return get_3

        if muti == True and table == '':
            get_1 = self.db.execute(sql).fetchall()
            if get_1 == []:
                return None
            for get_2 in range(len(get_1)):
                get_3 = []
                get_3.append(get_1)
                get_3 = get_3[0]#extracts the desired data from the tuple
                return get_3
        if muti == True and table == 'custom_quiz':
                get_1 = self.custom_quiz.execute(sql).fetchall()
                if get_1 == []:
                    return None
                for get_2 in range(len(get_1)):
                    get_3 = []
                    get_3.append(get_1)
                    get_3 = get_3[0]#extracts the desired data from the tuple
                    return get_3
        if muti == False and table == 'custom_quiz':
                get_1 = self.custom_quiz.execute(sql).fetchall()#takes the data from the sql table
                if get_1 == []:
                    return None
                get_2 = get_1[0]#removes it from the tuple
                get_3 = get_2[0]#removed it from the list to turn it into useable values
                return get_3
        else:
            return Exception.with_traceback()


    def delete_quiz(self, username: str,which_quiz:str,remove:str,remove_title:str):
        error = 0
        if delete != None or remove == None and remove_title != None:
            sql = f"SELECT quizid,quiz_type FROM quiz_ids_in_use WHERE teacher = '{username}'"#used to form the same table as easlier
            quiz_data = Q.retrive_data_SQL(sql,'id_use',True)
            quiz_codes = []
            quiz_type = []
            quiz_titles = []
            quiz_attempts = []
            for i in range(len(quiz_data)):
                quiz_codes.append(quiz_data[i][0])
                quiz_type.append(quiz_data[i][1])
                sql = f"SELECT title FROM custom_quiz WHERE quiz_number = '{quiz_type[i]}'"
                quiz_title = Q.retrive_data_SQL(sql,'custom_quiz',False)
                if quiz_title == None:
                    quiz_title = 'this quiz has been removed'
                quiz_titles.append(quiz_title)
                sql = f"SELECT student_name FROM quiz WHERE quizid = '{quiz_codes[i]}'"
                partisapents = Q.retrive_data_SQL(sql,'',True)
                if partisapents == None:
                    partisapents = 0
                else:
                    partisapents = len(partisapents)
                quiz_attempts.append(partisapents)
            print('<div class="floatLeft1">')
            print('<table border="3">'
                  '<caption>your quizzes</caption>'
                  '<tr>'
                  '<th>code</th>'
                  '<th>title</th>'
                  '<th>attampts</th>'
                  '</tr>')
            for i in range(len(quiz_data)):
                print('<tr>'
                      '<td>{0}</td>'
                      '<td>{1}</td>'
                      '<td>{2}</td>'
                        '</tr>'.format(quiz_codes[i],quiz_titles[i],quiz_attempts[i]))
            print('<form method="post" action="quiz.pyw">')
            print('<br><br>')
            print('<p>Enter the code of the quiz you want to remove</p>')
            if username == 'max':
                sql = (f"SELECT title FROM custom_quiz")
                Q.debug_table(sql, 'custom', 'these are the titles of custom quizzes you can remove')
                print('<br><br>')
                print('title<input name="remove_title" type="text">')
                print('<br><br>')
            print('code<input maxlength="6" name="remove_id" type="text">')
            print('<br><br>')
            print('<input type="submit" value="delete" name="remove">')
            print('</form>')

        else:
            if remove_title == None:#checks to see if the quiz exists
                sql = (f"SELECT * FROM quiz where quizid = '{which_quiz}' AND teacher = '{username}'")
                check1 = Q.retrive_data_SQL(sql,'',True)
                sql = (f"SELECT * FROM quiz_ids_in_use WHERE quizid = '{which_quiz}' AND teacher = '{username}'")
                check2 = Q.retrive_data_SQL(sql,'id_use',True)
                if check1 == None and check2 == None and remove_title == None:
                    sql = (f"SELECT quizid FROM quiz_ids_in_use WHERE teacher = '{username}'")
                    Q.debug_table(sql, 'id_use', 'these are the codes for the quizzes you have set for you to delete')
                    print('<form method="post" action="quiz.pyw">')
                    print('<p>this quiz doesnt exist</p>')
                    print('<br><br>')
                    print('<p>Enter the code of the quiz you want to remove</p>')
                    print('code<input maxlength="6" name="remove_id" type="text">')
                    print('<br><br>')
                    print('<input type="submit" value="delete" name="remove">')
                    print('</form>')
                    return None
                try:
                    sql = (f"DELETE FROM quiz where quizid = '{which_quiz}' AND teacher = '{username}'")#removes the quiz data
                    self.db.execute(sql)
                    self.conn.commit()
                except:
                    error += 1
                try:
                    sql = (f"DELETE FROM quiz_ids_in_use WHERE quizid = '{which_quiz}' AND teacher = '{username}'")#removes the code attached to that quiz
                    self.used_ids.execute(sql)
                    self.used_commit.commit()

                except:
                    error += 1
            if remove_title != None:
                try:
                    sql =(f"DELETE FROM custom_quiz where title = '{remove_title}'")#removed the quiz with the title
                    self.custom_quiz.execute(sql)
                    self.custom_quiz_connect.commit()
                    sql = (f"SELECT quizid FROM quiz_ids_in_use WHERE teacher = '{username}'")
                    Q.debug_table(sql, 'id_use', 'these are the codes for the quizzes you have set for you to delete')
                    print('<form method="post" action="quiz.pyw">')
                    print('<br><br>')
                    print('<p>Enter the code of the quiz you want to remove</p>')
                    print('<p> custom quiz deleted</p>')
                    if username == 'max':
                        sql = (f"SELECT title FROM custom_quiz")#allows admin to delete custom quizes
                        Q.debug_table(sql, 'custom', 'these are the titles of custom quizzes you can remove')
                        print('title<input name="remove_title" type="text">')
                    print('code<input maxlength="6" name="remove_id" type="text">')
                    print('<br><br>')
                    print('<input type="submit" value="delete" name="remove">')
                    print('</form>')
                    return None
                except:
                    sql = (f"SELECT quizid FROM quiz_ids_in_use WHERE teacher = '{username}'")
                    Q.debug_table(sql, 'id_use', 'these are the codes for the quizzes you have set for you to delete')#used to print the lost of quizes to remove
                    print('<form method="post" action="quiz.pyw">')
                    print('<br><br>')
                    print('<p>Enter the code of the quiz you want to remove</p>')
                    print('<p> custom quiz deleting failed</p>')
                    if username == 'max':
                        sql = (f"SELECT title FROM custom_quiz")
                        Q.debug_table(sql, 'custom', 'these are the titles of custom quizzes you can remove')
                        print('title<input name="remove_title" type="text">')
                    print('code<input maxlength="6" name="remove_id" type="text">')
                    print('<br><br>')
                    print('<input type="submit" value="delete" name="remove">')
                    print('</form>')
                    return None
            if error <= 0:
                sql = (f"SELECT quizid FROM quiz_ids_in_use WHERE teacher = '{username}'")
                Q.debug_table(sql, 'id_use', 'these are the codes for the quizzes you have set for you to delete')
                print('<form method="post" action="quiz.pyw">')
                print('<p>quiz deleted</p>')
                print('<br><br>')
                print('<p>Enter the code of the quiz you want to remove</p>')
                print('code<input maxlength="6" name="remove_id" type="text">')
                print('<br><br>')
                print('<input type="submit" value="delete" name="remove">')
                print('</form>')
            else:
                sql = (f"SELECT quizid FROM quiz_ids_in_use WHERE teacher = '{username}'")
                Q.debug_table(sql, 'id_use', 'these are the codes for the quizzes you have set for you to delete')
                print('<form method="post" action="quiz.pyw">')
                print('<p>opps something went wrong</p>')
                print('<br><br>')
                print('<p>enter the code of the quiz you want to remove</p>')
                print('code<input maxlength="6" name="remove_id" type="text">')
                print('<br><br>')
                print('<input type="submit" value="delete" name="remove">')
                print('</form>')


    def selecter(self,set_:str,delete:str,veiw:str,code:str,username:str,quiz_num:str,name:str,q1:str,q2:str,q3:str,q4:str,q5:str,q6:str,q7:str,q8:str,q9:str,q10:str,quizid:str,order:str,which_quiz:str,remove:str,set_quiz:str,submit_quiz:str,do_quiz:str,results:str):
        error_check = True#this is the method which desides which method is run based on which button you pressed within the site
        if preview_quiz != None:
            Q.preveiw(quiz_num)
            error_check = False
        if set_ != None:
            Q.set(None)
            error_check = False
        if delete != None or remove != None or remove_title != None:
            Q.delete_quiz(username,which_quiz,remove,remove_title)
            error_check = False
        if veiw != None or quizid != None or order != None or results != None:
            Q.results(username,quizid,order,results)
            error_check = False
        if code != None or do_quiz != None:
            Q.do_quiz(code,False)
            error_check = False
        if set_quiz != None:
                if quiz_num == None:
                    print('<p>please select a quiz</p>')
                    Q.set(None)
                    return
                x = Q.quiz_id(quiz_num, username)
                print('<p>This code in important as it is required for the students to enter to do the quiz.it is also required to access the data from the quiz so keep it somewhere safe</p>')
                print('<a href = "../login.html" >return home</a>')
                print('<form method = "POST" action = "quiz.pyw">')
                print('Return to set another quiz<input type="submit" name="set">')
                print('</form>')
                error_check = False
        if name != None or submit_quiz != None:
            Q.quiz_results(name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)
        else:
            if error_check == True:
                print('<div class="error"></div>')

Q = Quiz()

if create_quiz != None or enter_quiz !=None:
    Q.create_quiz(enter_quiz,quiz_title,question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,answer_correct1,answer_correct2,answer_correct3,answer_correct4,answer_correct5,answer_correct6,answer_correct7,answer_correct8,answer_correct9,answer_correct10,answer_incorrect1,answer_incorrect2,answer_incorrect3,answer_incorrect4,answer_incorrect5,answer_incorrect6,answer_incorrect7,answer_incorrect8,answer_incorrect9,answer_incorrect10)
else:
    Q.selecter(set_,delete,view,code,username,quiz_num,name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,quizid,order,which_quiz,remove,set_quiz,submit_quiz,do_quiz,results)
print("</body>")
print("</html>")

