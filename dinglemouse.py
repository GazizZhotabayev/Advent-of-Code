class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = queues
        self.capacity = capacity
        self.occupants = 0
        self.floor = 0
        self.visited = [0]
        self.direction = 'up'

    def next_action(self):

        if self.occupants == 0: #if empty lift, keep going in current direction
            return self.direction
        else:


    def theLift(self):
        #while lift isn't empty
        while sum(sum(queue) for queue in self.queues) > 0:
            
        return []

tests = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
  
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    