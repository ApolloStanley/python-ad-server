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
