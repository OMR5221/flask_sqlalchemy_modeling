# config.py: Has configuration variables for the app (ex: database details)

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Test configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_BINDS = {
        'local': 'sqlite:///esbi_config_local.db',
        'orx_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
        'orx_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
        'orx_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD'
    }


class QAConfig(Config):
    """
    QAConfig configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_BINDS = {
        'local': 'sqlite:///esbi_config_local.db',
        'orx_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
        'orx_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
        'orx_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD'
    }

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {
        'local': 'sqlite:///esbi_config_local.db',
        'orx_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
        'orx_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
        'orx_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD'
    }

app_config = {
    'qa': QAConfig,
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
