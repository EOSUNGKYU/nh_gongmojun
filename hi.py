for i in range(1,9):
    globals()[f'ifo_{i}'] = pd.read_csv(f'NASDAQ_RSS_IFO_20230{i}.csv', encoding='latin-1')

column_mapping = {
    'rgs_dt': '발행일자',
    'tck_iem_cd': '티커종목코드',
    'til_ifo': '제목정보',
    'ctgy_cfc_ifo': '카테고리분류정보',
    'mdi_ifo': '미디어정보',
    'news_smy_ifo': '뉴스요약정보',
    'rld_ose_iem_tck_cd': '관련해외종목티커코드',
    'url_ifo': 'url'
}


dataframes = [ifo_1, ifo_2, ifo_3, ifo_4, ifo_5, ifo_6, ifo_7, ifo_8]

for df in dataframes:
    df.rename(columns=column_mapping, inplace=True)
