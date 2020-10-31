choice = input("Vilken karusell vill ni åka: ")
if choice == "PopExpressen":
    print("Minst 1.40m")
elif choice == "FrittFall":
    print("Minst 1.50m, max 2.1m")
elif choice == "Blå tåget":
    print("Minst 1.2m")
else:
    print("Den karusellen finns ej, försök igen.")