def vast_simple(IP, PORT):
    return f"""<?xml version="1.0"?>
<VAST version="2.0"><Ad><InLine>
<AdSystem>local</AdSystem><AdTitle>wm-test</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:10</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/media.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad></VAST>"""

def vast_custom(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0"><Ad id="custom-beacon-test"><InLine>
<AdSystem>local</AdSystem><AdTitle>beacon-test</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?midPoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/ad_one.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad></VAST>"""

def vast_stream1_custom(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0"><Ad id="custom-beacon-test-stream1"><InLine>
<AdSystem>local</AdSystem><AdTitle>beacon-test-stream1</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?impression&stream=1]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start&stream=1]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?firstQuartile&stream=1]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?midPoint&stream=1]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?thirdQuartile&stream=1]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete&stream=1]]></Tracking>
</TrackingEvents>
<MediaFiles>
<MediaFile id="GDFP" delivery="progressive" width="640" height="360" type="video/mp4" bitrate="733" scalable="true" maintainAspectRatio="true">
<![CDATA[http://{IP}:{PORT}/640x360_1.mp4]]>
</MediaFile>
</MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad></VAST>"""

def vast_stream2_custom(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0"><Ad id="custom-beacon-test-stream2"><InLine>
<AdSystem>local</AdSystem><AdTitle>beacon-test-stream2</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?impression&stream=2]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start&stream=2]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?firstQuartile&stream=2]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?midPoint&stream=2]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?thirdQuartile&stream=2]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete&stream=2]]></Tracking>
</TrackingEvents>
<MediaFiles>
<MediaFile id="GDFP" delivery="progressive" width="640" height="360" type="video/mp4" bitrate="733" scalable="true" maintainAspectRatio="true">
<![CDATA[http://{IP}:{PORT}/640x360_2.mp4]]>
</MediaFile>
</MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad></VAST>"""

def vast_stream3_custom(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0"><Ad id="custom-beacon-test-stream3"><InLine>
<AdSystem>local</AdSystem><AdTitle>beacon-test-stream3</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?impression&stream=3]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start&stream=3]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?firstQuartile&stream=3]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?midPoint&stream=3]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?thirdQuartile&stream=3]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete&stream=3]]></Tracking>
</TrackingEvents>
<MediaFiles>
<MediaFile id="GDFP" delivery="progressive" width="640" height="360" type="video/mp4" bitrate="733" scalable="true" maintainAspectRatio="true">
<![CDATA[http://{IP}:{PORT}/640x360_3.mp4]]>
</MediaFile>
</MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad></VAST>"""

def vast_multiple(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0">
<Ad id="ad-one" sequence="1"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-one</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad1_impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad1_start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad1_firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad1_midpoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad1_thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad1_complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_1.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-two" sequence="2"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-two</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad2_impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad2_start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad2_firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad2_midpoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad2_thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad2_complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_2.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-three" sequence="3"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-three</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad3_impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad3_start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad3_firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad3_midpoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad3_thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad3_complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_3.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-four" sequence="4"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-four</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad4_impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad4_start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad4_firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad4_midpoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad4_thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad4_complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_1.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-five" sequence="5"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-five</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad5_impression]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad5_start]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad5_firstQuartile]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad5_midpoint]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad5_thirdQuartile]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad5_complete]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_2.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
</VAST>"""

def vast_error(IP, PORT):
    template = r"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="3.0">
  <Ad id="6195996899">
    <InLine>
      <AdSystem>local</AdSystem>
      <AdTitle>fria-overlay-test</AdTitle>
      <Description></Description>
      <Advertiser>46530509</Advertiser>
      <Impression><![CDATA[http://__IP__:__PORT__/?impression]]></Impression>
      <Error><![CDATA[http://__IP__:__PORT__/?error]]></Error>
      <Creatives>
        <Creative id="2449462747_linear">
          <Linear>
            <Duration>00:00:30</Duration>
            <TrackingEvents>
              <Tracking event="start"><![CDATA[http://__IP__:__PORT__/?start]]></Tracking>
              <Tracking event="firstQuartile"><![CDATA[http://__IP__:__PORT__/?firstQuartile]]></Tracking>
              <Tracking event="midpoint"><![CDATA[http://__IP__:__PORT__/?midpoint]]></Tracking>
              <Tracking event="thirdQuartile"><![CDATA[http://__IP__:__PORT__/?thirdQuartile]]></Tracking>
              <Tracking event="complete"><![CDATA[http://__IP__:__PORT__/?complete]]></Tracking>
            </TrackingEvents>
            <MediaFiles>
              <MediaFile delivery="progressive" type="video/mp4" width="640" height="360"><![CDATA[http://__IP__:__PORT__/ad_one.mp4]]></MediaFile>
            </MediaFiles>
          </Linear>
        </Creative>
        <Creative AdID="138419550241" id="2449462747">
          <NonLinearAds>
            <NonLinear width="350" height="20" apiFramework="roku-ria-inline">
              <NonLinearClickTracking><![CDATA[http://__IP__:__PORT__/?nonlinear_clicktracking]]></NonLinearClickTracking>
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
                "clickParams": "gwObjects=[{\"uri\":\"http:\\/\\/__IP__:__PORT__\\/overlay.png\",\"posTop\":789,\"posLeft\":0,\"width\":672,\"height\":189,\"slideDuration\":1}];overlayTimeout=15;cueOut=25;providerProductId=badPPID",
                "clickURL": "http://__IP__:__PORT__/?compAdClick",
                "FHDBannerURL": "",
                "FHDBannerURL_1": "",
                "FHDBannerURL_2": "",
                "FHDBannerURL_3": "",
                "Description": "",
                "Title": "FRIA test - subscribe",
                "ShortDescriptionLine1": "",
                "ShortDescriptionLine2": "FRIA test - subscribe",
                "Screentype": "subscribe",
                "ImpressionURL": "http://__IP__:__PORT__/?compAdImp",
                "installURL": "http://__IP__:__PORT__/?compAdInstall",
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
                "ErrorPixels": "http://__IP__:__PORT__/?errorpixel&err_code=[ERRORCODE]&msg=[ERROR_MESSAGE]"}]]>
            </CreativeExtension>
          </CreativeExtensions>
        </Creative>
      </Creatives>
    </InLine>
  </Ad>
</VAST>"""
    return template.replace("__IP__", IP).replace("__PORT__", str(PORT))

