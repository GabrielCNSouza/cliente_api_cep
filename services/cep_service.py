import requests

from models.resultado_consulta import ResultadoConsulta
from models.endereco import Endereco


def normalizar_cep(cep:str) -> str:
    return cep.strip().replace('-','')


def validar_cep(cep:str) -> bool:
    return len(cep) == 8 and cep.isdigit()


def consultar_cep(cep:str) -> ResultadoConsulta:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5) # se demorar mais que 5 segundos a consulta é abortada.

        if resposta.status_code != 200:
            return ResultadoConsulta(
                dados=None,
                erro=f'Erro HTTP: {resposta.status_code}'
            )
        
        dados = resposta.json()

        if dados.get('erro'):
            return ResultadoConsulta(
                dados=None,
                erro='CEP não encontrado.'
            )
        
        endereco = Endereco(
            cep=dados.get('cep', ''),
            logradouro=dados.get('logradouro', ''),
            bairro=dados.get('bairro', ''),
            cidade=dados.get('localidade', ''),
            estado=dados.get('estado', '')
        )

        return ResultadoConsulta(
            dados=endereco,
            erro=None
        )
    
    except requests.Timeout:
        return ResultadoConsulta(
            dados=None,
            erro='Tempo limite excedido ao consultar a API.'
        )
    
    except requests.ConnectionError:
        return ResultadoConsulta(
            dados=None,
            erro='Erro de conexão. Verifique sua internet.'
        )
    
    except requests.RequestException:
        return ResultadoConsulta(
            dados=None,
            erro='Erro inesperado ao consultar a API.'
        )
    
    except ValueError:
        return ResultadoConsulta(
            dados=None,
            erro='A API retornou uma resposta inválida.'
        )