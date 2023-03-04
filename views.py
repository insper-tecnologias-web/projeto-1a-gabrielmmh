from utils import *
from database import *
import urllib.parse

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            cv = chave_valor.split('=')
            params[cv[0]] = urllib.parse.unquote_plus(cv[1])

        formata_nota(params) 
        
        adicionar_nota(params)

        return build_response(code=303, reason='See Other', headers='Location: /')
    
    note_template = load_template('templates/components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in load_data('banco')
    ]
    notes = '\n'.join(notes_li)

    body = load_template('templates/index.html').format(notes=notes)
    
    return build_response(body)

def delete(request):
    """Implemente a função delete, que recebe uma string com a requisição e devolve uma string com a resposta HTTP.
    """
    db = Database('banco')
    id = request.split("delete/")[1].split(' HTTP')[0]
    db.delete_id(id)
    return build_response(code=303, reason='See Other', headers='Location: /')

def update(request):
    route = extract_route(request)
    id = route.split('/')[1]
    
    db = Database('banco')
    note = db.get(id)

    body = load_template('templates/update.html').format(id=note.id, title=note.title, details=note.content)
    print('oi1')
    print(note)
    print(body)
    if request.startswith('POST'):
        request = request.replace('\r', '') 

        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            cv = chave_valor.split('=')
            params[cv[0]] = urllib.parse.unquote_plus(cv[1])

        formata_nota(params) 
        
        note.title = params['titulo']
        note.content = params['detalhes']

        db.update(note)
        return build_response(code=303, reason='See Other', headers='Location: /')
    
    return build_response(body=body)