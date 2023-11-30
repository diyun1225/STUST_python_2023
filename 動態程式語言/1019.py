#題目：input一段英文文章，輸出要要把文章的單字開頭由a到z排列
#output一行”單字 單字出現次數“
# ex  input: This is a nice day
#     output: a 1
#            day 1
#            nice 1
#            today 1

            #word_list為使用者輸入的句子
def sort_word(word_list):#計算出現過的單字及其次數
    #f_word為 對使用者輸入的句子做處理
    f_word = [x.lower() for x in word_list] #把字母都變小寫
    f_word = sorted(f_word) #從a->z排列
    
    for i in range(len(f_word)): 
        #刪除標點符號 #rstrip是一個一個處理所以要用for
        #不可以直接s.rstrip()
        f_word[i] = f_word[i].rstrip(". , ? !") #"放要刪除的標點符號"
    #set_word裡放的是f_word變成集合
    #轉集合是因為要把重複的元素刪除，這樣才不會有同個單字跳很多次的問題
    set_word=sorted(set(f_word))  
    
    #count是 set_word在f_word出現了幾次
    for i in set_word: #計算出現次數
        count=f_word.count(i)
        print(i,count)
    
    return 

if __name__ == '__main__':
    word = "This is a nice day" #word儲存使用者輸入的句子
    word = word.split() #分割
    sort_word(word)