def AA_OK_SMS_FIRST_V1(IP, PORT):
    xml_head = f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="3.0">
  <Ad id="6195996899">
    <InLine>
      <AdSystem>local</AdSystem>
      <AdTitle>fria-overlay-test</AdTitle>
      <Description></Description>
      <Advertiser>46530509</Advertiser>
      <Impression><![CDATA[http://{IP}:{PORT}/?impression]]></Impression>
      <Error><![CDATA[http://{IP}:{PORT}/?error]]></Error>
      <Creatives>
        <Creative id="2449462747_linear">
          <Linear>
            <Duration>00:00:30</Duration>
            <TrackingEvents>
              <Tracking event="start"><![CDATA[http://{IP}:{PORT}/?start]]></Tracking>
              <Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?firstQuartile]]></Tracking>
              <Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?midpoint]]></Tracking>
              <Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?thirdQuartile]]></Tracking>
              <Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?complete]]></Tracking>
            </TrackingEvents>
            <MediaFiles>
              <MediaFile delivery="progressive" type="video/mp4" width="640" height="360"><![CDATA[http://{IP}:{PORT}/640x360.mp4]]></MediaFile>
            </MediaFiles>
          </Linear>
        </Creative>
        <Creative AdID="138419550241" id="2449462747">
          <NonLinearAds>
            <NonLinear width="350" height="20" apiFramework="roku-ria-inline">
              <NonLinearClickTracking><![CDATA[http://{IP}:{PORT}/?nonlinear_clicktracking]]></NonLinearClickTracking>
            </NonLinear>
          </NonLinearAds>
          <CreativeExtensions>
            <CreativeExtension type="action_ads">
              <![CDATA["""

    creative_extension_json = r"""{
                  "ad": {
                      "AdID": "{{ creative_id }}",
                      "LineID": "{{ placement_id }}",
                      "cID": "{{ campaign_id }}",
                      "advId": "{{ adv_id }}",
                      "FHDBannerURL": "https://ads.w55c.net/t/cs/assets/CAM:v1:oren/2025-07-09_17-59-28.487_0fcb0dc7-9fa1-4414-8c6d-833ebf7ac080_US_Q225__20Players_Action-Ad_Overlay_624x429.jpg",
                      "clickHandlerImg": "https://ads.w55c.net/t/cs/assets/CAM:v1:oren/2025-07-09_17-59-45.484_31cc2765-30ae-470f-945a-1c4d6ef954aa_US_Q225__20Players_Action-Ad_BrandShowcaseTile_441x221_20copy.jpg",
                      "clickHandlerBG": "0x8F8598",
                      "clickAction": "FlexibleGateway",
                      "clickID": "0",
                      "clickParams": "gwObjects=[{\"uri\":\"https://ads.w55c.net/t/cs/assets/CAM:v1:oren/2025-07-09_17-59-28.487_0fcb0dc7-9fa1-4414-8c6d-833ebf7ac080_US_Q225__20Players_Action-Ad_Overlay_624x429.jpg\",\"posTop\":549,\"posLeft\":0,\"width\":624,\"height\":429,\"slideDelay\":1,\"slideDuration\":1},{\"uri\":\"https://ads.w55c.net/t/cs/assets/CAM:production:v1/2024-12-11_13-56-58.554_55e3ce79-5ee4-4b72-9760-bdb932876f25_hint.png\",\"posTop\":0,\"posLeft\":1266,\"width\":654,\"height\":205,\"slideDelay\":0,\"animType\":\"opacity\"}];brand=The Roku Channel;isSendingConfirmation=false;confirmationMsg=none;payLoadMsg=Every TV deserves the Roku experience. \n\nShop Roku players now at https://go.roku.com/rokuplayers_t2.\n\nThis requested message was sent by Roku on behalf of Roku;stopAckMsg=;offerOverride=;bgLaunch=true;cueOut=25",
                      "ShortDescriptionLine1": "https://docs.roku.com/published/userprivacypolicy/en/us",
                      "ShortDescriptionLine2": "Press OK for offer",
                      "Screentype": "sms",
                      "isCreativeServiceResp": true,
                      "clickURL": "",
                      "ImpressionURL": "",
                      "installURL": "",
                      "ThirdPartyImpressions": "",
                      "ThirdPartyClicks": "",
                      "ThirdPartyInstalls": "",
                      "altid":"-",
                      "avsource":"",
                      "FlexibleTitle": "",
                      "FHDBannerURL_1": "",
                      "FHDBannerURL_2": "",
                      "FHDBannerURL_3": "",
                      "FHDSmallIconURL": "",
                      "isSameOverlay": "",
                      "overlayMessage1": "",
                      "overlayMessage2": "",
                      "messageAlignment1": "",
                      "messageAlignment2": "",
                      "overlayImage1": "",
                      "overlayImage2": "",
                      "messageLink": "",
                      "productID": "",
                      "shoppableProductId": "",
                      "productCatalogID": "",
                      "channeltype": "",
                      "sms": "",
                      "duration": "",
                      "start_date": "",
                      "end_date": "",
                      "is_live": "",
                      "is_recurring": "",
                      "show_time": "",
                      "show_timezone": "",
                      "readabletime": "",
                      "Title": "",
                      "AlertOverlayGraphic": "",
                      "mediatype": "",
                      "contentid": "-",
                      "Description": ""
                  }
              }"""

    xml_tail = """]]>
            </CreativeExtension>
          </CreativeExtensions>
        </Creative>
      </Creatives>
    </InLine>
  </Ad>
</VAST>"""

    return xml_head + creative_extension_json + xml_tail