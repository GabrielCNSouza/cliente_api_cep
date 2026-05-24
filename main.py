from services.cep_service import consultar_cep, normalizar_cep, validar_cep
from models.endereco import Endereco


def exibir_endereco(dados:Endereco) -> None:

    print('\nCEP encontrado:')
    print(f'CEP: {dados.cep}')
    print(f'Logradouro: {dados.logradouro}')
    print(f'Bairro: {dados.bairro}')
    print(f'Cidade: {dados.cidade}')
    print(f'Estado: {dados.estado}')


def main() -> None:

    print('--- Consulta de CEP ---')
    print('Digite um CEP ou "sair" para encerrar.\n')

    while True:

        entrada = input('Digite o CEP: ')

        if entrada.strip().lower() == 'sair':
            print('Programa encerrado.')
            break

        cep = normalizar_cep(entrada)

        if not validar_cep(cep):
            print('CEP inválido. Digite 8 números.')
            continue # pula para a próxima tentativa

        resultado = consultar_cep(cep)

        if resultado.erro:
            print(resultado.erro)
            continue

        if resultado.dados is None:
            print('Não foi possível consultar o CEP.')
            continue

        exibir_endereco(resultado.dados)


if __name__ == "__main__":
    main()

