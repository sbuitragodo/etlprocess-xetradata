"""Running the Xetra ETL pipeline"""
import logging
import logging.config

import yaml

def main():
    """
     entry point to run the xetra ETL job
    """
    # Parsing YAML file
    config_path = 'C:/Users/Flia BuiSar/Documents/"Docs Sebastian"\
                   /Courses/ETLPythonProject/etlprocess-xetradata\
                   /configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test")

if __name__ == '__main__':
    main()
