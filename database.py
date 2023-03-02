import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')

    def add(self, note):
        self.conn.execute('INSERT INTO note (title, content) VALUES (?, ?)', (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        lista = []
        cursor = self.conn.execute('SELECT id, title, content FROM note')
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id, title, content))
        return lista

    def update(self, entry):
        self.conn.execute('UPDATE note SET title = ?, content = ? WHERE id = ?', (entry.title, entry.content, entry.id))
        self.conn.commit()

    # Implemente o método delete(self, note_id), que recebe o valor de um id e apaga essa entrada do banco de dados. Obs: lembre-se de chamar o método commit depois do execute.

    # Se tudo der certo. O teste test_delete_row e todos os outros devem passar com sucesso.

    def delete_id(self, note_id):
        self.conn.execute(f'DELETE FROM note WHERE id = {note_id}')
        self.conn.commit()
        