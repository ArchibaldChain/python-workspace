'''
test file
'''
# f = open(r'test_file.txt', 'x')
# f.close

# clear and rewrite
f0 = open(r'I:\Programming\Python\python-workspace\Workspace for Python\studying file\File_IO\test_file.txt', 'w')
f0.write('123454')
list = ['a', 'b\n', 'c\n']
f0.writelines(list)
f0.close

f2 = open(r'I:\Programming\Python\python-workspace\Workspace for Python\studying file\File_IO\test_file.txt', 'a')  # add
f2.write('add a line')
f2.close

f1 = open(r'test_file.txt', 'r')
lines = f1.readlines()
line = f1.readline()
print(line)
print("d**************************\n")
print(lines)
f1.close

# with donot need
