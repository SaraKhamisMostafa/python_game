'''
Game:
   -welcom massage:options games
   -enter game number-->start game
   -ask play again
   -games:
   -names---count
   -x,y-->1:100/x and y
   -sentence ----> no duplicaate
'''


class Game:


    def __init__(self):
        while True:
            print('''Welcome
            1: Names Count
            2: Divieded By
            3: Sentence No Duplicate
            4: to exit''')
            user_choise=int(input('Enter Game Number: '))
            if user_choise==4:
                print('Good bye..... ')
                break
            elif user_choise==1:
                self.names_count()
            elif user_choise==2:
                self.divided_by() 
            elif user_choise==3:
                self.sentence_no_duplicate()

            else:
                print(f'no game with this number: {user_choise}')  
            play_again=input('Press any key to play again, n to exit')
            if play_again=='n':
                print('Good bye..... ')
                break

    def names_count(self):
        names=(input('Enter Names comma seperated :').split(','))
        names_count=[len(i) for i in names]
        print(names_count)
    def divided_by(self):
        x=int(input('Enter First Number'))
        y=int(input('Enter Second Number'))
        result=[]
        for n in range(1,101):
            if n%x==0 and n%y==0:
                result.append(n)

        print(result)        
    def sentence_no_duplicate(self):
        sentence=input('Enter Sentence: ')
        word= sentence.split(' ')
        words_no_duplicate=[]
        for i in word:
            if i not in words_no_duplicate:
                words_no_duplicate.append(i)
        print(' '.join(words_no_duplicate))        



g1 = Game()