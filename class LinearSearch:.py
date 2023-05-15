# input
dataTypeinput = int(input("Enter 1 for string and 2 for number datatype: "))

if dataTypeinput == 1:
    array = list(input("Enter the array to be searched and sorted in, separate it by spaces: ").split())
    input = input("Enter the element to be searched:")
else:
    array = list(map(int, input("Enter the array to be searched and sorted in, separate it by spaces: ").split()))
    input = int(input("Enter the element to be searched: "))



# Sorting
class Sorting: 
    # Insertion Sort
    def insertionSort(self, array):
        for i in range (1, len(array)):
            key = array[i]
            j = i-1

            while j>=0 and key<array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1]=key
            
        return (f"Insertion Sort: {array} ")  
    
    # Selection Sort
    def selectionSort(self, array):
        for i in range(len(array)):
            startElement = i
            
            for j in range(startElement+1, len(array)):
                if array[j] < array[startElement]:
                    startElement = j
            array[i], array[startElement] = array[startElement], array[i]
        return (f"Selection Sort: {array} ")  
    
    # Bubble Sort
    def bubbleSort(self, array):
        lengthOfArray = len(array)
        for i in range(lengthOfArray):
            for j in range(0, lengthOfArray-i-1):
                if array[j]>array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return (f"Bubble Sort: {array} ")  
    
    # Merge Sort
    def mergeSort(self, array):
        temporaryArray = array
        if len(array)>1:
            mid = len(array)//2
            Left = array[:mid]
            Right= array[mid:]

            self.mergeSort(Left)
            self.mergeSort(Right)


            i=j=k=0

            while i<len(Left) and j<len(Right):
                if Left[i] <= Right[j]:
                    temporaryArray[k] = Left[i]
                    i+=1
                else:
                    temporaryArray[k] = Right[j]
                    j+=1
                k+=1

            while i<len(Left):
                temporaryArray[k]=Left[i]
                i+=1
                k+=1

            while j<len(Right):
                temporaryArray[k]=Right[j]
                j+=1
                k+=1
        return (f"Merge Sort: {temporaryArray}")
    
    
        
# Searching
class Search:
    # Linear Search
    def linearSearch(self, array, element):
        for i in range(0,len(array)):
            if array[i] == element:
                return (f"Linear Search: {i}")
        return -1
    

    # Binary Search
    def binarySearch(self, sortedArray, low, high, element):
        if high>=low:
            mid = low + (high-low)//2

            if sortedArray[mid] == element:
                return (f"Binary Search: {mid}")
            elif sortedArray[mid]>element:
                return (f"Binary Search: {self.binarySearch(sortedArray, low, mid-1, element)}")
            else:
                return (f"Binary Search: {self.binarySearch(sortedArray, mid+1, high, element)}")
        else:
            return -1
    
# Binding objects
Search = Search()
Sorting = Sorting()

# Printing
print(Sorting.insertionSort(array))
print(Sorting.selectionSort(array))
print(Sorting.bubbleSort(array))
print(Sorting.mergeSort(array))
print(Search.linearSearch(array, input))
print(Search.binarySearch(array, 0, len(array)-1, input))





    
    







    




        


