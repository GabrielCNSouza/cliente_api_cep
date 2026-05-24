from services.cep_service import consultar_cep, normalizar_cep, validar_cep
from models.endereco import Endereco


def exibir_endereco(dados:Endereco) -> None:

    print('CEP encontrado:')
    print(f'CEP: {dados.cep}')
    print(f'Logradouro: {dados.logradouro}')
    print(f'Bairro: {dados.bairro}')
    print(f'Cidade: {dados.cidade}')
    print(f'Estado: {dados.estado}')


def main() -> None:
    cep = normalizar_cep(input('Digite o CEP: '))

    if not validar_cep(cep):
        print('CEP inválido. Digite 8 números.')
        return

    resultado = consultar_cep(cep)

    if resultado.erro:
        print(resultado.erro)
        return

    exibir_endereco(resultado.dados)


if __name__ == "__main__":
    main()

