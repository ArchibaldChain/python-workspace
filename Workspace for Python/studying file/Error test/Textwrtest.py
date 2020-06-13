def textwrtest(a):
    sault = ["Hello", "How are you", "See you"]
    ab = open("greed.txt", 'wt+')
    try:
        ab.write(sault[a])
        print(sault[a])
        print("correct")
    except:
        print("IndexError")
    finally:
        ab.close()
        return "down"


print(textwrtest(1))
print(textwrtest(5))
