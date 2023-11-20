#list of alphabets
alphabets = ['a','b','d','e','i','j','o']
vowels = ['a','e','i','o','u']
new_list = []
filtered_alphbets =[]

#define a self-defined sub-method to filter out vowels(母音)
def filiter_vowels_from_list(alphabets):
    print("Length of the alphabets list = {}".format(len(alphabets)))
    #for i in alphabets:
        #if alphabets == vowels:
            #new_list.insert(alphabets[i])
    #for i in alphabets:
        #for j in vowels:
            #if i == j:
                #print(i)
                #new_list.append(i)
    #for elem in alphabets:
        #if elem in vowels:
            #print("vowels: ",elem)
            #new_list.append(elem)
        #else:
            #print("none vowels: ",elem)
    #cost_of_if = 0
    for elem in alphabets:
        if elem == 'a' or elem == 'e' or elem == 'i':
            print("vowel:",elem)
            #cost_of_if+=1
        elif elem == 'o':
            print("vowel:",elem)
            #cost_of_if+=1
        elif elem == 'u':
            print("vowel:",elem)
            #cost_of_if+=1
        else:
            print("not vowel:",elem)
            #add non vowel char into list filtered_alphabets
            filtered_alphbets.append(elem) 
     
    #print(new_list)
    #print("cost of if for element {}={}",elem,cost_of_if)
#function call of sub-method
filiter_vowels_from_list(alphabets)
print(filtered_alphbets)
