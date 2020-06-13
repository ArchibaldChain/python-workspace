def testTry(index):
    stulst = ["Jojn", "Jenny", "Tom"]
    try :
        astu = stulst[index]
        print(astu)
    except IndexError:
        print("Indexerror")
    finally:
        print("end")

testTry(1)
testTry(4)
