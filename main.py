from website import create_app

app = create_app()

# rodando nosso web server dentro de main
if __name__ == '__main__':
    app.run(debug=True)
    