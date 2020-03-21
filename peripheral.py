from pybleno import *
from Config import Config
from ConfigService import ConfigService
from WifiService import WifiService

bleno = Bleno()
config = Config()
configService = ConfigService(config)
wifiService = WifiService()

name = 'Tide light'
uuids = ['ec00', 'ec01']

#
# Wait until the BLE radio powers on before attempting to advertise.
# If you don't have a BLE radio, then it will never power on!
#
def onStateChange(state):
    if (state == 'poweredOn'):
        #
        # We will also advertise the service ID in the advertising packet,
        # so it's easier to find.
        #
        def on_startAdvertising(err):
            if err:
                print(err)

        bleno.startAdvertising(name, uuids, on_startAdvertising)
    else:
        bleno.stopAdvertising();
bleno.on('stateChange', onStateChange)
    
def onAdvertisingStart(error):
    if not error:
        print('advertising...')
        
        bleno.setServices([
            configService,
            wifiService
            
        ])
        
bleno.on('advertisingStart', onAdvertisingStart)

bleno.start()

print ('Hit <ENTER> to disconnect')


input()

bleno.stopAdvertising()
bleno.disconnect()

