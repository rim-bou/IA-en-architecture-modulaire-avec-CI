from loguru import logger

def calcul(x: int) -> int:
    logger.info("calcul() appelé avec x={}", x)
    return x * x
