from login import login
from fetch_one_page import fetch_and_parse, write_to_file, read_to_data


urls1 = [
    "https://detail.tmall.com/item.htm?id=789512157493&pisk=gijjF3ZlejcXuV0VJleyRY1Uslt151ZUlA9OKOnqBnKvCc6h1t-NBCS6f_fJWi-V3_Z1K6T2WGRNfxj5Oco4irXtfh-TTWrUYtXWjhFe1iKNFxvwQCpx_KK-yhXX3Wi8YtXDjxGTLaEE1nlpFddO6ELJwdA-kjpO6UKJdQnvBmptw89MwhhvHdBJ2KJxHdCtDYEJLd99HKnveup9wCK9Xb0ENdzXBtwlPloUnRg5YQitXg98IBWj10vO4KOyOtIbzzyMhEOdHQNeK2d9yOY1jAm65tQhspCxMW8cBa1WhhZrkHB5W69lDklXEZWRLQBIpDBpcdTpXUMtXTtDZUIJvkhWEaBVWifjCcpc0M86tUwtjF-RYeQdGA2henpOsejatmAAB9jh8HZrkHB5W6_14zneOuUs5YTnfLOUF8giSaC_JjXht2fHkLvYY8wSNVYvELOUF8giSEpkHwy7FbgG.&spm=pc_detail.29232929.guessitem.d4&skuId=5555657106357",
    "https://detail.tmall.com/item.htm?id=693460014688&pisk=gDXIFJ2GX20Ci_GFM8EwGcsBQpJ5Paw4O0tRmgHE2pppVYscPMJP2UWWFNb9w9JFYNw5mZOewT8PFDX1lYkU-Wj-FLJ8ury43Mj6ELUVAji5J2x2mHey2vhOxMS7lVe43MjnYHEVX-WeLJa6qUpJ9QdtXFxXv2QJwGd9S3x-J3HLfGLMWH3JJXHTB3tqe4QJ2RL9mn8JyBL-6cKHWUpJeboE53PB2MZG1uR92SFA7FM-eOtTqEIQGx-CdHwXlMT_kWWsoBTAvFM8ufUJeUTGHPP1jZ1d8hb7hP9lS_QJVN3TzBjR1NtC8rgkz9jFFeSQ9PI6ee9Opsi-eG9B-QWJO2a6k9jOnddaHosOIwShCgo8eh72WMXpF-EDdpLpChXzSvL56_BetL0LuBjR1NtBHg7K3EwTNbi6iYt6ulZsZbfOPS3hmZccoBKMv-r_fVGk9hx6ulZsZbApjHC4flgsZ&spm=pc_detail.29232929.guessitem.d0&sku_properties=21433%3A25408974172",
    "https://detail.tmall.com/item.htm?id=789517612540&pisk=g4NIFPfgWHxICl9UH_QZhFOp9ClSOu1VdUg8ozdeyXhKPQa0Vylzy0PSNlqteWlU8l17ooMEe7ozNeV_cQRFx94JNblR0i5Vgy4sZbI2_xiYrH0jo3CryvUT-yz5chCVgy4H82Q4WsPET9_qr0h-pYH9Wc0XpQE-efLtj40Jv4dd5PniXQ3Jp0nt643peBEJ9FCtu4tpevHJ6V3oX0h-wbXef4WIyy_gCM_Bk3pbocOJw5gOrmUBvB30M2MqcyFCMsBoRviYJcsqoKn-BzD7ZUASFye0qqEpvik3yRZsRb1wpjU_eogg9s-ISJzTucUXkIUxO4MxwATJwPGnjAFtMsKsSRUUeWqBPQ33TSkSmA_JZYlTgxeYAUb0WX38qxVPmBmLyrV03j1wpjU_eow54edqc1BWFFMDNViV5N9kERE5HH40mKqmpV0dgN_6fLDKSViV5N9kEv3iJ-715h9l.&spm=pc_detail.29232929.guessitem.d6&sku_properties=21433%3A22108466621",
    "https://detail.tmall.com/item.htm?id=673206585072&pisk=gaaneL6AokoIDnxsF1uCqGYvk5sOABgSE8L-e4HPbAk_ykHRAafoISodO8e8jY2aIvPKe6aujJNqv8V5ObkzU8D8vGQYOWgSztBlkZFITgfVe8mELN7a1jpy8ZKKzSfqztBAkhdZA93zpXqt3APZCbcraUyy7FljQblEa8kZbjlvL4uzU1cZZXYy8Dke_hlrQ3JEL0PwbjheYY8E41VZCblrpHkYzozNdZ-P7LyCrzhnxxPELJeL7NikA7kgxkatt52zTQTyzPcnxzphgHxZvuPjcyFlrFgLiluZMW_HSqPEiJHT3Z8i75FaemZ1FEn_Izmz8mRyY54oKmzEjQL4iVczU0q1nEhnJlm0-k1WQWyxKouQwIXLsmqicfowZHuLDSUS0y7HhAnjZJHT3Z8i70SPEh-qKYLS__UwV3iE1fDvttgKB3Hst_CGsnFSYfGjH1fMV3iE1fDAs1xYPDlsGxC..&spm=pc_detail.29232929.guessitem.d9&sku_properties=134942334%3A25326464224",
]

