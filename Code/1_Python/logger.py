import logging

logging.basicConfig(
    # filename="applic.log",
    # filemode="w",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S - %d-%m-%Y',
    force=True  # This forces reconfiguration of logging
)