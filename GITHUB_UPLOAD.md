# 🚀 Instrukcje wrzucenia projektu GREDA na GitHub

## 📋 Pliki gotowe do uploadu:

✅ **index.html** - główna strona  
✅ **styles.css** - style i logo  
✅ **script.js** - animacje i interakcje  
✅ **README.md** - dokumentacja projektu  
✅ **LICENSE** - licencja MIT  
✅ **.gitignore** - pliki do zignorowania  
✅ **DEPLOYMENT.md** - instrukcje wdrożenia  
✅ **deployment/** - folder z plikami produkcyjnymi  

## 🌐 Kroki upload na GitHub:

### Krok 1: Utwórz nowe repozytorium
1. Wejdź na https://github.com
2. Kliknij **"New repository"** (zielony przycisk)
3. Nazwa repozytorium: **`GREDA`**
4. Opis: **"Nowoczesna wizytówka firmowa GREDA - responsive website"**
5. Ustaw jako **Public** (żeby było widoczne)
6. ❌ **NIE** zaznaczaj "Initialize with README" (mamy już własny)
7. Kliknij **"Create repository"**

### Krok 2: Upload plików
**Opcja A: Przez interfejs GitHub (Zalecana)**
1. Na stronie nowego repo kliknij **"uploading an existing file"**
2. Przeciągnij wszystkie pliki z folderu `C:\Users\g.greda\GREDA\`
3. **UWAGA:** Folder `deployment/` też przeciągnij
4. W polu "Commit changes" wpisz: `Initial commit - GREDA company website`
5. Kliknij **"Commit changes"**

**Opcja B: Przez Git (jeśli zainstalujesz)**
```bash
git init
git add .
git commit -m "Initial commit - GREDA company website"
git branch -M main
git remote add origin https://github.com/[TWOJA-NAZWA]/GREDA.git
git push -u origin main
```

### Krok 3: Konfiguracja GitHub Pages (Opcjonalne)
1. W repozytorium idź do **Settings**
2. Scroll w dół do sekcji **"Pages"**
3. W "Source" wybierz **"Deploy from a branch"**
4. Branch: **"main"** 
5. Folder: **"/ (root)"**
6. Kliknij **"Save"**
7. Strona będzie dostępna pod: `https://[TWOJA-NAZWA].github.io/GREDA`

### Krok 4: Dodaj tematy (Topics)
W głównej sekcji repo kliknij ⚙️ obok "About" i dodaj:
- `html`
- `css` 
- `javascript`
- `website`
- `business-card`
- `responsive-design`
- `greda`

## 📊 Co zyskujesz:
✅ **Backup projektu** w chmurze  
✅ **Wersjonowanie** - historia zmian  
✅ **Współpraca** - możliwość pracy zespołowej  
✅ **GitHub Pages** - dodatkowe hostowanie  
✅ **Portfolio** - prezentacja Twoich projektów  

## 🔗 Przydatne linki:
- 📘 [GitHub Docs](https://docs.github.com)
- 🎓 [Git Tutorial](https://git-scm.com/docs/gittutorial)
- 🌐 [GitHub Pages Guide](https://pages.github.com)

---
**Powodzenia z wrzuceniem projektu na GitHub!** 🎉