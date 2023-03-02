import json
from database import *

def extract_route(request):
    """Implemente a função extract_route, que recebe uma string com a requisição e devolve a rota, excluindo o primeiro caractere (/).
    """
    # return request.split()[1][1:]
    if request == "":
        return ""
    return "/".join(request.splitlines()[0].split("/")[1:]).split("HTTP")[0].strip()

def read_file(filepath):
    """Implemente a função read_file, que recebe um caminho de arquivo e devolve o conteúdo do arquivo.
    """
    with open(filepath, 'rb') as f:
        return f.read()

def load_data(banco):
    """Implemente a função load_data, que recebe um caminho de arquivo e devolve um dicionário com os dados contidos no arquivo.
    """
    db = Database(f'{banco}')

    notes = db.get_all()

    return notes

def load_template(filepath):
    """Implemente a função load_template, que recebe um caminho de arquivo e devolve uma string com o conteúdo do arquivo.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def formata_nota(nota):
    # title = chave da nota
    # details = valor da nota
    return {'titulo': nota.keys(), 'detalhes': nota.values()}

def adicionar_nota(nota):
    """Implemente a função adicionar_nota, que recebe um dicionário com os dados da nota e adiciona a nota ao arquivo notes.json.
    """
    db = Database('banco')
    size = len(nota)
    note = Note(title=nota['titulo'], content=nota['detalhes'])
    db.add(note)

def build_response(body='', code=200, reason='OK', headers=''):
    """Implemente a função build_response, que recebe um corpo, um código, um motivo e um cabeçalho e devolve uma string com a resposta HTTP.
    """
    if len(headers) == 0:
        return f'HTTP/1.1 {code} {reason}\n{body}'.encode()
    else:	
        return f'HTTP/1.1 {code} {reason}\n{headers}\n{body}'.encode()

    