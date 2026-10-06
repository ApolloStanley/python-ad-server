
def vast_multiple_mv(IP, PORT):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<VAST version="2.0">
<Ad id="ad-one" sequence="1"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-one</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad1_impression&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad1_start&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad1_firstQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad1_midpoint&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad1_thirdQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad1_complete&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_1.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-two" sequence="2"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-two</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad2_impression&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad2_start&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad2_firstQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad2_midpoint&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad2_thirdQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad2_complete&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_2.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-three" sequence="3"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-three</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad3_impression&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad3_start&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad3_firstQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad3_midpoint&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad3_thirdQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad3_complete&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_3.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-four" sequence="4"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-four</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad4_impression&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad4_start&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad4_firstQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad4_midpoint&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad4_thirdQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad4_complete&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_1.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
<Ad id="ad-five" sequence="5"><InLine>
<AdSystem>local</AdSystem><AdTitle>multi-ad-five</AdTitle>
<Impression><![CDATA[http://{IP}:{PORT}/?ad5_impression&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Impression>
<Creatives><Creative><Linear><Duration>00:00:30</Duration>
<TrackingEvents>
<Tracking event="start"><![CDATA[http://{IP}:{PORT}/?ad5_start&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="firstQuartile"><![CDATA[http://{IP}:{PORT}/?ad5_firstQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="midpoint"><![CDATA[http://{IP}:{PORT}/?ad5_midpoint&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="thirdQuartile"><![CDATA[http://{IP}:{PORT}/?ad5_thirdQuartile&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
<Tracking event="complete"><![CDATA[http://{IP}:{PORT}/?ad5_complete&sessionId=ROKU_MV_SESSION_ID&concurrentViews=ROKU_MV_NUM_CONC_VIEWS&screePercent=ROKU_MV_SCREEN_PCT&focusedView=ROKU_MV_FOCUSED_VIEW]]></Tracking>
</TrackingEvents>
<MediaFiles><MediaFile delivery="progressive" type="video/mp4" width="640" height="360">
<![CDATA[http://{IP}:{PORT}/640x360_2.mp4]]>
</MediaFile></MediaFiles>
</Linear></Creative></Creatives>
</InLine></Ad>
</VAST>"""
