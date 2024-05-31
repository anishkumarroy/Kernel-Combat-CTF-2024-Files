new_flag = "3a_2}3pyhr_1_nc135_7_7_0ul4_830_fyu_n471rpm07_0t015_n1_7y553rbm3_nta{umklobneKre"
flag = ''

# Undo the operations inside the loop
for i in range(0, len(new_flag), 5):
    flag += new_flag[i+4]
    flag += new_flag[i]
    flag += new_flag[i+3]
    flag += new_flag[i+1]
    
    
    flag += new_flag[i+2]
    

# Reverse the flag
original_flag = flag[::-1]

print(original_flag)
