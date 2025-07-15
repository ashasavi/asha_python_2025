# fruit =input("enter a fruit:")
#
# match fruit:
#     case"Apple":
#         print("you have given an apple!")
#     case"Mango":
#             print("you have given an Mango!")
#     case"oranga":
#         print("you have given an orange!")
#     case _:
#         print("maybe some random fruit or invalid entry")

day = int(input("enter a day:"))

match day:
    case 1:
        print("you have given an Monday!")
    case 2:
            print("you have given an Tuesday!")
    case 3:
        print("you have given an Wednesday!")
    case _:
        print("maybe some random day or invalid entry")
