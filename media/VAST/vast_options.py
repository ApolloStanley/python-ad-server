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
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/ad_one.mp4?stream=1]]>
</MediaFile></MediaFiles>
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
<MediaFile id="GDFP" delivery="progressive" width="1280" height="720" type="video/mp4" bitrate="3198" scalable="true" maintainAspectRatio="true">
<![CDATA[
http://redirector.gvt1.com/videoplayback/id/7bb3afce79f3998f/itag/22/source/gfp_video_ads/xpc/EgVovf3BOg%3D%3D/acao/yes/mime/video%2Fmp4/ctier/L/ip/0.0.0.0/ipbits/0/expire/1788378327/sparams/ip,ipbits,expire,id,itag,source,xpc,acao,mime,ctier/signature/5E4ED47794E65D6BD49E6BD4CD217577B4A4F5E7.5DED3AB4993A2B2336A567FC1CF536FF489966F3/key/ck2/file/file.mp4
]]>
</MediaFile>
<MediaFile id="GDFP" delivery="progressive" width="640" height="360" type="video/mp4" bitrate="733" scalable="true" maintainAspectRatio="true">
<![CDATA[
http://redirector.gvt1.com/videoplayback/id/7bb3afce79f3998f/itag/18/source/gfp_video_ads/xpc/EgVovf3BOg%3D%3D/acao/yes/mime/video%2Fmp4/ctier/L/ip/0.0.0.0/ipbits/0/expire/1788378327/sparams/ip,ipbits,expire,id,itag,source,xpc,acao,mime,ctier/signature/49FFFD84F2857C3135B31553D0D89184B6A556CB.8E83D3DC5114379A24971F8CD23EAA260BD28014/key/ck2/file/file.mp4
]]>
</MediaFile>
<MediaFile id="GDFP" delivery="progressive" width="1280" height="720" type="video/mp4" bitrate="3052" scalable="true" maintainAspectRatio="true">
<![CDATA[
http://redirector.gvt1.com/videoplayback/id/7bb3afce79f3998f/itag/106/source/gfp_video_ads/xpc/EgVovf3BOg%3D%3D/acao/yes/mime/video%2Fmp4/ctier/L/ip/0.0.0.0/ipbits/0/expire/1788378327/sparams/ip,ipbits,expire,id,itag,source,xpc,acao,mime,ctier/signature/2148264B79C438F28298855A508B8B6762EF5BE2.B203577EA406BABBA77907F6854466D6CC88474A/key/ck2/file/file.mp4
]]>
</MediaFile>
<MediaFile id="GDFP" delivery="progressive" width="854" height="480" type="video/mp4" bitrate="1101" scalable="true" maintainAspectRatio="true">
<![CDATA[
http://redirector.gvt1.com/videoplayback/id/7bb3afce79f3998f/itag/109/source/gfp_video_ads/xpc/EgVovf3BOg%3D%3D/acao/yes/mime/video%2Fmp4/ctier/L/ip/0.0.0.0/ipbits/0/expire/1788378327/sparams/ip,ipbits,expire,id,itag,source,xpc,acao,mime,ctier/signature/8C2E69C4B9906CAE30E9FD704F30F4D4273F4C42.6516EF168813ECE43EB9666C2C7B486E4B704D7F/key/ck2/file/file.mp4
]]>
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
<![CDATA[http://{IP}:{PORT}/ad_one.mp4]]>
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
<![CDATA[http://{IP}:{PORT}/ad_two.mp4]]>
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
