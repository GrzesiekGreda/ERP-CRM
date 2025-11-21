# 🔗 VS Code + GitHub - Kompletna konfiguracja

## ✅ **Co już mamy:**
- ✅ Git zainstalowany (v2.52.0)
- ✅ Rozszerzenia VS Code: GitHub Pull Requests, GitLens
- ✅ Git skonfigurowany z email: eesiek@gmail.com
- ✅ Repozytorium Git zainicjalizowane

## 🚀 **Następne kroki:**

### **Krok 1: Połącz VS Code z GitHub**
1. **Naciśnij** `Ctrl + Shift + P`
2. **Wpisz:** `GitHub: Sign In`
3. **VS Code** otworzy przeglądarkę
4. **Zaloguj się** do swojego konta GitHub
5. **Potwierdź** autoryzację dla VS Code

### **Krok 2: Połącz lokalny projekt z GitHub repo**
```bash
# W terminalu VS Code (Ctrl + `)
git remote add origin https://github.com/[TWOJA-NAZWA]/GREDA.git
git add .
git commit -m "Initial commit - connect to GitHub"
git branch -M main  
git push -u origin main
```

### **Krok 3: Weryfikacja połączenia**
- Ikona GitHub powinna pojawić się na lewym panelu
- W statusie VS Code (dół) powinno być widać branch (main)
- Możliwość push/pull z GitHub

## 🛠️ **Funkcje po połączeniu:**

### **Source Control (Ctrl + Shift + G)**
- 📝 **Commit** - zapisywanie zmian
- 🔄 **Push/Pull** - synchronizacja z GitHub  
- 🌿 **Branch** - tworzenie gałęzi
- 📊 **History** - historia zmian

### **GitHub Panel**
- 🔍 **Issues** - zarządzanie zadaniami
- 🔃 **Pull Requests** - przegląd kodu
- 👥 **Collaborators** - współpraca zespołowa
- 📈 **Actions** - CI/CD pipeline

### **GitLens Features**
- 👤 **Blame** - kto zmienił linię kodu
- 📅 **History** - historia pliku
- 🔍 **Search** - szukanie w historii
- 📊 **Insights** - statystyki repo

## 🎯 **Po skonfigurowaniu będziesz mógł:**

### **Replikowanie projektów:**
1. **Clone** - `git clone [URL]` lub przez VS Code
2. **Fork** - kopiowanie cudzych projektów  
3. **Template** - tworzenie na bazie szablonu

### **Management projektów:**
1. **Create** - nowe repo bezpośrednio z VS Code
2. **Sync** - automatyczna synchronizacja
3. **Branch** - równoległe wersje projektu
4. **Merge** - łączenie zmian

### **Współpraca:**
1. **Issues** - zgłaszanie problemów
2. **Pull Requests** - propozycje zmian
3. **Code Review** - przegląd kodu
4. **Teams** - praca zespołowa

## ⚙️ **Przydatne skróty klawiszowe:**
- `Ctrl + Shift + G` - Source Control
- `Ctrl + Shift + P` - Command Palette  
- `Ctrl + \`` - Terminal
- `F1` - Wszystkie komendy

## 🔧 **Troubleshooting:**

### Problem: "Git not found"
**Rozwiązanie:** Restartuj VS Code po instalacji Git

### Problem: "Authentication failed"  
**Rozwiązanie:** Użyj Personal Access Token zamiast hasła

### Problem: "Push rejected"
**Rozwiązanie:** Najpierw `git pull` potem `git push`

---
**Po wykonaniu tych kroków będziesz miał pełną integrację VS Code z GitHub!** 🎉