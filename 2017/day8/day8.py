
f = open(r'C:\Users\310282769\Desktop\aoc\day8\input.txt', 'r')

d = {}
maxval = 0
for line in f:
   statement= line.split()
   print(statement)
   check_var = statement[4]
   check_operation = statement[5]
   check_val = statement[6]
   
   subject_var = statement[0]
   subject_operation = statement[1]
   if subject_operation == 'dec':
       subject_operation = '-'
   elif subject_operation == 'inc':
       subject_operation = '+'
   subject_val = statement[2]
   try:
       val = d[check_var]
   except:
       val = 0
       d[check_var]= 0
   stat = str(val) + check_operation + check_val
   print(stat)
   truth = eval(stat)
   print(truth)
   if truth:
       try:
           val = d[subject_var]
       except:
           val = 0
           d[subject_var]= 0
       string = str(val)+subject_operation+ subject_val
       print(string)
       output = eval(string)
       print(output)
       d[subject_var] = output
       if output > maxval:
           maxval = output

print(max(list(d.values())))

print(maxval)   