import matplotlib
import matplotlib.pyplot as plt
class Data():
    @staticmethod
    def make_chart(sql_list:list):
        results = []
        New_Colors = []
        bars = Data.getbars(sql_list)#this is the fuction which is used to extract each students scores from the list of them extracted from the table
        for i in range(len(bars)):
            results.append(sum(bars[i]))#this line adds up the total class score for each question
            if sum(bars[i]) > int(len(bars[i])/2):#these lines then deside based on that if the bar needed to be coloured green,red or orange
                rgb = 'g'
            elif sum(bars[i]) == int(len(bars[i])/2):
                rgb = 'orange'
            else:
                rgb = 'r'
            New_Colors.append(rgb)
        New_Colors.insert(0,'b')#this creates the colour of the attempts column so the graph is easier for the user to interpret this creates the colour of the attempts column so the graph is easier for the user to interpret
        questions = ['attempts','q1', 'q2', 'q3', 'q4', 'q5','q6','q7','q8','q9','q10']
        results.insert(0,(len(bars[0])))#this then gives the attempt bar its correct length
        plt.bar(questions,results,color=New_Colors)#this produces the graph
        plt.title('number of people in the class who got each question correct', fontsize=14)
        plt.xlabel('question', fontsize=14)
        plt.ylabel('score', fontsize=14)
        plt.grid(True)
        plt.savefig('images/data.png')#this then saves the graph as a picture
        print('<img class="floatRight" src="../images/data.png" width="800" height="400">')
        pass


    @staticmethod
    def getbars(sql_list: list):
        bars = [[] for _ in range(10)]
        for x, extracted in enumerate(sql_list):
            for i in range(10):
                bars[i].append(extracted[i + 2])#exrtracts all but the first two values to enable the creation of the graph
        return bars

    @staticmethod
    def average(sql_list: list):
        totals = [i[1] for i in sql_list]#this runs through the program to enable the avarage to be worked out by taking each students total score
        average = sum(totals) / len(totals)
        return average

    @staticmethod
    def student_scores(sql_list:list,order='',message='the quiz results'):
        score = [[i[0] for i in sql_list],[i[1] for i in sql_list]]#this creates the 2D list of the students name and then the score they got
        score = Data.bubblesort(score)#sends the 2D list to be sorted into the correct order
        if order == None:#reverses the order of the list if decending isnt selected
            score[1].reverse()
            score[0].reverse()
        Data.make_table(score,message)#sends the score list and the table title
        return score
    @staticmethod
    def make_table(table_list:list,message:str):#simply just forms the table based on a 2D list
        print('<table class="floatLeft2"border="3">'
              '<caption>{0}</caption>'
              '<tr>'
              '<th>name</th>'
              '<th>score</th>'
              '</tr>'.format(message))
        for i in range(len(table_list[0])):
            print('<tr>'
                  '<td>{0}</td>'
                  '<td>{1}</td>'
                  '</tr>'.format(table_list[0][i],table_list[1][i]))
        print('</table>')
        print('</div>')

    @staticmethod
    def bubblesort(list):
        runthrough_count = 1
        pass_count = 0
        swap_count = 0
        list_len_change = 1
        while list_len_change != 0:
            list_len_change = 0
            pass_count += 1
            for i in range(len(list[1]) - pass_count):
                list_len_change = +1
                if list[1][i] > list[1][i + 1]:
                    swap_temp_store = list[1][i]
                    swap_temp_store2 = list[0][i]#this movement is done to both parts of the 2D list as only numbers can be sorted into highest to lowest however the names of the students need to move aswell
                    list_len_change += 1
                    swap_count += 1
                    list[0][i] = list[0][i + 1]
                    list[1][i] = list[1][i + 1]
                    list[1][i + 1] = swap_temp_store
                    list[0][i +1] = swap_temp_store2
                    runthrough_count += 1
                    i -= 1
        return list