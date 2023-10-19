print("Привет, как у тебя настроение сегодня?")
text = input()
if "хорошо" in text or "замечательно" in text or "круто" in text:
    print("Отлично, у меня тоже всё хорошо :)")
elif "плохо" in text or "отвратительно" in text or "ужастно" in text:
    print("Ничего, скоро всё наладится")
else:
    print("Извините я вас не понимаю.")