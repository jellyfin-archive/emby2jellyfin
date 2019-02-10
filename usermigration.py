from configurator.mediaserver import mediaServer_config
from mediaServer.server import MediaServer
import logging

_log = logging.getLogger(__name__)

sourceconfig = mediaServer_config(cfg_file='mediaserver-source-config.json')
destconfig = mediaServer_config(cfg_file='mediaserver-destination-config.json')

try:
    sourcemediaserver = MediaServer(sourceconfig)
except Exception as inst:
    _log.critical(inst)

try:
    destmediaserver = MediaServer(destconfig)
except Exception as inst:
    _log.critical(inst)

# get users from source media server
sourceusers = sourcemediaserver.getusers()

for sourceuser in sourceusers:
    try:
        destuser = destmediaserver.createuserbyname(sourceuser.Name)
    except Exception as inst:
        _log.critical(inst)
    destuser.Policy = sourceuser.Policy
    destuser.Configuration = sourceuser.Configuration
    destmediaserver.updateuserconfig(destuser)
    destmediaserver.updateuserpolicy(destuser)

