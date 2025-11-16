import logging

from src.utils import pegar_data_hora

def config_logger():
    # Configurar o logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Define o nível de registro para INFO ou superior
    logging.basicConfig(level=logging.INFO)  # Define o nivel do registro que irá aparecer no terminal

    # Criar um manipulador de saída (ex: para um arquivo)
    file_handler = logging.FileHandler(f'./logs/GCPJ_Inclusao/log_GCPJ_Incl_{pegar_data_hora()[2]}.log', encoding='utf-8')  # Registra no arquivo error.logs

    # Criar um formatador de mensagens
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Adicionar o formatador ao manipulador
    file_handler.setFormatter(formatter)

    # Adicionar o manipulador ao logger
    logger.addHandler(file_handler)
    return logger

# Função para registrar erros
def log_error(message, exception=None):
    logger = config_logger()
    if exception:
        logger.error(f'\n{message}', exc_info=True)  # Registra a mensagem com informações de exceção
    else:
        logger.error(f'\n{message}')

# Função para registrar avisos (opcional)
def log_warning(message, exception=None):
    logger = config_logger()
    if exception:
        logger.warning(f'\n{message}', exc_info=True)  # Registra a mensagem com informações de exceção
    else:
        logger.warning(f'\n{message}')

def log_info(message):
    logger = config_logger()
    logger.info(f'\n{message}')
