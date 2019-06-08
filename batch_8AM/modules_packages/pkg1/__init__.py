print("This file is invoked whenever {} package is imported".format(__name__))

#import pkg1.mod1,pkg1.mod2

data = {
        'name' : ['simran','garima','annu','tarun','jatin'],
        'course' : ['dev','python','adv python','java','c++']
    }

__all__ = [
        'mod1',
        'mod2'
        ]
