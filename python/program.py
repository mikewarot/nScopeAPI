import nScopePy as ns

ns.loadFirmware()

print "Firmware version: ",ns.nScopeAPI.nScope_check_API_version()
