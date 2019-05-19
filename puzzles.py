
###############################################################
#    puzzle1                                                  #
###############################################################
import RhetoricalQuestion

def ponder(task,subject,goal):
    question = RhetoricalQuestion()
    is_reached = False
    how many = 0
    while not is_reached:
        question.ask(task,subject,goal)
        how_many+=1
        is_reached=question.goal_reached()
    return how_many

tasks = ['walk road',
        'sail seas',
        'fly',
        'exist',
        'exist',
        'turn head',
        'look up',
        'have ears',
        'require death']

subjects = ['man',
            'white dove',
            'cannonballs',
            'mountain',
            'some people',
            'man',
            'man',
            'man',
            '']

goals = ['called a man',
         'sleep in sand',
         'forever banned',
         'washed to the sea',
         'allowed to be free',
         'pretend to not see',
         'see the sky',
         'hear people cry',
         'too many to die']


blowin_in_the_wind=[ponder(i,j,k) for i,j,k in zip(tasks,subjects,goals)]


#############################################################################
#    puzzle 2.                                                              #
#############################################################################
import Shelters


date = 'that day'
where = [Shelters.rock(),
         Shelters.sea(),
         Shelters.river(),
         Shelters.Lord()]

i = 0

While True:
    try:
        place = where[i]
        ran = place.run_to(date)
        if ran:
            print('ran to {}'.format(i.name))
            break
        else:
            print(place.status())
            i += 1
   
   except IndexError:
       print('run to the devil, the devil\'s a waitin\'')
       break


#############################################################################
#    puzzle 3.                                                              #
#############################################################################
import Girl, Guy

girl, me = Girl(),Guy()

for i in ['tomorrow','today']:
    girl.love(me)
me.go_away()










