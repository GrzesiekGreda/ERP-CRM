# 🚀 INSTRUKCJE WDROŻENIA STRONY GREDA

## 📋 Lista plików do przesłania na serwer:
✅ index.html (2.3 KB) - główna strona
✅ styles.css (3.7 KB) - style i logo  
✅ script.js (3.8 KB) - animacje i interakcje

## 🌐 Wdrożenie na greda.pl

### Metoda 1: Panel hostingowy (ZALECANA)
1. Zaloguj się do panelu zarządzania hostingiem greda.pl
2. Znajdź sekcję "Menedżer plików" lub "File Manager"
3. Przejdź do katalogu głównego strony (public_html/www/htdocs)
4. Prześlij wszystkie 3 pliki z folderu "deployment"
5. Ustaw index.html jako stronę główną (jeśli potrzeba)

### Metoda 2: FTP/SFTP
**Dane do połączenia (uzyskaj od dostawcy hostingu):**
- Serwer: ftp.greda.pl (lub podobny)
- Port: 21 (FTP) lub 22 (SFTP)
- Login: [twoj_login]
- Hasło: [twoje_hasło]

**Kroki:**
1. Uruchom FileZilla, WinSCP lub inny klient FTP
2. Połącz się z serwerem
3. Przejdź do katalogu głównego strony
4. Prześlij pliki z folderu "deployment"

### Metoda 3: Git (jeśli dostępne)
```bash
git init
git add index.html styles.css script.js
git commit -m "Deploy GREDA website"
git remote add origin [adres_repo]
git push origin main
```

## ✅ Po wdrożeniu sprawdź:
1. Czy strona ładuje się pod adresem https://greda.pl
2. Czy logo GREDA wyświetla się poprawnie
3. Czy animacje działają
4. Czy strona jest responsywna na telefonie

## 🔧 Możliwe problemy:

### Problem: Strona nie ładuje się
**Rozwiązanie:** 
- Sprawdź czy index.html jest w katalogu głównym
- Zweryfikuj uprawnienia plików (644 dla plików, 755 dla folderów)

### Problem: Brak stylów/animacji
**Rozwiązanie:**
- Sprawdź czy wszystkie 3 pliki są na serwerze
- Zweryfikuj ścieżki w index.html (styles.css, script.js)

### Problem: Logo nie wyświetla się
**Rozwiązanie:**
- Sprawdź czy Google Fonts są dostępne (połączenie internetowe)
- Zweryfikuj plik styles.css

## 📞 Wsparcie techniczne:
Jeśli masz problemy, skontaktuj się z działem technicznym dostawcy hostingu greda.pl

---
Strona gotowa do produkcji! 🎉