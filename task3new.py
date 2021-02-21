class TVController():
    
    def __init__(self, CHANNELS):
        self.CHANNELS=CHANNELS
        self.chan=0  

    def first_channel(self):
        self.chan=0

    def last_channel(self):
        self.chan=len(self.CHANNELS)-1


    def turn_channel(self,N) :
        self.chan=N-1
      
    def next_channel(self) :
        if self.chan < len(self.CHANNELS)-1:
            self.chan=self.chan+1
        
        else:
            self.chan=0          
    
    def previous_channel(self):
        if self.chan<1:
            self.chan=len(self.CHANNELS)-1
        else:
            self.chan=self.chan-1
               
    def is_exist(self,N):
        if type(N)==int:
            if N >0 and N<=len(self.CHANNELS):
               return 'Yes'
            else:
                return'No'
        
        elif type(N) == str:
            if N in self.CHANNELS:
                return 'Yes'            
            else:                
                 return 'No' 
        
              
    def current_channel(self) :
        return self.CHANNELS[self.chan]       
    
CHANNELS=['BBC', 'Discovery', 'TV1000']
controller = TVController(CHANNELS)
controller.first_channel()
print(controller.current_channel())
controller.last_channel()
print(controller.current_channel())
controller.turn_channel(1)
print(controller.current_channel())
controller.next_channel()
print(controller.current_channel())
controller.previous_channel() 
print(controller.current_channel())
controller.current_channel() 
print(controller.current_channel())

print(controller.is_exist(4))
print(controller.is_exist('BBC'))
