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
