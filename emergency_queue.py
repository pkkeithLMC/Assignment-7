class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency





class MinHeap:
    def __init__(self):
        self.data = []


    def print_heap(self):
        print("\n Current Patients")
        for patient in self.data:
            print(f"-{patient.name} (Urgency: {patient.urgency})")


    def peek(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None

    def heapify_up(self, index):
        while index > 0:
            #Get the parent index for the current child index
            parent_index = (index - 1) // 2

            #Get the tasks
            current_task = self.data[index]
            parent_task = self.data[parent_index]

            #Check if the current priority value is smaller than the parent.  If so, we need to move it up the list
            #If not we can stop
            if current_task.urgency < parent_task.urgency:
                #Swap the items position in the list
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                #Move up the heap
                index = parent_index
            else:
                break


    def heapify_down( self, index):
        #calculate the index of the left and right child
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index  #assume current is the smalles

        #Check if the left child exists and has a smaller urgency that the current smallest
        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        #If the smallest is not the currnet, we need to swap and continue.  Otherwise the function stops

        if smallest != index:
            #Swap the curent task with the task that has the smaller priority
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp

            #Recursivly heapify the affect subtree
            self.heapify_down(smallest)
        

    def insert( self, patient):
        self.data.append(patient)  #Step 1: Add the itme tot he end
        self.heapify_up(len(self.data)-1)  #Step 2:  Call heapify up at the ned of the list where the value was added.

    def remove_min(self):
        if not self.data:  #Handle the empty list
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return min_value



# Test your MinHeap class here including edge cases

heap = MinHeap()
heap.insert(Patient("Riley", 3))
heap.insert(Patient("Bob", 1))
heap.insert(Patient("Jim", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)

served = heap.remove_min()
print(f"Just served {served.name}")
heap.print_heap()
