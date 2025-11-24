from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("    System ERP/CRM uruchomiony!")
    print("=" * 60)
    print(f"  URL: http://localhost:8080")
    print(f"  Login: admin@example.com")
    print(f"  Hasło: admin123")
    print("=" * 60)
    print()
    
    app.run(host='0.0.0.0', port=8080, debug=True)
