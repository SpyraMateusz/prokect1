Temat projektu
Task Manager - Aplikacja do zarządzania zadaniami.

# Cel projektu i oczekiwane rezultaty

Celem projektu jest stworzenie aplikacji do zarządzania zadaniami, która umożliwia użytkownikom dodawanie, usuwanie i edytowanie zadań oraz ich priorytetów. Oczekiwane rezultaty to łatwość w zarządzaniu zadaniami, przejrzysty interfejs użytkownika oraz solidne mechanizmy obsługi błędów.

# Opis funkcjonalności projektu

- Dodawanie nowych zadań.
- Usuwanie istniejących zadań.
- Edytowanie szczegółów istniejących zadań.
- Wyświetlanie wszystkich zadań wraz z ich szczegółami.
- Obsługa wyjątków i błędów, takich jak próba usunięcia nieistniejącego zadania.
  Opis technologii użytych w projekcie
  Python 3
  Standardowa biblioteka Pythona
  keras

# Analiza wymagań

Spis wymagań funkcjonalnych i niefunkcjonalnych projektu
Wymagania funkcjonalne
Użytkownik może dodać nowe zadanie, podając tytuł, opis i priorytet.
Użytkownik może usunąć zadanie, podając jego identyfikator.
Użytkownik może edytować istniejące zadanie, zmieniając jego tytuł, opis i priorytet.
Użytkownik może wyświetlić wszystkie zadania.
Wymagania niefunkcjonalne
System powinien być łatwy w użyciu i intuicyjny.
System powinien efektywnie zarządzać zadaniami, nawet przy dużej liczbie zadań.
System powinien obsługiwać błędy i wyjątki w sposób informacyjny dla użytkownika.
Określenie interfejsu użytkownika i funkcjonalności systemu
Interfejs użytkownika jest prostym interfejsem wiersza poleceń.
Użytkownik wprowadza polecenia, które są następnie przetwarzane przez system zarządzania zadaniami.
Implementacja
Użycie wybranej struktury danych
Zadania są przechowywane w słowniku, gdzie kluczami są identyfikatory zadań, a wartościami obiekty klasy Task.
Klasa i wyszukiwanie atrybutów w klasie
Klasa Task definiuje strukturę zadania i przechowuje jego atrybuty (id, title, description, priority).
Organizacja kodu w modułach
Projekt jest podzielony na moduły: task.py, task_manager.py, exceptions.py, main.py.
Wykorzystanie błędów i wyjątków
Generatory i listy składane są używane do przetwarzania i wyświetlania list zadań.

# Temat projektu

Task Manager - Aplikacja do zarządzania zadaniami.

# Cel projektu i oczekiwane rezultaty

Celem projektu jest stworzenie aplikacji do zarządzania zadaniami, która umożliwia użytkownikom dodawanie, usuwanie i edytowanie zadań oraz ich priorytetów. Oczekiwane rezultaty to łatwość w zarządzaniu zadaniami, przejrzysty interfejs użytkownika oraz solidne mechanizmy obsługi błędów.

# Opis funkcjonalności projektu

- Dodawanie nowych zadań.
- Usuwanie istniejących zadań.
- Edytowanie szczegółów istniejących zadań.
- Wyświetlanie wszystkich zadań wraz z ich szczegółami.
- Obsługa wyjątków i błędów, takich jak próba usunięcia nieistniejącego zadania.

# Opis technologii użytych w projekcie

Python 3
Standardowa biblioteka Pythona
Keras (dla części związanej z uczeniem maszynowym - do dodania w przyszłych wersjach)

# Analiza wymagań

# Spis wymagań funkcjonalnych i niefunkcjonalnych projektu

Wymagania funkcjonalne

Użytkownik może dodać nowe zadanie, podając tytuł, opis i priorytet.
Użytkownik może usunąć zadanie, podając jego identyfikator.
Użytkownik może edytować istniejące zadanie, zmieniając jego tytuł, opis i priorytet.
Użytkownik może wyświetlić wszystkie zadania.

# Wymagania niefunkcjonalne

System powinien być łatwy w użyciu i intuicyjny.
System powinien efektywnie zarządzać zadaniami, nawet przy dużej liczbie zadań.
System powinien obsługiwać błędy i wyjątki w sposób informacyjny dla użytkownika.
Określenie interfejsu użytkownika i funkcjonalności systemu
Interfejs użytkownika jest prostym interfejsem wiersza poleceń.
Użytkownik wprowadza polecenia, które są następnie przetwarzane przez system zarządzania zadaniami.

# Implementacja

Użycie wybranej struktury danych
Zadania są przechowywane w słowniku, gdzie kluczami są identyfikatory zadań, a wartościami obiekty klasy Task.
Klasa i wyszukiwanie atrybutów w klasie
Klasa Task definiuje strukturę zadania i przechowuje jego atrybuty (id, title, description, priority).
Organizacja kodu w modułach
Projekt jest podzielony na moduły: task.py, task_manager.py, exceptions.py, main.py.
Wykorzystanie błędów i wyjątków
Niestandardowy wyjątek TaskNotFoundException jest używany do obsługi błędów związanych z nieistniejącymi zadaniami.
Wykorzystanie generatorów i list składanych
Generatory i listy składane są używane do przetwarzania i wyświetlania list zadań.
Zastosowanie wybranego elementu biblioteki standardowej
Standardowe elementy biblioteki Pythona, takie jak input i print, są używane do interakcji z użytkownikiem.
Wykorzystanie jednego z frameworków służących do wykorzystania sztucznej inteligencji, np. TensorFlow, Numpy, Keras
W przyszłych wersjach planowane jest dodanie funkcjonalności uczenia maszynowego za pomocą Keras do przewidywania priorytetów zadań.

# Testowanie

Implementacja testu jednostkowego
Testy jednostkowe są zaimplementowane w pliku test_task_manager.py.
Opis wyników testów i ewentualne poprawki
Wszystkie testy przeszły pomyślnie. W przypadku wykrycia błędów, zostaną one opisane i naprawione w przyszłych wersjach.

# Wnioski

Wnioski i możliwe usprawnienia projektu
Aplikacja spełnia swoje podstawowe funkcje i jest użyteczna do zarządzania zadaniami.
Możliwe usprawnienia obejmują dodanie interfejsu graficznego oraz integrację z systemami powiadomień.

# (Dodatykowe)

1.Definicja klasy Task:
Klasa ta będzie reprezentować pojedyncze zadanie z atrybutami takimi jak id, title, description, priority.

2.Definicja klasy TaskManager:
Klasa ta będzie zarządzać listą zadań. Powinna zawierać metody do dodawania, usuwania, edytowania zadań oraz wyświetlania wszystkich zadań.

3.Definicja wyjątków:
Stwórz niestandardowe wyjątki, takie jak TaskNotFoundException, aby obsłużyć błędy związane z zarządzaniem zadaniami.

4.Interfejs użytkownika w main.py:
Zapewnij prosty interfejs wiersza poleceń, który pozwoli użytkownikowi na interakcję z aplikacją.

Zeby uruchomić wpisać trzeba python3 main.py
