try:
    file = open('text.txt', w)
except Exception as result:
    print(result)
else:
    print("no exception")
finally:
    file.close()
