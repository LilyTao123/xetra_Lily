''' Xetra ETL Component '''
from typing import NamedTuple
import logging 

from xetra.common.s3 import S3BucketConnector

class XetraSourceConfig(NamedTuple):
    '''
    Class for source configuration data

    src_first_extract_date: determines the date for extracting the source
    src_columns: source column names
    src_col_date: column name for date in source
    src_col_isin: column name for isin in source
    src_col_time: column name for time in source
    src_col_start_price: column name for starting price in source
    src_col_min_price: column name for minimum price in source
    src_col_max_price: column name for manimum price in source
    src_col_traded_vol: column name for traded volumn in source

    '''
    src_first_extract_date: str
    src_columns: str
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class XetraTargetConfig(NamedTuple):
    '''
    Class for target configuration data

    trg_col_isin: column name for isin in target
    trg_col_date: column name for date in target
    trg_col_op_price: column name for opening price in target
    trg_col_clos_price: column name for closing price in target   
    trg_col_min_price: column name for minimum price in target
    trg_col_max_price: column name for manimum price in target 
    trg_col_dail_trad_vol: column name for daily traded volumn in target
    trg_col_ch_prev_clos: column name for change to previous day's closing price in target
    trg_key: basic key of target file
    trg_key_date_format: date format of target file key
    trg_format: file format of the target file

    '''
    trg_col_isin: str
    trg_col_date: str
    trg_col_op_price: str
    trg_col_clos_price: str   
    trg_col_min_price: str
    trg_col_max_price: str 
    trg_col_dail_trad_vol: str
    trg_col_ch_prev_clos: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class XetraETL():
    '''
    Reads the Xetra data, transforms and writes the transformed to target
    '''

    def __init__(self, s3_bucket_srcc: S3BucketConnector,
                 s3_bucket_trg: S3BucketConnector,
                 src_args: XetraSourceConfig, trg_args: XetraTargetConfig):
    '''
    Constructor for XetraTransformer
    
    :params s3_bucket_src: connection to source S3 bucket
    :params s3_bucket_trg: connection to target S3 bucket
    :params meta_key: used as self.meta_key -> key of meta file
    :params src_args: NamedTuple class with source configuration data
    :params trg_args: NamedTuple class with target configuration data
    '''
    
    self.logging = logging.getLogger(__name__)
    self.s3_bucket_src = s3_bucket_src
    self.s3_bucket_trg = s3_bucket_trg
    self.meta_key = meta_key
    self.src_args = src_args
    self.trg_args = trg_args
    self.extract_date = 
    self.extract_date_list = 
    self.meta_update_list = 

def extract(self):
    pass

def transform_report1(self):
    pass

def load(self):
    pass

def et1_report1(self):
    pass
    































