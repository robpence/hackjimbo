#!/usr/bin/env python

import gobject
import phony.headset
import phony.base.ipc
import phony.audio.alsa
import phony.bluetooth.adapters
import phony.bluetooth.profiles.handsfree

class HeadsetService:
    _hs = None
    _call_in_progress = False

    def device_connected(self):
        print 'Device connected!'

    def incoming_call(self, call):
        print 'Incoming call: %s' % call
        if self._call_in_progress:
            self._hs.deflect_call_to_voicemail()

    def call_began(self, call):
        print 'Call began: %s' % call
        self._call_in_progress = True

    def call_ended(self, call):
        print 'Call ended: %s' % call
        self._call_in_progress = False
        
    def start(self):
        bus = phony.base.ipc.BusProvider()
                            
        with phony.bluetooth.adapters.Bluez5(bus) as adapter, \
             phony.bluetooth.profiles.handsfree.Ofono(bus) as hfp, \
             phony.audio.alsa.Alsa() as audio, \
             phony.headset.HandsFreeHeadset(bus, adapter, hfp, audio) as hs:

            hs.on_device_connected(self.device_connected)
            hs.on_incoming_call(self.incoming_call)
            hs.on_call_began(self.call_began)
            hs.on_call_ended(self.call_ended)

            hs.start('MyBluetoothHeadset', pincode = '1234')
            hs.enable_pairability(timeout = 30)

            self._hs = hs

            gobject.MainLoop()

    def voice_dial(self):
        self._hs.initiate_call()

    def dial_number(self, phone_number):
        self._hs.dial(phone_number)

if __name__=="__main__":
    hs = HeadsetService()
    hs.start()
