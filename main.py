# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

banco = {
    "livros":
        [{'id': 1,
          'nome': 'diagrama de sequência',
          'status': False},
         {'id': 2,
          'nome': 'banco de dados sql 2022',
          'status': False}],

    'alunos':
        [{'id': 1,
          'nome': 'Renan',
          'livros_empres': 0},
         {'id': 2,
          'nome': 'Priscila',
          'livros_empres': 0}],

    'func':
        [{'id': 1,
          'nome': 'Maria',
          'nivel': 3,
          'status': True}]}


class Funcionario:
    def __init__(self, id_func):
        self.id_func = id_func

    def validar_func(self):
        for x in banco['func']:
            if self.id_func == x['id']:
                return [True, x['nome']]
            else:
                return False


class Livro:
    def __init__(self, cod_livro):
        self.cod_livro = cod_livro

    def pesquisar_livro(self):
        for x in banco['livros']:
            if self.cod_livro == x['id']:
                return [x['id'], x['nome']]
        else:
            return False


class Aluno:
    def __init__(self, cod_aluno):
        self.cod_aluno = cod_aluno

    def pesquisa_aluno(self):
        for x in banco['alunos']:
            if self.cod_aluno == x['id']:
                return [x['id'], x['nome']]
        else:
            return False


class Emprestimo:
    def __init__(self, cod_aluno, cod_func, cod_livro):
        self.aluno = cod_aluno
        self.func = cod_func
        self.livro = cod_livro

    def efetuar_emprestimo(self):
        pass  # poderia ter ou chamar function que alterava os status do livro e aluno


class TelaEmprestimo:
    def __init__(self, cod_aluno, cod_func, cod_livro):
        self.aluno = cod_aluno
        self.func = cod_func
        self.livro = cod_livro

    def botao_efetuar_emprestimo(self):
        botao = ''
        _func = Funcionario(self.func).validar_func()

        if _func[0]:  # é a mesma coisa que if _func == True
            _livro = Livro(self.livro).pesquisar_livro()
            _aluno = Aluno(self.aluno).pesquisa_aluno()

            r_click = Emprestimo(_aluno, _func, _livro)

            return f'FUNCIONARIO: {r_click.func[1]}\nALUNO: {r_click.aluno[1]}\nEMPRESTOU LIVRO ID: {r_click.livro[0]} \nNOME DO LIVRO: {r_click.livro[1]}'
        else:
            print(f'funcionario id:{self.func} não tem permissão!')
        return botao


if __name__ == '__main__':
    #  instancias do objeto TelaEmprestimo passando como argumento (cod_aluno, cod_func, cod_livro)
    retorno = TelaEmprestimo(2, 1, 1).botao_efetuar_emprestimo()
    print(retorno)
