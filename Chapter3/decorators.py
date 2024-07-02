def anuncio(f):
    def wrapper():
        print("Executando a função")
        f()
        print("Função executada")
    return wrapper

@anuncio
def hello():
    print("Ola mundo")

hello()