urls2 = [
    "https://detail.tmall.com/item.htm?id=842582560548&pisk=gFajEjbuwKvfl9K4vNCrABs0kqg_1R_FcCGTt5L26q3xBCw86EHtHfd8wfGMXcHNmRi_Q8mTuqP4FI47dF8VniV95VuOL97F8SVSSVBeKIzoAIcZMdh9QFhJ2VcnJ9a58SVmII9OTuQeCqJ7LFKtBR3-2fctWEHxW_g-1X09kcLv2LHo6V3tHndJyfcwXnHxM_O-tf-vBchv27hE9d3tWRF-amJS_iGTG_qzv1GMTOVjFFLTPbCipS1e-jUnGgMQGY6dpz9ncvFxFFB32H4-CY4dUgNudoeqZR_CFV2uXRh_eLBZm5E7FjwVddDaoSzs3SsAe7gth4UYACLTNqMmbPnXhTMLo7Uny07dO7Uu3S47_CQtaJk8ir31J60jkx3SZPWkkAZ8XromSKBEm5E7Fjgd4TYEdaI6fQiH5bMFN_tMjue1vKjQPqyoDbcA8_1WFhmxZbMFN_tMjmhoMk55NLtG.&spm=a21xtw.29178619.product_shelf.10.7ab366adCR4uRL&skuId=5613144308019",
    "https://detail.tmall.com/item.htm?id=842395321770&pisk=gfw-E7Y4GZblB0K2Le1mtWDJckI0pJErHzr6K20kOrUYAzgo-4MIlIirAD9SAkiIprah44qCzyeKlYGUZ20oJvEUWibGIOqz4vuCSNXMQJTNJYiWdbO5AtitbNY75OLU4vkCJnvCsOEz5XhG42iIcinnx2gQR4gbcqoKA0aIPjTjXckIRyaIltirX2iIA0gXhqoWdDgWNKgjvDLWPvaQcinEw_S-u3iJpWREYF3clkvBd-n-GtqSlDiOxDh8pu0A5Nwv7b3_VqpC7SOah234CZfY0PF7rmzdBZHUuWaIvrTf-brQMrn8rNLE-8rup4qRNZZxd4HbF5KBdoH-zX2IwUQx58rbQxGcCGEb3zqzHkxCdm4iluySpOsZeYgSHmyhuLgLGWwoav85SbrQMrn-CguLIRBHmF0txQsADBRENmr8VfORU0SdYm3GVbOeTXmqDVjADBRENmoxSg9WTBln0&spm=a21xtw.29178619.product_shelf.8.7ab366adCR4uRL&skuId=5781323030885",
    "https://detail.tmall.com/item.htm?id=842395269080&pisk=gmujEbTowtXfIzIqvFdzA6tmkrashATec1NttfQV6rUYB1M-6ZeTH5C-w5NGXlewmAZsQYqturlqFs0SdN72nncO5Pz9Lp8e8jc7SPpFKsuuAsVa15QAQNQ82PV3JpgW8jc0Is69T0LFCrWSqNITBAU825VTWZeYWQa8_SUOklQA2Teu6PUTHiCRy5VNXieYMQ18t57AMSEO2UFgMRUTWAh-wC67_nNtGQmrvCNMhXGYFNQtkhqbd12YZSg7xoeL28_T44NbcJhxuGNuD73rPkrP_Lz-t0kYNyTPDyhSXviKIHSulfnxIuMDEgwr2qcTBo1OlbZ_h03YV1QtZz2_XcMXhi2x0YZ3wuC6-7kUej0xVCX-Mvybk7EyJBG8X0u0xqJRlynngrotIHSulfnYPgWl8JTJfG17xNN7LQO5jGm-CHBDA4aqEoFuMeRWNTsgD7V7LQO5jGqYZSneNQ65j&spm=a21xtw.29178619.product_shelf.7.7ab366adCR4uRL&skuId=5781321494151",
    "https://detail.tmall.com/item.htm?id=842395085009&pisk=ga5-eNiVhoqu6r0qTDwDK9A-lwU0S6QyMg7stHxodiIARgtkx3OBcxTyReGWRwTB9is3z3bQ4MCpcQ9FEHxkvBQFXrqgs5bPzB-QjlVi_6iavCuSVpinljTyO0O_6sQPzB-IoDwGhaopKm2EOetQkITpRHOBV3_bkeYKFBtWdmMX5ntBOMt7GqTMReMBP3GbkU86RbMWPZgXSetIPMOQkZGJizKqPUhdLv8EXn0AbXGCMUpbiatXHLUHlLINynE_fsnweh_WDXZNhA5Xvn5_m-QVXTskuMFTDBSVdMTdcmZHUw6ADUIuXD-haafpqae7cZdB2I15B2GCkQKyK69-2oK1aZ1wGKV_WZ1Vqa5A-2NBoGxfz_OL1PRJN3Ovu6qqNHBfd_vyT0ZMUw6ADUd14pCG6W0mjhLnFrUxLvJWuaQWCYFyzyUekh4WFvkeKE8vjrUxLvJWuEKgPbMELpYV.&spm=a21xtw.29178619.product_shelf.6.7ab366adCR4uRL&skuId=5781320746040",
    "https://detail.tmall.com/item.htm?id=842394425323&pisk=geyxEPTzNabcBH-yQF1os5DvVlIlqREqerrBIV0D1zU8frgmSqMsPQiqfc9jflisBzaG0qq1uPetPxGaiV0mWAEaJgbhK9q40Au1-wXHLRTFWxiX5I9ff0iKDwYbR9La0Ak1W3v1t9E4RfhhgVisVgnijVg_5qg7V4otccaslbTSvDks5PasPTiqvVisfmgWF4oXCcgXG0iSXDpjfqa_VgnZwwSxznivB5RZbe3llz96C8nxNTqjPSVlj0hxHo3RRwwJ8j3Qc4p187OUFV3zdaf84yFbo0zOpaHaz5asXzT5Sjr_wznYowLZS-r0BqqAGaZ-CqH7hWK6CuHxuf2sMEQ-R-r7LYGldME7Urq4elx1C04nPoyjB9sEHxgje0yGzKgTN5wmgA8f-jr_wznxdgk8KJBMqe0KjIsR2CRZG0rYcXOA3mSOb03hcjOw_fmr22jR2CRZG0o--i9X_Cli4&spm=a21xtw.29178619.product_shelf.5.7ab366adCR4uRL&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?id=842119830020&pisk=gRRqEGwm0jhVzPlCPaCN8vJaAxCA9smIuCs1SFYGlijccCtwSNbgiRVGsTjl8gNsksMO_hSyXi6fiCJ8_eL9GqCsksLA61mIAXGwkECTnxt-LC5uEZ_E1-XgsEEo2cxrAXGBzxbA1UmBGt-qPwQQs1XcIUYl2NFcjhXDrbjRWNqcSS0yrgIuirVGoUXl8wP0nhVGrTb17rqGm1YlENIlj1fiZtxMD7SPn2ZCvabIN1BVxEjzT3dPoyjK9gNM9Qbc3CYc4T6WaZWVxTQlVEdDVFAXMTHuU1LWLhJMXvwRgFvciwTxg75HoLONPCg_QixvaUAlUrP2Ys-NKIXzS5TA_g5PrB0_pgOPchAVE2NFC_ACKsvSem61gw-MMnzasHYWRIBJ_DrlXK_dZwTxg75HoNjzylQlZZd93l2NnaQPA4urpVua59z5Kx2TBTkRzMgKJReOnaQPA4uzBRBywaSIJ2C..&spm=a21xtw.29178619.product_shelf.4.7ab366adCR4uRL&skuId=5615494997245"
]

