# Projekt GREDA - Wizytówka Firmowa 🏢

Nowoczesna wizytówka internetowa dla firmy GREDA, zaprojektowana z myślą o profesjonalnym wyglądzie i funkcjonalności.

## ✨ Demo na żywo
🌐 **[Odwiedź stronę: https://greda.pl](https://greda.pl)**

## 🎯 Funkcje

- ✅ **Responsywny design** - działa na wszystkich urządzeniach
- ✅ **Nowoczesne logo** - czarne tło z efektownymi czerwonymi akcentami  
- ✅ **Płynne animacje** - profesjonalne efekty wizualne
- ✅ **Optymalizacja SEO** - poprawna struktura HTML5
- ✅ **Szybkie ładowanie** - zoptymalizowany kod bez zewnętrznych zależności  

## Struktura projektu

```
/
├── index.html          # Główna strona HTML
├── styles.css          # Style CSS z logo i animacjami
├── script.js          # JavaScript z interakcjami
├── README.md          # Ten plik
└── .vscode/
    └── tasks.json     # Zadania VS Code
```

## Uruchomienie

### Metoda 1: Live Server (Zalecana)
1. Otwórz projekt w VS Code
2. Kliknij prawym na `index.html`
3. Wybierz "Open with Live Server"

### Metoda 2: Python HTTP Server
```bash
# W folderze projektu uruchom:
python -m http.server 8000
# Następnie otwórz: http://localhost:8000
```

### Metoda 3: Bezpośrednio w przeglądarce
1. Otwórz plik `index.html` w przeglądarce
2. Strona będzie działać bez serwera

## Technologie

- **HTML5** - semantyczna struktura
- **CSS3** - nowoczesne style z Flexbox/Grid
- **Vanilla JavaScript** - animacje i interakcje
- **Google Fonts** - czcionki Orbitron i Roboto

## Konfiguracja logo

Logo firmy GREDA wykorzystuje:
- Czarne tło `#000`
- Czerwone akcenty `#dc2626`
- Czcionkę Orbitron (futurystyczna)
- Efekty świecenia i cieni
- Animacje hover

## Dostosowanie

### Zmiana kolorów
W pliku `styles.css` znajdź zmienne:
```css
/* Główny kolor akcentu */
border: 4px solid #dc2626;

/* Kolor tekstu logo */
color: #fff;
```

### Dodanie sekcji
1. Dodaj nową sekcję w `index.html`
2. Dodaj style w `styles.css`
3. Opcjonalnie dodaj animacje w `script.js`

## Deployment na greda.pl

1. Skopiuj wszystkie pliki na serwer
2. Ustaw `index.html` jako stronę główną
3. Upewnij się, że serwer obsługuje pliki statyczne

## Dalszy rozwój

Strona jest przygotowana do rozbudowy:
- Dodanie galerii
- Formularz kontaktowy
- Blog/aktualności
- Sklep internetowy
- Panel administracyjny

## Wsparcie

Projekt stworzony z myślą o łatwej rozbudowie i utrzymaniu.
Wszystkie pliki są dobrze skomentowane i zorganizowane.

---

© 2025 GREDA. Wszystkie prawa zastrzeżone.