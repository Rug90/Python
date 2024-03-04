def main():
    def convert():
        feelings=input('Are you happy or sad? ')
        AllTheFeelings=feelings.replace(':)','🙂').replace(':(', '🙁')


        return AllTheFeelings
    print(convert())

main()
