def iZACgmeQ(IP, PORT):
    xml_head = r"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="3.0">
  <Ad id="6195996899"> 
    <InLine>
      <AdSystem>DoubleClick</AdSystem>
      <AdTitle>-</AdTitle>
      <Description></Description>
      <Advertiser>46530509</Advertiser>
      <Impression><![CDATA[https://securepubads.g.doubleclick.net/pcs/view%3Fxai%3DAKAOjstc2dyagABXOcAwpW0RU1NTTpuDAkLH6zVR_x9GHD8HQwRjPXzYLFl7myP_Z4QAiynY-44uRkCIb56W_ckXnYIR59gYdcE3yk-wTk7Kny_ArSIJM32lEHNverVnChpUSl4IFjuTXpNZnToNMvxeCGyqjThewVcti1kYVOkJsfxmwUH6DWh5jix82GjphI1JzupIG97haPnVRsHnegB2WmoZHVVPHp0pBNX748t9oqUUIww3FiKxtxTmByJYrNW-2yUiFj7yuPfr62-Izp76wZU-_YbAkHRnplEyCjX-ZVZC8o%26sai%3DAMfl-YRVQLqRRuqFLHK7tt5KKJZloI0IcpkwgAvQN0d24tG3sYjKNPuhopvPgHCqG4Bt5gJRTy_EO5hNo0Mby68m2ipKqGjRdiDVzmhxsfbnXN2s4kSRnLY9UJHyC3bf4d7Kjc44W4gNfKbpmJSO2h9WCOxNLayYopvJl1iHmebVATwuxzTc1psKLsVHGJky10isY4siGau4OaJyKD9Z1oS_iTfdTD6tugHBGgko9KJuCR-38WY0w%26sig%3DCg0ArKJSzEMJpm5LvT1-EAE%26uach_m%3D%5BUACH%5D%26urlfix%3D1%26adurl%3D]]></Impression>
      <Error><![CDATA[https://ravm.tv/errorpixelexample]]></Error>
      <Creatives>
        <Creative AdID="138419550241" id="2449462747">
          <NonLinearAds>
            <NonLinear width="350" height="20" apiFramework="roku-ria-inline">
              <NonLinearClickTracking><![CDATA[https://adclick.g.doubleclick.net/pcs/click?xai=AKAOjstJux54RFbPlRpWSLvcCLLXFtdrw1Sq01Tewgfml9BR4O311ZsjymPhI_uU8uZ6w7ZZ_ht9EVBeDD8shmDvXzAPqNcjt_N_trpcH5glYfItIsHCDJCJOCbw3eoIZW55CmHtXzOc3Np68BBfCBn_k6BnXMS11lvgqf-xcFE0ZBY0qWyos_pF_ESsYvUkYsk1n__6ZnjZRE9DaybhJrdW6JLMtf1PVEGyIZANfvaatkg53UheZug-ANJkyBMXSWu3iz8VC5-dmzdHXRTs0E74NNuQOO4IyGgEMh87&sai=AMfl-YS4QfY_vCBRXai26hBFCHzrEFWpQBMgLn-23wWy1pc20x2eHwpZMWQuu9bJQl584U_neMqr_zpVabiUsl2s_HBK7kiHwVLvLdIQlSOxCaoOIk4iKxJOQkdfcanxCwK_th9uILWTT3T_1ycj-HB_owaff5jchcJXLvtRilVeEcfF2pIZikTc2UcONt7kBkapncIoiR2GHE7Pid3N6OeNUmziFHKX4ufEY_5Ksn0&sig=Cg0ArKJSzOdBGFrdTjwVEAE&fbs_aeid=[gw_fbsaeid]&urlfix=1&adurl=]]></NonLinearClickTracking>
            </NonLinear>
          </NonLinearAds>
          <CreativeExtensions>
            <CreativeExtension type="roku-ria-inline">
              <![CDATA[
{
"AdID": "XReNSNaruk",
"LineID": "",
"cID": "",
"AdvertiserID": "440",
"clickHandlerImg": "",
"clickHandlerBG": "",
"FlexibleTitle": "SingleOverlay",
"clickAction": "FlexibleGateway",
"clickID": "151908",
"clickParams": "gwObjects=[{\"uri\":\"https:\\/\\/ads.w55c.net\\/t\\/d\\/XassetKZeYlqU1.png\",\"posTop\":789,\"posLeft\":0,\"width\":672,\"height\":189,\"slideDuration\":1}];overlayTimeout=15;cueOut=25;providerProductId=badPPID",
"clickURL": "https://i.w55c.net/a.gif?btid=C1YeA3BS5iuYSpsuLbYrSw&rts=0&ev=compAdClick",
"FHDBannerURL": "",
"FHDBannerURL_1": "",
"FHDBannerURL_2": "",
"FHDBannerURL_3": "",
"Description": "",
"Title": "FRIA test - subscribe",
"ShortDescriptionLine1": "",
"ShortDescriptionLine2": "FRIA test - subscribe",
"Screentype": "subscribe",
"ImpressionURL": "https://i.w55c.net/a.gif?btid=C1YeA3BS5iuYSpsuLbYrSw&rts=0&ev=compAdImp",
"installURL": "https://i.w55c.net/a.gif?btid=C1YeA3BS5iuYSpsuLbYrSw&rts=0&ev=compAdInstall",
"ThirdPartyImpressions": "",
"ThirdPartyClicks": "",
"ThirdPartyInstalls": "",
"AlertOverlayGraphic": "",
"channeltype": "",
"is_live": "",
"duration": "",
"mediatype": "",
"contentid": "",
"readabletime": "",
"show_time": "",
"show_timezone": "",
"sms": "",
"is_recurring": "",
"start_date": "",
"end_date": "",
"ErrorPixels": "https://ravm.tv/pixel/display/v1?meType=0&evType=3&adv_id=46530509&cID=3211209109&plID=6315454046&crID=138419550241&sw_version=&dev_model=&ott_id=2721a2c2-cd3e-50ee-bf71-5ee258123b8e&ip=24.6.214.121&adguid=453a9385-1afd-5cee-ab78-73317eec7d08&last_channel=&bnr_loc=overlay&locale=en_US&is_lat=1&country_code=us&trc_version=&trc_channel_version=&grandcentral_version=9.5.514&davinci_version=DAVINCI_CODE&ad_srv=prod&libversion=3.0607&platform=&app=&clientversion=&trc_genre_row=&trc_category_id=&abrejectcount=&guest_mode=&providerproductids=ROKU_ADS_PPIDS&adunitpath=&adunitID=ADUNIT_ID&width=560&height=309&screensaver=&ria_adid=&ria_altid=&cr_type=0&demand_source=DFP_DISPLAY&device_id=&adreq_id=453a9385-1afd-5cee-ab78-73317eec7d08&theme=&amoeba_exp_bkt=&image_code=16007283816147257181%3F&err_code=[ERRORCODE]&msg=[ERROR_MESSAGE]"}]]>
            </CreativeExtension>
          </CreativeExtensions>
        </Creative>
      </Creatives>
    </InLine>
  </Ad>
</VAST>"""
 
    return xml_head


def ewmPj998(IP, PORT):
     return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="3.0">
<Ad id="6195996899">
<InLine>
<AdSystem>DoubleClick</AdSystem>
<AdTitle>-</AdTitle>
<Description></Description>
<Advertiser>46530509</Advertiser>
<Impression><![CDATA[http://{IP}:{PORT}/?impression]]></Impression>
<Error><![CDATA[http://{IP}:{PORT}/impression/error?err=%5BERRORCODE%5D&msg=%5BERROR_MESSAGE%5D]]></Error>
<Creatives>
<Creative AdID="138419550241" id="2449462747">
<NonLinearAds>
<NonLinear width="350" height="20" apiFramework="roku-ria-inline">
<NonLinearClickTracking>
<![CDATA[https://adclick.g.doubleclick.net/pcs/click?xai=AKAOjstJux54RFbPlRpWSLvcCLLXFtdrw1Sq01Tewgfml9BR4O311ZsjymPhI_uU8uZ6w7ZZ_ht9EVBeDD8shmDvXzAPqNcjt_N_trpcH5glYfItIsHCDJCJOCbw3eoIZW55CmHtXzOc3Np68BBfCBn_k6BnXMS11lvgqf-xcFE0ZBY0qWyos_pF_ESsYvUkYsk1n__6ZnjZRE9DaybhJrdW6JLMtf1PVEGyIZANfvaatkg53UheZug-ANJkyBMXSWu3iz8VC5-dmzdHXRTs0E74NNuQOO4IyGgEMh87&sai=AMfl-YS4QfY_vCBRXai26hBFCHzrEFWpQBMgLn-23wWy1pc20x2eHwpZMWQuu9bJQl584U_neMqr_zpVabiUsl2s_HBK7kiHwVLvLdIQlSOxCaoOIk4iKxJOQkdfcanxCwK_th9uILWTT3T_1ycj-HB_owaff5jchcJXLvtRilVeEcfF2pIZikTc2UcONt7kBkapncIoiR2GHE7Pid3N6OeNUmziFHKX4ufEY_5Ksn0&sig=Cg0ArKJSzOdBGFrdTjwVEAE&fbs_aeid=[gw_fbsaeid]&urlfix=1&adurl=]]>
</NonLinearClickTracking>
</NonLinear>
</NonLinearAds>
<CreativeExtensions>
<CreativeExtension type="roku-ria-inline"><![CDATA["bad JSON"]]></CreativeExtension>
</CreativeExtensions>
</Creative>
</Creatives>
</InLine>
</Ad>
</VAST>"""
