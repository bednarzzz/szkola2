import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("Brak zadań na liście.")
    else:
        print("\nTwoja lista zadań:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Podaj treść nowego zadania: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Dodano zadanie!")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Podaj numer zadania do usunięcia: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Usunięto zadanie: {removed}")
        else:
            print("Nieprawidłowy numer.")
    except ValueError:
        print("Wpisz liczbę.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- ToDo Lista ---")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nie ma takiej opcji.")

if __name__ == "__main__":
    main()
