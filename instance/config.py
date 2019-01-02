SECRET_KEY = 'NEER_ESBI_TEST_APP_OXR0MQY'

SQLALCHEMY_DATABASE_URI = 'sqlite:///app\esbi_config_local.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_BINDS = {
    'local': 'sqlite:///esbi_config_local.db',
    'orx_dev_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
    'orx_dev_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
    'orx_dev_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD',
    'orx_qa_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
    'orx_qa_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
    'orx_qa_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD',
    'orx_prod_es_dw': 'oracle://ES_DW_OWNER:.8+4=EOV@PGSDWD',
    'orx_prod_es_ods': 'oracle://ES_ODS_OWNER:yD8J;Czg@PGSDWD',
    'orx_prod_solar_ods': 'oracle://SOLAR_ODS_OWNER:b}674xm3@PGSDWD'
}
