try:
    f = open("test2.txt")
    if f.name == "test2.txt":
        raise Exception
except FileNotFoundError as e:
    print("Sorry, file does not exist", e)
except Exception as e:
    # print("exception type: ", type(e).__name__)
    print("Sorry, an error occurred")
else:
    print(f.read())
    f.close()
finally:
    print("Final Code Execution")
