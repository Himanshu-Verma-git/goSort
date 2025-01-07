GoSort

A.) Description
Sorting algorithm for distinct elements.

Algorithm (goSort(array)):
Step 1:If length of array of array is equal to or smaller than 1 then return array
Step 2:Get middle element as target element of the array.
Step 3: For all elements on the left of target element move elements greater than target elements to the right of the target element
Step 4:For all elements on the right of the target element move elements smaller then the target to the left of the target element
step 5:return goSort(arr[:target_index]) + [target] goSort(arr[target_index+1:])

Algorithm (goSort(array)):
Step : If length of array of array is equal to or smaller than 1 then return array.
Step :  mid_element_index = array_length // 2
        left_start = mid_element_index - 1
        right_start = mid_element_index + 1
        target = array[mid_element_index]
Step : move towards left by decrementing 'i' while i >= 0
          if value at index array[i] > target then swap until element array[i] goes to right of target
        Repeat until exhaust the subarray in left

Step : move towards right by increasing j while j < array_length
          if value at index arra[j] < target then swap until element array[j] goes to left of target
       Repeat until exhaust the subarray in right
Step : return goSort(array[:target_index]) + [target] + goSort(array[target_index+1 :])

B.) Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

C.) Usage
C1.) Illustrations
C2.) Python Example:
def moveRight(l:list, ind:int, t:int):
    while(l[ind+1] != t):
        l[ind], l[ind+1] = l[ind+1], l[ind]
        ind+=1
    l[ind], l[ind+1] = l[ind+1], l[ind]

def moveLeft(l:list, ind:int, t:int):
    while(l[ind-1] != t):
        l[ind], l[ind-1] = l[ind-1], l[ind]
        ind-=1
    l[ind], l[ind-1] = l[ind-1], l[ind]

def sort(l:list)->list:
    if(len(l) == 0 or len(l) == 1):return l
    mid = len(l)//2
    t = l[mid]
    i = mid-1
    j = mid+1
    
    while(i >= 0):
        if(l[i] > t):moveRight(l, i, t)
        i-=1
    
    while(j <= len(l)-1):
        if(l[j] < t):moveLeft(l, j, t)
        j+=1
    
    ind = l.index(t)
    print(l)
    return sort(l[:ind]) + [t] + sort(l[ind+1:])

D.) Support
Email: work.himashuverma@outlook.com

Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

License
For open source projects, say how it is licensed.

Project status
Currently in development for streamlining the sorting algorithm. Implementation in other languages.
