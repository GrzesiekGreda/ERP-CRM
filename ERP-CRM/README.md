# System ERP/CRM

Kompleksowy system zarządzania przedsiębiorstwem (ERP) i relacjami z klientami (CRM) zbudowany w Python Flask.

## Technologie

- **Backend**: Python 3.10+, Flask 3.0.0
- **Database**: SQLite + SQLAlchemy 3.1.1
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.2.1, WTForms 3.1.1
- **Frontend**: Bootstrap 5, Bootstrap Icons

## Funkcjonalności

### 📊 Panel główny (Dashboard)
- Statystyki: liczba klientów, produktów, zamówień, przychód
- Ostatnio dodani klienci
- Produkty z niskim stanem magazynowym

### 👥 CRM (Zarządzanie klientami)
- Lista klientów z paginacją
- Dodawanie/edycja klientów
- Pełne dane kontaktowe (email, telefon, NIP, adres)
- Historia zamówień klienta
- Statystyki sprzedaży dla klienta

### 📦 Magazyn (Inventory)
- Zarządzanie produktami
- Unikalne SKU
- Ceny sprzedaży i koszty zakupu
- Stan magazynowy z alertami
- Poziom ponownego zamówienia
- Obliczanie marży

### 🛒 Sprzedaż (Sales)
- Wielopozycyjne zamówienia
- Automatyczne generowanie numerów zamówień (ORD-YYYYMMDD-XXXX)
- Statusy: oczekujące, potwierdzone, wysłane, dostarczone, anulowane
- Automatyczne kalkulacje sum
- Historia zamówień

### 📄 Faktury (Invoicing)
- Automatyczne generowanie faktur
- Terminy płatności (domyślnie 30 dni)
- Śledzenie płatności (nieopłacone, częściowo, opłacone, przeterminowane)
- Widok do druku

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/GrzesiekGreda/ERP-CRM.git
cd ERP-CRM
```

2. Utwórz wirtualne środowisko:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

4. Uruchom aplikację:
```bash
python run.py
```

5. Otwórz przeglądarkę: http://localhost:8080

## Domyślne dane logowania

- **Email**: admin@example.com
- **Hasło**: admin123

## Struktura projektu

```
ERP-CRM/
├── app/
│   ├── __init__.py          # Factory aplikacji
│   ├── models/              # Modele bazy danych
│   │   ├── user.py
│   │   ├── customer.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── invoice.py
│   ├── routes/              # Blueprinty routingu
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── crm.py
│   │   ├── inventory.py
│   │   ├── sales.py
│   │   └── invoices.py
│   ├── templates/           # Szablony HTML
│   └── static/              # Pliki statyczne (CSS, JS, obrazy)
├── config.py                # Konfiguracja aplikacji
├── run.py                   # Punkt wejścia
└── requirements.txt         # Zależności
```

## Licencja

© 2025 GREDA. Wszystkie prawa zastrzeżone.

## Kontakt

Email: kontakt@greda.pl