urls3 = [
    "https://detail.tmall.com/item.htm?abbucket=4&id=810837883100&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.12.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=810956642904&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.16.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=810958446128&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.20.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=811212420575&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.24.6ecc7300twYOB8&skuId=5674395155994",
    "https://detail.tmall.com/item.htm?abbucket=4&id=810847419607&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.28.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=811214772992&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.32.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=810844587271&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.36.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=811130601421&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.40.6ecc7300twYOB8&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=810960018477&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.44.6ecc7300twYOB8&skuId=5503337944372",
    "https://detail.tmall.com/item.htm?abbucket=4&id=811219664907&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.48.6ecc7300twYOB8&sku_properties=134942334%3A25351185550"
]

urls4 = [
    "https://detail.tmall.com/item.htm?abbucket=4&id=848965857802&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.28.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=849186908407&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.12.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848661446126&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.16.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848939581341&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.20.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848544191204&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.24.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=849185664395&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.32.1b9e2140PbrbsD&skuId=5638226453918",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848547203817&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.44.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=849183544754&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.40.1b9e2140PbrbsD&skuId=5635935660924",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848565503447&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.36.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848684646528&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.48.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848685658519&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.52.1b9e2140PbrbsD&skuId=5638224413957",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848549267086&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.56.1b9e2140PbrbsD&skuId=5803869034666",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848974365111&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.60.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848548639323&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.64.1b9e2140PbrbsD&skuId=5805604511407",
    "https://detail.tmall.com/item.htm?abbucket=4&id=849152628977&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.68.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848568079543&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.80.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848538095917&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.76.1b9e2140PbrbsD&skuId=5635803452205",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848671154484&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.72.1b9e2140PbrbsD&skuId=5638189597892",
    "https://detail.tmall.com/item.htm?abbucket=4&id=849180740512&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.84.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848683638510&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.88.1b9e2140PbrbsD&skuId=5805693267060",
    "https://detail.tmall.com/item.htm?abbucket=4&id=848951973918&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.92.1b9e2140PbrbsD&skuId=5805610471509"
]

URLS = [
    [],
    urls1,
    urls2,
    urls3,
    urls4
]

def main(urlIndex, filepath, need_login=False):
    if need_login:
        login()
    for url in URLS[urlIndex]:
        data = fetch_and_parse(url)
        write_to_file(data, filepath)
        # if soup:
        #     data = read_to_data(soup, page)
        #     # write_to_file(data, filepath)
        # else:
        #     print("Failed to fetch the page")