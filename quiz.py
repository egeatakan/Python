questions = ("3ün ikinci kuvveti kaçtır ?",
             "Saat 9dan 2 saat ilerdeyse saat kaçtır ?",
             "Periyodik tablonun 2. elementi hangi gruptadır ?",
             "Periyodik tablonun ilk elementi hangisidir ?",
             "3 + 5 * 2 = ?")

options = (("A. 9", "B. 3", "C. 2", "D. 7", "E. 11"),
           ("A. 10", "B. 11", "C. 12", "D. 1", "E. 2"),
           ("A. 8A", "B. 2A", "C. 3A", "D. 1A", "E. Alkali Metaller"),
           ("A. Hidrojen", "B. Helyum", "C. Oksijen", "D. Karbon", "E. Sodyum"),
           ("A. 2", "B. 4", "C. 5", "D. 11", "E. 13"))

answers = ("A", "B", "A", "A", "E")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Cevabı Giriniz: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
            score += 1
            print("helalll")
    else:
     print(f"yanlış bok ye doğru cevap {answers[question_num]} ")
    question_num += 1

print("--------------------")
print("------Sonuçlar------")
print("--------------------")


print(f"answers :", end="")
for answer in answers:
    print(answer, end=" ")
print()

print(f"guesses :", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Doğru sayın :{score}")
print()