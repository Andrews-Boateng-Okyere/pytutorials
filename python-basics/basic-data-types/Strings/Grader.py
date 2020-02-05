class Grader(object):
    def __init__(self, obj):
        self.obj = obj

    def scorer(self, total, correct):
        print(f'==================\n You scored {(correct/total)} \n==================')

    def string_ex1(self):
        first_name, last_name = self.obj
        if type(first_name) == str and type(last_name) == str:
            print('==================\nCorrect! You scored 1.0\n==================')
            # return 1
        else:
            print('wrong! recheck it')
            # return 0

    def string_ex2(self):
        text, slicee = self.obj
        if text[1:-2] == slicee:
            return print('==================\nCorrect! You scored 1.0\n==================')
        else:
            return 'Wrong! recheck your answer'

    def list_ex1(self):
        llist = [
            ['Goat', 5, 11.5, '?', '?'],
            ['Samsung',2,2900,'?','?'],
            ['Iphone', 1, 3400, '?','?'],
            ['Rim', 4, 100.6, '?', '?'],
            ['Yam', 20, 2, '?', '?']
        ]
        correct = 0
        ll = self.obj
        for i,j in enumerate(ll):
            if j in llist and i == llist.index(j):
                correct +=1
        return Grader.scorer(self,len(ll), correct)


